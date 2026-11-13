# Run the library with local models (Qwen Code)

**Just do this** (Linux or WSL, Python 3, Qwen Code installed and pointed at your local model):

```bash
cd ~/agent-skills
python3 tools/gen_local_agents.py --install          # skills, roles and rule sheet into ~/.qwen
python3 tools/gen_local_agents.py --install-hooks    # reinstall automatically after a pull
python3 tools/gen_local_agents.py --check-install    # verify
```

Small models: add `--rules core` to the install for a short rule sheet (under 450 tokens) instead of the full one. Undo everything
with `--uninstall` and `--uninstall-hooks`. The details follow.

**Local LLM agents (Qwen Code):** `python3 tools/gen_local_agents.py --install` links the same skills, roles and
rule sheet into `~/.qwen`, turns on Qwen Code's sandbox and gives its agents their own git identity, recording what
was there before (`--check-install` verifies). Then `python3 tools/gen_local_agents.py --install-hooks` adds
post-merge and post-checkout hooks to the clone's `.git/hooks` (a hook of the same name you already had still runs,
first), so a pull or branch switch that changes `agents/`, `skills/` or `AGENTS.md` reruns the install;
`--uninstall-hooks` puts the hooks back as they were. A rerun updates only what is still as the install wrote it: a
setting, link or file you changed since is left as you left it and reported (`kept ...`). Runs take turns on a lock,
and a run that is killed halfway is finished by the next one. The roles are generated into `local-agents/`: rerun
the generator without arguments after changing `agents/`, `skills/` or `AGENTS.md`. The docstring says what Qwen
Code reads and why.

**Core rules for local models:** `python3 tools/gen_local_agents.py --install --rules core` installs a short sheet
(`local-agents/qwen/AGENTS-core.md`, 330 tokens, where the full sheet, `LOCAL-TOOLS.md` and `SKILLS.md` load 6,641 by
the local endpoint's tokenizer on 2026-10-08) as Qwen Code's rules, with core-mode roles (`local-agents/qwen/agents-core/`)
that point at it and carry their own core rules and the identity rule; the full sheet, the skills list and
`LOCAL-TOOLS.md` stay installed for the agent to read when it needs detail (the sheet's last line names them).
`--rules full` (the default, until the 2026-10-08 A/B test decides) goes back; the choice is recorded, kept by
`--sync` and the hooks, and undone by `--uninstall`. Both are generated from `docs/REQUIREMENTS.tsv`: a row's `core`
cell is its line and its `scope` says where it goes (`all`: the shared sheet, only for rules from `AGENTS.md`, a skill
or the generator; a role's name: that role's core-mode file, only for a rule from that role). Each line is tagged
with its row and each file names its sources' git blob hashes: to change them, edit those columns and regenerate.
`--check` fails if they are stale or the sheet is over 450 tokens (estimated offline; the tests also measure it on
the local endpoint's tokenizer when it answers); `tools/check_requirements.py` fails on a mis-scoped row.

**Known limits:**

- **Uninstall:** `--uninstall` removes what the install owns and puts back what it recorded from before. What you
  changed since the install stays as you left it, and a settings key counts as one value: change one field of
  `tools.executionSandbox` and the whole key is yours, so uninstall leaves all of it. A settings file comes back
  byte for byte only if nothing else in it changed.
- **Empty state folder:** a run killed just after it created the lock can leave an empty
  `~/.local/state/gen_local_agents` folder. It is harmless and safe to delete.
- **Claude-only text:** the library is written for Claude Code and mentions tools, modes, commands and settings
  Qwen Code doesn't have. It isn't filtered (no list of such phrasings can be complete). Instead every generated
  role and the rule sheet start with a note telling the agent to ignore those parts and say so when an instruction
  depends on one. `--check` prints how often the known terms appear per file, as a report; `LOCAL-TOOLS.md` gives
  substitutes for the common ones.
- **Rule files in subfolders:** Qwen Code reads rule files (`AGENTS.md`, `CLAUDE.md`) only from the folder it is
  started in and that folder's parents. A subfolder's are never loaded, and telling the model to read them first
  failed in 3 of 3 tests (2026-10-08). Workaround: start the agent in the folder it works in.
