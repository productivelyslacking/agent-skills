---
name: game-assets
description: Bringing art, audio and fonts into a game: placeholder packs, licences (CC0, CC BY), credits, replaceable setup. Use when adding, replacing or sourcing an asset, writing credits, or when an asset is wrong in a build.
---

# Game assets

Assumes **ground-truth** and **dependency-policy**: an asset is a dependency with a licence. Most assets start as
placeholders, and the cost comes later: nobody knows which are still stand-ins, a replacement lands under the wrong
name, or a CC BY credit is missing from the shipped game. Incidents and measurements behind these rules are in
`NOTES.md`; read it before generating, importing or judging an asset.

## Set up for replacement from the first asset

- **Code asks for assets by game id, never by path** (`ability:slash`, `item:helm`): one manifest maps id to
  file, so replacing art is a file swap.
- **Name files after the game id, not their source** (`icons/abilities/slash.svg`), so the path survives
  replacement.
- **Mark placeholders in the manifest** with a `source` field naming pack and file, so "what's still placeholder?"
  is a search and the fetch script knows which files it owns.
- **Fetch placeholders with a committed script** pinned by URL and SHA-256, copying only manifest files; it refuses
  on a hash mismatch and never overwrites an entry without `source` (a replacement).
- **Test coverage both ways:** every id the game draws has an entry, every entry's file exists, and every file in
  the art folders is named by an entry, so new content without art and misnamed replacements both fail.
- **Write a one-page doc:** where art lives, how to replace or add one, the licence duties.

## Licences

| Licence | In practice |
|---|---|
| **CC0** (Kenney, KayKit, Quaternius, Poly Haven, ambientCG) | Public domain: commercial use, modify, no credit required |
| **CC BY** (game-icons.net, 3.0) | **Credit each author where players see it** (credits screen or store page); a repo CREDITS file alone isn't enough once it ships |
| **Per-file** (OpenGameArt, Poly Pizza, itch.io packs) | Check every file; mixed packs are where non-commercial or share-alike slips in |
| **"Free" but not open** (Mixamo, engine stores) | Usable in a game, often not redistributable as raw files, which a public repo is; read the terms before committing |

- **Generate CREDITS from the manifest** with author names and links, so it can't drift and a replaced CC BY
  asset's credit goes with it.
- **Verify the licence at download, from the source,** and keep its text beside the files: packs change terms,
  and a remembered licence is a guess.
- **Before release,** list every asset still carrying a `source` and confirm each CC BY credit is visible in the
  build or on the store page.

## Engine specifics

- **Check the export for non-resource files:** Godot packs only resources, so a manifest JSON read through
  `res://` vanishes from the export; embed or include it (see **godot-dotnet**).
- **Commit the engine's import metadata** (Godot's `.import`) with each asset.
- **Use white-on-transparent icons as placeholders** and tint them in the engine; strip game-icons.net's black
  square in the fetch script.
- **Paint a missing-looking piece a debug colour** to tell "not drawn" from "drawn but hidden" before resizing it.
- **Pick button glyphs for the target device, not its reported pad name,** which can mislead (Steam Input reports
  a Steam Deck as an Xbox pad).

## Choosing placeholder packs

- **Prefer one consistent pack per kind** over the best icon from five sources.
- **For swappable gear, choose character models that share a skeleton** (KayKit's adventurers do), so one item fits
  every body.
- **Make placeholders look like placeholders** where it matters, so testers judge gameplay, not art that's going.

For images, also load **art-direction** (what to ask for, how to judge it) and **generated-art** (making them with
a model).
