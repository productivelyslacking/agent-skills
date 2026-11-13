# Agent team: notes

Read on demand: the incidents, numbers and sources behind the rules in SKILL.md.

## Who does what

- The producer delegates hands-on work: the owner's call (2026-10-05).

## Work the critical path

- Measured on two projects run with this discipline (2026-11-03, D13): on one, merge reviews outnumbered builds 92
  to 58, and 32 of its last 44 issues were follow-ups raised by reviews and checkers while the milestones that led
  to the deliverable closed nothing.
- Start the next path task unasked: on a Linux service project (2026-10-21) the user had to ask twice while one
  review ran.

## Handoffs that work

- Read the evidence, not the report: on an action RPG, repeatedly, a build reported success with a stale assembly;
  a docker build "passed" because the command ended in `tail`; a render looked fine while every model was a
  placeholder.
- A fix starts red on main, on the device's path: on a web app (2026-10-18) one bug took 6 landings, 23 h and about
  158 M tokens because two fixes passed every gate on a path the phone didn't use (the lab saved a re-encode; evals
  ran wasm, the phone WebGPU); a review even noted "main draws it right here too" and the fix landed.
- A fresh reviewer gets only the brief and the artifacts: on a mystery game (2026-11-07) an art reviewer was pointed
  at a "check list" that was the previous reviewer's full verdict, and read it before any image. An open-source
  video kit's review guide (seen 2026-11-13) gives its fresh reviewer only the storyboard and the contact sheets,
  for the same reason.

## The board

- An action RPG keeps it at `docs/BOARD.md`.

## Running agents in parallel

- "Make a worktree", not "a new branch": an agent took the latter literally and switched the main checkout's
  branch under everyone else (2026-10-05).
- An action RPG makes worktrees with `tools/worktree.sh` and backs up git-ignored outputs with
  `tools/sync-backup.sh`. Removing a merged worktree lost the code-built roofs' textures, which had to be
  regenerated (2026-10-05).
- Per-checkout files: both failures (a whole-file copy over main's newer file; a worktree's backup replacing
  main's) happened on 2026-10-05.
- Shared scratchpad: writing to its root overwrote other agents' files three times on 2026-10-05 (a script that
  shadowed Python's `inspect`, a mixed `base/` tree, render scripts).
- Negative controls failing for the wrong reason: seen twice (wall controls, area-checker fixtures).
- CLAUDE.md read twice: on 2026-10-06 all 19 runs briefed "Read CLAUDE.md with the Read tool first" got the
  17 k-char Read result and then the 16 k-char attachment.
- Stopping by name: `pkill -x python3` (or godot, gamescope) killed other agents' jobs, and on a handheld a name
  matched the system compositor (2026-10-05, both happened).
- Strays: the owner on an action RPG (2026-10-06): "agents can clean up any studio strays too if they can be
  verified as legitimate strays".
- GPU lock: an action RPG's `tools/gpu-lock.sh`, used by its render scripts. Four renders at once once faulted a
  consumer GPU until reboot.
- Builders chasing main: on a Linux service project (2026-10-21) two builders each stopped a 30-minute end-to-end
  run on a "main moved" notice that touched none of their files.
- Agent count: at five to seven agents, every landing forced the others to rebase and re-check. Long-lived resumed
  agents grew to about 950 k of context. Bugs only a real phone showed passed every headless test (a web app,
  2026-10-15).
- Shared machine: a build beside a resident LLM server set off a machine-wide OOM kill, and a heap flag didn't
  bound the build (a web app, 2026-10-13). One agent's CPU burners sent another hunting sub-second test failures
  (a Linux service project, 2026-10-21).
- Per-run names: on a Linux service project (2026-10-21) the end-to-end script's fixed container names made one
  builder wait up to 46 min three times, marked another run suspect, and failed a third agent's check once;
  per-run names (and a concurrent-run test) fixed it.
- Job router: on an action RPG, the day after the router merged, about 300 jobs still ran by hand against 60
  through it, plus 365 hand ssh probes and rsyncs (about 79 M tokens; team-ops, 2026-10-06).

## Running the factory lean (never at quality's cost)

- The tech lead's audit on an action RPG (2026-10-05; 100 agents, 40 merge reviews): the producer was 40% of all
  input tokens (average context 612 k, one compaction all day); half the first reviews were REJECTs, 11 of them for
  fixes needing no judgement (four README-table rebase conflicts, seven stale lines, numbers or one warning), 12
  for real defects. The owner the same day: "we never reduce quality".
- Producer context: the threshold used was about 400 k.
- Detail-file names: Claude Code's Write tool refuses `report.md`, `summary.md` and `findings.md` to subagents
  ("return findings as text"; 6 refusals in 5 runs on 2026-10-06); `details.md` is accepted.
- Overlapping briefs: on 2026-10-06 three branches started within an hour (natural placement, irregular rooms,
  terrain) all changed the area checker, the terrain code, the zone view and the bit-for-bit area dumps; each
  landing made the others rebase and re-run dumps, playthroughs, stills and review.
- Confirming a look: "paths bend" became added bends; the user meant paths worn straight that bend only around
  obstacles, and a branch's roads, stills, playthroughs and review were redone (2026-10-06).
- Search budget: the session's web searches are shared (200 by default,
  `CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION`). On 2026-10-06 four research agents started together spent 117
  searches; the session hit 200 four minutes later, and the next name screening ran with none.
- Code does what logic can: the owner (2026-10-06): "any time something logic can handle it instead". Team-ops
  finds candidates with `tools/team_repeats.py` in the skill library.
- Adopt before you build: the owner (2026-10-07) asked to research whether "a well known open source tool exists
  that fits our need" instead of building "as a reflex".
- Waiting: from 2026-10-04 to 06, 121 to 175 repeat waits cost 30 to 46 M context tokens. A measure launched twice
  41 s apart ran 17 playthroughs twice at once into the same output files (about 264 CPU-minutes, 2026-10-06). A
  `pgrep -f` wait matched its own shell, and a web app's review sat idle six hours after its end-to-end run had
  ended (2026-10-17).
- Stalls: on a web app (2026-10-17) a review sat stuck six hours unnoticed, and thirteen landings passed without
  the team-ops measurement.

## Common rationalizations

- "One more follow-up issue is cheap": review follow-ups became most of one project's new issues while the
  deliverable stood still (the D13 measurement above).

## Single sightings

Moved from the library's candidate list on 2026-11-13 (D29): true of running a team, not yet seen twice.

- **2026-10-22, web-app - Give agents one wait-once CI command, or each writes its own poller.** With no shared tool, 40 agents in a day wrote about 30 CI pollers (ci.py, ci-status.py, wait-ci.py ...), 259 calls and 43 M context tokens, several watching the wrong field. The tool blocks up to just under the shell tool's limit, reads the required list from main (never the branch), exits 0 green / 1 red / 3 still pending, and tells a cancelled job from a failed one: Forgejo's commit-status API reports a job cancelled by a later push as `failure`, so a superseded main commit looks red. Target: agent-team ("Code does what logic can").
- **2026-10-22, web-app - A CI job that serializes on one runner sets the studio's pace; measure each lane's busy share before adding builders.** One `forge` runner ran every check and e2e job one at a time: e2e alone was 14.5 h of a 16.8 h day (87%), a commit's first-task-to-e2e-end wall p50 60 min / p90 94, and each landing made the other branches merge main and push again (12 merge-main commits for 16 landings). Forgejo creates a task only when a runner takes the job, so queue time is not in the tasks API: compute each job name's summed run time over the window instead. Target: agent-team (running agents in parallel).
- **2026-11-06, learning-game - A role linked mid-session may not be startable by type straight away.** Just after landing and linking a new role, `subagent_type: <role>` failed with "not found" though the file was in `~/.claude/agents`; the role appeared in the agent list later in the same session (delay not measured, cause unknown). Don't conclude a role is unavailable for the session. What worked meanwhile: a general agent whose brief opens by reading the role file and holding to its limits, which are then a convention, not enforced tools. Target: agent-team.
- **2026-11-07, mystery-game - A Forgejo token with repository and issue scope can't create a repo.** Creating one needs write:user or write:organization (Forgejo 15, verified 2026-11-07). Ask for the narrow token and have the owner click create, or ask once for the wider scope; don't discover this after asking. Target: agent-team.
