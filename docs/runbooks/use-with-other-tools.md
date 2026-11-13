# Use the library with other AI tools

**Just do this:** clone the repo, then link the skills into the folder your tool reads and point its rules file at
`AGENTS.md`. Claude Code is the tested setup (README, "Run it"). Every other row below comes from the vendor's docs,
read 2026-11-13, and is **untested here**; check a tool's docs if a path has moved.

Three parts, in order of value:

- **Skills** (`skills/<name>/SKILL.md`) follow the open [Agent Skills](https://agentskills.io/specification) format.
- **Rules** (`AGENTS.md`): the working rules and the skill index, meant to load every session.
- **Roles** (`agents/*.md`): Claude Code subagent files. Gemini CLI, Cursor and Copilot read the same Markdown
  shape, but their tool names differ; untested.

Parts of the text name Claude Code features (CLAUDE.md, subagents, slash commands). Other tools should treat those
as background and use their own equivalents.

## The shared skills folder

Most tools read `~/.agents/skills`. One command links every skill there (bash; on Windows, Git Bash with Developer
Mode on, README "Run it"):

```bash
mkdir -p ~/.agents/skills && for s in /path/to/agent-skills/skills/*/; do ln -sfn "$s" ~/.agents/skills/"$(basename "$s")"; done
```

Re-run it after a pull that adds a skill. Tools that read both `~/.claude/skills` and `~/.agents/skills` (OpenCode,
Cursor) may list each skill twice; link only one of the two for them.

## Per tool

| Tool | Skills | Rules (`AGENTS.md`) | Roles |
|---|---|---|---|
| **Claude Code** | `~/.claude/skills` (`tools/sync-claude`) | `~/.claude/CLAUDE.md` imports the repo's `CLAUDE.md` | `~/.claude/agents` |
| **Codex CLI** | `~/.agents/skills`; symlinks followed | Link or copy to `~/.codex/AGENTS.md` (no import syntax) | TOML in `~/.codex/agents`: not compatible |
| **Gemini CLI** | `~/.agents/skills`, or `/skills link /path/to/agent-skills/skills --scope user` | `~/.gemini/GEMINI.md` holding `@/path/to/agent-skills/AGENTS.md` | `~/.gemini/agents` (Markdown) |
| **OpenCode** | `~/.agents/skills` or `~/.claude/skills` | `"instructions": ["/path/to/agent-skills/AGENTS.md"]` in `~/.config/opencode/opencode.json` (it doesn't follow `@` imports) | `~/.config/opencode/agents` (own format) |
| **Copilot CLI** | `~/.agents/skills` | Copy into `~/.copilot/copilot-instructions.md` (no import syntax) | `.agent.md` in `~/.copilot/agents` |
| **Copilot in VS Code** | `~/.copilot/skills` (Copilot harness) | `~/.copilot/copilot-instructions.md` | `~/.copilot/agents` |
| **Cursor** | `~/.agents/skills` or `~/.claude/skills` | Paste into User Rules (Settings); a project's `AGENTS.md` is read | `~/.claude/agents` read |
| **Grok Build** (xAI CLI) | `~/.agents/skills`, or `[skills] paths` in `~/.grok/config.toml` | Global rules in `~/.grok/` (file name not documented); a project's `AGENTS.md` is read | `~/.grok/agents` (format not documented) |
| **ChatGPT** | Upload each skill folder in Skills (Business, Enterprise, Healthcare, Edu plans only) | Paste into Custom Instructions or a Project's instructions (5,000 characters on paid plans; `AGENTS.md` is about 5,200, so leave out "Working on this library") | None |
| **grok.com** | Upload in Skills; the format isn't documented | Not documented | None |

Gemini CLI's docs say it was replaced by Antigravity CLI for unpaid and Google One users on 2026-06-18; Antigravity
wasn't checked.

## Verify

Ask the tool, in a new session: "Which skills can you load? Quote the bold title of working rule 10." It should list
the library's skills and answer "Design for a human with little time and attention." If the rule is missing, the
rules file isn't loading; if skills are missing, check the link target and that the folder name matches the skill's
`name`.

## Sources (read 2026-11-13)

Claude Code: code.claude.com/docs/en/memory, /skills, /sub-agents. Codex: learn.chatgpt.com/docs/build-skills,
/agent-configuration/agents-md, /agent-configuration/subagents. ChatGPT: help.openai.com articles 20001066 (Skills),
8096356 (Custom Instructions), 10169521 (Projects). Gemini CLI: geminicli.com/docs/cli/skills, /cli/gemini-md,
/core/subagents. OpenCode: opencode.ai/docs/skills, /rules, /agents. Copilot: docs.github.com (Copilot CLI: add-skills,
add-custom-instructions, create-custom-agents-for-cli); code.visualstudio.com/docs/copilot/customization/agent-skills.
Cursor: cursor.com/docs/context/skills, /rules, /subagents. Grok: docs.x.ai/build/features/skills-plugins-marketplaces,
/project-rules, /subagents; x.ai/news/grok-skills.
