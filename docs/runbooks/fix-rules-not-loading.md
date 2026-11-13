# Fix rules not loading

**Just do this:** in a new session run `/context`. Under **Memory files** you must see `~/.claude/CLAUDE.md`, the
library's `CLAUDE.md` and the library's `AGENTS.md`. In the desktop app, `/context` shows only a token total for
Memory files (seen 2026-11-13); open the app's Memory panel instead, which lists each file and the imports under it.
Whichever is the first one missing is where the chain broke:

| First missing | Cause | Fix |
|---|---|---|
| the library's `CLAUDE.md` | `~/.claude/CLAUDE.md` doesn't import it, or names a path that doesn't exist | make its first line `@/path/to/agent-skills/CLAUDE.md` (the clone's real path) |
| the library's `AGENTS.md` | the library's `CLAUDE.md` is not the line `@AGENTS.md`, or `AGENTS.md` is missing | `tools/layout-check .` in the library names which |
| a skill (`/skills` lacks it) | its link in `~/.claude/skills/` is missing or dangling | re-run README, "Run it", step 2 |

Imports fail silently: nothing warns when a path doesn't resolve. Two checks without opening a session:

```bash
# The whole chain, as every session gets it (~/.claude/CLAUDE.md -> library CLAUDE.md -> AGENTS.md):
cd "$(mktemp -d)" && claude -p --tools "" <<< 'Quote the bold title of working rule 10, or say NOT FOUND.'
# Only the library's own hop (CLAUDE.md -> AGENTS.md), without ~/.claude/CLAUDE.md's import:
cd /path/to/agent-skills && \
  claude -p --setting-sources project --tools "" <<< 'Quote the bold title of working rule 10, or say NOT FOUND.'
```

Each answers "Design for a human with little time and attention." when its part works. If the first fails and
the second passes, the break is in `~/.claude/CLAUDE.md`. Don't test with a scratch folder whose `CLAUDE.md`
imports the library by absolute path: in `claude -p`, a project file's imports from outside its folder are not
loaded (they need an approval prompt), so it answers NOT FOUND even when the chain is fine (seen 2026-10-08).
