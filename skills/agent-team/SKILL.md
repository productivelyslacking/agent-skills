---
name: agent-team
description: Splitting a project across role agents: briefs, parallel worktrees, evidence before "done", cutting the team's token waste. Use when planning work for agents, writing a brief, running agents in parallel, checking an agent's claimed result, or measuring team cost.
---

# Agent team: roles, briefs, evidence

Assumes **ground-truth**. Thesis: **the producer (the main session) turns the user's direction into written briefs;
specialists do the work; nothing is done until its evidence is seen.** Roles live in `agents/` here, linked into
`~/.claude/agents`; the project's CLAUDE.md supplies its facts, and a same-named file in a project's `.claude/agents/` overrides one. `NOTES.md` here holds the
incidents behind these rules.

**The core cast fits any software project:** producer, developer, tech-lead, qa and, when merge approval is delegated,
merge-reviewer. Games and story work add designer, writer, presentation, publishing, director and psychologist; skip
them and the GPU lock where they don't apply. Game examples generalize: player data is customer data, a
playthrough an end-to-end check.

## Who does what

| Role | Owns | Hands back |
|---|---|---|
| **producer** (main session) | Briefs from the direction, order and dependencies, decision numbers, merging, telling the user | Status the user can act on |
| **designer** | Mechanics, progression, balance, levels, quest structure | A spec with numbers and acceptance criteria; content data |
| **writer** | Lore bible, dialogue, quest and in-world text, names, in the bible's voices | Text in the content format; bible updates for every new fact |
| **tech-lead** | Structure, interfaces, cross-system review, build and tooling | A design note or review findings |
| **developer** | Gameplay, systems, tools, their tests | Code on its branch, tests, build output |
| **presentation** | Art direction within the user's style and the director's look targets; assets, UI, animation, audio, effects | Engine-ready assets, before/after renders |
| **qa** | Independent checks: tests, renders, clips, perf, saves, regressions | Pass/fail per criterion with evidence; bug reports |
| **team-ops** | How the team runs: tokens per merged change, review round trips, rebase hotspots, GPU waits. Never trades quality for a saving | Metrics against the last run; library fixes on a branch; project changes as briefs |
| **publishing** | Funding and selling: comparables, backer expectations, demo checklist, pitch, budget, store copy. Never contacts, publishes, spends or signs | Sourced research; drafts for the user |
| **director** (story-led only) | The vision across story, look, voice and pacing: what the work rejects, which scenes exist, whether a piece goes in. Reads all story; doesn't write it or make art. Named veto (`agents/director.md`) | Recorded decisions, notes on reels; plot-free status when story is sealed |
| **psychologist** (when a brief asks; loads **psychology-review**) | Likely effect of a scene, lesson or character choice on learning and the audience. Advises; doesn't decide | Effect, evidence and kind, how sure, a proposed test |
| **merge-reviewer** (when merge approval is delegated) | The merge gate: retests the branch rebased on main; checks the brief's evidence and project rules | APPROVE, REJECT or HOLD (what the user keeps: look, save formats, destructive or public steps) |

**The producer delegates hands-on work** and keeps to briefs, reviews, decisions and the user: a producer doing the
work is unavailable, and its work goes unreviewed.

**A director only when story is the product;** other projects skip the role (D25). The producer decides budget,
schedule, order and how long a scene's done condition may run; the director, what's in the work and whether a piece
goes forward; neither waives the other's. In a forced cut the producer sets the size, the director picks what goes. A
dispute goes to a test, else after one round to the user, plot-free. Premise, cast balance, content limits, art style
and voices stay the user's. If story is kept from the user, follow
"Keeping story from the owner" in **directing**, and **the project's CLAUDE.md says so in the words given there.**

**The user judges feel and look** at each milestone by a human playtest, or, if story is kept from them, by
plot-free frames and a test scene until their first play. A render proves something is drawn, not
that it is good. **Human tests attach to commitments:** run one before the work it could change is finished; fresh testers, not the user or team, answer "would a stranger understand this" (D25;
**production-stages**).

**Split a role only when it becomes the bottleneck;** a role is started per task, not a standing process.

## Work the critical path

Busy is not progress; a moving deliverable is (D13).

- **Every task the producer starts is on the path to the current milestone's exit:** an open issue in it, or something
  one needs. Hardening, tooling, docs passes and review follow-ups are off the path unless a milestone issue needs
  them; the brief names which.
- **When an agent finishes, start the next path task unasked,** if one can't collide with work under review.
- **Follow-ups go to the backlog labelled `later`;** unattended work never picks one, and only the user moves one out.
  File player-facing bugs as issues; anything else is a PR comment.
- **When everything left needs the user** (a look or feel call, a playtest, a sign-in, spend), send one message listing
  it, each with a recommendation, and stop: invented work refills the queue.
- **Every report to the user opens with `<milestone>: n of m closed`.** Two rounds with nothing closed: ask whether to
  re-scope.

## The brief (every handoff)

```
Outcome:     what the player (or the team) can do afterwards, in one or two sentences.
Ownership:   the files and systems this agent may change; everything else is read-only.
Constraints: decisions that bind it (by number), interfaces, budgets (frame time, memory), style.
Acceptance:  numbered, checkable criteria. "Feels good" is not one; "the dash covers 6 m in 0.25 s" is.
Evidence:    what proves each criterion: test names, build output, a still or clip at a named frame,
             a perf line. Say where it must be saved.
Context:     the branch or worktree, related decisions, what was tried before, and the main it starts
             from. Main moves while you work: don't bring it in for that; bring it in once before hand-back
             (rebase if nothing is pushed yet, merge if anything is), keeping both sides of any conflict in
             an append-only doc; any other conflict goes in the hand-back.
```

A brief the agent can't check itself against is the producer's bug.

## Handoffs that work

- **Spec → build → independent check → review → merge.** QA checks the acceptance criteria, not the summary; the tech lead
  reviews before merge. Art and audio join once behaviour is stable; where story carries the work, finished art and
  final voice also wait for its story test (**production-stages**).
- **Read the evidence, not the report** (sealed story: the exception in **directing**). "Done" is a claim: open the
  render, read the test output; builds report success on stale output and renders look fine over placeholders.
- **A reviewer or checker that returned nothing did not pass.** Timed out, crashed, denied a tool or no verdict: retry
  once, then record it as **not run**, with what it would have covered, never as zero findings. A landing that needs
  its verdict waits, or the user decides (D15).
- **With CI, the branch head's run is the build and test evidence;** the hand-back links it. Builders run the
  narrowest check covering their change; QA and the tech lead read the run's output and re-run only what it misses
  (renders, clips, playthroughs, cases beyond the brief). The merge-reviewer's rebased run (D9) is the one full
  re-run.
- **A fix for a bug the user saw starts red on main, on the device's path:** the backend it selects, the original
  input bytes, any server fallback. Then show the branch passing; a fix proven on another path passes every gate and
  leaves the bug. If main can't be made to fail, report "not reproduced" and diagnose instead of fixing.
- **Subagents may lack publishing tools:** they hand back a file path; the producer publishes.
- **A fresh reviewer gets only the brief and the artifacts;** past reads and rulings come after its own read, if at
  all, or they anchor it. Check what a file holds before calling it a check list.
- **QA doesn't fix what it judges.** It returns findings for the producer to route; lacking Edit/Write
  but not Bash, that is a convention, not a sandbox.

## The board

Keep the team's state in a repo file (e.g. `docs/BOARD.md`): in progress (work, role, branch), next, waiting on the
user, recently done. The producer updates it at every hand-off and merge; agents run one task and stop, so it is the
plan's only home outside the producer's session.

## Running agents in parallel

Merging a branch: **landing**.

- **Each coding agent gets its own worktree and branch.** Write "make a worktree", not "work on main with a new
  branch", which an agent may read as switching the main checkout.
- **A bare worktree lacks everything git-ignored** (fetched art, generated models, caches), so agents there render
  placeholders and believe them. Use the project's worktree setup script, not the agent
  `isolation: worktree` setting, for roles that render.
- **Removing a worktree deletes its git-ignored files, maybe the only copy.** Run `git status --ignored` there, copy
  what's worth keeping to the main checkout and back it up; never `--force` without that look. Better, briefs install
  outputs to a shared, backed-up location.
- **Per-checkout files (a local art overlay) don't merge with git.** Back up main's copy, add only the branch's new
  entries (its whole file lacks what main gained), and diff. Their backup tools refuse to run from a worktree.
- **Put "use scratchpad/<task>/" in every brief:** agents in one session share its scratchpad and overwrite its root.
- **A negative control must fail for its stated reason:** give each broken copy the words or code its failure must
  contain, and fail the run otherwise, or it can pass for the wrong cause.
- **Don't open CLAUDE.md (or the AGENTS.md it imports):** it is attached, with the root's, when an agent first Reads a
  file in its folder, so an explicit read loads it twice. Briefs name the first file to open. Bash reads attach
  nothing, so a Bash-only agent first Reads one main-checkout file. Every rule stays in the root file.
- **Stop processes by PID, process group or session, never by name:** a name matches other agents' jobs and, on a
  handheld, the compositor. A stray another agent left may be stopped by PID once verified as the team's (our account,
  a team script or tool) with its owner finished and nothing waiting on it; say so in the hand-back and report
  unverified ones to the producer.
- **Anything a test creates on a shared host is named per run and removed only by that run** (containers, networks,
  volumes, compose projects, temp folders, free ports): fixed names make parallel agents clobber or wait on each other.
- **One GPU job at a time.** Renders, clips, perf runs and generation take the project's GPU lock, since parallel GPU
  jobs can fault the card until reboot; coding and tests run in parallel. Every lock logs wait, acquire and release
  with a job name on every machine, so queue waits are measured.
- **Shared files conflict on merge** (the decisions log, asset manifests, scenes). **The producer hands out decision
  numbers** in the brief; one owner per scene or binary at a time; shared docs keep lists one item per line. **Rebase
  before the first push, merge after** (the brief's Context): a pushed commit may be pinned by a reviewer, CI run or
  evidence link, so never rewrite or force-push it; a reviewer's throwaway copy can always be rebased (D16).
- **Builders don't chase main:** tell a running builder that main moved only when the landed change touches its
  Ownership (not append-only docs).
- **Two or three agents on shared code, fresh per task:** more makes every landing force rebases, and long-lived
  agents bloat; brief a fresh one with the last one's details file. Each user-facing landing ends with 2-4 things to
  try on the user's device, where some bugs only show; on a sealed project, from a plot-free test scene.
- **On a shared machine** check free memory against a heavy job's measured peak, time-box load tests and log them
  where others look; on someone else's, gate every job on nobody using its GPU.
- **One router for heavy work, by default:** with several machines, a job router (code, not an agent) places builds,
  tests, simulations, renders and generation, each kind only on machines proven to match the reference machine (same
  input, difference measured, plus a one-line-change control that differs, recorded with the route). Route by
  strength, never by a lower setting; briefs make the router the default. "Keep work off X" is one switch everything
  honours, not a message to each agent.

## Running the factory lean (never at quality's cost)

**Quality is never the saving:** no skipped check, weaker gate, thinner needed context or cheaper asset setting; a
proposal that can't show quality holds is dropped.

- **Pick the model tier by the task, not the role:** strongest for judgment (designs, reviews, merge gates, story and
  look calls, diagnosing a failure), fast for mechanical work (searching, running a known script, moving text,
  extracting data), balanced otherwise; effort follows the same split. Never move a gate down a tier: a weaker gate
  misses defects silently. Move other work down only after running one task on both tiers and comparing (D30). Role
  files keep `model: inherit` until a comparison says otherwise.

- **The producer keeps its context small:** at a milestone or past ~400 k tokens, write state to the board and
  direction file, then compact or start fresh.
- **Hand-backs are about 1,500 characters:** verdict, one line per acceptance criterion, findings with file:line (never
  cut to fit), and a detail file `scratchpad/<task>/details.md`. Claude Code refuses subagents files named
  `report.md`, `summary.md` or `findings.md`.
- **The brief carries the task, not the house rules:** identity, commit trailer, worktree, GPU lock, scratch and
  process rules live once in the project CLAUDE.md's team section (or the brief, where there is none). Name what to
  read ("D82; DESIGN 'Gods'"), not whole docs.
- **Briefs that change the same code run in sequence,** or the later starts from the earlier's branch: each landing
  makes the others redo their evidence. First compare each brief's Ownership with every branch in flight (`git diff
  --name-only main...BRANCH`); append-only docs don't count.
- **Confirm a look or feel direction before the full build:** restate it as one concrete change and confirm, or make
  the first deliverable one still or sketch. A verbatim quote fails beside a producer rule that says otherwise.
- **Research briefs carry a search budget,** since a session's searches are shared and capped; reserve some for checks
  that must be complete (name screening), and mark a check incomplete when they run out.
- **Numbers every branch changes stay out of prose:** no test counts in STATUS or READMEs. Only the producer edits the
  board and STATUS, at merge. A table most branches add to is generated from its sources, with a `--check`.
- **Code does what logic can:** steps agents repeat (landing, a review copy, a contact sheet) become a script that
  prints a summary and exits non-zero on any failure, with a negative control; only where as trustworthy, and its
  output is still read. Team-ops ranks the candidates.
- **Adopt before you build:** a brief for a new tool, service or pipeline stage names the established open-source
  candidates and an adopt, wrap or build decision with reasons (**dependency-policy**, "Before building a tool"); the
  producer approves no build brief without it.
- **Wait once per job:** block in one call until its end line, success or failure, or its process is gone, with a
  timeout near the tool's limit (`timeout 590 bash -c 'until grep -qE "^(done|FAILED)" LOG || ! kill -0 PID; do sleep
  10; done'`), or submit through the router in the foreground; each sleep-and-look re-reads the context. A job with no
  log may be queued: check the router before restarting it. Never wait on a `pgrep -f` of a string the loop contains:
  it matches itself.
- **Watch for stalls with code:** on every agent notification, a check flags any in-flight task folder with no new
  file for 30 minutes. Diagnose a review past 2 h, a dev task past 4 h, a second round or re-check.
- **Team-ops runs** every ten merges or at day's end, against the last run.

## Common rationalizations

| Rationalization | Reality |
|---|---|
| "This check needs a check of its own." | A harness that tests the tests is more code to test. Negative controls are for gates. |
| "While I'm here, I'll fix the other places too." | The branch keeps growing. List them; sweep only gate, security, data. |

## Roles learn

When an agent's report teaches something general about its role and it cost real time, the producer records it the same
day: in the role's file only if it passes **durable-knowledge**, "Admitting a rule, skill or role" (replace or merge
first, within the role's budget), otherwise as a candidate. Facts about one project go to that project's lessons file.

## Phases

**Concept** (owner, producer, designer: audience, core loop, what "finished" means) → **prototype** (designer,
developer: is the core fun, placeholder art) → **look test** (presentation, a few shots at target quality, D25) →
**production** (developers and content, QA on every increment) → **polish and release** → **post-launch** (reports
feed a fix queue). What each stage must prove, and when finishing waits for a story test: **production-stages**.
