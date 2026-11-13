# Design

How the library works and what it is meant to be. Install steps are in README, "Run it".

The thesis running through all of it: **something that sounds right, passes review because it sounds right, and
is wrong** is the failure worth engineering against. Distilled from convention files that grew across a dozen
real repos (compliance authoring, a data pipeline, a marketing site, a PowerShell module suite, a knowledge base,
an employee handbook), then generalized to the parts that hold anywhere.

## Two layers

**`AGENTS.md` is always loaded.** It carries the rule headlines and the skill index: enough to change behaviour
on its own, small enough to cost little. Every line in it is paid for in every session on every machine, so it
stays short.

**Skills load on demand.** Each has a `description` in its frontmatter naming the situations it applies to;
Claude loads the body when the work matches, or when invoked by name. The depth lives there.

## How a session gets the rules (the import chain)

```
~/.claude/CLAUDE.md                     (per machine: "@/path/to/agent-skills/CLAUDE.md" + machine notes)
  -> <library>/CLAUDE.md                (the one line "@AGENTS.md"; its path never changes, D2)
       -> <library>/AGENTS.md           (the rule sheet and index)
~/.claude/skills/<name>  -> <library>/skills/<name>/      (one link per skill)
~/.claude/agents/<role>.md -> <library>/agents/<role>.md  (one link per role)
```

Claude Code resolves a relative import against the file that contains it, so `@AGENTS.md` finds the file beside
the library's `CLAUDE.md` wherever the library is checked out. Proved with `claude -p` on 2026-10-08
(`docs/DECISIONS.md`, D2). Tools that don't follow `@` imports (opencode, Qwen Code) must be pointed at
`AGENTS.md` itself, not `CLAUDE.md`.

## How it grows

- **The rule sheet tells every session to route lessons here.** A lesson or decision that would hold beyond its
  project goes into a skill, or waits in `docs/CANDIDATES.md` until it recurs (**durable-knowledge**, "Feeding
  the library").
- **Admission** of a candidate, rule, role lesson or skill follows **durable-knowledge**, "Admitting a rule, skill
  or role"; this file doesn't restate it.

## Checks

`tools/check.sh` runs them all; CI runs it on every push.

- `tools/check.py`: skill names and frontmatter, the index against the folders and README's tables, the candidate
  format, detail-file names subagents can write, and that durable-knowledge's "Repo layout" agrees with
  `tools/repo-layout.json`.
- `tools/layout-check .`: this repo against the standard layout.
- `tests/`: the layout checker's own tests, each with a broken input that must fail.

## The repo layout standard

The standard's text is durable-knowledge, "Repo layout". Its machine-readable copy is `tools/repo-layout.json`;
`tools/layout-check` reads it to check a repo and to write the template's stub files (`--stub`), so the template
(`lab/template` on the forge) is generated from the same source. `tools/check.py` fails if the section's tree,
four-questions table or forbidden names differ from the JSON.

## A note on the content

These rules came from mistakes, not from theory. Where one seems oddly specific (check for the absence of the
retired claim, not just the presence of the right one; a test that has never failed proves nothing; rationale
written beside the thing it governs does not survive a migration) it is specific because something broke that way
first.
