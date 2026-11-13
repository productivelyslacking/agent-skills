# landing: notes

Read on demand. Holds the incidents, numbers and dates behind the rules in `SKILL.md`, under its section headings. The
rules moved here from **agent-team** (D20).

## What blocks, and how long it takes

- **Filing minor bugs, not blocking on them:** a web app, 2026-10-16: the user asked that bugs be filed, not stop
  development. Filing every finding made follow-ups most of one project's new issues.
- **Two rounds:** a web app, 2026-10-16: a review-tooling branch went four rounds over nine hours on edge cases no worse
  than main.
- **Risk-weighted review:** the user adopted it on a web app, 2026-10-15.
- **Small branches:** a web app, 2026-10-15: a branch whose fix rounds each added scope took 5 review rounds, each
  re-reviewing everything; small focused branches landed in one pass.
- **PR check length:** on one project the pull request check took 28 minutes.
- **Docs-only:** examples of checks that read a changed doc are a queue or lore checker. Half the real defects caught on
  2026-10-05 were in docs and designs.

## Review rounds

- **Settled list:** the same issue in the same place means the fix failed or a later edit undid it.
- **Fix the class:** 2026-10-06, a review-prep script: rounds 2, 3 and 4 each found one more branch-controlled input the
  checks trusted (its test.sh, the fast-suite filter, a warnings config), 181 M tokens of fix and re-review rounds,
  about 140 M of it after the pattern was first visible.
- **Fresh re-review:** the same reviewer averaged 118 k per call in round 1 and 358 k in round 4 (211 calls, 75.6 M;
  2026-10-06).
- **Messaging a running review:** three forced duplicate verdicts on 2026-10-05.

## Merging

- **Open pull requests:** one direct push took an open pull request from 1 conflicting file to 15 (D15).
- **Keep-both:** it restored a row one side had deleted, and the result read as plausible.
- **Mechanical re-check on a smaller model:** the user approved this, 2026-10-07.
- **Producer's own commits:** on 2026-10-06, 60 of 163 commits to the game's main were the producer's own docs, and they
  caused 4 of the 7 re-checks forced only by main moving.
- **Pinned main:** a Linux service project, 2026-10-21: main moved 12 times under 8 of 14 reviews in one day, each
  sending the reviewer back to a 30-minute end-to-end run. Adopted for that project, 2026-10-21.
- **Append-only docs:** the `merge=union` and merge-driver failures were both measured on a Linux service project,
  2026-10-21. Same project and day: 11 landings; main moved 12 times under 8 of 14 reviews, and every rebase conflict was
  in LESSONS, DECISIONS or STATUS (none in code); 8 review findings, one of them a REJECT, were STATUS lines gone stale
  within hours; a decision landed without its index line, and a decision's own text went stale ("D43, D44 and D46 are
  taken by branches in review"). "On its branch" is another self-status line.
- **Destructive CI step:** on a web app, 2026-10-15, a new cleanup step deleted 94 volumes on the CI host before anyone
  had approved it.
