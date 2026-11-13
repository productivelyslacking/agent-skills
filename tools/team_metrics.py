#!/usr/bin/env python3
"""Team-ops metrics from a Claude Code session's logs (Python 3 standard library only).

Usage: team_metrics.py SESSION_JSONL --cut ISO [--from ISO] [--to ISO] [--json OUT]
       team_metrics.py --selftest

SESSION_JSONL is the producer's log, `~/.claude/projects/<project>/<session>.jsonl`; its subagents are read
from the `<session>/subagents/` folder beside it. Times are UTC ISO prefixes (2026-10-06T03:54). Rounds
(an agent's work up to each SubagentHandback) starting before --cut are "before", the rest "after".

Prints, per period: input tokens per role and for the producer, counting each model call once (a message's
content blocks are logged as separate entries repeating its usage: dedupe by message.id); the producer's
average and peak context and its compactions; hand-back lengths; merge-review verdicts (first line);
explicit reads of a CLAUDE.md that also arrived as an attachment (a double load); Write calls refused as
report files; permission denials (tool results "Permission for this ... denied"), by the classifier's reason. --selftest builds a tiny fake session and fails if the dedupe or the double-load count breaks
(a negative control: the raw entry sum must differ from the deduped one).
"""
import argparse, collections, glob, json, os, re, statistics, sys, tempfile

VERDICT = re.compile(r"\b(APPROVE-IF|APPROVE|REJECT|HOLD)\b")
DENIED = re.compile(r"^Permission for this (action|command) was denied")

def denial_reason(body):
    """The classifier's bracketed reason, "safety check" for the built-in removal check, else "unexplained"."""
    m = re.search(r"Reason: \[([^\]]+)\]", body)
    return m.group(1) if m else ("safety check" if "safety check" in body[:200] else "unexplained")

def text_of(content):
    if isinstance(content, str):
        return content
    return " ".join(x.get("text", "") for x in content or [] if isinstance(x, dict) and x.get("type") == "text")

def ctx_of(usage):
    return sum(usage.get(k, 0) for k in ("input_tokens", "cache_read_input_tokens", "cache_creation_input_tokens"))

def read_agent(path):
    """Rounds of one subagent: list of dicts (t0, cum, raw, peak, calls, hb, claude_reads, claude_attached)."""
    rounds, cur, seen = [], None, set()
    attached, reads, pend, refused = set(), [], {}, 0
    for line in open(path, errors="replace"):
        try:
            e = json.loads(line)
        except ValueError:
            continue
        m = e.get("message") or {}
        if e.get("type") == "attachment":
            a = e.get("attachment") or {}
            if a.get("type") == "nested_memory":
                attached.add(os.path.realpath(a.get("path", "")))
            continue
        if e.get("type") == "user":
            c = m.get("content")
            if isinstance(c, list) and any(isinstance(x, dict) and x.get("type") == "tool_result" for x in c):
                for x in c:
                    if isinstance(x, dict) and x.get("type") == "tool_result" and cur is not None:
                        body = x.get("content") if isinstance(x.get("content"), str) else text_of(x.get("content"))
                        if DENIED.match(body or ""):
                            cur["denied"].append(denial_reason(body))
                    if isinstance(x, dict) and x.get("type") == "tool_result" and x.get("tool_use_id") in pend:
                        kind, arg = pend.pop(x["tool_use_id"])
                        body = text_of(x.get("content")) if not isinstance(x.get("content"), str) else x["content"]
                        if kind == "Write" and x.get("is_error") and "report files" in body:
                            refused += 1
                continue
            t = text_of(c)
            if t.strip() and (not e.get("isMeta") or t.startswith("The coordinator sent")) and not t.startswith("<system"):
                if cur is None or cur["hb"] is not None:
                    cur = dict(t0=e.get("timestamp", ""), cum=0, raw=0, peak=0, calls=0, hb=None, denied=[])
                    rounds.append(cur)
            continue
        if e.get("type") == "assistant" and cur is not None:
            ctx = ctx_of(m.get("usage") or {})
            cur["raw"] += ctx
            if m.get("id") not in seen and ctx:
                seen.add(m.get("id"))
                cur["cum"] += ctx; cur["calls"] += 1; cur["peak"] = max(cur["peak"], ctx)
            for x in m.get("content") or []:
                if not isinstance(x, dict) or x.get("type") != "tool_use":
                    continue
                inp = x.get("input") or {}
                if x.get("name") == "SubagentHandback":
                    cur["hb"] = inp.get("message", "")
                elif x.get("name") == "Write":
                    pend[x["id"]] = ("Write", inp.get("file_path"))
                elif x.get("name") == "Read" and str(inp.get("file_path", "")).endswith("CLAUDE.md"):
                    reads.append(os.path.realpath(inp["file_path"]))
                elif x.get("name") == "Bash" and re.match(r"\s*(cd [^;&|]+(;|&&)\s*)?(cat|sed -n|head)\b[^|;&]*CLAUDE\.md", inp.get("command", "")):
                    reads.append("bash:" + inp["command"][:80])
    double = sum(1 for r in reads if r in attached or r.startswith("bash:"))
    return rounds, double, refused

def producer(path):
    calls, seen, comp, denied = [], set(), [], []
    for line in open(path, errors="replace"):
        try:
            e = json.loads(line)
        except ValueError:
            continue
        if e.get("type") == "system" and "compact" in str(e.get("subtype", "")):
            comp.append((e.get("timestamp", ""), (e.get("compactMetadata") or {}).get("preTokens")))
        if e.get("type") == "user" and not e.get("isSidechain") and isinstance((e.get("message") or {}).get("content"), list):
            for x in e["message"]["content"]:
                if isinstance(x, dict) and x.get("type") == "tool_result":
                    body = x.get("content") if isinstance(x.get("content"), str) else text_of(x.get("content"))
                    if DENIED.match(body or ""):
                        denied.append((e.get("timestamp", ""), denial_reason(body)))
        if e.get("type") == "assistant" and not e.get("isSidechain"):
            m = e["message"]; ctx = ctx_of(m.get("usage") or {})
            if ctx and m.get("id") not in seen:
                seen.add(m.get("id")); calls.append((e["timestamp"], ctx))
    return calls, comp, denied

def run(session, cut, t_from="", t_to="9999"):
    sub = os.path.join(session[:-6], "subagents")
    per = lambda t: None if not (t_from <= t < t_to) else ("before" if t < cut else "after")
    out = {p: dict(roles=collections.defaultdict(lambda: [0, 0, 0]), hb=[], verdicts=collections.Counter(),
                   double=0, refused=0, producer=[], denied=collections.Counter()) for p in ("before", "after")}
    for f in sorted(glob.glob(os.path.join(sub, "*.jsonl"))):
        meta = json.load(open(f[:-6] + ".meta.json"))
        rounds, double, refused = read_agent(f)
        for i, r in enumerate(rounds):
            p = per(r["t0"])
            if not p:
                continue
            o = out[p]; role = o["roles"][meta.get("agentType", "?")]
            role[0] += 1; role[1] += r["cum"]; role[2] += r["raw"]
            for reason in r["denied"]:
                o["denied"][(meta.get("agentType", "?"), reason)] += 1
            if r["hb"] is not None:
                o["hb"].append(len(r["hb"]))
                if meta.get("agentType") == "merge-reviewer":
                    v = VERDICT.search(r["hb"][:300]); o["verdicts"][(v.group(1) if v else "?", "first" if i == 0 else "re-check")] += 1
            if i == 0:
                o["double"] += double; o["refused"] += refused
    calls, comp, pdenied = producer(session)
    for t, c in calls:
        p = per(t)
        if p:
            out[p]["producer"].append(c)
    for t, reason in pdenied:
        p = per(t)
        if p:
            out[p]["denied"][("producer", reason)] += 1
    return out, comp

def report(out, comp):
    for p, o in out.items():
        sub = sum(v[1] for v in o["roles"].values()); raw = sum(v[2] for v in o["roles"].values())
        pr = o["producer"]
        print(f"== {p}: subagent input {sub/1e6:.0f} M (raw entries {raw/1e6:.0f} M); producer {sum(pr)/1e6:.0f} M "
              f"over {len(pr)} calls, average context {statistics.mean(pr)/1e3 if pr else 0:.0f} k, peak {max(pr or [0])/1e3:.0f} k")
        for role, (n, cum, _) in sorted(o["roles"].items(), key=lambda kv: -kv[1][1]):
            print(f"   {role:16} rounds {n:3}  input {cum/1e6:7.1f} M")
        hb = sorted(o["hb"])
        if hb:
            print(f"   hand-backs {len(hb)}: median {statistics.median(hb):.0f} chars, p90 {hb[int(.9*(len(hb)-1))]}, "
                  f"<=1,500: {sum(1 for x in hb if x <= 1500)}")
        print(f"   merge verdicts {dict(o['verdicts'])}")
        print(f"   CLAUDE.md read explicitly though attached: {o['double']}; Write refused as a report file: {o['refused']}")
        print(f"   permission denials {sum(o['denied'].values())}: " +
              ", ".join(f"{who} {why} x{n}" for (who, why), n in sorted(o["denied"].items())))
    print("compactions:", comp)

def selftest():
    d = tempfile.mkdtemp()
    sess = os.path.join(d, "s.jsonl"); os.makedirs(os.path.join(d, "s", "subagents"))
    u = {"input_tokens": 10, "cache_read_input_tokens": 990}
    msg = lambda i, c: {"type": "assistant", "timestamp": "2026-01-01T01:00", "message": {"id": i, "usage": u, "content": c}}
    agent = [
        {"type": "user", "timestamp": "2026-01-01T01:00", "message": {"content": "Brief"}},
        msg("m1", [{"type": "text", "text": "x"}]),
        msg("m1", [{"type": "tool_use", "id": "r1", "name": "Read", "input": {"file_path": d + "/CLAUDE.md"}}]),
        {"type": "attachment", "attachment": {"type": "nested_memory", "path": d + "/CLAUDE.md"}},
        msg("m2", [{"type": "tool_use", "id": "w1", "name": "Write", "input": {"file_path": d + "/report.md"}}]),
        {"type": "user", "message": {"content": [{"type": "tool_result", "tool_use_id": "w1", "is_error": True,
            "content": "<tool_use_error>Subagents should return findings as text, not write report files.</tool_use_error>"}]}},
        msg("m4", [{"type": "tool_use", "id": "b1", "name": "Bash", "input": {"command": "git rebase main"}}]),
        {"type": "user", "message": {"content": [{"type": "tool_result", "tool_use_id": "b1", "is_error": True,
            "content": "Permission for this action was denied by the Claude Code auto mode classifier. Reason: [Git Destructive]."}]}},
        msg("m5", [{"type": "tool_use", "id": "b2", "name": "Bash", "input": {"command": "false"}}]),
        {"type": "user", "message": {"content": [{"type": "tool_result", "tool_use_id": "b2", "is_error": True,
            "content": "Permission denied (publickey)."}]}},
        msg("m3", [{"type": "tool_use", "id": "h1", "name": "SubagentHandback", "input": {"message": "REJECT. x"}}]),
    ]
    with open(os.path.join(d, "s", "subagents", "agent-a1.jsonl"), "w") as f:
        f.writelines(json.dumps(x) + "\n" for x in agent)
    json.dump({"agentType": "merge-reviewer"}, open(os.path.join(d, "s", "subagents", "agent-a1.meta.json"), "w"))
    with open(sess, "w") as f:
        f.write(json.dumps({"type": "assistant", "timestamp": "2026-01-01T02:00", "message": {"id": "p1", "usage": u}}) + "\n")
        f.write(json.dumps({"type": "assistant", "timestamp": "2026-01-01T02:00", "message": {"id": "p1", "usage": u}}) + "\n")
    out, _ = run(sess, "2026-01-01T00:00")
    a = out["after"]; role = a["roles"]["merge-reviewer"]
    checks = [("deduped input is 5 calls x 1000", role[1] == 5000), ("raw entries differ (control)", role[2] == 6000),
              ("producer counted once", a["producer"] == [1000]), ("one double load", a["double"] == 1),
              ("one refused report file", a["refused"] == 1), ("verdict REJECT first", a["verdicts"][("REJECT", "first")] == 1),
              ("one denial, its reason read; a plain error not counted (control)",
               dict(a["denied"]) == {("merge-reviewer", "Git Destructive"): 1})]
    for name, ok in checks:
        print(("ok   " if ok else "FAIL ") + name)
    return 0 if all(ok for _, ok in checks) else 1

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("session", nargs="?"); ap.add_argument("--cut"); ap.add_argument("--from", dest="t_from", default="")
    ap.add_argument("--to", default="9999"); ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        sys.exit(selftest())
    if not (a.session and a.cut):
        ap.error("SESSION_JSONL and --cut are required")
    report(*run(a.session, a.cut, a.t_from, a.to))
