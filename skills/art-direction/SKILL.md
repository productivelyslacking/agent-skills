---
name: art-direction
description: Deciding what an image should show and whether it works: style guides, composition, palette, lighting, cast and costume, motion and loops, flash safety, sequence review. Use when writing an art brief or reviewing a panel, sprite, concept or contact sheet. Generated images: also generated-art.
---

# Art direction

Assumes **ground-truth**. Thesis: **ask for what can be checked, judge images in sequence at real size, and leave look
and feel to the owner**, rather than approve fluent images one at a time on folklore or an agent's taste.

**How far to trust this.** Unused in real work: written from a research review (D24); revise after the next run on real
models. Mostly craft opinion, rated for standing and agreement, not proof it works; almost nothing was tested on panels.
`NOTES.md` holds the examples and numbers cut from here.

**Reading a rule:** claim, reason, kind, sources. `[#3]` is in `EVIDENCE-DIRECTION.md`, `[C44]` in
`../generated-art/EVIDENCE-GENERATION.md`. Kinds: *measured*, rated only *one study*, *several* or *disputed*;
*practitioner*; *critic*; *demonstrated* (a work does it; not shown to cause success); *vendor*; *normative* (a
standard's text); *inference*, the research author's or "(editor)"; *owner*; *binding* (set in D24, not a finding).
"Read 2026-11-06" dates a reading, not a test. Read the entry's limits before a hard decision; add no sources from
memory.

## Who judges

- **The owner judges look and feel; an agent's image shows something is drawn, not that it's good.** Nothing measures
  fit to a story, and scorers barely predict general preference. Owner's rule; the scorers are measured,
  one study, SD-era images [D24, C38].
- **Trust the owner's eye on what reads and what's seen first; its reach into craft is untested, and it doesn't limit
  what the owner may decide.** Trained and untrained viewers look at much the same places, though page order needs
  experience and gaze isn't judgement. Measured, disputed, a 1935 study cited second-hand; the use is inference [#66,
  #5].
- **Before an image reaches the owner, run what can fail (silhouette, greyscale, locks side by side, swap test, flash
  report) and say what can't be checked (good, moving, right for this story).** Inference (editor) [#8, #20, #29,
  #59, #65]. **Remove an image only for a failed check or the exclusion, never taste, and say how many and why.**
  Inference (editor) [C25].

## Style guide

- **Write checks, not adjectives** (camera angle, canvas baseline, light direction from the artist's view, shadow and
  highlight hue, outline rule, smallest detail), **and a tie-breaker** ("reads at display size beats rendering").
  Practitioner, via a vendor blog on art bibles; the only proof is that they shipped; the example is inference [#28].
- **Lock a short list and check it across images** (reserved colours, silhouette envelope, baseline, light, outline,
  frame count): drift is invisible one image at a time. Vendor, selling this very constraint layer, no data [#29].
- **Give a few construction constants and list what must vary:** unnoticed constants can bind a style (practitioner,
  reverse-engineering one game) but pull faces to one template, so name jaw, nose bridge, eye spacing and age marks as
  variable (inference, no source) [#27, #45].
- **Show rejected examples with reasons:** a cheap habit, not a proven one. Inference, weak [#30].
- **Ask for materials and their results, and choose one chain** (film print, broadcast and home tape differ; tutorials
  mix them; the split is inference). Critic and hobbyist only: **no cel-era technical account was found** [#32,
  #33, #34].
- **Never name a living artist as a style; use several references from different media, each named for one borrowed
  property, plus the process.** No artist's name in a prompt; a note for people may name a work for the property. Two
  productions did this, neither saying why. Binding on naming; demonstrated on references [D24, #42, #35].
- **Ask for the local cause of everything (who pays for this sign?): a genre default identifies nothing.** Name the
  choices you want from a genre, not the genre. Critics call genre defaults worn,
  unmeasured; **no practitioner method was found**; one film took its palette from a real place (demonstrated).
  Critic; the method is inference [#26, #37, #39, #41, #22].
- **Use a real script or culture only if someone can read and check it;** as wallpaper it reads as an outsider's view (a
  critique not all share). Critic; the rule is inference [#40].

## Composition

- **Ask what people land on, not where a line leads:** viewers agree on where, not order; clear axes may set direction.
  Measured, disputed [#1, #2]. **Count the faces,** each claims attention: dim, turn or crop those who aren't the point
  (inference). Practitioner, an informal eye-tracking demo, one painting [#3].
- **Don't spend a note on thirds or golden sections:** an informal demo found the golden section alone draws no
  attention; nothing tested thirds. Practitioner; dropping the note for thirds is inference [#3].
- **Rank what must be read before asking for the image, each level on its own channel** (colour, silhouette, detail);
  mind where the highest contrast goes (the frame's-interest rule). Practitioner; panels are inference [#9].
- **With several panels on screen, borders lead and text position matters; a comics reader isn't a novice test.**
  Measured, one study each, one abstract only, one on blank panels [#4, #5].

## Colour and light

- **Lay out the story's colour as a strip before any final image,** a swatch and emotion per scene, so monotony shows.
  Practitioner through a review, demonstrated in feature animation; the check is inference [#19].
- **Light plainly, then bring the palette in from sources in the scene;** a single wash soon bores. Practitioner, one
  unattributed production document for a real-time game [#21].
- **State a character's base skin colour apart from the light,** or skin takes the light's colour (inference, no
  technical source); saturated coloured light on dark skin is praised, and needn't lighten it (demonstrated, one film)
  [#46, #22].
- **Run greyscale as a test that can fail, not a law;** "value before hue" has process mentions and no test. Inference
  [#20].

## First-person staging

Few models to copy; monotony is the main risk. Inference [#12].

- **Ration eye contact; a frontal centred stare is a fault to justify,** reading as monotonous or creepy. Critic, one
  work each, voiced games a counter-case; rationing is inference [#12, #14]. Each look at the viewer is an invitation or
  isn't, so default to the conversation. Critic, one character; the default is inference [#48].
- **Put variety in the staging, since panels lack a game's free movement:** a task in hand, a third person, something
  changing hands. Games use movement (critic); the fix is inference, untested [#14].
- **Spend first-person panels where being there matters: threat, a lie, an offer.** Developers named threat,
  pre-release. Practitioner; the rest is inference [#15].
- **Show the viewer's hands when they act, with skin, sleeve and age constant;** repeated hand business wears thin. **No
  craft source covers viewer hands in stills.** Critic, demonstrated; the rule is inference [#11, #18].
- **Say who each person looks at, and why,** so they play to a person, not the lens. Demonstrated; use in a brief is
  inference [#11].
- **Decide once, in the guide, whether the viewer is ever shown.** Demonstrated, not shown to cause anything
  [#11, #13].
- **Break long stretches with planned exceptions (a cutaway, a memory, a recording):** even a first-person comic isn't
  mostly drawn from the eye, though narration differs from framing. Critic, abstract, one work; the plan is inference
  [#16].
- **Decide what a cut means; keep a speaker's screen side steady.** **The 180-degree rule and eyelines have no source
  here.** Inference only; check against film editing texts first [#10].

## Cast and costume

- **Test each character filled black, then at its real crop and size,** where silhouette at bust crop means hair, hat,
  collar, shoulders (inference). Practitioner, demonstrated, a shooter at distance; no measured result [#8, #43]. **Make
  identifying marks big:** a small one failed playtest. Practitioner, reported second-hand [#43].
- **Brief a person, not an ethnicity plus a costume: heritage and skin colour as facts, then job, age, today's clothes,
  haircut.** A generator collapsed groups into a caricature bundle (measured, one study, abstract, read 2026-11-06), so
  check a group shot for sameness within a group. The brief is inference; **no practitioner source on hair and dress by
  culture** [#44].
- **Put age in the design (lines, jaw, neck, hands) and have a person check it:** **no practitioner source was found**,
  and it's too important for reasoning alone. Inference [#50].
- **Give each person a body from a life, in three layers, and say which may change:** born with (height, frame,
  features); life so far (muscle, weight, posture, hands, skin, grooming, from job and care); chosen per shot (makeup,
  hair, outfit, how dressed up or tired). Drift in the first two, or an unrequested third-layer change, is a fault. Most
  people sit near average and nobody has to stand out; a large or small feature alone isn't grounds to discard
  (sexualised framing and reading young are separate faults, screened whatever the build). A job shapes a body, not the
  person. Build doesn't follow gender, race, temperament or plot role; scene choices are a person's habit, not a gender
  rule. Owner's direction, one project; untested.
- **A person who looks young, with any sexual or suggestive content, is excluded outright, however made.** Discard
  doubtful images. Automatic checks can't gate this: numbers and review rule are in **generated-art**. Binding, not a
  research finding [D24, C62].
- **Ask whether the frame's interest in a body matches the scene:** context beats skin count; compare rendering detail
  on body against face and hands. Practitioner, one webcomic artist; critics dispute who decides [#47, #48]. Run the
  swap test (same pose and framing on a man of the same role and age: ridiculous now?) and count across the sheet who's
  undressed and where the frame lingers. Practitioner and fan practice, unmeasured [#47, #49].

## Motion and flash

- **Advance on the viewer's input; loops run while waiting; nothing blocks text or a click.** Comics voices blame lost
  pace for the form's failure, without reader data; cutscene-trained audiences may differ; keeping control didn't save
  one product. Practitioner, critic; the rule is inference [#52, #53, #54].
- **Put surprises on the click, the digital page turn.** Critic, abstract; inference [#55].
- **A hold is respectable and motion isn't owed, but holds rest on strong stills;** long pans need something to find
  (inference). Critic, demonstrated [#57, #58].
- **Check loop seams and layer sync; overlap unequal lengths.** A taxonomy of loops, not a test. Practitioner; the
  checks are inference [#56].
- **State the flash limit in the brief, run a tool, never judge flashing by eye.** WCAG 2.3.1: at most three flashes a
  second unless under the general and red thresholds; the red test catches deep pinks and magenta-to-red changes but not
  magenta alone (editor's arithmetic; thresholds in `NOTES.md`). Use the normative area limit (25% of a 10-degree field), not the conflicting informative figure. An off switch isn't a fix. Choose PEAT or Harding (W3C
  lists both; neither run here) by **dependency-policy** before the first flashing asset. Normative, read 2026-11-06
  [#59].
- **Name which test applies: area rules differ.** WCAG's normative limit is 25% of a 10-degree field, about 2.8% of a
  fullscreen frame on the conservative reading (editor's inference); don't use the informative page's larger figure.
  Harding: 25% of the frame, a duration rule, stripe tests. Vendor docs, read 2026-11-06; console requirements weren't
  found [#59, #60].

## Reviewing a sequence

- **Judge in order as well as alone, on a contact sheet at display size:** ordered strips were understood faster, and
  context moved gaze. Measured, one study, abstract, wordless strips [#6].
- **Swap a panel with the one before;** if nothing breaks, ask what it's for. Inference [#65].
- **Watch for people dropping out and furnished rooms replacing events:** describe-and-regenerate loops drift to a few
  pleasant motifs. Measured, one study, read second-hand; a directed project isn't that loop [#62].
- **List what the story tracks; a fresh reviewer checks each across every frame,** since frame-by-frame checks miss a
  plot prop or count (crossed-off days) that doesn't match its moment. Practitioner, two projects [#67].
- **Do what the owner asks, and record the note as reported effect plus suspected cause;** if you suspect another
  cause, show your alternative beside it. The owner decides; the exclusion isn't a look decision and stands.
  Practitioner, no outcome evidence [#61, D24].

## Questions the owner can answer

At real size, a few seconds before any text. All inference, untested [#1, #3, #6, #52, #61, #66].

1. Glance two seconds, then away: what did you see first? Does the scene need that?
2. Who's speaking, and who's in charge, without the text?
3. What is this person feeling? Would you bet on it?
4. Where and when are we? Is this place like any other in the story?
5. Seen it on a hundred posters? What could only belong to this story?
6. Swap it with the panel before: does anything break?
7. Is this person's look at you what the moment calls for?
8. Is the frame more interested in a body than the action? Silly on a man of the same role and age?
9. With a hand over the clothes, are these different people?
10. Side by side, the same person as last time?
11. Tired after ten panels? All a head in the middle?
12. What moved? Did it pull you from reading, or tell you anything?
13. Did you ever wait for the screen, or feel hurried?
14. What are you sure of, and what's a guess? An effect ("she seems meek") helps as much as a fix.

Not for the owner: flash compliance (a tool's report), hand anatomy beyond "something's off", lock numbers.

## Not established

Write as unknown: the gaps marked above (shot grammar [#10], culture [#44, #45], skin under coloured light [#46]); how
much movement is too much and how long to hold [#56]; costume by setting [#51]; period comics materials [#36]; getting
past the generated look [#64]; telling clean from meaningful [#65]; saturation fatigue (forum reports only; check in
play) [#25]. `EVIDENCE-DIRECTION.md` ends with where practitioners disagree and what's weakly supported.
