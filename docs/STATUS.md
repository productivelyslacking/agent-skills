# Status

Where things stand today and the next step (pick up here). Updated 2026-11-13, after D33. Open work is in the issue tracker.

## Where things stand

- **The library is in use on `main`:** the standard layout, the condensed rules with `docs/REQUIREMENTS.tsv`, and the
  core rule sheet (D1-D10) are all merged, and their `work/*` branches are gone. CI's `check` passed on D15's commit.
- **Latest decisions:** D13 keeps the studio on the goal, D14 syncs each machine at session start, D15 adds four review
  rules from Google's Elephant-Goldfish Model, D16 pins merges to the tested head, and D17 vets third-party skills and limits
  repeated fixes. D18 adopts the rest of the outside research. One D15 rule and the diagnosis rule have had small baseline tests
  (D17, D18); none has been used in real work. D22 adds two teaching skills from a literature review; as of 2026-11-06 they
  haven't been used in real work or baseline tested, and are due a revision after a Python learning game's first playtest.
  D23 adds two story skills the same way; as of 2026-11-06 they have the same status, and are due a revision after a story
  game's first playtest.
  D24 adds two art skills from research; as of 2026-11-06 they haven't been used either, none of `generated-art/NOTES.md`'s tests has been
  run, and their first real test is the next run on real models.
  D25 adds production-stages, directing and a director role the same way; as of 2026-11-06 unused, and due a revision
  after a story-led game's first owner playthrough. Its biggest open risk, written in directing: nothing shows AI cold readers predict human surprise.
  D26 adds the psychologist role and psychology-review skill the same way; as of 2026-11-06 neither has reviewed real work, and
  they are due a revision after their first review of a story game that teaches programming.
- **Machines:** set up and checked on Linux (2026-11-07) and Windows with the check in WSL (2026-11-13): README, "Run it".
  Machine notes and personal rules live in each owner's `~/.claude/CLAUDE.md`, not here (D27).
- **Local agents (Qwen Code):** the generated files are on `main` and `--check` passes. Qwen Code is not installed on
  this machine (no `~/.qwen`). The owner isn't using them as of 2026-11-07 but may again, so the files stay, `--rules full`
  stays the default, and the full-or-core question waits (#13).

## Next step

Public since 2026-11-13 at https://github.com/productivelyslacking/agent-skills, as one squashed commit; the
pre-squash history is archived privately as `agent-skills-presquash`. Later (D33): a pinned install distinct from
tracking `main`; the team workflow as an explicitly optional profile. All open work: `gh issue list`.
