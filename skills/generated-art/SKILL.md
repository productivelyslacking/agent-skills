---
name: generated-art
description: Making images with a model: model choice, prompts, references, LoRA, character consistency, matting, judging output, provenance, rights, AI disclosure. Use when prompting or training an image model or checking images before the owner sees them. Also load art-direction.
---

# Generated art

Assumes **ground-truth**; load **art-direction** and **game-assets** too. Thesis: **name the exact model, treat its
output as evidence that something was drawn, and let someone who didn't prompt it check it**, so no self-approved
recipe from another model reaches the owner or a store untraceable.

**How far to trust this.** Unused in real work: written from a research review (D24); revise after the next run on real
models. No image was generated for it, so nothing shows how any model looks. Not legal advice.

**Reading a rule:** claim, reason, kind, sources. `[C44]` is in `EVIDENCE-GENERATION.md`, `[#44]` in
`../art-direction/EVIDENCE-DIRECTION.md`, `T13` (an untested test) in `NOTES.md`. Kinds: *measured*, rated only *one
study*, *several* or *disputed*; *vendor* (a maker on its own product, never independently shown); *practitioner*;
*agency*; *secondary*; *inference*, the research author's or "(editor)"; *owner*; *binding* (set in D24, not a
finding). "Read 2026-11-06" dates a reading, not a test; "extract" means via a summarising fetch, so check before
quoting; "checked" means the independent review opened the source. Read the entry's limits before a hard decision; add
no sources from memory.

**Model facts decay,** so each names its model and date. They, the numbers behind these rules, recipes, LoRA settings,
licence traps, tool rules and the To-test list are in `NOTES.md`.

## Before the first prompt

- **Start from a dated live query of current models, not memory:** rank says nothing of permission, and a top
  download can be research-only. Inference (editor), from vendor terms; commands in `NOTES.md` [C72].
- **Name the exact model, variant and pipeline in every rule, prompt and record:** variants differ on guidance and
  negatives, and "guidance" isn't one setting. Vendor, extract, read 2026-11-06 [C5, C6, C11].
- **Re-check a recipe against the model's current card before use, then re-date it;** most were read through a
  summariser, none shows a test. Inference (editor) [C1, C7].
- **Read the base licence through every link (LoRA, VAE, adapter, reference):** a permissive tag can sit on a LoRA of a
  non-commercial base. Vendor terms, the reading is inference, read 2026-11-06 [C18, C33, C72].
- **Pin model and revision on day one;** a style shift can force replacing old art. Practitioner, its opener probably a
  vendor, extract; the rule is inference [C85].

## Production order

- **While testing, use the cheapest images that answer the question; train no models, make no final layered assets and
  finish no motion before story and look are settled,** or it's wasted. Owner's rule, the producer's
  wording; when it's settled: **production-stages** [D24].

## Prompting

- **Write in the form the model was trained on** (see `NOTES.md`); quality tags suit only
  tag-trained models, and nothing independent shows they work. Vendor, no test shown, read 2026-11-06 [C1, C7, C8].
- **Find out by test whether a negative prompt is read:** same seed with and without, byte-compared (T2); vendor
  docs and a practitioner guide conflict. Read 2026-11-06 [C2, C4, C7].
- **Describe the wanted state; where negatives work, still check for the excluded thing:** vendors advise positive
  wording (vendor); removal is far from complete (measured, one study, extract, checked). Read 2026-11-06 [C3, C10,
  C12].
- **Know your pipeline's token budget before calling a prompt long;** they cut at different lengths, and "longer is
  better" has no test. Vendor docs, read 2026-11-06; the conclusion is inference [C9].
- **Treat a seed as reproducibility only; record its device and hash the output:** PyTorch doesn't guarantee a match,
  and "same seed keeps the character" is unmeasured. Seedless, the output file is the source of truth. Vendor
  docs, read 2026-11-06 [C13, T3, T4].

## Consistency

- **Approve one neutral-lit master per character and edit from it, never chaining edits;** identity drift is reported,
  without a rate (vendor, practitioner). Inference, untested [C20, C60, T20].
- **Use an identity score to rank, not pass, on one-character cut-outs in neutral light; set thresholds from your own
  data with planted impostors (T6).** Photo-trained face embeddings read palette change as identity drift (measured, one
  preprint, authors' own metric, extract); anime scores are makers' own tests (vendor, read 2026-11-06); lighting alone
  may cross a threshold (inference, T7) [C22, C23, C24, C25].
- **Check named props, costume and palette separately:** a high consistency score passed a sprite without its gun.
  Measured, one study, SD 1.5 era, extract, read 2026-11-06 [C21].
- **Before training a LoRA, read its section in `NOTES.md`;** caption all but what it teaches; record every training
  image's source. Vendor and practitioner, read 2026-11-06 [C14, C16, C18].

## Layers and matting

- **Choose a matte tool by testing on your own art, generated with margin on a background unlike the hair:** published
  scores are vendor figures on photos, seen second-hand; none tested illustration or coloured rim light. One
  practitioner's failures shape the method, which is inference [C27, C28, C29, T8].
- **For variants, composite the masked result over the original; prove pixels outside the mask unchanged.**
  Inference from vendor docs, untested; **no source covers mouth or blink frames** [C35, C37, T9].

## What automatic checks can and can't do

Before an image reaches the owner, run what can fail; output flags and a ranking, never a quality score (inference
[C48]). Prove each check with a planted fault, and report what wasn't checked. **Nothing here can check taste, story
fit or the owner's look.** Versions and numbers: `NOTES.md`, "Check cards".

| Check | What the numbers say | Use |
|---|---|---|
| Near-black or NaN, size, alpha fringe, duplicate hash, palette hue, OCR on blank areas | Not measured; inference from one project's failures [C48] | Run all |
| Aesthetic, CLIP and generic quality scores | Barely predict preference; what they favour is disputed; weak on hands. Measured, one study, SD-era, extract, checked, read 2026-11-06 [C38, C39, C40, C41, C42] | Don't filter on these |
| Vision models on artifacts | "Who scores", below [C44] | Measure with T13 |
| Identity, era, skin-tone and hand classifiers | Vendor's own tests, not on generated art, read 2026-11-06 [C24, C26, C47, C61] | Rank and flag only |
| Adult appearance, sexual content | Below | **Never a gate** |

Budget review for distortions: by the study's own detector, most models distorted more images than not.
Measured, one study, photoreal-leaning, extract, checked [C43].

## Who scores an image

- **The agent that prompted an image doesn't score it; qa or a fresh session does, given the image and a defect list,
  not the prompt:** judges favour their own text (several papers) and pass more of their own rubric failures (by over
  half, in one). Measured, extract, checked in part. Applying this to an agent that prompted
  another model's image is inference, on two counts; T13 compares both settings [C46].
- **Plant known faults (six fingers, wrong costume, mirrored insignia, swapped eye colour, garbled sign) and report the
  reviewer's hit and false-alarm rates beside every verdict,** which bound any rating. Inference,
  untested [C25, T13].
- **Vision-model figures come from photoreal tests only; no anime or cel test was found.** A cautious model's clean
  verdict may miss half or more, a sensitive one's defect report means little (humans score near 100%), and a zero
  false-claim rate on photos doesn't carry to generated images. Measured, one study, multiple choice, single turn,
  **photoreal only**, extract, checked, read 2026-11-06; unknown on your art until T13; papers disagree [C44, C45].

## Adult appearance and sexualised drift

- **A person who looks young, paired with any sexual or suggestive content, is excluded outright:** no threshold, no
  retouching. Binding, not a research finding [D24].
- **No automatic check is ever a gate for adult appearance or sexualised drift, whatever the numbers,** which are
  poor anyway. The teen classifier passes many teen-labelled images, with undefined labels (vendor's own test, checked);
  sexual-content detectors often class art safe (measured, one study, mostly SD, no anime, extract, checked; NudeNet's
  false negatives not opened); the rating classifier often reads `sensitive` as `general` (vendor, checked), where
  drift would happen (inference). **The research's searches found no
  measure of adults drawn younger and no benchmark for gradual drift.** Read 2026-11-06 [C58, C62, C63, C64, C65, C67].
- **Instead, a human or an independent look at every image that could break the rule; discard doubtful images.** Drift
  needs no prompt, so every image with a person is in scope (editor). Independent: it didn't prompt the image;
  its error rate on stylised art is unknown. A model's look can only discard or send to a person; finding nothing
  clears nothing. Discard rather than edit; never generate someone young and then fix them. Inference,
  untested [C60, C65, C67].
- **Design adults clearly, with a person's sign-off per character before any scene.** Photoreal models follow a stated
  age closely but may skew young (measured, one study, photo-trained estimators, extract, checked, read 2026-11-06):
  useful, not sufficient; unmeasured on anime. Don't run photo age estimators on stylised art. Inference
  [C57, C60, #50].
- **Watch drift per character, as a trend, and review the whole cast's sheets at intervals:** count clothing and framing
  tags against the character's master (tagger F1 is its maker's own, vendor); a cast average hides one character.
  Inference, untested; gaps by group are measured on SD 2.1, one study [C55, C66, T12].
- **Never build a test combining young-looking people with sexual or suggestive content,** as control or planted
  fault; use a non-sexual control between adults and report sensitivity as unknown. Inference, from the
  research's safety note [T12].

## Bias

- **Assign heritage, gender, skin tone and age per character in writing, and measure each model you adopt:** skews
  differ by model, even in sign. Measured (one study, one preprint), photoreal, extract, checked, read 2026-11-06
  [C51, C52].
- **Don't generate a character from words per expression; edit from the approved face:** an emotion word swings age
  and race. Measured, one preprint, not character-locked, extract, checked, read 2026-11-06; the remedy is inference
  [C54, T9].
- **Test per model whether descriptors hold, starting with the character it's least likely to give; if one doesn't,
  edit from the approved master or change model, never the character** (inference) [C54]. Counter-stereotype prompts
  failed on 2022-era models (measured, one study, abstract); anime output showed stronger imbalance (measured, a
  poster, read 2026-11-06) [C56, C59, T11].

## Provenance, rights and disclosure

- **Write the provenance record at generation time, in a sidecar keyed by asset id** (the manifest says where a file is
  and whether it's a placeholder), saying how it was made: prompt, references and licences, seed, device,
  output hash, every model and LoRA with revision and strength, guidance by name, every human edit, who selected it
  from how many, disclosure class. Inference, not a legal standard; embedded data may not survive matting [C74, T18].
- **Tell the owner plainly that a purely generated image likely has no protection on its own;** record what can change
  that: choosing and arranging many into a work, or perceptible human edits (not re-rolls, picks or minor edits). US
  Copyright Office, an agency position; a pending case may change it, so check. Read 2026-11-06 [C68, C69, C70].
- **Describe traits; don't name artists, shows or studios:** style generally isn't protected, so it's a risk choice.
  Agency, pre-publication [C71].
- **Count every shipped generated image for disclosure,** store-page marketing and shipped placeholders included (the
  latter is inference); awards were withdrawn over shipped placeholders. Secondary and news [C73,
  C78].
- **Re-check each store, award and law at release; see a lawyer before an EU release.** Secondary [C76, C77].
- **Keep every image swappable (game-assets):** shipped games have withdrawn generated art.
  Secondary, extract [C79].

## Not established

Write as unknown every gap marked above, and: how any model looks on your style; rim-light edges and lighting match
[C37]; LoRA dataset size [C15]; suits against generators (not searched). `EVIDENCE-GENERATION.md` ends with
disagreements and unsupported claims.
