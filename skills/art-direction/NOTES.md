# art-direction: notes

Read on demand. Holds the examples, numbers and dates behind `SKILL.md`'s rules, cut from it on 2026-11-13; the sources
themselves, with their limits, are in `EVIDENCE-DIRECTION.md` under the same tags.

## How far to trust this

- Written on 2026-11-06 from a research review (D24 in the library's `docs/DECISIONS.md`); its first real test is the
  next run on real models.

## Style guide

- The art-bible source [#28] was a vendor blog covering four art bibles.
- Construction constants [#27] came from one practitioner reverse-engineering one game.
- Rejected-example advice [#30] is near-identical pages that may copy each other, hence "weak".
- Genre's local cause [#26, #37, #39, #41, #22]: examples were who pays for a sign, what it sells, what the weather has
  damaged; a genre choice worth naming is a key-to-fill ratio.
- Script as wallpaper [#40]: the critique was of Asian signage used as a Western view of the place.

## Composition

- [#1, #2]: 65 viewers of three landscapes, against 32 viewers of fourteen paintings of one subject.
- [#3]: Gurney's informal demo, one painting.
- [#9]: Valve assigned team to colour, class to silhouette, detail to the chest, in a shooter.

## Colour and light

- [#22]: the praised example was saturated pink and green light on dark skin, in one film.

## First-person staging

- [#12, #14]: constant direct address read as monotonous in a 1947 film; a locked close-up read as creepy in a 2023 work.
- [#11, #18]: a hand on a doorknob wore thin fast in a 1947 review; the same film's actors played to a person, not the
  lens. [#11, #13]: one film showed the viewer in mirrors, another gave a story reason.

## Cast and costume

- [#8, #43]: Valve validated characters in silhouette before shading; a sleeve patch failed playtest as an identifier in
  a shooter at distance.
- [#44]: the caricature-bundle study was on Stable Diffusion, variant not read.

## Motion and flash

Thresholds, from [#59, #60] (normative and vendor text, read 2026-11-06; arithmetic by the editor):

- WCAG 2.3.1: three or fewer flashes a second needs no tool. A red state is R/(R+G+B) of at least 0.8 on linear values;
  a transition to or from it needs a chromaticity change above 0.2. Pure red counts; pinks count only up to about
  #FF0088 (hotpink is 0.63); magenta alone doesn't, magenta to red does.
- Area: WCAG's normative limit is 25% of a 10-degree field, 21,824 CSS px (2.8% of 1024x768). One informative sentence
  on W3C's Understanding page says 87,296 px (11.1%), which conflicts with it: don't use it.

## Reviewing a sequence

- [#67]: a mystery game's phone was rotary in one frame and push-button in another, which read as a planted clue;
  another project's first cut showed nine crossed-off days on night one. Fresh reviewers caught both; frame-by-frame
  checks hadn't.
