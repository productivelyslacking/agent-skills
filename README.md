<p align="center">
  <img src=".github/banner.svg" alt="AGENT//SKILLS: a retro-future starship bridge, crew at their stations, looking out at a nebula and a ringed planet" width="100%">
</p>

<p align="center">
  <a href="LICENSE"><img alt="MIT licence" src="https://img.shields.io/badge/licence-MIT-ff4fd8?style=flat-square"></a>
  <a href="https://agentskills.io/specification"><img alt="Agent Skills format" src="https://img.shields.io/badge/format-Agent%20Skills-3cf2ff?style=flat-square"></a>
  <img alt="24 skills, 11 roles" src="https://img.shields.io/badge/skills-24%20%C2%B7%20roles%2011-ffe36e?style=flat-square">
</p>

# agent-skills

**Your AI coding agent is fast. This is built to make it careful.** A library of skills, rules and team roles that
asks agents to check their own work, keep records that outlive the chat, say what they don't know, and show evidence
before calling anything done. Plus deep kits for games, stories, art and learning products.

> **Tested with Claude Code.** The skills use the open Agent Skills format, and the
> [setup guide for other tools](docs/runbooks/use-with-other-tools.md) (Codex, Gemini CLI, Cursor, Copilot and more)
> comes from their docs; those integrations are unverified.

## What's in the box

| | What it is | When it loads |
|---|---|---|
| ⚡ **Rules** | `AGENTS.md`: eleven working rules, such as *verify against the real thing* and *never claim what you can't show* | Every session: about 1,500 tokens; with **ground-truth**, which most tasks load, about 5,400 (estimated) |
| ◆ **Skills** | 24 folders of know-how, each a `SKILL.md` in the open [Agent Skills](https://agentskills.io/specification) format | Only when a task needs one |
| ▸ **Roles** | 11 team agents (developer, QA, tech lead, merge reviewer, director and more) the main session hands work to | When you split work across agents |

**How a skill works, in 30 seconds.** Your agent sees each skill's name and a one-line "use when". When your request
matches, it reads the whole skill and follows it. You just ask normally:

> *"Plan the move of our docs from Confluence to SharePoint."* → loads **migrations**: inventory first, dry run,
> resumable runs, validate against the source.
>
> *"Is it safe to add this npm package?"* → loads **dependency-policy**: licence, provenance, vulnerabilities, and
> whether a tool you already have does the job.
>
> *"Split this feature between a developer and QA."* → loads **agent-team**: written briefs, separate worktrees,
> evidence before anything counts as done.

## Quick start

1. **Clone it:** `git clone https://github.com/productivelyslacking/agent-skills.git ~/agent-skills`
2. **Link it into your tool.** Claude Code: run `~/agent-skills/tools/sync-claude` (details in "Run it" below). Codex, ChatGPT,
   Gemini, OpenCode, Copilot, Cursor or Grok: [docs/runbooks/use-with-other-tools.md](docs/runbooks/use-with-other-tools.md).
3. **Check it loaded:** in a new session, ask *"Quote the bold title of working rule 10."* It should say *Design for a
   human with little time and attention.*

**Make it yours:** fork it, and keep anything personal (machine notes, standing permissions, names that must never be
written) in your own `~/.claude/CLAUDE.md`, not in the repo. The library improves itself as you work: lessons from your
projects come back as candidates and earn their way in ([how](skills/durable-knowledge/SKILL.md)).

## The skills

◇ marks a skill built from published research and not yet proven in real use; its claims say how far to trust them.

### ⚡ Core discipline

| Skill | Use when |
|---|---|
| **ground-truth** | Any work: the full working rules, verification that can fail, one source of truth |
| **durable-knowledge** | Recording lessons and decisions, setting up a repo's docs, writing or admitting a skill |
| **prose-editing** | Cutting and shaping docs, runbooks, reports and instructions for models |
| **claim-integrity** | A document makes claims someone will rely on: policy, compliance, security plans, marketing |

### ◆ Build and ship

| Skill | Use when |
|---|---|
| **agent-team** | Splitting work across role agents: briefs, parallel worktrees, evidence, model tiers, cost |
| **landing** | Getting a branch onto main: what blocks, review rounds, merge conflicts |
| **dependency-policy** | Adding third-party code, or about to build a tool someone else already built |
| **ops-scripting** | Scripts that run unattended: scheduled jobs, endpoint automation, CI steps |
| **migrations** | Any move between platforms, with a cutover |
| **data-pipelines** | Reports, warehouses or metrics from several sources, or two numbers that disagree |

### ▸ Story, art and learning

| Skill | Use when |
|---|---|
| **story-design** | ◇ Any story meant to hold an audience: structure, openings, twists, fair clues |
| **interactive-story** | ◇ The player's choices shape the story: branching, agency, stuck players |
| **directing** | ◇ Holding a story-led project's vision across story, look, voice and pacing |
| **art-direction** | ◇ Deciding what an image should show and whether it works |
| **generated-art** | ◇ Making images with a model: prompts, consistency, checks, rights, disclosure |
| **psychology-review** | ◇ How an audience or learner will likely read a scene, line or choice |
| **teaching-design** | ◇ Anything that teaches a skill so it lasts |
| **teaching-programming** | ◇ Coding lessons, exercises, autograders and error help |
| **production-stages** | ◇ When to commit to final art, voice and locks in a game or story production |

### ◈ Game development

Learned on a Godot 4 C# action RPG and generalized.

| Skill | Use when |
|---|---|
| **godot-dotnet** | Godot 4 C# builds, exports and CI, where the toolchain fails silently |
| **game-simulation-testing** | Game rules, AI and balance tested without a human |
| **game-saves** | Save files that never lose a player's progress |
| **game-assets** | Art, audio and fonts: placeholders, licences, credits |
| **gamedev-team-practices** | Readying a game project for collaborators |

The index in `AGENTS.md` is the source of truth for what exists; `tools/check.py` fails if these tables list different
skills.

## Run it

Link it into Claude Code (Linux, with bash; other tools: the runbook above):

```bash
~/agent-skills/tools/sync-claude    # pulls main, links every skill and role, imports the rule sheet; safe to re-run
```

Then make every session do the same, by adding this to `hooks` in `~/.claude/settings.json`, with this clone's path:

```json
"SessionStart": [{"matcher": "startup|resume", "hooks": [{"type": "command", "command": "/path/to/agent-skills/tools/sync-claude", "timeout": 20}]}]
```

The clone stays on the latest `main` without anyone remembering to pull. If it can't update (offline, local edits that
conflict, another branch checked out), the session starts anyway and says so. Skills are read when used, so they are
current at once. If the rule sheet changed, the session is told to re-read it, because a hook may run after it loaded.

The same steps by hand (macOS / Linux; edits here take effect in the next session):

```bash
# 1. The rule sheet and skill index: ~/.claude/CLAUDE.md imports this repo's CLAUDE.md (which is "@AGENTS.md").
#    Put this line first in ~/.claude/CLAUDE.md, followed by that machine's own notes:
#      @/path/to/agent-skills/CLAUDE.md
# 2. The skills and the role agents, one link each (Claude Code keeps its own synced/ folder in ~/.claude/skills):
for s in /path/to/agent-skills/skills/*/; do ln -sfn "$s" ~/.claude/skills/"$(basename "$s")"; done
mkdir -p ~/.claude/agents
for a in /path/to/agent-skills/agents/*.md; do ln -sfn "$a" ~/.claude/agents/"$(basename "$a")"; done
# 3. The layout checker, on PATH:
ln -sfn /path/to/agent-skills/tools/layout-check ~/.local/bin/layout-check
```

Re-run step 2 after adding a skill or role. Then, in a new session, run `/context`: `CLAUDE.md` and `AGENTS.md`
from this repo must both appear under **Memory files**. An import that fails to resolve does so silently. In the
desktop app, `/context` gives Memory files only as a token total; its Memory panel names the files instead.

**Windows** (set up and checked on 2026-11-13). `tools/sync-claude` and its hook run in Git Bash, and
`tools/check.sh` runs in WSL. Three one-time steps first:

1. Turn on Developer Mode (Settings > System > For developers). Without it, Git Bash can't make symlinks, and
   sync-claude fails with `Operation not permitted`.
2. Make `python3` work in Git Bash. A python.org install has only `python.exe`, so `python3` falls through to the
   Microsoft Store stub, which exists but fails. In PowerShell:
   `New-Item -ItemType SymbolicLink -Path "$d\python3.exe" -Target "$d\python.exe"`, with
   `$d = "$env:LOCALAPPDATA\Programs\Python\Python314"` (adjust the version).
3. Run `tools/sync-claude` from Git Bash, then add the hook above with the command `C:/path/to/agent-skills/tools/sync-claude`.
   It writes `~/.claude/CLAUDE.md`'s import as `@C:/repo/...`, a path Claude Code on Windows can read.

Run `tools/check.sh` in WSL: `wsl -e bash -lc "cd /mnt/c/repo/agent-skills && tools/check.sh"`. Its tests assume
Unix (symlinks, `fcntl`, running scripts by their shebang), and under Windows Python they fail by the dozen.
`.gitattributes` keeps every checkout on LF, because the generated files record their sources' git blob hashes.

**Copying instead of linking:** copy `AGENTS.md` (not `CLAUDE.md`, which is only the import line) to
`~/.claude/CLAUDE.md`, merging with any machine notes there, and `skills/*` into `~/.claude/skills/`. A copy
drifts; prefer the links.

A project overrides a role with a same-named file in its own `.claude/agents/`. Skills can also live in a repo's
`.claude/skills/` to scope them to it. **Never put `~/.claude` itself under version control**: it holds
`.credentials.json` and every conversation under `projects/`.

Every check this repo has: `tools/check.sh` (CI runs it on every push).

**Local models (Qwen Code):** [docs/runbooks/local-agents-qwen.md](docs/runbooks/local-agents-qwen.md).

## Layout

The standard repo layout (durable-knowledge, "Repo layout"); `skills/` and `agents/` are this repo's code.

| Entry | What it is |
|---|---|
| `README.md` | This page: what it is, how to install it, what is where |
| `AGENTS.md` | The rule sheet and skill index every session loads. The product, and this repo's agent rules |
| `CLAUDE.md` | One line, `@AGENTS.md`. `~/.claude/CLAUDE.md` imports this file by path, so its name never changes |
| `docs/` | `STATUS.md`, `DESIGN.md`, `DECISIONS.md`, `LESSONS.md`, `CANDIDATES.md` (lessons seen once, waiting to recur), `REQUIREMENTS.tsv` (every requirement in `AGENTS.md` and the roles, with the owner's quotes behind them, and the local agents' core rules in its `core` and `scope` columns), `runbooks/` |
| `skills/` | One folder per skill, `skills/<name>/SKILL.md`; linked into `~/.claude/skills/` |
| `agents/` | The role agents (**agent-team**), one file each; linked into `~/.claude/agents/` |
| `tools/` | `sync-claude` (keeps a machine on the latest library), `check.sh` (every check), `gen_local_agents.py` and `hooks/` (the Qwen Code install), `check.py` (library consistency), `check_requirements.py` (no requirement or quote dropped from `AGENTS.md` and the roles), `layout-check` and `repo-layout.json` (the repo layout standard), team metrics scripts |
| `tests/` | Tests for `tools/` |
| `local-agents/` | Generated by `tools/gen_local_agents.py` from `agents/`, `AGENTS.md` and `docs/REQUIREMENTS.tsv`: the roles and the rule sheet for Qwen Code, their core-sheet versions (`qwen/AGENTS-core.md`, `qwen/agents-core/`), and `LOCAL-TOOLS.md` |

## Credits

The banner image is AI-generated; the title over it is set as text in `.github/banner.svg`.

## When it breaks

- **A session doesn't follow the rules, or `/context` lacks them:** [docs/runbooks/fix-rules-not-loading.md](docs/runbooks/fix-rules-not-loading.md).
- **`tools/check.sh` fails:** each line names the file and what is wrong; fix that and re-run.
