# game-saves: notes

Facts seen on one project, kept for whoever hits the same thing. They haven't recurred enough to be rules, so check them against your versions. Moved from `docs/CANDIDATES.md` on 2026-11-07 (D21).

- **2026-10-05, action-rpg - A settings field that grows from a bool to a choice: read the old field, keep writing it.** `"Handheld": true|false` became `"Graphics": "Handheld"|"Full"|"High"`. The new reader takes the old field only when the new one is absent; the writer still emits the old bool so an older build reading a new file keeps its choice; the choice is saved by name, and an unknown name (a newer build's) reads as the default instead of failing the whole file. Test with a real file the old build wrote, kept as a never-edited fixture. Target: game-saves.
- **2026-10-05, action-rpg - The negative control for a save upgrade step is the same data loaded as the new version.** A step that refunds skill points was tested by writing a current save, rewriting it as the old format (version down, new fields removed) and loading it: points back, one notice. The control loads the untouched current-format JSON, which keeps the points, so the refund is the step's doing. The step's notices travel out of the deserializer (a list argument), not into the save. Target: game-saves.

## Restoring

- In an action RPG, a duplicate check against the constructor's default ability bar emptied saved ability slots; the
  whole-state round-trip test caught it.
