---
name: landing
description: Getting a branch onto main: what blocks, review rounds, disputed findings, pinned merges, merge conflicts. Use when reviewing a branch for merge, deciding whether a finding blocks, resolving a conflict, or when reviews keep going round.
---

# Landing

Assumes **ground-truth**. Thesis: **what lands is a tree that was built and tested, after at most two review rounds in which
only real problems block.** It holds for any project (D20): where a rule says saves or players, read stored data and users.
The merge gate itself is `agents/merge-reviewer.md`. `NOTES.md` beside this file holds the incidents and numbers.

## What blocks, and how long it takes

- **Besides the merge-reviewer's bar, only breaking and major issues block a landing.** Breaking: the change fails its
  main job, regresses something that works on main, or loses or corrupts data or saves. Major: wrong money or data,
  security, safety. A minor bug a player could hit is filed as an issue labelled `later` and the change lands; a nit,
  refactor, hardening idea or "while you're here" goes in one combined pull request comment and is not filed, since
  filing every finding buries real issues in follow-ups.
- **Two review rounds at most.** After a second REJECT, the producer lands the smallest version no worse than main, or
  drops the change and says so.
- **Weigh the merge review by risk.** Wording, UI copy and docs get a light review (the build and the checks that read
  the changed doc still run); money, security, saves, player data and CI get the full one. Every change still goes
  through the merge-reviewer (D9); only the depth changes.
- **Small branches.** One change per branch: a few hundred lines, one acceptance list. Fix rounds fix findings only; a
  new problem becomes its own branch, because each added scope costs a full re-review. When a review rejects one piece
  of a separable branch, land the pieces that passed.
- **Keep the PR check under about ten minutes**: every landing re-runs it on each open branch, so it sets how fast work
  lands. Slow suites (playthroughs, renders, end-to-end runs, long simulations) run on main, nightly, or on branches
  touching their paths; the merge-reviewer still runs what the project's rules require.
- **"Docs-only" means no file a test, tool or build reads.** Such a review skips the test suites but not the build, the
  checks that read the changed doc, or the content review: docs and designs carry real defects.

## Review rounds

- **Keep a settled list across review rounds** and give it to the next reviewer, who otherwise can't tell a closed
  finding from an open one (D15). A finding is settled when a reviewer withdrew it after checking the evidence, or the
  user accepted the risk; it stays closed unless that evidence proves wrong. A fix doesn't settle a finding: the same
  issue in the same place reopens it. A new finding that reverting a fix would resolve is churn: stop and put the
  choice to the user. Only the user can waive a miss on the merge-reviewer's bar, and a gate's plants are still re-run.
- **A dispute needs evidence the reviewer can read:** a file and symbol, a run, or a recorded decision. "It was
  intentional" is not evidence. Evidence no reviewer could read (the user's word, an unwritten convention) goes to the
  user, and if confirmed into the decisions log. Dispute a severity the same way, never by relabelling it. Add text to
  a doc when a human reader needs it, not only to satisfy a reviewer with no history (D15).
- **Fix the class, not the instance, for gate, security and data findings.** When such a finding is one case of a
  pattern (a check that trusts a file the branch can change; a claim with no measurement), the reviewer names the
  pattern, and the fix sweeps for every other case and lists the sweep in the hand-back; otherwise each round finds one
  more. For any other finding the hand-back lists the other places and leaves them, since a sweep keeps growing.
- **A long re-review starts fresh.** Past about 200 k context, a re-check goes to a new reviewer given the previous
  rounds' details files (every finding and planted break) and the settled list, re-running each earlier plant before
  looking for new ones; not a SendMessage to the old one, which carries the whole history into every call.
- **Don't message a running review.** Queue new direction and send one combined re-check after the verdict, or each
  message forces a duplicate verdict.

## Merging

- **Conditional approval instead of a round trip.** For a fix needing no judgement (prose, a number the reviewer
  measured, an analyzer warning, a conflict resolved by keeping both sides), the reviewer applies it to its throwaway
  copy, re-runs what it touches, stages it (`git add -A`) and returns APPROVE-IF with the patch (`git diff --cached
  --binary`) and `git write-tree`, the tested tree including the fix (`HEAD^{tree}` would omit it). The producer applies
  the patch, commits, and merges only if `git rev-parse HEAD^{tree}` equals it; otherwise it's a REJECT. The reviewer
  never writes to a branch.
- **Look for open pull requests before pushing to a file they touch.** `gh pr list`, and a trial merge shows the damage
  without touching anything (`git merge-tree --write-tree main BRANCH`); a direct push can multiply an open PR's
  conflicts (D15).
- **Keep-both is safe only when both sides purely add**; otherwise it can plausibly restore a deleted row. Check the
  result against both parents: every line either added is present, every line either deleted is absent.
- **A landing gate waits for every required check to exist.** A status read too early is blank or pending, not final.
  Accept pass or skipping, since a job skipped by its `if:` counts as success, and still require the platform's merge
  state.
- **A re-check forced only by main moving is mechanical and can run on a smaller model:** rebase, confirm no conflict
  and that the diff from the reviewed tree is main's change alone, re-run build, tests and docs checks, report the tree.
  Its brief says to stop and answer ESCALATE on any conflict, failure or surprise, which the first reviewer takes.
- **Pin a pull request's merge to the head that was tested:** `gh pr merge <n> --merge --match-head-commit <sha>`, never
  `--admin`, so GitHub refuses if the head moved. Only branch protection also refuses a red or stale head, and on a
  private repo it needs a paid plan, so without it read the CI run yourself first. A session permission rule is not
  that gate: every agent in the session shares it (D16).
- **The producer holds its own commits to main while a review is out,** because every commit to main sends a review back
  for the exact-tree re-check. Board, direction and CLAUDE.md edits are batched and pushed right after the next landing
  in one commit, unless a brief about to start needs the new rule (then commit first, and tell the reviewers out).
- **Where a landing script or merge queue proves the exact tree, reviews judge on a pinned main**, so main moving doesn't
  send each reviewer back to a long end-to-end run. The review judges the branch on the main its brief names; the
  landing step (code) rebases onto current main, stops on any conflict outside append-only docs or any change to the
  branch's own non-doc diff, runs the full checks and the end-to-end check on that exact tree, and only then
  fast-forwards. Main's new commits touching the branch's non-doc files send it back to review; other moves don't. It
  changes a gate, so the user turns it on per project.
- **Append-only docs: conflicts resolved by a tool run on purpose; nothing generated is written by hand.** A resolver
  script, started by whoever merges from a copy
  they trust (the landing script: main's), merges only when each side keeps every base entry unchanged, keeps each
  side's new entries whole where that side put them, never deduplicates, and otherwise leaves git's conflict. Not
  `merge=union`: it drops the lines two appended entries both end with and joins two edits of one line, and after a
  rebase neither shows as a deleted line. Not a merge driver in `.gitattributes`: git runs it from the work tree on
  every merge and rebase, so merging a branch runs that branch's code on the host. The check walks the branch commit by
  commit: a commit changing an existing entry carries its own reason trailer, a merge holds no entry neither parent
  has, new entries are well formed, and entries are parsed fence-aware on "\n" only (CRLF, U+2028 and form feed fail).
  A decisions index is generated from the headings with a `--check`; reserved numbers live in the producer's log, never
  in the file. Branches write no status lines about themselves ("under review", "next step"), which go stale within
  hours; the producer folds STATUS at merge.
- **A branch adding a destructive CI step isn't pushed until the deletion is approved,** or the step ships disabled (a
  dry run) and is switched on after landing: CI runs branch code on push, before any gate. The reviewer reads a
  workflow diff's destructive steps as a deletion, not as code.
