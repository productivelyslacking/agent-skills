# durable-knowledge: notes

Read on demand; holds the evidence behind SKILL.md's rules: the incidents, numbers, dates and approvals.

## Where it goes

- A project built a test and a tool only to hold lessons: checkers for its lessons file's order and dates. Hence
  "never build a test or tool only to hold a lesson".

## Repo layout

- The standard layout was approved by the user on 2026-10-08 ("as recommended").
- The template repo on the forge did not exist yet on 2026-10-08: the agent's token could not create repos in the
  forge organization. Until it exists, `layout-check --stub` in an empty `git init` stands in.
- Committing evidence for every change put 338 files, about 6 MB, into one project in three days, each one more
  thing to review and to conflict on.
- The second form (per-file decisions and status) was approved by the owner for a web app on 2026-10-21 (that
  project's audit decision D-1; D12 in the library's `docs/DECISIONS.md`).
- "Open work lives in the issue tracker" came from the owner on 2026-10-20, after one project's backlog was moved
  into issues: the owner asked for a rule enforcing it going forward.
- This library's own STATUS said merged work was unmerged for four weeks: why status claims carry a date or commit.
- One project's agent read-first list came to about 140 KB, paid again by every agent on every task.
- Agent CLIs that read `AGENTS.md` directly: opencode, Qwen Code, Codex, Gemini CLI.

## Format

- Example of an incident headline to avoid: "2026-10-30: `/opt` broke the build".
