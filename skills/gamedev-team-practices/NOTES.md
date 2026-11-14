# gamedev-team-practices: notes

Read on demand. Holds the evidence behind `SKILL.md`'s rules: which ones were tested in our own work, and where.

## Repository

- Committing `.import` and `.uid` and ignoring `.godot/` was tested on an action RPG.

## Branches and builds

- The in-game build stamp with version, commit and an uncommitted-changes flag was tested on one of our game
  projects.

## Definition of done

- **One behaviour per control** was admitted on 2026-11-14 as an experiment, on the owner's say-so, from a web app
  where two screens' search boxes behaved differently (one picked the first result on Enter, the other didn't; owner,
  2026-10-16). Should improve: no review finds two screens' copies of a control disagreeing. Might regress: a screen
  forced onto a shared component that fits it badly. Revisit when a second project applies it, or a review disputes
  a difference it flagged.
