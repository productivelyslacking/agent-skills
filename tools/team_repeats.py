#!/usr/bin/env python3
"""Repeated work that code could do instead of agents' turns (Python 3 standard library only).

Usage: team_repeats.py SESSION_JSONL [--from ISO] [--to ISO] [--patterns FILE.json] [--top N]
       team_repeats.py --selftest

Reads the producer's log and its `<session>/subagents/*.jsonl` (+ `.meta.json` for the role). For every tool call
it takes the context of the model call that issued it (input + cache read + cache creation), split evenly
between the tool calls of that one model call (a message's blocks are logged as separate entries repeating
its usage: count each message.id once). Then, per pattern (a regex over the Bash command; first match wins),
prints calls, agents, roles and context tokens: what those turns cost, an upper bound on what a script that
does the same steps in one call saves. Also: wait chains (a wait or a peek at a job's output followed by
another before any other work: the second and later are turns a single blocking wait would not have taken).

The default patterns are an action RPG's (2026-10-06); pass --patterns {"name": "regex", ...} for another project.
Numbers are context tokens, not money: most are cache reads. --selftest builds a fake session and fails if the
per-message split or the wait-chain count breaks (a negative control: the unsplit sum must differ).
"""
import argparse, collections, glob, json, os, re, sys, tempfile

PATTERNS = {
    "land (producer: pull, rebase, apply, ff-merge, push, worktree remove)":
        r"git merge (-q )?--ff-only|merge -q --ff-only|git apply [^|]*approve-if|git write-tree",
    "board/status edit": r"(BOARD|STATUS)\.md",
    "review copy setup (worktree --detach, art copy, rebase)":
        r"worktree add --detach|git clone [^|]*/tmp|ls-files --others --ignored|cp --reflink",
    "worktree remove/prune": r"worktree (remove|prune)",
    "standard gates (build, tests, doc checks)": r"dotnet (build|test)|check-docs|check-lore|godot[^|]*--import",
    "art.local.json (per-checkout overlay)": r"art\.local\.json",
    "contact sheet / side-by-side": r"Image\.new|\.paste\(|montage |magick [^|]*(append|montage)|hstack|vstack",
    "html review page": r"<html|\.html\b",
    "remote idle/process probe": r"ssh[^|]*(gpu-idle|docker ps|pgrep|uptime|loginctl|ps -[eu])",
    "hand rsync/scp to a box": r"\b(rsync|scp)\b[^|]*\S+:",
    "backup sync": r"sync-backup\.sh",
    "router (tools/jobs)": r"tools/jobs/|jobs submit",
}
WAIT = re.compile(r"^\s*(sleep \d+\s*[;&]|until\b|while\b|timeout \d+ bash -c .(until|while))|do sleep \d+")
PEEK = re.compile(r"^\s*(tail|cat|grep)\b[^|;]*tasks/\w+\.output|^\s*tail -\w* ?\d* \S+\.log\s*$")

def ctx(u):
    return sum(u.get(k, 0) for k in ("input_tokens", "cache_read_input_tokens", "cache_creation_input_tokens"))

def calls_of(path, role, agent):
    out, per_msg = [], collections.Counter()
    for line in open(path, errors="replace"):
        try:
            e = json.loads(line)
        except ValueError:
            continue
        m = e.get("message") or {}
        if e.get("type") != "assistant":
            continue
        for b in m.get("content") or []:
            if isinstance(b, dict) and b.get("type") == "tool_use":
                per_msg[m.get("id")] += 1
                out.append(dict(role=role, agent=agent, ts=e.get("timestamp", ""), tool=b.get("name"),
                                cmd=(b.get("input") or {}).get("command", "") if b.get("name") == "Bash" else "",
                                mid=m.get("id"), ctx=ctx(m.get("usage") or {})))
    for c in out:
        c["share"] = c["ctx"] / per_msg[c["mid"]]
    return out

def load(session, t0="", t1="~"):
    base = session[:-6]
    calls = calls_of(session, "producer", "main")
    for f in sorted(glob.glob(base + "/subagents/*.jsonl")):
        meta = f[:-6] + ".meta.json"
        role = json.load(open(meta)).get("agentType", "?") if os.path.exists(meta) else "?"
        calls += calls_of(f, role, os.path.basename(f)[:-6])
    return [c for c in calls if t0 <= c["ts"] < t1]

def head(cmd):
    return cmd.split("<<")[0][:600]

def analyse(calls, patterns):
    pats = [(n, re.compile(p, re.M)) for n, p in patterns.items()]
    agg = collections.OrderedDict((n, dict(n=0, ctx=0.0, agents=set(), roles=collections.Counter())) for n in patterns)
    for c in calls:
        if c["tool"] != "Bash":
            continue
        name = next((n for n, p in pats if p.search(c["cmd"])), None)
        if name:
            a = agg[name]; a["n"] += 1; a["ctx"] += c["share"]; a["agents"].add(c["agent"]); a["roles"][c["role"]] += 1
    by = collections.defaultdict(list)
    for c in calls:
        by[c["agent"]].append(c)
    repeat, rctx = 0, 0.0
    for L in by.values():
        L.sort(key=lambda c: c["ts"]); run = 0
        for c in L:
            h = head(c["cmd"])
            if c["tool"] == "Bash" and (WAIT.search(h) or PEEK.search(h)) and not h.lstrip().startswith(("cat >", "python3 -")):
                run += 1
                if run > 1:
                    repeat += 1; rctx += c["share"]
            else:
                run = 0
    return agg, repeat, rctx

def report(calls, patterns, top):
    agg, repeat, rctx = analyse(calls, patterns)
    total = sum(c["share"] for c in calls)
    print(f"tool calls {len(calls)}, context tokens behind them {total/1e6:.1f} M (each model call once)")
    print(f"{'pattern':66} {'calls':>6} {'agents':>6} {'ctx M':>7}  roles")
    for n, a in sorted(agg.items(), key=lambda kv: -kv[1]["ctx"])[:top]:
        print(f"{n[:66]:66} {a['n']:6} {len(a['agents']):6} {a['ctx']/1e6:7.1f}  {dict(a['roles'].most_common(3))}")
    print(f"wait chains: {repeat} repeat waits/peeks, {rctx/1e6:.1f} M (turns one blocking wait would not take)")

def selftest():
    d = tempfile.mkdtemp()
    s = os.path.join(d, "s.jsonl"); os.makedirs(os.path.join(d, "s", "subagents"))
    def asst(mid, ts, blocks, c):
        return json.dumps(dict(type="assistant", timestamp=ts, message=dict(id=mid, usage=dict(input_tokens=c), content=blocks)))
    bash = lambda i, cmd: dict(type="tool_use", id=i, name="Bash", input=dict(command=cmd))
    with open(s, "w") as f:  # one message, two tool calls (logged as two entries repeating its usage)
        f.write(asst("m1", "2026-01-01T00:00", [bash("a", "git merge --ff-only work/x")], 1000) + "\n")
        f.write(asst("m1", "2026-01-01T00:00", [bash("b", "sed -i s/a/b/ docs/BOARD.md")], 1000) + "\n")
    sub = os.path.join(d, "s", "subagents", "agent-x")
    with open(sub + ".jsonl", "w") as f:
        f.write(asst("n1", "2026-01-01T00:01", [bash("c", "sleep 30; tail -3 run.log")], 500) + "\n")
        f.write(asst("n2", "2026-01-01T00:02", [bash("d", "sleep 30; tail -3 run.log")], 600) + "\n")
        f.write(asst("n3", "2026-01-01T00:03", [bash("e", "until grep -q done run.log; do sleep 5; done")], 700) + "\n")
        f.write(asst("n4", "2026-01-01T00:04", [bash("f", "dotnet test")], 800) + "\n")
    json.dump(dict(agentType="developer"), open(sub + ".meta.json", "w"))
    calls = load(s)
    agg, repeat, rctx = analyse(calls, PATTERNS)
    bad = []
    total = sum(c["share"] for c in calls)
    if total != 1000 + 500 + 600 + 700 + 800:
        bad.append(f"per-message split: total {total}, want 3600")
    if sum(c["ctx"] for c in calls) == total:
        bad.append("negative control: the unsplit sum should double-count message m1 and differ")
    if agg["land (producer: pull, rebase, apply, ff-merge, push, worktree remove)"]["ctx"] != 500:
        bad.append("land pattern should get half of m1's 1000")
    if (repeat, rctx) != (2, 1300):
        bad.append(f"wait chain: {repeat} repeats, {rctx} ctx; want 2 and 1300")
    print("selftest:", "FAIL\n  " + "\n  ".join(bad) if bad else "OK")
    return 1 if bad else 0

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("session", nargs="?")
    ap.add_argument("--from", dest="t0", default="")
    ap.add_argument("--to", dest="t1", default="~")
    ap.add_argument("--patterns")
    ap.add_argument("--top", type=int, default=20)
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        sys.exit(selftest())
    if not a.session:
        ap.error("SESSION_JSONL or --selftest")
    report(load(a.session, a.t0, a.t1), json.load(open(a.patterns)) if a.patterns else PATTERNS, a.top)
