#!/usr/bin/env python3
"""Checks that every requirement in docs/REQUIREMENTS.tsv is still in the rule sheet or role it names, and that
every source tag in those files has its full quote there (Python 3 standard library only). Exits 1 naming each
problem. Usage: check_requirements.py [REPO]

- Each row's must_contain phrases (joined by " && ") appear in its file, compared with runs of whitespace
  collapsed, so rewrapping a line is not a change. Rewording a rule means updating its row in the same commit;
  dropping a rule means deleting its row, which a reviewer sees in the diff (docs/DECISIONS.md, D6).
- A source tag ("owner, YYYY-MM-DD" or "(D<n>)") in AGENTS.md or agents/*.md resolves to a row for that file with
  that tag and a full quote. A row with a tag needs its quote, and its tag inside its own phrases.
- A row's quote is not also inline in AGENTS.md or agents/*.md (no six-word run of it): quotes live here.
- A row naming a decision has its quote verbatim in that docs/DECISIONS.md entry.
- Rows for the rules only local agents get (L01...) name tools/gen_local_agents.py, which holds them; rows for a
  rule a skill sets for every role (G01, the brief's Ownership) name that skill's SKILL.md. Those files are checked
  for their rows' phrases only (they carry no source tags).
- A `core` cell, the row's line on the local agents' core rules (tools/gen_local_agents.py writes them), is one
  line of at most CORE_MAX characters, and has a `scope`: `all` (the shared sheet, local-agents/qwen/AGENTS-core.md)
  for a rule from AGENTS.md, tools/gen_local_agents.py or a skill, which hold for every role; or the role's name
  (that role's core-mode file only) for a rule from agents/<role>.md. A role's rule scoped to `all` or to another
  role fails, so a rule like the developer's "never merge" can't reach the merge-reviewer.
"""
import csv, pathlib, re, sys

COLUMNS = ["id", "rule", "was (file:line at 8c17427)", "file", "must_contain", "tag", "quote", "date",
           "quote_source", "decision", "core", "scope"]
LOCAL = "tools/gen_local_agents.py"  # where the local-agent-only rules live
CORE_MAX = 200
TAG = re.compile(r"\b(?:user|owner), \d{4}-\d{2}-\d{2}\b|(?<=\()D\d+(?=\))")


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def words(s):
    return re.findall(r"[a-z0-9']+", s.lower())


def check(root):
    root = pathlib.Path(root)
    problems = []
    with open(root / "docs/REQUIREMENTS.tsv", newline="") as f:
        rows = list(csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE))
    if not rows or list(rows[0]) != COLUMNS:
        return [f"docs/REQUIREMENTS.tsv: columns must be {COLUMNS}"]
    targets = [root / "AGENTS.md"] + sorted((root / "agents").glob("*.md"))
    text = {str(p.relative_to(root)): p.read_text() for p in targets}
    flat = {k: norm(v) for k, v in text.items()}
    flat[LOCAL] = norm((root / LOCAL).read_text()) if (root / LOCAL).exists() else ""
    for p in sorted((root / "skills").glob("*/SKILL.md")):  # phrases only, like LOCAL
        flat[str(p.relative_to(root))] = norm(p.read_text())
    shared = {"AGENTS.md", LOCAL} | {k for k in flat if k.startswith("skills/")}
    roles = {pathlib.Path(k).stem for k in text if k.startswith("agents/")}
    decisions = (root / "docs/DECISIONS.md").read_text()
    ids = [r["id"] for r in rows]
    for rid in sorted({i for i in ids if ids.count(i) > 1}):
        problems.append(f"{rid}: id used twice")

    for r in rows:
        rid, f = r["id"], r["file"]
        if f not in flat:
            problems.append(f"{rid}: names {f}, which is not AGENTS.md, a role, a skill or {LOCAL}")
            continue
        phrases = [norm(p) for p in r["must_contain"].split(" && ") if p.strip()]
        if not phrases:
            problems.append(f"{rid}: no must_contain phrase ({r['rule'][:60]})")
        for p in phrases:
            if p not in flat[f]:
                problems.append(f"{rid} ({f}): requirement missing: \"{p[:90]}\" (rule: {r['rule'][:80]})")
        if r["tag"] and not r["quote"].strip():
            problems.append(f"{rid} ({f}): tag ({r['tag']}) has no quote (rule: {r['rule'][:80]})")
        if r["quote"].strip() and not r["tag"]:
            problems.append(f"{rid} ({f}): a quote with no tag, so no rule cites it")
        if r["tag"] and not any(r["tag"] in p for p in phrases):
            problems.append(f"{rid} ({f}): its tag ({r['tag']}) is not in its rule's phrases: a quote with no rule")
        if r["quote"].strip():
            q = words(r["quote"])
            for name, body in flat.items():
                if name not in text:  # LOCAL and skills hold no quotes
                    continue
                b = " ".join(words(body))
                runs = [" ".join(q[i:i + 6]) for i in range(max(1, len(q) - 5))]
                if any(run and f" {run} " in f" {b} " for run in runs):
                    problems.append(f"{rid}: its quote is still inline in {name}; it lives in docs/REQUIREMENTS.tsv")
        core = r["core"] or ""
        if core and (core != core.strip() or len(core) > CORE_MAX):
            problems.append(f"{rid}: core line has stray whitespace or is over {CORE_MAX} characters")
        scope = r["scope"] or ""
        if bool(core) != bool(scope):
            problems.append(f"{rid}: a core line needs a scope (all or a role) and a scope needs a core line")
        elif scope == "all" and f not in shared:
            problems.append(f"{rid}: scoped to all, but it comes from {f}, one role's file: scope it to that role")
        elif scope and scope != "all" and f != f"agents/{scope}.md":
            what = "no role" if scope not in roles else f"agents/{scope}.md"
            problems.append(f"{rid}: scoped to {scope} ({what}), but it comes from {f}")
        if r["decision"]:
            m = re.search(rf"^## {re.escape(r['decision'])} - .*?(?=^## |\Z)", decisions, re.M | re.S)
            if not m:
                problems.append(f"{rid}: names decision {r['decision']}, which docs/DECISIONS.md lacks")
            elif norm(r["quote"]) not in norm(m.group(0)):
                problems.append(f"{rid}: {r['decision']} in docs/DECISIONS.md lacks the quote verbatim")

    quoted = {(r["file"], r["tag"]) for r in rows if r["tag"] and r["quote"].strip()}
    for name, body in text.items():
        for n, line in enumerate(body.splitlines(), 1):
            for m in TAG.finditer(line):
                if (name, m.group(0)) not in quoted:
                    problems.append(f"{name}:{n}: source tag ({m.group(0)}) has no row with its quote in "
                                    "docs/REQUIREMENTS.tsv")
    return problems


if __name__ == "__main__":
    root = sys.argv[1] if len(sys.argv) > 1 else pathlib.Path(__file__).resolve().parents[1]
    found = check(root)
    for p in found:
        print(p)
    if found:
        sys.exit(1)
    print("requirements: every row found, every tag quoted")
