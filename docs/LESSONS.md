# Lessons

Traps and corrected facts about this repo. Lessons from other projects waiting to become skills are in
`CANDIDATES.md`, not here (docs/DECISIONS.md, D3).

- **2026-10-08 - The library's `CLAUDE.md` is imported by path on every machine: never rename or move it.** Its
  content is the line `@AGENTS.md`; the rules are in `AGENTS.md`. Copying `CLAUDE.md` somewhere copies only the
  import line, which resolves against the copy's folder and silently loads nothing.
- **2026-10-08 - `claude -p --setting-sources project` loads `~/.claude/CLAUDE.md`'s own text but not its imports.**
  (Seen 2026-10-08: its machine facts were quoted, the library rules it imports were NOT FOUND.) That is how to
  test an import chain without touching the real one: put the chain in a scratch folder's `CLAUDE.md` and ask for a quote
  only the chain carries; break one link and the same prompt must answer NOT FOUND. Keep the files under the scratch
  folder: there, a project `CLAUDE.md`'s imports from outside its folder are not loaded (they need approval).
- **2026-10-08 - Run `tools/check.sh` before every library commit, not only in CI.** `tools/check.py` was red on
  main from e59f7fc (one candidate wrote "Candidate home:" for "Target:") and later commits landed on top of it.
- **2026-11-13 - On Windows, run `tools/check.sh` in WSL. Don't port the tests to Windows Python.** Under Git Bash,
  the check failed four ways in turn: `python3` was the Store stub, files decoded as cp1252, `fcntl` is missing, and
  relative paths came out with `\`. After those, 87 of 107 tests still failed on Unix assumptions. In WSL, all
  107 passed with no code change. Only the session hook has to run on the Windows side (README, "Run it").
- **2026-11-13 - Git for Windows checks out CRLF by default (`core.autocrlf=true`), so `.gitattributes` forces LF.**
  `tools/gen_local_agents.py` hashes source bytes as git blobs, so in a CRLF checkout every generated file reads as
  stale. After adding `.gitattributes`, re-check out existing files: rules apply only on the next write.
- **2026-11-13 - Moving the clone: `tools/sync-claude` won't clean up after the old path.** It adds the new import
  line to `~/.claude/CLAUDE.md` without removing the old one (the rules then load twice), and it prunes only broken
  links that point into its own clone. To move: change the import line and the hook's path by hand, delete the links
  in `~/.claude/skills` and `~/.claude/agents` that point at the old clone, then run `tools/sync-claude` from the new one.
- **2026-11-13 - A tree exported and re-added on Windows loses its executable bits.** `git archive | tar -x` into a
  new repo under Git for Windows (`core.filemode=false`) committed every script as 100644, and CI failed with
  "Permission denied" on `tools/check.sh`. Restore modes with `git update-index --chmod=+x` from the source tree's
  `git ls-tree` and confirm with `git ls-files -s` before the first push.
- **2026-11-13 - OpenCode 2.2.7 fails quietly, and its docs describe more than it does.** It skips an agent file in
  Claude Code's format, and drops a bad field (a colour name) from a v2 one, with only a log line; it reads neither
  `~/.claude/CLAUDE.md` (its rules page says it does) nor `@` imports. Its background service keeps the old config
  until `opencode reload`. Test what it loads, not the files: `tools/sync-opencode --check`, and for the rules
  `opencode run "Quote the bold title of working rule 10, or say NONE"`, which must answer NONE after `--uninstall`.
