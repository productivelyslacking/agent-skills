#!/usr/bin/env python3
"""Generates the library's role agents for Qwen Code, the studio's local-LLM agent tool, and installs the
library for it (Python 3 standard library only); also generates the roles for OpenCode (tools/sync-opencode installs those). agents/*.md, skills/ and AGENTS.md stay the one source;
local-agents/ is generated from them, committed, and checked for staleness.

    python3 tools/gen_local_agents.py                  write local-agents/ from agents/*.md and the library text
    python3 tools/gen_local_agents.py --check          exit 1 if local-agents/ is stale or the core sheet is over
                                                       its token budget; prints (doesn't fail on) a count of
                                                       Claude-specific terms per file
    python3 tools/gen_local_agents.py --install        link the outputs into ~/.qwen, set the owned settings keys,
                                                       and record everything (with prior values) in the manifest;
                                                       rerun (or --sync, from the hooks), it updates only what is
                                                       still as it wrote it, and reports ("kept ...") the rest
    python3 tools/gen_local_agents.py --install --rules core   the same, with the short core sheet as ~/.qwen/AGENTS.md
                                                       and roles that point at it (--rules full goes back; the
                                                       choice is recorded, and --sync and the hooks keep it)
    python3 tools/gen_local_agents.py --check-install  exit 1 if the install is missing, stale or points elsewhere
    python3 tools/gen_local_agents.py --uninstall      remove what the install owns and put back what the manifest
                                                       says was there before; a key, link or file the user changed
                                                       since is left as the user left it
    python3 tools/gen_local_agents.py --install-hooks  add post-merge and post-checkout hooks to this clone's
                                                       .git/hooks (an existing hook of the same name still runs
                                                       first), so a pull or checkout that changes agents/, skills/
                                                       or AGENTS.md reruns --sync; --uninstall-hooks undoes it

Interrupt safety: --install, --sync and --uninstall take a lock (flock on STATE_DIR/lock), so two runs serialise.
Each plans every change first and writes the plan (the journal) before making any; each file or link is replaced
by an atomic rename. A run killed halfway leaves the journal, and the next run finishes it before doing its own.

What Qwen Code 0.25.0 reads (its source at tag v0.25.0, read 2026-10-08):
- skills: ~/.qwen/skills, ~/.agents/skills and settings `skills.directories` (core/src/skills/skill-manager.ts),
  through its `skill` tool, which it withholds inside its execution sandbox (docs/users/features/sandbox.md);
  ~/.qwen/SKILLS.md, written here, lists each skill's file to read instead.
- agents: ~/.qwen/agents/*.md, Claude Code's frontmatter, but `tools` must be Qwen's own tool names
  (subagent-manager.ts resolveToolNames keeps an unknown name and the tool is then simply absent).
- context files: ~/.qwen/<name> and the workspace's, for each settings `context.fileName`; imports outside the
  file's git root are refused (utils/memoryImportProcessor.ts), so the rule sheet can't be imported: its text is
  copied into local-agents/qwen/AGENTS.md after the preamble (PREAMBLE), and that file is linked.
- rule files: only the start folder's and its parents', at start (memoryDiscovery.ts). A subfolder's AGENTS.md is
  never loaded and telling the model to read it failed 3 of 3 live runs (2026-10-08), so an agent has to be
  started in the folder it works in; LOCAL-TOOLS.md says so.

OpenCode (D35): local-agents/opencode/ holds the roles in OpenCode's v2 agent format and the same rule-sheet wrapper;
tools/sync-opencode links them in. What OpenCode 2.2.7 reads, checked on it 2026-11-13: agents from
~/.config/opencode/agents/*.md, where a file with Claude Code's frontmatter (`tools:` as a string, a colour name) is
skipped with only a log warning; permissions as an ordered list, last match wins (opencode.ai/docs/permissions).
"""
import argparse, base64, csv, fcntl, hashlib, json, math, os, pathlib, re, signal, stat, subprocess, sys
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = "local-agents"
HOME = pathlib.Path.home()
QW_DIR = HOME / ".qwen"
OC_DIR = HOME / ".config" / "opencode"  # the pre-manifest builds' opencode.json keys, cleaned up by --uninstall
STATE_DIR = HOME / ".local" / "state" / "gen_local_agents"
MANIFEST = STATE_DIR / "manifest.json"
JOURNAL = STATE_DIR / "journal.json"  # the planned changes of a run in progress; present only if it was interrupted
LOCK = STATE_DIR / "lock"
MADE_DIRS = STATE_DIR / "made-dirs.json"  # the folders above STATE_DIR this script created, for --uninstall
PRIVATE = 0o600  # mode of every file in STATE_DIR: they hold copies of settings.json, which can hold an API key
TMP = ".gen_local_agents.tmp"  # suffix of a file's temporary copy, in the same folder, before the atomic rename
MARK = "GENERATED by tools/gen_local_agents.py"
# Every generated role and the rule-sheet wrapper start with this (producer, 2026-10-08): a list of Claude-only
# phrasings can never be complete (a review found 17 of 20 new ones passing), so the agent is told the class instead.
PREAMBLE = ("Some instructions below mention Claude Code features (its tools such as Agent, Skill, SendMessage, plan "
            "mode, slash commands, scratchpad, permission prompts or settings) that don't exist here. Ignore those "
            "parts and use your own tools; when an instruction depends on one, say so in your hand-back.")
# Local agents commit as themselves, never as the user (the coordinator, 2026-10-08: a paused retest's agents set
# git config and committed as the user). Qwen Code gets it through settings `env`.
AGENT_NAME, AGENT_EMAIL = "local-agent", "local-agent@forge.local"

# Claude Code tool name -> Qwen Code tool names. A tool name not listed here stops the generator: a new tool in
# an agent needs a mapping decision, not a silent drop.
QWEN = {
    "Read": ["read_file"], "Edit": ["edit"], "Write": ["write_file"], "NotebookEdit": ["notebook_edit"],
    "Glob": ["glob", "list_directory"], "Grep": ["grep_search"], "Bash": ["run_shell_command"],
    "WebFetch": ["web_fetch"], "WebSearch": ["web_search"], "Skill": ["skill"], "Agent": ["agent"],
    "Task": ["agent"], "TodoWrite": ["todo_write"],
}
# Claude Code tool name -> OpenCode v2 permission actions (opencode.ai/docs/permissions, read 2026-11-13; the names
# match `opencode debug agents` on 2.2.7). Edit, Write and NotebookEdit are all `edit` there. TodoWrite has none:
# OpenCode's todos are an experimental flag, not a permission.
OPENCODE = {
    "Read": ["read"], "Edit": ["edit"], "Write": ["edit"], "NotebookEdit": ["edit"], "Glob": ["glob"],
    "Grep": ["grep"], "Bash": ["shell"], "WebFetch": ["webfetch"], "WebSearch": ["websearch"], "Skill": ["skill"],
    "Agent": ["subagent"], "Task": ["subagent"], "TodoWrite": [],
}
# Claude Code's agent colours -> the six-digit hex OpenCode requires (a name makes it skip the file).
COLORS = {"red": "#e5484d", "orange": "#f76b15", "yellow": "#ffc53d", "green": "#30a46c", "blue": "#0090ff",
          "purple": "#8e4ec6", "pink": "#d6409f", "cyan": "#00a2c7"}

# Claude-specific terms in the library's text a Qwen Code agent reads (a role's description and body: the generator
# rewrites the rest of its frontmatter). Each is (id, pattern, what it means for a Qwen Code agent); the explanation
# goes into LOCAL-TOOLS.md, and --check prints a count of hits per file as a report, not a gate: no list can name
# every Claude-only phrasing, so PREAMBLE tells the agent the class (producer, 2026-10-08). The terms that stay are
# the ones with a useful substitute (the scratch folder, the web-search cap, the tool table). CATCH_ALL below counts
# every mention of Claude or Anthropic no term covers.
TERMS = [
    ("claude-md", r"CLAUDE\.md",
     "A folder's CLAUDE.md (or AGENTS.md) is its rule file. Qwen Code loads only the ones in the folder it was "
     "started in and that folder's parents, once, at start; nothing loads a subfolder's or another folder's when you "
     "work there, and being told to read them first proved unreliable (3 of 3 test runs didn't). So the person "
     "starting you starts you in the folder you work in. If your task takes you into another folder that has its own "
     "AGENTS.md or CLAUDE.md, read it before changing anything there and say in your report that you did. Where a "
     "line says CLAUDE.md arrives by itself or not to open it, that is Claude Code's behaviour: here, do read it. "
     "`~/.claude/CLAUDE.md` is Claude Code's machine file; yours are ~/.qwen/AGENTS.md (this rule sheet) and "
     "~/.qwen/CLAUDE.md (machine facts)."),
    ("claude-home", r"~/\.claude\b",
     "Claude Code's user folder. Yours is ~/.qwen: the rule sheet ~/.qwen/AGENTS.md, the skills listed in "
     "~/.qwen/SKILLS.md, the roles in ~/.qwen/agents/, session logs under ~/.qwen/projects/<project>/."),
    ("dot-claude", r"(?<![\w/~])\.claude/",
     "A project's .claude/ folder holds Claude Code's per-project roles and skills. Qwen Code reads .qwen/agents/ "
     "and .qwen/skills/ (or .agents/skills/) instead."),
    ("claude-code", r"\bClaude Code\b", "Describes Claude Code itself: background, not how this tool behaves."),
    ("claude-env", r"\bCLAUDE_CODE_\w+",
     "A Claude Code environment setting; Qwen Code doesn't read it. CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION has a "
     "twin: Qwen Code also stops `web_search` at 200 calls a session by default (`tools.webSearch.maxPerSession` or "
     "WEB_SEARCH_MAX_PER_SESSION, core/src/tools/web-search.ts), so a research brief's search budget holds as "
     "written. Inside Qwen Code's sandbox you have no web_search at all: say a research task needs it."),
    ("scratchpad", r"(?i)scratch ?pad",
     "Claude Code gives each session a scratch folder (the session scratchpad); `scratchpad/<task>/` means your "
     "task's folder in it. You have no scratchpad: use the per-task folder your brief names; if it names none, use "
     "`scratch/<task>/` in the folder you were started in (the sandbox refuses writes outside it), don't commit it, "
     "and give its absolute path in your report."),
    ("plan-mode", r"(?i)\bplan mode\b",
     "Claude Code's read-only planning mode. Qwen Code's is the `plan` approval mode, which the user sets (/plan); "
     "you can't switch it."),
    ("slash-command", r"(?<![\w/.~\])>-])/[a-z][a-z-]*(?![\w/.(-])",
     "A word starting with `/`: a path (the library's hits, /tmp and the `AudioStreamWAV`/playback pair, are these) "
     "or a Claude Code slash command (/compact, /clear, /context), which the user types, not you. Qwen Code's "
     "differ (/compress for /compact; /help lists them)."),
    ("compaction", r"(?i)\bcompact(?:ion|ed|s)?\b",
     "Claude Code's context compaction (/compact). Qwen Code compresses the chat history near its limit too (/compress "
     "by hand); what isn't in a file is lost either way, so the advice holds."),
    ("model-name", r"(?i)\b(?:opus|sonnet|haiku)\b",
     "A Claude model. You run whatever model the local endpoint serves; where a brief or role asks for a Claude model, "
     "use yours and name it in your report."),
    ("mcp", r"(?i)\bmcp\b|\.mcp\.json",
     "Claude Code's MCP servers (.mcp.json). Qwen Code has its own in settings `mcpServers`; this library installs none, "
     "so say a tool you'd need is missing."),
    ("claude-feature",
     r"(?i)\b(?:sub-?agents?|hooks?|artifacts?|plugins?|auto[- ]?memory|MEMORY\.md|output styles?|status ?line|"
     r"auto mode|permission mode|settings(?:\.local)?\.json)\b",
     "A Claude Code feature, or a word that names one. Subagents are your roles, started with the `agent` tool; "
     "plugins, output styles, auto memory and artifacts in the sense of Claude's published pages (\"artifacts, external "
     "pages\") you don't have: say so. The word artifact in its general sense (a file, a build's or deployment's "
     "output, the evidence behind a claim) is the library's own and holds as written; so is a build or git hook."),
    ("tool-name", r"\b(Read|Write|Edit|Bash|Glob|Grep|WebFetch|WebSearch|TodoWrite|Task|Agent|Skill) tool\b",
     "A Claude Code tool name; the table above gives yours."),
    ("claude-tool", r"\b(SendMessage|SubagentHandback|AskUserQuestion|ToolSearch|ScheduleWakeup|Artifact|Monitor tool)\b",
     "A Claude Code tool you don't have: say so rather than improvise one."),
    ("agent-setting", r"isolation: worktree|permissionMode|run_in_background",
     "A Claude Code agent setting. Inside Qwen Code's sandbox the `agent` tool refuses worktree agents."),
    ("session-log", r"subagents/\*\.jsonl|\.meta\.json",
     "Claude Code's session-log layout. Qwen Code's: ~/.qwen/projects/<project>/chats/*.jsonl and "
     "subagents/<session>/agent-*.jsonl with .meta.json."),
    ("claude-cli", r"\bclaude -p\b|/context\b", "The Claude Code command line; not available here."),
    ("identity", r"project's identity|commit(?:s|ted)? as [A-Z]|user\.(?:name|email)",
     f"An identity rule. You commit as {AGENT_NAME} <{AGENT_EMAIL}>, never as the user."),
    # Filled by scan(): each CATCH_ALL hit outside every match above.
    ("claude-other", None,
     "Names Claude, Anthropic or a Claude Code piece no line above covers: background about the tool the library was "
     "written for. Anything it asks you to use that you don't have: say so, don't improvise it."),
]
CATCH_ALL = r"(?i)claude|anthropic"


def rules_file(root):
    """The library's rule sheet and skill index: AGENTS.md when it exists, else CLAUDE.md, following CLAUDE.md
    when all it holds is `@file` import lines (the layout where CLAUDE.md is `@AGENTS.md`). Qwen Code doesn't
    follow such an import from ~/.qwen, so the file linked must be the one with the text. Stops on a dangling or
    empty one rather than handing the tool an empty rule sheet."""
    agents = root / "AGENTS.md"
    if agents.exists():
        path = agents
    else:
        path = root / "CLAUDE.md"
        if not path.exists():
            sys.exit(f"{root}: neither AGENTS.md nor CLAUDE.md exists")
        lines = [l.strip() for l in path.read_text().splitlines() if l.strip()]
        if lines and all(l.startswith("@") for l in lines):
            if len(lines) > 1:
                sys.exit(f"{path}: imports {len(lines)} files; the local tools need one rule-sheet file")
            path = root / lines[0][1:]  # an absolute import replaces root
            if not path.exists():
                sys.exit(f"{root / 'CLAUDE.md'}: imports {lines[0][1:]}, which doesn't exist")
    if not path.read_text().strip():
        sys.exit(f"{path}: the rule sheet is empty")
    return path


def blob(path):
    """The file's git blob hash (what `git hash-object` prints), so a generated file names its exact source."""
    data = path.read_bytes()
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def frontmatter(path):
    text = path.read_text()
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not m:
        sys.exit(f"{path}: no frontmatter")
    front = {}
    for line in m.group(1).splitlines():
        key, _, value = line.partition(":")
        front[key.strip()] = value.strip()
    return front, text[m.end():]


def tool_list(front, key, path):
    names = [t.strip() for t in front.get(key, "").split(",") if t.strip()]
    unknown = [t for t in names if t not in QWEN or t not in OPENCODE]
    if unknown:
        sys.exit(f"{path}: {key} names {unknown}, which have no mapping in tools/gen_local_agents.py")
    return names


def q(s):
    return json.dumps(s, ensure_ascii=False)


def qwen_agent(root, path):
    front, body = frontmatter(path)
    if front.get("model", "inherit") != "inherit":
        sys.exit(f"{path}: model '{front['model']}' has no local mapping (only inherit does)")
    names = tool_list(front, "tools", path)
    allowed = [n for t in names for n in QWEN[t]]
    denied = [n for t in tool_list(front, "disallowedTools", path) for n in QWEN[t]]
    allowed = [n for i, n in enumerate(allowed) if n not in denied and n not in allowed[:i]]
    lines = ["---", f"name: {q(front['name'])}", f"description: {q(front['description'])}",
             f"tools: [{', '.join(allowed)}]"]
    if denied:
        lines.append(f"disallowedTools: [{', '.join(dict.fromkeys(denied))}]")
    if front.get("color"):
        lines.append(f"color: {front['color']}")
    lines.append("---")
    rel = path.relative_to(root)
    pairs = ", ".join(f"{k}={'/'.join(QWEN[k])}" for k in names)
    note = (f"<!-- {MARK} from {rel} (git blob {blob(path)}); edit that file, not this one. -->\n"
            f"{PREAMBLE}\n\n"
            f"(For Qwen Code: this role's text uses Claude Code's tool names; yours are {pairs}. Only the rule files"
            f" of the folder you were started in and its parents were loaded; if you work in another folder that has an"
            f" AGENTS.md or CLAUDE.md, read it before changing anything there and say so in your report. Where the text"
            f" says `scratchpad/<task>/`, use the per-task folder your brief names, else `scratch/<task>/` in the folder"
            f" you were started in, and give its absolute path."
            f" Commit as {AGENT_NAME} <{AGENT_EMAIL}>, never with the user's or \"the project's\" identity."
            f" Where the text names something only Claude Code has, LOCAL-TOOLS.md in your instructions says what"
            f" to do instead.)\n\n")
    return "\n".join(lines) + "\n" + note + body


def scanned(root):
    return [rules_file(root)] + sorted((root / "skills").glob("*/SKILL.md")) + sorted((root / "agents").glob("*.md"))


def agent_text(path):
    """The part of a role a Qwen Code agent reads as written: its description (carried into the generated role)
    and its body."""
    front, body = frontmatter(path)
    return f"description: {front.get('description', '')}\n{body}"


def scan(root):
    """{term id: {relative path: hits}} over the text a Qwen Code agent reads: roles' descriptions and bodies,
    skills and the rule sheet whole. claude-other counts each CATCH_ALL hit that no other term's match covers."""
    found = {tid: {} for tid, _, _ in TERMS}
    for path in scanned(root):
        rel = str(path.relative_to(root))
        body = agent_text(path) if rel.startswith("agents/") else path.read_text()
        spans = []
        for tid, pattern, _ in TERMS:
            if pattern is None:
                continue
            ms = list(re.finditer(pattern, body))
            spans += [m.span() for m in ms]
            if ms:
                found[tid][rel] = len(ms)
        other = [m for m in re.finditer(CATCH_ALL, body) if not any(a <= m.start() < b for a, b in spans)]
        if other:
            found["claude-other"][rel] = len(other)
    return found


def term_report(root):
    """Lines for --check: each scanned file's hits per term. A report, not a failure (see TERMS)."""
    found, by_file = scan(root), {}
    for tid, hits in found.items():
        for rel, n in hits.items():
            by_file.setdefault(rel, []).append(f"{tid} {n}")
    return [f"terms: {rel}: {', '.join(v)}" for rel, v in sorted(by_file.items())]


def local_tools_note(root):
    found = scan(root)
    sources = sorted({rel for hits in found.values() for rel in hits})
    tools = "\n".join(f"| {k} | {', '.join(v)} |" for k, v in QWEN.items())
    terms = []
    for tid, _, explanation in TERMS:
        if found[tid]:
            files = ", ".join(f"`{rel}` ({n})" for rel, n in sorted(found[tid].items()))
            terms.append(f"- **{tid}**: {explanation} Appears in: {files}.")
    provenance = "\n".join(f"  {rel} (git blob {blob(root / rel)})" for rel in sources)
    return f"""<!-- {MARK} from the library text; regenerate, don't edit. Sources:
{provenance}
-->
# Using this skill library from Qwen Code

The working rules, skills and roles you were given were written for Claude Code. They hold here too, with
these translations.

- **Claude Code features you don't have:** every role and the rule sheet start with a note saying so. The
  text below lists the ones found in the library with what to use instead, but it can't name every one: where
  an instruction depends on a tool, mode, command or setting you don't have, skip that part and say so in your
  hand-back rather than improvising it.
- **Skills:** with a `skill` tool, load one by name when the work matches its description. Inside Qwen Code's
  execution sandbox you have none: SKILLS.md in your instructions lists each skill's description and file, so
  read that file with your read tool before starting the work it describes. "Load the X skill" means either.
- **Folder rule files (a known limitation):** Qwen Code reads AGENTS.md/CLAUDE.md only from the folder it was
  started in and that folder's parents, once, at start. A subfolder's or another folder's rule file is never
  loaded, and an instruction to read it first did not work: in 3 of 3 test runs (Qwen3-Coder-Next, 2026-10-08)
  the agent wrote into a subfolder without reading its AGENTS.md. The workaround is to start the agent in the
  folder it works in. If your task still takes you into another folder that has its own AGENTS.md or CLAUDE.md,
  read it before changing anything there and say in your report that you did.
- **Your identity:** commit as `{AGENT_NAME} <{AGENT_EMAIL}>` (set in your environment). Where a project's
  CLAUDE.md or a role says to commit as the user, under the user's name, or with "the project's identity", that
  is for Claude Code sessions: don't set `user.name`/`user.email`, `--author` or `-c user.*` to anyone else, or
  change the `GIT_AUTHOR_*`/`GIT_COMMITTER_*` variables.
  Keep the commit trailer, naming your own model.
- **Full or core rules:** this file is loaded with the full rule sheet (`--install`, or `--install --rules full`:
  the default until the 2026-10-08 agent-capability A/B test decides). `--install --rules core` loads instead the
  core sheet (`local-agents/qwen/AGENTS-core.md`, under {CORE_BUDGET} tokens: the rules every role keeps) and
  core-mode roles (`local-agents/qwen/agents-core/`, each with its own core rules and the identity rule); this file,
  the full sheet (~/.qwen/AGENTS-full.md) and SKILLS.md are then read when needed. Both are generated from
  `docs/REQUIREMENTS.tsv` (its `core` and `scope` columns) by `tools/gen_local_agents.py`; don't edit them.
- **Role agents** (designer, developer, qa, ...): start one with the `agent` tool (`subagent_type` = the role's
  name). Each role keeps the tool set its Claude Code file gives it; a role without edit tools cannot edit.
- **`@/path/file.md` lines** in a CLAUDE.md are Claude Code imports; the library's rule sheet is loaded separately.
- **Claude Code tool names** in the text, and yours:

| Claude Code | Qwen Code |
|---|---|
{tools}

## Claude-specific text, and how to read it

{chr(10).join(terms)}
"""


def rules_wrapper(root):
    """local-agents/qwen/AGENTS.md: PREAMBLE, then the rule sheet's text (Qwen Code won't import it from here)."""
    path = rules_file(root)
    rel = path.relative_to(root) if path.is_relative_to(root) else path
    return (f"<!-- {MARK} from {rel} (git blob {blob(path)}); edit that file, not this one. -->\n"
            f"{PREAMBLE}\n\n" + path.read_text())


# --- the core sheet ------------------------------------------------------------------------------------------------
# A short rule sheet for local models (the owner, 2026-10-08: two layers from one source, the full rules for Claude
# and a generated core sheet for local models). Its lines are the `core` cells of docs/REQUIREMENTS.tsv whose
# `scope` is `all` (rules every role keeps), in the file's order, each tagged with its row's id; a row scoped to a
# role goes in that role's core-mode file instead (producer, 2026-10-08: the developer's "never merge, push" on the
# shared sheet contradicted the merge-reviewer). The rows' must_contain phrases and scopes
# (tools/check_requirements.py) keep each line tied to a rule still in AGENTS.md, a role, a skill or this file.
# --install --rules core installs them.
REQUIREMENTS = "docs/REQUIREMENTS.tsv"
CORE_SHEET = f"{OUT}/qwen/AGENTS-core.md"
CORE_BUDGET = 450  # tokens, by the endpoint's tokenizer; --check fails above it
# Characters per token for the estimate --check uses (offline, the same in CI). Calibrated 2026-10-08 with the
# endpoint's tokenizer (Qwen3-Coder-Next, model "default"): AGENTS.md 5160 chars / 1220 tokens = 4.23,
# agents/developer.md 3690/887 = 4.16, agents/qa.md 2350/566 = 4.15, two drafts of the core sheet 1594/423 = 3.77
# and 1457/387 = 3.76 (its [id] tags and paths tokenize densely), and the shared-rules sheet with its source's git
# blob hash 1168/330 = 3.54 (the 40 hex digits cost 41 tokens). Set below the lowest, so the estimate counts high;
# tests/test_gen_local_agents.py TokenBudget re-measures the sheet on the endpoint and fails if it ever counts lower.
CHARS_PER_TOKEN = 3.2
ENDPOINT = "http://127.0.0.1:8081/tokenize?model=default"
ENDPOINT_KEY = HOME / ".config" / "llm-endpoint" / "api-key"
FULL_POINTER = ("For detail, read ~/.qwen/AGENTS-full.md (all rules), ~/.qwen/SKILLS.md (skills) or "
                "~/.qwen/LOCAL-TOOLS.md (Claude Code terms).")


def core_rows(root, scope="all"):
    """[(id, core line)] of the rows with a `core` line and this `scope` (`all`, or a role's name)."""
    if not (root / REQUIREMENTS).exists():
        sys.exit(f"{root / REQUIREMENTS}: missing; the core sheet is generated from it")
    with open(root / REQUIREMENTS, newline="") as f:
        rows = list(csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE))
    if rows and not {"core", "scope"} <= set(rows[0]):
        sys.exit(f"{root / REQUIREMENTS}: no `core` and `scope` columns")
    roles = {p.stem for p in (root / "agents").glob("*.md")}
    for r in rows:
        if (r.get("core") or "").strip() and (r.get("scope") or "") not in roles | {"all"}:
            sys.exit(f"{root / REQUIREMENTS}: {r['id']}: scope {r.get('scope')!r} is neither `all` nor a role")
    return [(r["id"], r["core"].strip()) for r in rows if (r.get("core") or "").strip() and r["scope"] == scope]


def identity_line(root):
    """The L01 core line, which every core-mode file carries: the role text's "the project's identity" is for
    Claude Code sessions, and in core mode LOCAL-TOOLS.md (which says so in full mode) isn't loaded."""
    line = dict(core_rows(root)).get("L01")
    if not line:
        sys.exit(f"{root / REQUIREMENTS}: L01 (the local agents' identity) has no core line scoped to all")
    return line


def core_sheet(root):
    rows = core_rows(root)
    if not rows:
        sys.exit(f"{root / REQUIREMENTS}: no row has a `core` line; the core sheet would be empty")
    identity_line(root)
    lines = "\n".join(f"- {text} [{rid}]" for rid, text in rows)
    return (f"<!-- {MARK} from {REQUIREMENTS} (git blob {blob(root / REQUIREMENTS)}); [id] is its row. -->\n"
            f"# Core rules\n\n{lines}\n\n{FULL_POINTER}\n")


def estimate_tokens(text):
    return math.ceil(len(text) / CHARS_PER_TOKEN)


def endpoint_tokens(text, timeout=5):
    """The endpoint tokenizer's count, or None if it can't be reached (no key file, refused, timed out). The key
    is read from its file and sent only to the local endpoint; it is never printed."""
    try:
        key = ENDPOINT_KEY.read_text().strip()
        req = urllib.request.Request(ENDPOINT, data=json.dumps({"model": "default", "content": text}).encode(),
                                     headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return len(json.load(resp)["tokens"])
    except (OSError, ValueError, KeyError):
        return None


def core_agent(root, path):
    """A role for --rules core: the role's own text, with a short note that points at the core sheet instead of
    restating the rules (folder rule files, Claude features) the full roles' note carries, then the identity rule
    (overriding the role's own, as the full note does) and the core lines scoped to this role."""
    full = qwen_agent(root, path)
    front_end = full.index("\n---\n") + 5
    front, body = frontmatter(path)
    rel = path.relative_to(root)
    pairs = ", ".join(f"{k}={'/'.join(QWEN[k])}" for k in tool_list(front, "tools", path))
    own = "".join(f"- {text} [{rid}]\n" for rid, text in core_rows(root, path.stem))
    note = (f"<!-- {MARK} from {rel} (git blob {blob(path)}) and {REQUIREMENTS} (git blob "
            f"{blob(root / REQUIREMENTS)}) for --rules core; edit those, not this. -->\n"
            f"(For Qwen Code: the core rules in your instructions hold here. This role's text uses Claude Code's tool"
            f" names; yours are {pairs}. Where it says `scratchpad/<task>/`, use the per-task folder your brief names,"
            f" else `scratch/<task>/` in the folder you were started in, and give its absolute path. Where it says"
            f" CLAUDE.md arrives by itself or not to open it, read it.)\n\n"
            f"Core rules for this role:\n"
            f"- {identity_line(root)} [L01] Where the text below says to commit with the project's identity or as"
            f" the user, that is for Claude Code sessions, not you.\n{own}\n")
    return full[:front_end] + note + body


def opencode_agent(root, path):
    """A role in OpenCode's v2 agent format: a subagent whose permissions deny everything, then allow the actions
    its Claude Code tools map to (last match wins). The id is the file name; `name` and `tools` are v1 fields."""
    front, body = frontmatter(path)
    if front.get("model", "inherit") != "inherit":
        sys.exit(f"{path}: model '{front['model']}' has no OpenCode mapping (only inherit does)")
    color = front.get("color")
    if color and color not in COLORS:
        sys.exit(f"{path}: color '{color}' has no hex value in tools/gen_local_agents.py COLORS")
    names = tool_list(front, "tools", path)
    denied = {a for t in tool_list(front, "disallowedTools", path) for a in OPENCODE[t]}
    actions = [a for a in dict.fromkeys(a for t in names for a in OPENCODE[t]) if a not in denied]
    # Roles work in worktrees outside the folder OpenCode started in, so paths outside it stay open, as in Claude Code.
    perms = [("*", "*", "deny")] + [(a, "*", "allow") for a in actions] + [("external_directory", "*", "allow")]
    if "read" in actions:  # OpenCode's own default: ask before reading a .env file (the deny-all above replaced it)
        perms += [("read", "*.env", "ask"), ("read", "*.env.*", "ask"), ("read", "*.env.example", "allow")]
    lines = ["---", f"description: {q(front['description'])}", "mode: subagent"]
    if color:
        lines.append(f"color: {q(COLORS[color])}")
    lines.append("permissions:")
    for action, resource, effect in perms:
        lines += [f"  - action: {q(action)}", f"    resource: {q(resource)}", f"    effect: {effect}"]
    lines.append("---")
    pairs = ", ".join(f"{k}={'/'.join(OPENCODE[k]) or 'none'}" for k in names)
    note = (f"<!-- {MARK} from {path.relative_to(root)} (git blob {blob(path)}); edit that file, not this one. -->\n"
            f"{PREAMBLE}\n\n"
            f"(For OpenCode: this role's text uses Claude Code's tool names; your permissions are {pairs}. Load a skill"
            f" with the `skill` tool. Where the text says `scratchpad/<task>/`, use the per-task folder your brief"
            f" names, else `scratch/<task>/` in the folder you were started in, and give its absolute path. Where it"
            f" says a project's CLAUDE.md arrives by itself or not to open it, read it yourself before changing"
            f" anything there: OpenCode may not have loaded it.)\n\n")
    return "\n".join(lines) + "\n" + note + body


def generate(root):
    out = {f"{OUT}/LOCAL-TOOLS.md": local_tools_note(root), f"{OUT}/qwen/AGENTS.md": rules_wrapper(root),
           CORE_SHEET: core_sheet(root), f"{OUT}/opencode/AGENTS.md": rules_wrapper(root)}
    for path in sorted((root / "agents").glob("*.md")):
        out[f"{OUT}/qwen/agents/{path.name}"] = qwen_agent(root, path)
        out[f"{OUT}/qwen/agents-core/{path.name}"] = core_agent(root, path)
        out[f"{OUT}/opencode/agents/{path.name}"] = opencode_agent(root, path)
    return out


def budget(root):
    """(estimated tokens, problem or None) for the core sheet as the library generates it now."""
    text = core_sheet(root)
    n = estimate_tokens(text)
    problem = (f"{CORE_SHEET}: about {n} tokens (estimate, {CHARS_PER_TOKEN} chars/token), over the budget of "
               f"{CORE_BUDGET}: shorten or unmark core lines in {REQUIREMENTS}") if n > CORE_BUDGET else None
    return n, problem


def check(root):
    """Problems with root/local-agents against what root's sources generate, and the core sheet over its token
    budget (by the estimate, which counts high, so it holds offline and in CI); [] when current."""
    problems = [p for p in [budget(root)[1]] if p]
    want = generate(root)
    for rel, text in want.items():
        path = root / rel
        if not path.exists():
            problems.append(f"{rel}: missing (run tools/gen_local_agents.py)")
        elif path.read_text() != text:
            problems.append(f"{rel}: stale (run tools/gen_local_agents.py)")
    have = {str(p.relative_to(root)) for p in (root / OUT).rglob("*") if p.is_file()} if (root / OUT).exists() else set()
    for rel in sorted(have - set(want)):
        problems.append(f"{rel}: generated file with no source (delete it or rerun the generator)")
    return problems


# --- install -------------------------------------------------------------------------------------------------

RULES = ("full", "core")  # --rules: which rule sheet and roles --install links; recorded in the manifest
DEFAULT_RULES = "full"  # until the agent-capability A/B test (2026-10-08) says which serves local models better


def links(root, rules):
    """(link, target) pairs --install creates. `core`: ~/.qwen/AGENTS.md is the core sheet, the roles are the
    agents-core/ ones, and the full sheet is linked as ~/.qwen/AGENTS-full.md (read on demand, not loaded)."""
    roles = "agents" if rules == "full" else "agents-core"
    pairs = [(QW_DIR / "agents" / p.name, p) for p in sorted((root / OUT / "qwen" / roles).glob("*.md"))]
    full = root / OUT / "qwen" / "AGENTS.md"  # PREAMBLE, the rule sheet and skill index
    pairs += [(QW_DIR / "AGENTS.md", full)] if rules == "full" else [
        (QW_DIR / "AGENTS.md", root / CORE_SHEET), (QW_DIR / "AGENTS-full.md", full)]
    pairs += [
        (QW_DIR / "CLAUDE.md", HOME / ".claude" / "CLAUDE.md"),  # this machine's own facts
        (QW_DIR / "LOCAL-TOOLS.md", root / OUT / "LOCAL-TOOLS.md"),
    ]
    return pairs


def skills_index(root):
    """~/.qwen/SKILLS.md: the stand-in for the skill tool, which Qwen Code withholds inside its execution
    sandbox (docs/users/features/sandbox.md, "the model Skill tool remain[s] unavailable"). Written at install
    because it names this clone's absolute paths."""
    rows = []
    for path in sorted((root / "skills").glob("*/SKILL.md")):
        front, _ = frontmatter(path)
        rows.append(f"- **{front['name']}** (`{path}`, git blob {blob(path)[:12]}): {front['description']}")
    return f"""<!-- {MARK} at install from {root / 'skills'}; rerun --install, don't edit. -->
# Skills

Each skill below is a file of working rules for one kind of work. When the work in front of you matches a
skill's description, read its file in full with your read tool before you start, and follow it. Load
**ground-truth** for any work that is more than trivial. If you also have a `skill` tool, it loads the same files.

{chr(10).join(rows)}
"""


def generated_files(root):
    """(path, text) files --install writes (not links: their text depends on where the clone is)."""
    return [(QW_DIR / "SKILLS.md", skills_index(root))]


# List-valued keys are merged into a user's own list (our items appended, recorded); any other key with a
# different value already there stops the install.
MERGED = {"skills.directories", "context.fileName"}


def owned_settings(root, rules="full"):
    """(settings file, dotted key, value) that --install sets; other keys in those files are left alone. Under
    `core` the context files are the core sheet and machine facts only: LOCAL-TOOLS.md and SKILLS.md (3,044
    and 2,254 tokens, 2026-10-08) stay installed and are read on demand (the sheet's last line names them)."""
    s = QW_DIR / "settings.json"
    return [
        (s, "skills.directories", [str(root / "skills")]),
        # QWEN.md first: save_memory writes to the first name, so it lands in ~/.qwen/QWEN.md, not the library.
        (s, "context.fileName", ["QWEN.md", "AGENTS.md", "CLAUDE.md"] + (["LOCAL-TOOLS.md", "SKILLS.md"]
                                                                         if rules == "full" else [])),
        # Writes outside the workspace refused by the kernel (Landlock here: no bwrap, and unprivileged user
        # namespaces are restricted on Ubuntu 26.04), not by file modes: an opencode run chmod'ed a read-only file
        # and edited it (coordinator, 2026-10-08). Landlock can't close the network, so `open`.
        (s, "tools.executionSandbox", {"backend": "auto", "filesystem": "workspace-write", "network": "open"}),
        (s, "env.GIT_AUTHOR_NAME", AGENT_NAME),
        (s, "env.GIT_AUTHOR_EMAIL", AGENT_EMAIL),
        (s, "env.GIT_COMMITTER_NAME", AGENT_NAME),
        (s, "env.GIT_COMMITTER_EMAIL", AGENT_EMAIL),
        # Off: the co-author trailer and the refs/notes/ai-attribution git note (one switch, core/src/tools/shell.ts).
        (s, "general.gitCoAuthor", {"commit": False, "pr": False}),
        # As the studio's earlier Qwen Code trials (2026-10-07): no self-update, no usage statistics leaving the
        # machine (Qwen's default is on, cli/src/config/settingsSchema.ts).
        (s, "general.enableAutoUpdate", False),
        (s, "privacy.usageStatisticsEnabled", False),
    ]


MISSING = object()
BOM = b"\xef\xbb\xbf"


def parse_settings(raw, path):
    """(data, style) of a settings file's bytes; style = (BOM, line ending, ends with a newline), so a rewrite
    keeps the user's encoding and line endings. Stops on anything but a plain JSON object: Qwen Code accepts
    comments, and a rewrite here would drop them. Callers read every file before changing anything."""
    bom = raw.startswith(BOM)
    try:
        text = raw[len(BOM):].decode("utf-8") if bom else raw.decode("utf-8")
        data = json.loads(text) if text.strip() else {}
    except (UnicodeDecodeError, json.JSONDecodeError) as e:
        sys.exit(f"{path}: not plain JSON ({e}); nothing was changed. This script can't keep comments, so remove "
                 f"them (or move the file aside) and rerun")
    if not isinstance(data, dict):
        sys.exit(f"{path}: not a JSON object; nothing was changed")
    return data, (bom, "\r\n" if "\r\n" in text else "\n", text.endswith("\n"))


def read_settings(path):
    return parse_settings(path.read_bytes(), path) if path.exists() else ({}, (False, "\n", True))


def settings_bytes(data, style):
    bom, nl, final = style
    text = json.dumps(data, indent=2, ensure_ascii=False) + ("\n" if final else "")
    return (BOM if bom else b"") + text.replace("\n", nl).encode("utf-8")


def load(path):
    return read_settings(path)[0]


def get(d, dotted):
    for part in dotted.split("."):
        if not isinstance(d, dict) or part not in d:
            return MISSING
        d = d[part]
    return d


def put(d, dotted, value):
    *parents, last = dotted.split(".")
    for part in parents:
        d = d.setdefault(part, {})
    d[last] = value


def drop(d, dotted, keep=None):
    """Remove a dotted key, and any parent it leaves empty unless `keep` (the file before the install) had it."""
    part, _, rest = dotted.partition(".")
    if rest and isinstance(d.get(part), dict):
        sub = keep.get(part) if isinstance(keep, dict) else None
        drop(d[part], rest, sub)
        if not d[part] and not isinstance(sub, dict):
            del d[part]
    elif not rest:
        d.pop(part, None)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def show(value):
    return "absent" if value is MISSING else json.dumps(value)


def read_manifest():
    return json.loads(MANIFEST.read_text()) if MANIFEST.exists() else None


# --- interrupt-safe changes ----------------------------------------------------------------------------------------
# A run plans every change first (Plan), journals the plan with the manifest it leads to (commit), then makes the
# changes one by one (finish). A run killed at any point leaves either no journal (nothing changed yet) or the
# journal, which the next --install, --sync or --uninstall finishes before its own work (recover). Each change is
# an atomic rename or unlink, so no file is ever empty or half-written.

_points = [0]


def fault(label):
    """Test hook, off unless GEN_LOCAL_AGENTS_KILL_AT=N is set: SIGKILLs this process at the Nth point (the journal
    write, each change, each file write's middle, the manifest write), so the tests can interrupt a run at every
    one. GEN_LOCAL_AGENTS_TRACE=1 prints each point."""
    at = os.environ.get("GEN_LOCAL_AGENTS_KILL_AT")
    if not at:
        return
    _points[0] += 1
    if os.environ.get("GEN_LOCAL_AGENTS_TRACE"):
        print(f"point {_points[0]}: {label}", file=sys.stderr, flush=True)
    if _points[0] == int(at):
        os.kill(os.getpid(), signal.SIGKILL)


def tighten_state():
    """The journal and manifest hold copies of settings.json, which can hold an API key: the state folder is 0700
    and every file in it 0600, also when an older version of this script left them looser."""
    STATE_DIR.chmod(0o700)
    for p in STATE_DIR.iterdir():
        if p.is_file() and not p.is_symlink():
            p.chmod(PRIVATE)


def fsync_dir(d):
    fd = os.open(d, os.O_RDONLY | os.O_DIRECTORY)
    try:
        os.fsync(fd)
    finally:
        os.close(fd)


def tmp_of(path):
    return path.with_name(path.name + TMP)


def clear_tmp(path):
    tmp = tmp_of(path)
    if tmp.is_symlink() or tmp.exists():
        tmp.unlink()


def atomic_write(path, data, mode=None, faults=True):
    """Replaces path's bytes so that a reader, or a run killed at any moment, sees the old bytes or the new, never
    a mix: a temporary copy in the same folder, fsync, rename, fsync of the folder. Keeps an existing file's mode
    (or sets `mode`); through a symlink, writes the file it points at."""
    path = pathlib.Path(os.path.realpath(path)) if path.is_symlink() else path
    clear_tmp(path)
    if mode is None and path.exists():
        mode = stat.S_IMODE(path.stat().st_mode)
    with open(tmp_of(path), "wb") as f:
        if mode is not None:
            os.fchmod(f.fileno(), mode)
        f.write(data[:len(data) // 2])
        f.flush()
        if faults:
            fault(f"mid-write {path}")
        f.write(data[len(data) // 2:])
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp_of(path), path)
    fsync_dir(path.parent)


def atomic_link(path, target):
    clear_tmp(path)
    os.symlink(target, tmp_of(path))
    os.replace(tmp_of(path), path)
    fsync_dir(path.parent)


def state(p):
    """What is at p now, as the journal records it."""
    if p.is_symlink():
        return {"link": os.readlink(p)}
    if p.is_file():
        return {"sha256": sha(p.read_bytes())}
    if p.is_dir():
        return {"dir": True}
    return {"absent": True} if not p.exists() else {"other": True}


class Plan:
    """The changes a run will make, each with what is at its path now, so they can be journalled before any is
    made. `dirs` are the folders it will create, so a later step under one doesn't plan it again."""

    def __init__(self):
        self.steps, self.dirs, self.notes = [], set(), []

    def mkdir(self, d):
        self.steps.append({"op": "mkdir", "path": str(d)})
        self.dirs.add(d)

    def link(self, p, target):
        self.steps.append({"op": "link", "path": str(p), "from": state(p), "target": str(target)})

    def write(self, p, data):
        p = pathlib.Path(os.path.realpath(p)) if p.is_symlink() else p
        self.steps.append({"op": "write", "path": str(p), "from": state(p), "b64": base64.b64encode(data).decode()})

    def unlink(self, p):
        self.steps.append({"op": "unlink", "path": str(p), "from": state(p)})

    def rmdir(self, d):
        self.steps.append({"op": "rmdir", "path": str(d)})


def result(s):
    if s["op"] == "mkdir":
        return {"dir": True}
    if s["op"] == "link":
        return {"link": s["target"]}
    if s["op"] == "write":
        return {"sha256": sha(base64.b64decode(s["b64"]))}
    return {"absent": True}


def apply_step(s):
    """Makes one journalled change unless it is already made (by the run that was interrupted); returns a log line
    or None. A path that is neither as planned nor as the plan found it changed meanwhile: it is left as it is."""
    p, op = pathlib.Path(s["path"]), s["op"]
    clear_tmp(p)  # an interrupted write's temporary copy
    now = state(p)
    if now == result(s):
        return None
    if op == "mkdir":
        if not now.get("absent"):
            return f"left {p}: not a folder"
        p.mkdir()
        return None
    if op == "rmdir":
        if not now.get("dir"):
            return f"left {p}: not a folder any more"
        if any(p.iterdir()):
            return f"left {p}: not empty"
        p.rmdir()
        return f"removed {p}"
    if now != s["from"]:
        return f"left {p}: changed while this run was making its changes"
    if op == "link":
        atomic_link(p, s["target"])
        return f"link {p} -> {s['target']}"
    if op == "write":
        atomic_write(p, base64.b64decode(s["b64"]))
        return f"wrote {p}"
    p.unlink()
    fsync_dir(p.parent)
    return f"removed {p}"


def commit(plan, manifest):
    """Journals the plan and the manifest it leads to (None: no manifest), then carries both out."""
    fault("journal")
    atomic_write(JOURNAL, (json.dumps({"steps": plan.steps, "manifest": manifest}, indent=1) + "\n").encode(), mode=PRIVATE)
    return plan.notes + finish()


def finish():
    """Carries out the journal: each change not yet made, then the manifest, then removes the journal. After an
    interruption, the next run calls it again and it picks up where the last one stopped."""
    j, lines = json.loads(JOURNAL.read_text()), []
    for s in j["steps"]:
        fault(f"{s['op']} {s['path']}")
        line = apply_step(s)
        if line:
            lines.append(line)
    fault("manifest")
    if j["manifest"] is None:
        if MANIFEST.exists():
            MANIFEST.unlink()
    else:
        atomic_write(MANIFEST, (json.dumps(j["manifest"], indent=2) + "\n").encode(), mode=PRIVATE)
    JOURNAL.unlink()
    fsync_dir(STATE_DIR)
    return lines


def recover():
    """Finishes a run that was interrupted (its journal is still there) before this one plans its own. Returns
    "uninstall" if that run was an uninstall, "install" if an install or sync, else None."""
    for p in (MANIFEST, MADE_DIRS):
        clear_tmp(p)
    if not JOURNAL.exists():
        clear_tmp(JOURNAL)  # killed while writing the journal: nothing had changed yet
        return None
    print(f"finishing an interrupted run first ({JOURNAL})")
    kind = "uninstall" if json.loads(JOURNAL.read_text())["manifest"] is None else "install"
    for line in finish():
        print(line)
    return kind


class Lock:
    """flock on STATE_DIR/lock for the whole run, so two runs (two hooks, a hook and a hand run) take turns. The
    folders it creates for the lock are recorded in MADE_DIRS. On release, if nothing is installed any more, it
    removes the lock, that record and those folders (and `extra_dirs`, an older manifest's record), if empty."""

    def __init__(self):
        self.extra_dirs = []

    def __enter__(self):
        while True:
            made, d = [], STATE_DIR
            while not d.exists():
                made.append(d)
                d = d.parent
            for d in reversed(made):
                d.mkdir(mode=0o700 if d == STATE_DIR else 0o777, exist_ok=True)
            try:
                fd = os.open(LOCK, os.O_RDWR | os.O_CREAT, 0o600)
            except FileNotFoundError:  # the run before removed the folder on release
                continue
            fcntl.flock(fd, fcntl.LOCK_EX)
            try:
                same = os.fstat(fd).st_ino == os.stat(LOCK).st_ino
            except FileNotFoundError:
                same = False
            if same:
                break
            os.close(fd)  # the run before removed this lock on release; take the new one
        self.fd = fd
        tighten_state()
        if made:
            have = json.loads(MADE_DIRS.read_text()) if MADE_DIRS.exists() else []
            atomic_write(MADE_DIRS, json.dumps(sorted(set(have) | {str(d) for d in made})).encode(), mode=PRIVATE, faults=False)
        return self

    def __exit__(self, *exc):
        try:
            if not MANIFEST.exists() and not JOURNAL.exists():
                dirs = [STATE_DIR] + [pathlib.Path(x) for x in self.extra_dirs]
                if MADE_DIRS.exists():
                    dirs += [pathlib.Path(x) for x in json.loads(MADE_DIRS.read_text())]
                for p in (MADE_DIRS, LOCK, tmp_of(MADE_DIRS), tmp_of(JOURNAL), tmp_of(MANIFEST)):
                    if p.exists():
                        p.unlink()
                for d in sorted(set(dirs), key=lambda p: len(p.parts), reverse=True):
                    if d.is_dir() and not any(d.iterdir()):
                        d.rmdir()
        finally:
            os.close(self.fd)


def upgrade_manifest(m, root):
    """Version 2 (26c129c) recorded no link targets, file hashes or written values, and kept the prior file as
    text. It always wrote the same values, so what is there now is taken as written: a change made before this
    upgrade can't be told apart from ours. Its prior text becomes bytes (it had already lost CRLF and BOM)."""
    if m.get("version", 2) >= 3:
        return m
    values = {(str(p), k): v for p, k, v in owned_settings(root, "full")}  # version 2 knew only full
    for e in m["created"]:
        p = pathlib.Path(e["path"])
        if e["kind"] == "link":
            e.setdefault("target", os.readlink(p) if p.is_symlink() else None)
        elif e["kind"] == "file":
            e.setdefault("sha256", sha(p.read_bytes()) if p.is_file() and MARK.encode() in p.read_bytes() else None)
    for spath, rec in m["settings"].items():
        if "prior_b64" not in rec:
            text = rec.pop("prior_text", None)
            rec["prior_b64"] = None if text is None else base64.b64encode(text.encode()).decode()
        rec.pop("written_sha256", None)
        for key, k in rec["keys"].items():
            if key in MERGED:
                k.setdefault("added", [])
                k.setdefault("declined", [])
            else:
                k.setdefault("written", values.get((spath, key), get(load(pathlib.Path(spath)), key)))
    m["version"] = 3
    return m


def mkdirs(path, created, plan):
    """Plans mkdir -p, recording each directory it creates (outermost first)."""
    missing = []
    while not (path.exists() or path in plan.dirs):
        missing.append(path)
        path = path.parent
    for d in reversed(missing):
        plan.mkdir(d)
        created.append({"path": str(d), "kind": "dir"})


def legacy_present():
    """Signs of an install from before the manifest (2026-10-08 builds): links into local-agents/ or a
    generated SKILLS.md, with no manifest to say what was there before."""
    found = []
    # ~/.qwen only: links into local-agents/ under ~/.config/opencode are now tools/sync-opencode's (D35).
    for p in sorted((QW_DIR / "agents").glob("*.md")) if (QW_DIR / "agents").is_dir() else []:
        if p.is_symlink() and f"/{OUT}/" in os.readlink(p):
            found.append(p)
    for name in ("AGENTS.md", "CLAUDE.md", "LOCAL-TOOLS.md"):
        p = QW_DIR / name
        if p.is_symlink() and (f"/{OUT}/" in os.readlink(p) or os.readlink(p).endswith(("/AGENTS.md", "/CLAUDE.md"))):
            found.append(p)
    p = QW_DIR / "SKILLS.md"
    if p.exists() and not p.is_symlink() and MARK in p.read_text():
        found.append(p)
    return found


def state_of(p):
    if p.is_symlink():
        return f"now points at {os.readlink(p)}"
    return "replaced by a file" if p.exists() else "removed"


def rules_mode(asked):
    """--rules if given, else what the manifest recorded (so --sync and the hooks keep the chosen sheet), else
    DEFAULT_RULES."""
    m = read_manifest()
    return asked or (m or {}).get("rules") or DEFAULT_RULES


def install(root, rules):
    """Install, or bring an install up to date (what --sync and the hooks run). Owns only what the manifest says it
    wrote, and only while it is still as written: a link, file or settings key the user changed since is left as
    it is, reported, and its record (the value from before the install) kept for --uninstall. `rules` (full or
    core) picks the rule sheet and roles; switching relinks them and is recorded, like the rest, for --uninstall."""
    m = read_manifest()
    if m is None and legacy_present():
        sys.exit("an install from before the manifest is present (" + ", ".join(map(str, legacy_present()[:3]))
                 + ", ...); run --uninstall once to remove it, then --install")
    m = upgrade_manifest(m, root) if m else {"version": 3, "created": [], "settings": {}}
    entries = {e["path"]: e for e in m["created"]}
    # Every conflict is found, and every settings file read, before anything changes.
    problems = []
    for path in [l for l, _ in links(root, rules)] + [p for p, _ in generated_files(root)]:
        if (path.exists() or path.is_symlink()) and str(path) not in entries:
            problems.append(f"{path}: already exists and isn't from this install; move it aside first")
    files = {p: read_settings(p) for p in sorted({p for p, _, _ in owned_settings(root, rules)})}
    for path, key, value in owned_settings(root, rules):
        rec = m["settings"].get(str(path), {}).get("keys", {}).get(key)
        current = get(files[path][0], key)
        if rec is None and current is not MISSING and current != value and key not in MERGED:
            problems.append(f"{path}: {key} is already {json.dumps(current)}; this install sets "
                            f"{json.dumps(value)}. Change or remove it yourself, then --install")
        if key in MERGED and current is not MISSING and not isinstance(current, list):
            problems.append(f"{path}: {key} is {json.dumps(current)}, not a list to add to")
    if problems:
        sys.exit("\n".join(problems))

    plan, kept = Plan(), []
    created = m["created"]
    m["root"] = str(root)
    m["rules"] = rules
    want_links = {link: str(target) for link, target in links(root, rules)}
    for e in [e for e in created if e["kind"] == "link" and pathlib.Path(e["path"]) not in want_links]:
        p = pathlib.Path(e["path"])  # a role removed from the library since the last install
        if p.is_symlink() and os.readlink(p) == e.get("target"):
            plan.unlink(p)
        elif p.exists() or p.is_symlink():
            kept.append(f"{p}: {state_of(p)} since the install; left as it is, and no longer this install's")
        created.remove(e)
    for link, target in want_links.items():
        e = entries.get(str(link))
        now = os.readlink(link) if link.is_symlink() else None
        if e is not None and now == target:
            e["target"] = target
            e.pop("kept", None)
            continue
        if e is not None and (e.get("kept") or now != e.get("target")):
            e["kept"] = True
            kept.append(f"{link}: {state_of(link)} since the install; left as it is (this install links {target})")
            continue
        mkdirs(link.parent, created, plan)
        if e is None:
            e = {"path": str(link), "kind": "link"}
            created.append(e)
        plan.link(link, target)
        e["target"] = target
    for path, text in generated_files(root):
        e, data = entries.get(str(path)), text.encode()
        cur = path.read_bytes() if path.is_file() and not path.is_symlink() else None
        if e is not None and cur == data:
            e["sha256"] = sha(data)
            e.pop("kept", None)
            continue
        if e is not None and (e.get("kept") or cur is None or sha(cur) != e.get("sha256")):
            e["kept"] = True
            kept.append(f"{path}: {'edited' if cur is not None else state_of(path)} since the install; left as it is")
            continue
        mkdirs(path.parent, created, plan)
        if e is None:
            e = {"path": str(path), "kind": "file"}
            created.append(e)
        plan.write(path, data)
        e["sha256"] = sha(data)
    for path, (data, style) in files.items():
        rec = m["settings"].setdefault(str(path), {
            "existed": path.exists(), "keys": {},
            "prior_b64": base64.b64encode(path.read_bytes()).decode() if path.exists() else None})
        before = json.loads(json.dumps(data))
        for p, key, value in owned_settings(root, rules):
            if p != path:
                continue
            k, cur = rec["keys"].get(key), get(data, key)
            if k is None:
                k = rec["keys"][key] = {"had": cur is not MISSING, "prior": None if cur is MISSING else cur}
            if key in MERGED:  # owned item by item: the user's own items, and ours they removed, are theirs
                k.setdefault("added", [])
                k.setdefault("declined", [])
                have = cur if isinstance(cur, list) else []
                gone = [x for x in k["added"] if x not in have]
                if gone:
                    k["declined"] += [x for x in gone if x not in k["declined"]]
                    kept.append(f"{path}: {key}: {json.dumps(gone)} removed since the install; not added back")
                stale = [x for x in k["added"] if x in have and x not in value]  # e.g. another clone's skills/
                new = [x for x in have if x not in stale]
                add = [x for x in value if x not in new and x not in k["declined"]]
                k["added"] = [x for x in k["added"] if x in have and x in value] + add
                if new + add != have:
                    put(data, key, new + add)
            elif "written" not in k or cur == k["written"] or cur == value:
                put(data, key, value)
                k["written"] = value
            else:
                kept.append(f"{path}: {key} is {show(cur)}, changed since the install; left as it is "
                            f"(this install sets {json.dumps(value)})")
        if data != before:
            mkdirs(path.parent, created, plan)
            if not path.exists() and not any(e["path"] == str(path) for e in created):
                created.append({"path": str(path), "kind": "settings"})
            plan.write(path, settings_bytes(data, style))
    for line in commit(plan, m):
        print(line)
    for line in kept:
        print(f"kept {line}")
    print(f"rules {rules}: ~/.qwen/AGENTS.md is {'the core sheet' if rules == 'core' else 'the full rule sheet'}")
    print(f"manifest {MANIFEST}")


def uninstall_legacy():
    """Removes what the 2026-10-08 builds before the manifest installed, listed here explicitly because they
    recorded nothing: links into local-agents/ under ~/.qwen and ~/.config/opencode, ~/.qwen's AGENTS.md,
    CLAUDE.md and LOCAL-TOOLS.md links, a generated ~/.qwen/SKILLS.md, and the settings keys those builds set,
    each only while it still holds the value they wrote. A settings file left empty is removed."""
    old = {
        QW_DIR / "settings.json": {
            "general.gitCoAuthor": {"commit": False, "pr": False}, "general.enableAutoUpdate": False,
            "privacy.usageStatisticsEnabled": False,
            "tools.executionSandbox": {"backend": "auto", "filesystem": "workspace-write", "network": "open"},
            "env.GIT_AUTHOR_NAME": AGENT_NAME, "env.GIT_AUTHOR_EMAIL": AGENT_EMAIL,
            "env.GIT_COMMITTER_NAME": AGENT_NAME, "env.GIT_COMMITTER_EMAIL": AGENT_EMAIL},
        OC_DIR / "opencode.json": {
            "$schema": "https://opencode.ai/config.json", "autoupdate": False, "share": "disabled"},
    }
    gone = legacy_present()
    if not gone:  # without one of its links or files, a matching key is the user's own (or a second --uninstall)
        return print("no install from before the manifest either; nothing to remove")
    files = {path: read_settings(path) for path in old if path.exists()}  # stops on JSONC before any change
    plan = Plan()
    for p in gone:
        plan.unlink(p)
    d = QW_DIR / "agents"
    if d.is_dir() and all(c in gone for c in d.iterdir()):
        plan.rmdir(d)
    for path, (data, style) in files.items():
        for key, value in old[path].items():
            if get(data, key) == value:
                drop(data, key)
        # Values that named the clone they were installed from: matched by shape.
        if path.name == "settings.json":
            dirs = get(data, "skills.directories")
            if isinstance(dirs, list) and all(str(x).endswith("/skills") for x in dirs) and len(dirs) == 1:
                drop(data, "skills.directories")
            for names in (["QWEN.md", "AGENTS.md", "CLAUDE.md", "LOCAL-TOOLS.md"],
                          ["QWEN.md", "AGENTS.md", "CLAUDE.md", "LOCAL-TOOLS.md", "SKILLS.md"]):
                if get(data, "context.fileName") == names:
                    drop(data, "context.fileName")
        else:
            instr = get(data, "instructions")
            if isinstance(instr, list) and len(instr) == 2 and instr[1].endswith(f"/{OUT}/LOCAL-TOOLS.md"):
                drop(data, "instructions")
            skill = get(data, "permission.skill")
            if isinstance(skill, dict) and skill.get("*") == "allow" and all(v in ("allow", "deny") for v in skill.values()):
                drop(data, "permission.skill")
        if data:
            plan.write(path, settings_bytes(data, style))
            plan.notes.append(f"removing the earlier build's keys from {path}")
        else:
            plan.unlink(path)
            plan.notes.append(f"removing {path} (left empty)")
    for line in commit(plan, None):
        print(line)


def uninstall(root, lock):
    """Removes what the install owns and puts back what the manifest recorded, but only what is still as this
    install left it: a key, link or file the user changed since stays as the user left it. A settings file whose
    remaining content equals the file from before the install gets those exact bytes back."""
    m = read_manifest()
    if m is None:
        print(f"no manifest at {MANIFEST}: removing an install from before the manifest, if any")
        return uninstall_legacy()
    m = upgrade_manifest(m, root)
    lock.extra_dirs = m.get("state_dirs", [])  # recorded by installs before the lock took that over
    plan = Plan()
    files = {pathlib.Path(s): read_settings(pathlib.Path(s)) for s in m["settings"] if pathlib.Path(s).exists()}
    for spath, rec in m["settings"].items():
        path = pathlib.Path(spath)
        prior = None if rec["prior_b64"] is None else base64.b64decode(rec["prior_b64"])
        if path not in files:
            if rec["existed"]:
                plan.notes.append(f"left {path} absent: removed since the install")
            continue
        data, style = files[path]
        prior_data = parse_settings(prior, path)[0] if prior is not None else {}
        for key, k in rec["keys"].items():
            cur = get(data, key)
            if key in MERGED:
                if isinstance(cur, list):
                    rest = [x for x in cur if x not in k.get("added", [])]
                    if rest != cur:
                        put(data, key, rest) if (rest or k["had"]) else drop(data, key, prior_data)
            elif cur == k.get("written"):
                put(data, key, k["prior"]) if k["had"] else drop(data, key, prior_data)
            else:
                plan.notes.append(f"left {path}: {key} is {show(cur)}, changed since the install")
        if prior is not None and data == prior_data:
            if path.read_bytes() != prior:
                plan.write(path, prior)
            plan.notes.append(f"restoring {path} byte for byte as it was before the install")
        elif prior is None and not data and not rec["existed"]:
            plan.unlink(path)
        else:
            new = settings_bytes(data, style)
            if new != path.read_bytes():
                plan.write(path, new)
            plan.notes.append(f"removing this install's keys from {path}; keeping what changed there since")
    for e in reversed(m["created"]):
        p = pathlib.Path(e["path"])
        if e["kind"] == "settings":
            continue  # handled above
        if e["kind"] == "link" and p.is_symlink() and os.readlink(p) == e.get("target"):
            plan.unlink(p)
        elif e["kind"] == "file" and p.is_file() and not p.is_symlink() and sha(p.read_bytes()) == e.get("sha256"):
            plan.unlink(p)
        elif e["kind"] == "dir":
            plan.rmdir(p)  # if empty once the rest is removed
        elif p.exists() or p.is_symlink():
            plan.notes.append(f"left {p}: changed since the install")
    for line in commit(plan, None):
        print(line)


def check_install(root, rules):
    problems = []
    if JOURNAL.exists():
        problems.append(f"{JOURNAL}: a run was interrupted; --install, --sync or --uninstall finishes it first")
    m = read_manifest()
    if m is None:
        problems.append(f"{MANIFEST}: no manifest; not installed (run --install)")
    elif m.get("root") != str(root):
        problems.append(f"{MANIFEST}: installed from {m.get('root')}, not {root}")
    if m is not None and m.get("rules", "full") != rules:
        problems.append(f"{MANIFEST}: installed with --rules {m.get('rules', 'full')}, not {rules}")
    for link, target in links(root, rules):
        if not link.is_symlink() or pathlib.Path(os.readlink(link)) != target:
            problems.append(f"{link}: not a link to {target}")
    for path, text in generated_files(root):
        if not path.exists() or path.read_text() != text:
            problems.append(f"{path}: missing or stale (rerun --install)")
    for path, key, value in owned_settings(root, rules):
        cur = get(load(path), key)
        ok = isinstance(cur, list) and all(x in cur for x in value) if key in MERGED else cur == value
        if not ok:
            problems.append(f"{path}: {key} is {show(cur)}, not {json.dumps(value)}")
    if m is not None:
        extra = {e["path"] for e in m["created"] if e["kind"] == "link"} - {str(l) for l, _ in links(root, rules)}
        problems += [f"{p}: links a role the library no longer has (rerun --install)" for p in sorted(extra)]
    if problems and m is not None:
        problems.append("(--install leaves anything changed since the install as it is; to take this install's "
                        "version, put it back yourself, or move yours aside and run --uninstall then --install)")
    return problems


# --- git hooks -----------------------------------------------------------------------------------------------------

HOOKS = ("post-merge", "post-checkout")
ORIG = ".pre-gen-local-agents"  # a clone's own hook of the same name, moved aside; the wrapper runs it first


def hooks_dir(root):
    """(core.hooksPath or "", the clone's .git/hooks as an absolute path; a worktree shares its main clone's)."""
    git = lambda *a: subprocess.run(["git", "-C", str(root), *a], capture_output=True, text=True)
    common = git("rev-parse", "--path-format=absolute", "--git-common-dir")
    if common.returncode:
        sys.exit(f"{root}: not a git clone ({common.stderr.strip()})")
    return git("config", "--get", "core.hooksPath").stdout.strip(), pathlib.Path(common.stdout.strip()) / "hooks"


def hook_wrapper(name):
    return f"""#!/bin/sh
# {MARK} --install-hooks. Runs this clone's own {name} hook first (moved to {name}{ORIG}),
# keeping its exit status, then the library's tools/hooks/{name}. Undo: gen_local_agents.py --uninstall-hooks
d=$(dirname "$0")
rc=0
if [ -x "$d/{name}{ORIG}" ]; then "$d/{name}{ORIG}" "$@"; rc=$?; fi
h="$(git rev-parse --show-toplevel)/tools/hooks/{name}"
if [ -x "$h" ]; then "$h" "$@"; fi
exit $rc
"""


def ours(p):
    return p.is_file() and not p.is_symlink() and MARK in p.read_text(errors="replace")


def install_hooks(root):
    """Adds post-merge and post-checkout to the clone's .git/hooks, each a wrapper that runs the clone's own hook
    of that name first (moved aside to <name>.pre-gen-local-agents), so a pull or checkout that changes what
    --install installs reruns --sync. Every other hook is untouched. Refuses a core.hooksPath set to another
    folder (its hooks run instead of .git/hooks); clears the one earlier versions set (tools/hooks), which hid the
    clone's own hooks."""
    current, d = hooks_dir(root)
    if current == "tools/hooks":
        subprocess.run(["git", "-C", str(root), "config", "--unset", "core.hooksPath"], check=True)
        print(f"{root}: unset core.hooksPath (tools/hooks, set by an earlier --install-hooks; it hid .git/hooks)")
    elif current:
        sys.exit(f"{root}: core.hooksPath is {current}, so .git/hooks doesn't run; not changing it. Add to its "
                 f"post-merge and post-checkout: \"$(git rev-parse --show-toplevel)/tools/hooks/<name>\" \"$@\"")
    if not d.is_dir():
        d.mkdir()
        (d / ".gen_local_agents-made").write_text("--install-hooks created this folder; --uninstall-hooks removes it\n")
    for name in HOOKS:
        p, orig = d / name, d / (name + ORIG)
        if (p.exists() or p.is_symlink()) and not ours(p):
            if orig.exists() or orig.is_symlink():
                sys.exit(f"{orig} and {p} both exist and neither is this script's; sort them out by hand")
            os.rename(p, orig)  # same folder: bytes, mode and a relative link's target kept
            print(f"moved {p} to {orig}; the wrapper runs it first")
        if not ours(p) or p.read_text() != hook_wrapper(name):
            atomic_write(p, hook_wrapper(name).encode(), mode=0o755)
            print(f"wrote {p}")
    print(f"{root}: hooks in {d} (undo: python3 tools/gen_local_agents.py --uninstall-hooks)")


def uninstall_hooks(root):
    """Removes the wrappers --install-hooks wrote and moves each original hook back, as it was."""
    current, d = hooks_dir(root)
    if current == "tools/hooks":
        subprocess.run(["git", "-C", str(root), "config", "--unset", "core.hooksPath"], check=True)
        print(f"{root}: unset core.hooksPath (tools/hooks, set by an earlier --install-hooks)")
    for name in HOOKS:
        p, orig = d / name, d / (name + ORIG)
        if not ours(p):
            if orig.exists() or orig.is_symlink():
                print(f"left {orig}: {p} isn't this script's wrapper any more; sort them out by hand")
            continue
        if orig.exists() or orig.is_symlink():
            os.replace(orig, p)
            print(f"moved {orig} back to {p}")
        else:
            p.unlink()
            print(f"removed {p}")
    made = d / ".gen_local_agents-made"
    if made.exists():
        made.unlink()
        if not any(d.iterdir()):
            d.rmdir()


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--root", type=pathlib.Path, default=ROOT, help="library root (default: this script's repo)")
    ap.add_argument("--rules", choices=RULES, help="with --install or --check-install: the full rule sheet or the "
                    f"core sheet (default: what the last install recorded, else {DEFAULT_RULES})")
    mode = ap.add_mutually_exclusive_group()
    for flag in ("--check", "--install", "--check-install", "--uninstall", "--install-hooks", "--uninstall-hooks",
                 "--sync"):
        mode.add_argument(flag, action="store_true")
    args = ap.parse_args()
    root = args.root.resolve()
    if args.check or args.check_install:
        if args.check:
            for line in term_report(root):
                print(line)
            print(f"core sheet: about {budget(root)[0]} tokens (estimate) of {CORE_BUDGET}")
        problems = check(root) if args.check else check_install(root, rules_mode(args.rules))
        for p in problems:
            print(p)
        print(f"{'local-agents' if args.check else 'install'}: {'OK' if not problems else f'{len(problems)} problem(s)'}")
        sys.exit(1 if problems else 0)
    if args.install or args.sync or args.uninstall:
        with Lock() as lock:
            if recover() == "uninstall" and args.uninstall:
                return print("the interrupted uninstall is finished")
            if args.uninstall:
                return uninstall(root, lock)
            if args.sync:  # from tools/hooks: only the checkout the install came from updates it
                m = read_manifest()
                if m is None or m.get("root") != str(root):
                    return print(f"gen_local_agents: install not from {root}; nothing to sync")
            stale = check(root)
            if stale:
                sys.exit("local-agents/ is stale; run tools/gen_local_agents.py first:\n" + "\n".join(stale))
            return install(root, rules_mode(args.rules))
    if args.install_hooks:
        return install_hooks(root)
    if args.uninstall_hooks:
        return uninstall_hooks(root)
    want = generate(root)
    for rel, text in want.items():
        path = root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        if not path.exists() or path.read_text() != text:
            atomic_write(path, text.encode())
            print(f"wrote {rel}")
    for path in sorted((root / OUT).rglob("*")):
        if path.is_file() and str(path.relative_to(root)) not in want:
            path.unlink()
            print(f"removed {path.relative_to(root)}")


if __name__ == "__main__":
    main()
