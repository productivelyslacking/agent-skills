---
name: gamedev-team-practices
description: Readying a game project for collaborators: repo for binary assets, branching, builds, bug and playtest process, milestones, definition of done. Use when onboarding people, setting up a team repo or CI, or deciding whether a feature is done.
---

# Game-dev team practices

Assumes **ground-truth**. **Unlike the other game skills, these are industry conventions, not our own lessons.** Each
is a default with a reason: adopt it deliberately, and record in the decisions doc which you took and declined. A rule
tested in our own work says so; `NOTES.md` beside this file says where.

## Repository

- **Set up Git LFS in `.gitattributes` before the first binary is committed:** moving later rewrites history.
- **Lock binaries (LFS locking), and give each scene one owner at a time or split it into instanced scenes:** Godot
  `.tscn`/`.tres` are text, but merged scene edits rarely work.
- **Commit engine metadata, ignore its caches:** for Godot, `.import` and `.uid` in, `.godot/` out (tested;
  **godot-dotnet**).
- **One-command setup and build in the README,** tested by someone else: a newcomer's first hour finds every
  undocumented step.
- **Pin tool versions and their source** (engine, SDK, export templates): "works on my editor version" is the commonest
  new-dev failure.

## Branches and builds

- **`main` always builds and runs;** work goes on short-lived branches merged through review.
- **CI on every branch** (build, headless tests, a target-platform export): a build one machine makes is a release risk.
- **Stamp every build with version and commit, readable in-game,** flagging uncommitted changes; bug reports and
  playtest notes cite it (tested).
- **Testers play release, developers reproduce on debug:** performance and timing differ.

## Bugs

- **A report has** the build stamp, repro steps, expected vs actual, frequency, and a save or screenshot: many RPG bugs
  need the save to reproduce.
- **Keep severity (how bad) apart from priority (when fixed):** an unused menu's crash can wait behind a progression
  blocker.
- **Triage regularly; close or defer explicitly:** an unpruned list stops being read.
- **Give a fixed bug a test** (sim test, fixture save): it'll come back.

## Playtests

- **Schedule them regularly, with fresh players where possible:** the team stops seeing problems.
- **Watch, don't explain:** needing to explain is the finding. Note where people got lost, died or stopped having fun.
- **Collect observations, then decide fixes:** one tester's suggestion isn't a decision.
- **Test on the target hardware** (for us, the Steam Deck through Proton), not only the dev PC.

## Milestones

| Milestone | Means |
|---|---|
| **Prototype** | Is the core loop fun? Throwaway code allowed |
| **Vertical slice** | One small part at shipping quality, every system touched. Disputed as a default: **production-stages** builds one only for a buyer or a named pipeline risk (D25) |
| **Alpha** | Feature complete; content may be placeholder |
| **Beta** | Content complete; fixing and polishing only |
| **Release candidate / gold** | Shippable; critical fixes only |

Write each milestone's exit criteria: an undefined "Alpha" becomes a date, not a state.

## Definition of done

Done means it works in a release build on the target hardware; works with a controller (if
controller-first) and the keyboard; saves and loads, with a format upgrade if it changed the format (**game-saves**);
has tests for its rules; has its decision recorded and status updated in the design doc; and leaves no untracked
placeholder assets (**game-assets**).

## Quality budgets and readiness

- **Set a frame-time budget and profile on the target hardware before optimizing.**
- **Be localization-ready early** (strings in data, not concatenated in code; UI that tolerates text 30–40% longer than
  English): both are expensive to retrofit.
- **Accessibility basics:** remappable controls; never colour alone for meaning (rarity has colour *and* a word);
  readable text on a handheld; subtitles for speech.
- **Logs and crash reports in a known place,** named in the bug-report template.

## Bringing in contributors

- **Settle IP ownership before anyone contributes:** a contributor or work-for-hire agreement assigning or licensing it
  to the project, or the work can't safely ship. Use a lawyer's template; this isn't legal advice.
- **Track every asset's licence** (**game-assets**): contributors bring assets from their own libraries.
- **Onboarding doc:** setup, where design, decisions and lessons live, branch and review rules, bug reporting, the
  definition of done.
- **Give AI agents and new people one entry point:** a `CLAUDE.md` or `AGENTS.md` pointing at the design, decisions and
  lessons docs.
