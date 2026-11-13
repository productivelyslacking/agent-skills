---
name: game-saves
description: Game save files: versioned formats, upgrades, slots, autosave, never losing a player's save. Use when changing what's saved, adding a save field or slot, or when a load fails or loses data.
---

# Game saves

Assumes **ground-truth**; for cutover discipline see **migrations**: a player's saves are data migrated on machines
you'll never see. The worst outcome isn't a crash but a lost character, and the paths that lose one are the ones nobody
runs: an old format, a half-written file, a newer build's save. Incidents and traps seen once are in `NOTES.md` beside
this file; read it when changing what a save or settings file holds.

## Format

- **Version every file and load through an upgrade chain** (v1→v2→…→current), one small tested step per change; never
  branch the loader on "looks like an old file".
- **Keep a never-edited fixture per version, loaded through the chain by a test:** editing one to pass hides a broken
  upgrade.
- **Round-trip a lived-in character** (save, load, save, compare the texts exactly): it catches restore bugs nobody
  thinks to test.
- **Validate on load and refuse clearly:** unknown ids, impossible values and dangling references are errors with a
  message, not silent defaults; any decoding exception means "malformed".
- **Use JSON while the format is young:** debuggable, diffable, hand-fixable in an emergency. Revisit
  only if size or tampering actually matters.

## Never lose a save

- **Write atomically:** temp file, flush, rename over the old one, keep the previous as `.bak`.
- **Set a damaged file aside, never delete it,** and load the `.bak` with a notice to the player.
- **Never overwrite a save from a newer build:** refuse to save that session and say why; it happens the first time
  someone switches between release and dev builds.
- **"Delete character" sets the file aside too:** players delete by accident.

## Restoring

- **Restore into a cleared object:** constructor defaults (a starting bar or item) left in place make checks corrupt the
  load.
- **Recompute derived values, never save them** (gear stats, level requirements, set bonuses): a saved copy drifts after
  a balance patch.

## What is saved, and when

- **Write down what is deliberately not saved, and why** (position, monsters, HP, cooldowns, an open run), or someone
  "fixes" it.
- **Save as it happens if progress matters:** once a second, fingerprint the saveable state and write only on change,
  plus an immediate save at big moments (level-up, boss, quest).
- **Give shared data (a stash) its own file,** with its own version, chain and never-lose rules.
- **Write once more on "return to title" or "quit",** even if autosave should have covered it.
