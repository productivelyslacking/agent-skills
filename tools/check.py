#!/usr/bin/env python3
"""Checks the library's own consistency (Python 3 standard library only). Exits 1 with every problem.

- Every skills/<name>/SKILL.md has frontmatter with `name: <name>` and a `description`.
- The index in AGENTS.md (the source of truth) and the tables in README.md list exactly those skills.
- Every docs/CANDIDATES.md entry has the documented format.
- durable-knowledge's "Repo layout" section and tools/repo-layout.json agree: the tree, the four-questions table,
  every second form's .layout-check line, and every forbidden name (the section is the standard; the JSON is the
  copy layout-check reads).
- No role or skill tells a subagent to write its detail file under a name Claude Code's Write tool refuses
  to subagents (report.md, summary.md, findings.md; measured 2026-10-06), so briefs name a path that works.
- local-agents/ (the roles and rule sheet generated for Qwen Code and OpenCode) is current: tools/gen_local_agents.py --check
  (which also prints, without failing, a count of Claude-specific terms per file).
"""
import importlib.machinery, importlib.util, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
problems = []

DESC_MAX = 300
skills = sorted(p.name for p in (ROOT / "skills").iterdir() if p.is_dir())
for name in skills:
    path = ROOT / "skills" / name / "SKILL.md"
    if not path.exists():
        problems.append(f"skills/{name}: no SKILL.md")
        continue
    m = re.match(r"---\n(.*?)\n---\n", path.read_text(), re.S)
    if not m:
        problems.append(f"skills/{name}/SKILL.md: no frontmatter")
        continue
    front = dict(line.split(":", 1) for line in m.group(1).splitlines() if ":" in line)
    if front.get("name", "").strip() != name:
        problems.append(f"skills/{name}/SKILL.md: name is '{front.get('name', '').strip()}', not '{name}'")
    if len(front.get("description", "").strip()) < 40:
        problems.append(f"skills/{name}/SKILL.md: description missing or too short to trigger on")
    if len(front.get("description", "").strip()) > DESC_MAX:
        problems.append(f"skills/{name}/SKILL.md: description over {DESC_MAX} characters (loaded every session)")

# Text every session loads, in characters (about 3.6 per token). Raise a budget only with a reason in DECISIONS (D28).
DESC_MAX, ROLE_DESC_MAX, AGENTS_MAX = 300, 420, 5500
for role in sorted((ROOT / "agents").glob("*.md")):
    d = re.search(r"^description: (.*)$", role.read_text(), re.M)
    if d and len(d.group(1)) > ROLE_DESC_MAX:
        problems.append(f"agents/{role.name}: description over {ROLE_DESC_MAX} characters (loaded every session)")
if len((ROOT / "AGENTS.md").read_text()) > AGENTS_MAX:
    problems.append(f"AGENTS.md: over {AGENTS_MAX} characters (loaded every session)")

def table_names(file):
    return sorted(re.findall(r"^\| \*\*([a-z0-9-]+)\*\* \|", (ROOT / file).read_text(), re.M))

for file in ("AGENTS.md", "README.md"):
    listed = table_names(file)
    for name in sorted(set(skills) - set(listed)):
        problems.append(f"{file}: skill '{name}' is missing from its table")
    for name in sorted(set(listed) - set(skills)):
        problems.append(f"{file}: lists '{name}', which has no skills/ folder")
    for name in sorted({n for n in listed if listed.count(n) > 1}):
        problems.append(f"{file}: lists '{name}' twice")

# Candidates (durable-knowledge, "Feeding the library"; D29, D31): every entry after the Format line is checked on its
# own, from any line that starts a list item or a heading, so a malformed entry can't hide inside its neighbour.
import datetime
CANDIDATES_MAX, CANDIDATE_DAYS, SKILL_BODY_MAX, ROLE_BODY_MAX = 30, 90, 18000, 7000
entry = re.compile(r"- \*\*(\d{4}-\d{2}-\d{2}), [a-z0-9-]+ - .+?\*\* .+ Target: [^\n]+\.", re.S)
text = (ROOT / "docs/CANDIDATES.md").read_text()
body = text.split("\nFormat:", 1)[-1].split("\n", 1)[-1] if "\nFormat:" in text else text
blocks = [b.strip() for b in re.split(r"\n(?=- |#)", "\n" + body) if b.strip()]
for b in blocks:
    m = entry.fullmatch(b)
    try:
        when = datetime.date.fromisoformat(m.group(1)) if m else None
    except ValueError:
        when = None
    if not when:
        problems.append(f"docs/CANDIDATES.md: entry doesn't match the format (date, project kind, Target): {b[:60]}...")
    elif (datetime.date.today() - when).days > CANDIDATE_DAYS:
        problems.append(f"docs/CANDIDATES.md: older than {CANDIDATE_DAYS} days with no second sighting: {b[:60]}...")
if len(blocks) > CANDIDATES_MAX:
    problems.append(f"docs/CANDIDATES.md: {len(blocks)} entries, over {CANDIDATES_MAX}: review with the owner (promote, merge, drop)")
for path, limit in [(p, SKILL_BODY_MAX) for p in sorted((ROOT / "skills").glob("*/SKILL.md"))] +                    [(p, ROLE_BODY_MAX) for p in sorted((ROOT / "agents").glob("*.md"))]:
    body = path.read_text().split("---", 2)[-1]
    if len(body) > limit:
        problems.append(f"{path.relative_to(ROOT)}: body {len(body)} characters, over {limit}: cut or merge rules")

# What loads, in characters (D31): the core loads for nearly every task, so it has a joint limit; the totals print on
# every run so a change's net growth is visible. NOTES.md loads only when cited and has no limit.
CORE_MAX = 20000
core = len((ROOT / "AGENTS.md").read_text()) + len((ROOT / "skills/ground-truth/SKILL.md").read_text().split("---", 2)[-1])
if core > CORE_MAX:
    problems.append(f"AGENTS.md + ground-truth: {core} characters, over {CORE_MAX} (they load for nearly every task)")
sizes = {k: sum(len(p.read_text().split("---", 2)[-1]) for p in (ROOT / d).glob(g))
         for k, d, g in (("skills", "skills", "*/SKILL.md"), ("roles", "agents", "*.md"), ("notes", "skills", "*/NOTES.md"))}
print(f"loaded chars: core {core}, skill bodies {sizes['skills']}, role bodies {sizes['roles']}; on demand: notes {sizes['notes']}")

refused = re.compile(r"scratchpad/[^`\s]*\b(report|summary|findings)\.md", re.I)
for path in sorted(list((ROOT / "agents").glob("*.md")) + list((ROOT / "skills").glob("*/SKILL.md"))):
    for n, line in enumerate(path.read_text().splitlines(), 1):
        if refused.search(line):
            problems.append(f"{path.relative_to(ROOT)}:{n}: names a detail file the Write tool refuses to subagents; use details.md")

loader = importlib.machinery.SourceFileLoader("layout_check", str(ROOT / "tools/layout-check"))
layout = importlib.util.module_from_spec(importlib.util.spec_from_loader("layout_check", loader))
loader.exec_module(layout)
spec = layout.load_spec(ROOT / "tools/repo-layout.json")
dk = (ROOT / "skills/durable-knowledge/SKILL.md").read_text()
section = dk[dk.find("\n## Repo layout\n"):]
section = section[:section.find("\n## ", 1)] if "\n## " in section[1:] else section
where = "skills/durable-knowledge/SKILL.md, \"Repo layout\""
block = re.search(r"```\n(.*?)\n```", section, re.S)
if not section:
    problems.append(f"{where}: section not found")
elif not block or block.group(1) != layout.tree(spec):
    problems.append(f"{where}: its tree differs from tools/repo-layout.json (tools/layout-check --tree prints the JSON's)")
rows = re.findall(r"^\| (.+?) \| (.+?) \|$", section, re.M)
want = [(q["question"], q["where"]) for q in spec["questions"]]
if [r for r in rows if r[0].endswith("?")] != want:
    problems.append(f"{where}: its four-questions table differs from tools/repo-layout.json")
for rule in spec["forbidden"]:
    if f"`{rule['pattern']}`" not in section:
        problems.append(f"{where}: doesn't name `{rule['pattern']}`, which tools/repo-layout.json forbids")
for name, form in spec["forms"].items():
    if name != "about" and f"\n{form['line']}\n" not in section:
        problems.append(f"{where}: doesn't give form {name}'s .layout-check line as tools/repo-layout.json does: "
                        f"{form['line']}")

sys.path.insert(0, str(ROOT / "tools"))
import gen_local_agents
problems += gen_local_agents.check(ROOT)

for p in problems:
    print(p)
print(f"{len(skills)} skills checked: {'OK' if not problems else f'{len(problems)} problem(s)'}")
sys.exit(1 if problems else 0)
