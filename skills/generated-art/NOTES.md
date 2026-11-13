# generated-art: notes

Model facts and the To-test list, read on demand, so `SKILL.md` stays general. **These decay: every fact carries its
date, and none has been tried on a real run.** Everything here comes from `EVIDENCE-GENERATION.md` (`[C2]`), or from
`../game-assets/NOTES.md`
where it says so. **Tie-breaker:** the model's current card wins over this file, this file's date says how stale it
may be, and an entry in the evidence file wins over this digest if the two disagree. When you re-check a fact, change
the date here.

## Live query: do this first

No list of "current" models here is current. Run these, save the output with its date, and pick from that; add names
from memory only as extras. Commands run 2026-11-06. They're a list, not a judgement: the rank says nothing about
licence or quality.

```
curl -s 'https://huggingface.co/api/models?pipeline_tag=text-to-image&sort=downloads&limit=25' curl -s 'https://huggingface.co/api/models?pipeline_tag=text-to-image&sort=trendingScore&limit=40' curl -s 'https://huggingface.co/api/models?pipeline_tag=image-segmentation&sort=trendingScore&limit=25' curl -s 'https://huggingface.co/api/models?search=matting&sort=downloads&limit=15'
```

Hosted models may not appear there, so check the vendor's own list as well (inference).

**Snapshot, read 2026-11-06, not evaluated.** By downloads: Qwen-Image-2.1 and its quantised forms, SDXL base 1.0,
Krea-2, FLUX.2 Klein 4B and 9B, Animagine XL 4.0, Z-Image-Turbo, NoobAI-XL 1.1. New and trending, licence tags
unverified: PrunaAI/P-H3-Image, lodestones/chroma-h3, lodestones/Kromoss, speridlabs/iris-3b, 0ppxnhximxr/snapref-v1a
and v2a-pre2, localai0301/Anima-RGBA. Matting: ZhengPeng7/BiRefNet family, briaai/RMBG-2.0,
facebook/sapiens2-matting-1b, nikopueringer/CorridorKey2.0. "Uncensored" LoRAs for MOSS-Image and Qwen-Image 2.1 were
trending too, which is a drift risk [C7]: don't use them (inference).

## Recipes by exact model

**Re-check against the card before use.** All are the maker's own statements unless marked, none shows a test, and
most came through a summarising fetch. "Guidance" means what that pipeline calls it [C11]. T2 is how to find out what
your front end actually does; these describe diffusers or the card, and ComfyUI's behaviour wasn't read [C2].

| Model, variant | Wording | Negative | Guidance, steps | Also | Read | Entry |
|---|---|---|---|---|---|---|
| FLUX.2 Klein 4B, 9B, step-distilled | Flowing prose; detail isn't expanded for you; light source, direction, hardness; a closing `Style: ... Mood: ...` line is a candidate to test; English | No text parameter in diffusers (embeds only, default empty) | Ignored; card example 1.0; 4 steps | Up to 4 references. 9B is non-commercial | 2026-11-06 | C1, C2, C19, C72 |
| FLUX.2 Klein base variants | Prose | Embeds only, default empty | 4.0 default. One practitioner: 3.5 to 5, 20 to 24 steps | LoRA base: 12 GB and 32 GB RAM on 4B. 18 GB fp16 runs out on 12 GB (practitioner) | 2026-11-06 | C2, C4, C14 |
| FLUX.2 pro, max; FLUX 3 Image | Prose; FLUX 3 adds layout boxes and references by position | None; phrase the wanted state | FLUX 3 Image: no `seed`, `guidance` or `prompt_upsampling` field (vendor, opened 2026-11-06). FLUX.2 pro, max: not on the pages read | Don't reuse Klein prompts unchanged on FLUX 3. FLUX 3 Klein has a revenue threshold | 2026-11-06 | C3, C72 |
| Z-Image-Turbo | Prose; card describes a prompt enhancer | Ignored below guidance 1 | 0; 8 effective steps (the card sets `num_inference_steps=9` for 8) | Maker rates variety across seeds low. Docs: fits 16 GB; nothing on 12 GB | 2026-11-06 | C5 |
| Z-Image base | Prose | Works, by maker's account | CFG 3 to 5; 28 to 50 steps | Fine-tunable; varies more than Turbo in composition, face and light. Its card rates diversity High, Turbo's card rates Z-Image Medium: they disagree | 2026-11-06 | C6 |
| Z-Anime base | Sentences, not tag lists | Full effect, by card | CFG 3 to 5, no higher than 9; 28 to 50 steps | euler_ancestral with beta. Author calls it experimental and says it can partly produce adult content, so check for drift from the first batch; training data undescribed | 2026-11-06 | C7 |
| Z-Anime distill-8, distill-4 | Sentences | Limited | CFG 1.0, at most 1.5; 8 or 4 steps | CFG 1 here against Turbo's documented 0 may be two front ends' "off": unverified (T2) | 2026-11-06 | C7 |
| Animagine XL 4.0 | Tags in trained order: subject count, character, series, rating, anything, then quality; score tags stronger than `masterpiece` | Standard list advised, unmeasured | CFG 4 to 7; 25 to 28 steps; Euler a; about 1024 px | Year tags `year 2005` to `year 2025` only, so an earlier period must come from other tags or a LoRA (T5). Weak: hands, text, several characters. Card uses a long-prompt pipeline (`lpw_stable_diffusion_xl`). Leave character and series out for original characters [C8, C71]. Use the `safe` rating unless a person has approved otherwise (inference) | 2026-11-06 | C8 |
| SDXL 1.0 base | Two encoders, `prompt`, `prompt_2`; the standard pipeline's CLIP cuts at 77 tokens (`../game-assets/NOTES.md`); some pipelines handle more, so check yours | One per encoder, plus negative size and crop conditioning | Default 1024 px; below 512 unlikely to work | Base model, not its anime fine-tunes | 2026-11-06 | C9 |
| gemini-nano-banana-2.1, gemini-3.1-flash-image, gemini-3-pro-image | Positive description, materials and purpose, background first, camera terms; generate wanted text, then the image containing it | Positive framing | No setting in the docs read | Refine in turns; feed earlier images back. Up to 14 references total: 4 characters on the first two, 5 characters and 3 style on 3 Pro. SynthID on all. Seed status unknown, so the output file is the source of truth | 2026-11-06 | C10, C19 |
| Qwen-Image-Edit-2511 | Not covered on the card read | One space in the example | Example: `true_cfg_scale` 4.0 with `guidance_scale` 1.0, unexplained; 40 steps | Claims better character consistency, no benchmark. "Show from behind" gave a mirror image on one project (`../game-assets/NOTES.md`) | 2026-11-06 | C11, C19, C20 |

**Klein LoRA guide (vendor, read 2026-11-06) [C14]:** 1,500 to 2,500 steps for style, 1,500 to 3,000 for characters;
LR 8e-5 to 1e-4, lower for style; trigger word; vary poses, angles, lighting. It gives no image count, and no licence
statement for trained LoRAs.

**Things to look for on Klein, not settings to copy (practitioner, no benchmarks, read 2026-11-06) [C4]:** waxy skin
above CFG 1.5 when distilled; mismatched steps give black or static images; crowded scenes lose track of who does
what; photo edits can invent a person.

## LoRA training

Only after the look is settled (`SKILL.md`, "Production order"). All untested here.

- **Caption everything visible except what it's teaching, and have the captions checked for naming the look.** BFL's
  guide for FLUX.2 Klein says so (vendor, read 2026-11-06). A character LoRA whose captions named the style reportedly
  stopped looking like it (practitioner, forum) [C14, C16].
- **Keep style and character LoRAs apart, test at more than one strength, and budget three runs per target.** Authors
  report baked-in style and retraining. Practitioner, SDXL-era forum posts, read 2026-11-06; the numbers are inference
  [C16].
- **Start with a dataset small enough to audit by hand.** Reports run from 8 to 400 images, with no controlled
  comparison. Practitioner, read 2026-11-06; the advice is inference [C15, T15].
- **Train on the checkpoint you'll ship with, and vary outfits in the set.** One poster's Z-Image base LoRA learned
  the outfit over the face, and another's Z-Image-Turbo LoRA failed on other checkpoints. Practitioner, one forum
  thread, read 2026-11-06 [C17].
- **Record where every training image came from.** BFL's API terms bar training other models on its output, as read by
  an earlier survey (not re-read), so that dataset may be a dead end. Anima's licence names LoRAs as derivatives. The
  exclusion in `SKILL.md` also covers reference and training images. Vendor terms, read 2026-11-06 [C18].

## Check cards

Exact versions and fuller numbers behind the table in `SKILL.md`. No row shows a check working on a real project's
art.

| Check, exact model | What the numbers say | Use | Read |
|---|---|---|---|
| LAION aesthetic, CLIP alignment, PickScore, HPS v2, ImageReward | Pairwise preference, 50% is chance: LAION 55.3, 56.8, 72.6, 57.35; CLIP 51.9, 60.8, 62.5, 54.82, on Picsart, Pick-a-Pic, HPD v2, ImageReward; on Picsart PickScore 62.6, HPS v2 59.4, ImageReward 60.48. Measured, one study, authors promoting their own metric, extract [C38] | Don't filter on these. Whether they favour photorealism or unedited fidelity is disputed [C39, C40]. LAION favoured images captioned with women in one audit [C39]: a filter could push towards sexualised images | 2026-11-06 |
| `anime_aesthetic` swinv2pv3_v0_448_ls0.2_x | 40.88% over seven score bands, AUC 0.82. Vendor's own test [C41] | Only if T14 justifies it | 2026-11-06 |
| BRISQUE, NIQE, HyperIQA, MUSIQ, Q-Align, DeQA-Score, HandEval on hands | Correlation with raters 0.006, 0.15, 0.49, 0.52, 0.52, 0.55, 0.67. Measured, one study, 100 test images, realistic hands [C42] | Not a hand check | 2026-11-06 |
| ViT-HD distortion detector on SD 3.5, Flux.1-dev, Recraft v3, Hunyuan | Image-level F1 0.884. The abstract says nearly 50% of images had distortions; its text says only SD 3.5 was above 50% undistorted, by the study's own detector. Measured, one study, photoreal-leaning; expert review agreed about 80% of the time [C43] | Not tested on stylised art | 2026-11-06 |
| Vision models, % flagged on artifact images / % false claim **on real photographs**: Gemini 3.1 Pro, Gemini 3.1 Flash Lite, Gemma-4-31B, Claude 4.6 Opus, GPT-5.4 | 99.37/49.72, 83.37/6.74, 86.32/31.74, 47.58/0.00, 4.63/0.00. On generated images with the defect removed, share rejecting it on every follow-up: 0.00, 0.00, 0.00, 0.84, 20.17, so a 0.00 false-claim figure doesn't carry over. Multiple choice, single turn. Best model right on all four questions for 53.26% of artifact images; humans near 100. Measured, one study, **photoreal only**, extract, Table 1 checked [C44] | No false-alarm rate here describes generated art: T13 | 2026-11-06 |
| CCIP `ccip-caformer_b36-24` | Best F1 0.94 at threshold 0.213, one-character images only. Vendor's own test, not on original characters or generated art. Face embeddings on stylised art: unreliable (measured, one preprint) [C22, C24] | Rank; find what it misses with T6 | 2026-11-06 |
| ViStoryBench consistency, CLIP on Grounding DINO crops for non-realistic characters | Self-consistency against human ratings: Kendall 0.50, Spearman 0.68, Pearson 0.80. Measured, sample size not given; the anime path isn't validated [C23] | A pattern to calibrate | 2026-11-06 |
| `anime_style_ages` caformer_s36_v0 | 71.03% over seven eras; per-class figures are on the card. Vendor's own test [C26] | Shows whether a prompt moved the era; not a judge of the look | 2026-11-06 |
| `anime_ch_skin_color` caformer_s36 | 79.26%; `dark` recall 88.0, precision 86.7; `pale` recall 60.7. Vendor's own test, four bins [C61] | Flag on the cast sheet, not a diversity measure | 2026-11-06 |
| `anime_hand_detection` | F1 0.75 at the tiny size shown. Vendor's own test; finds hands, doesn't judge them [C47] | Crop hands for the review sheet | 2026-11-06 |
| `anime_teen` caformer_s36_v0 | 220 of 1,319 labelled teen or contentious passed as `non_teen` (16.7%); 207 of 1,037 `non_teen` flagged (20.0%); predicted `non_teen` right 79.0%. By label: safe_teen 26.9% passed, contentious 9.8%. imgutils defaults to `mobilenetv3_v0_dist` (74.92%): set `model_name` or these figures don't apply. Labels undefined, dataset card unreachable. Vendor's own test [C62] | **Never a pass**; a flag at most | 2026-11-06 |
| GPT-4V, LLaVA, MultiHeaded, SD_Filter, NSFW_Detector, NudeNet on sexual content | F1 on AI-generated images 0.827, 0.866, 0.815, 0.727, 0.678, 0.596. Measured, one study, mostly SD, no anime, extract. NudeNet false negatives 4.4% to 14.4% on jailbroken images, not opened [C63, C64] | **Never a gate** | 2026-11-06 |
| `anime_dbrating` swinv2pv3_v0_ls0.2 | 84.16%; `explicit` read as `general` or `sensitive` 0.4%; `questionable` 10%; `sensitive` read as `general` about 18%. Vendor's own test on user ratings. `anime_censor_detection` F1 0.80 to 0.83 [C65] | Flag for gross nudity only | 2026-11-06 |
| WD tagger `wd-eva02-large-tagger-v3` | F1 0.4772 at threshold 0.5296. Vendor's own test; its vocabulary can itself be sexualised [C66] | Trend tags per character (T12) | 2026-11-06 |

## Licence traps, read 2026-11-06

Vendor terms as read; not legal advice. Read the licence yourself, and read the base model's through every link [C33,
C72].

- Tag and upstream disagree: NoobAI-XL (tag FAIPL, its card bans commercial use); Qwen-Image 2.1 (research only
  upstream, a repackager tags apache-2.0); Anima-RGBA (tag apache-2.0, LoRA derived from Anima) [C33, C72].
- Non-commercial: FLUX.2 Klein 9B, FLUX.1 dev, Anima. Anima's outputs clause reads differently, and that wasn't
  resolved [C33, C72].
- Revenue thresholds: Krea 2, FLUX 3 Klein [C72].
- Store rules are patchy, and EU Article 50's timing couldn't be verified. Secondary, read 2026-11-06 [C76, C77].
- Tool use only, read the text first: CorridorKey 2.0 (CC BY-NC-SA base plus terms; commercial projects allowed, no
  paid access or inference service) [C32]. VNCCS parts unknown, and which Qwen version it uses wasn't confirmed [C36].
- Bria RMBG-2.0 has its own non-open licence; BEN2's fuller model is API or commercial, base is MIT; IC-Light is
  Apache-2.0 by tag [C28, C29, C34].

## Other tool facts, read 2026-11-06

- **Light wording on Klein: sources conflict.** BFL tells Klein prompts to name the source and direction (vendor)
  [C1]; on one project, naming a source painted it in six of six FLUX seeds (`../game-assets/NOTES.md`). T1 decides.
- **Text in images.** A listed weakness on Animagine XL 4.0 (vendor) [C8]. Composite wanted text in the stage until
  T19 says otherwise (inference).
- **Rewrite the prompt rather than adding seeds on a low-variety variant.** The maker rates Z-Image-Turbo's variety
  low, Z-Image base's high, with no measure shown. Vendor, read 2026-11-06; the advice is inference [C5, C6, T17].
- **Grow the defect list from real rejects.** Sources list counts, fused parts, anatomy, text, identity; **style
  defects such as line-weight drift appear in none**. Measured and vendor, photoreal-leaning; the list is inference
  [C49].
- **Explore with prose changes and small batches; spend seeds once a direction is liked. Report approved images per
  owner minute.** Inference, no study compares methods [C86, T16].
- **Treat a vendor's "consistent characters" as untested.** Qwen-Image-Edit-2511 and gemini-3-pro-image give claims or
  reference counts, with no benchmark. Vendor, read 2026-11-06 [C19].
- **Measure skin tone on the neutral-lit master.** Readings shift with light and grading. Measured method, effect not
  quantified; the rule is inference [C53].
- **Don't promise tries per kept image, and plan human or scripted finishing.** Reports run from 4 (a vendor) through
  40 (one studio, 2023) to 100 (a forum post). Vendor and practitioner, partly not opened [C82, C83, C84].
- **Suspect copied house phrases when images look alike, and keep concrete nouns as the source.** Templates contribute
  to sameness in public prompt sets (measured, one study, correlational); describe-and-regenerate loops lost people
  and places (measured, one study, narrow setup, read second-hand) [#63, #62].
- **Treat native alpha as unsettled.** LayerDiffuse users preferred it 97% of the time (measured, authors' own study,
  SD-era, extract); Anima-RGBA's card calls hair weakest (vendor, extract). Read 2026-11-06 [C30, C31].
- **Tint and add rim sprites in the stage before trying a relight model.** IC-Light repaints the foreground, which may
  change line and face. Inference; its claim is vendor, SD 1.5 era, read 2026-11-06 [C34, T10].
- **Review a bundled recipe as a dependency (`dependency-policy`).** VNCCS and CorridorKey 2.0 carry licence questions
  [C32, C36].
- **BiRefNet variants (secondary summary of vendor figures) [C27]:** General for hard edges; Matting for hair, smoke,
  mesh, glass, may soften hard edges; HR trained at 2048 px, adds little on small inputs. MIT by tag. Scores are on
  photo sets.
- **Z-Image inpaint in diffusers (vendor) [C35]:** white is repainted, black preserved; at strength 1 it ignores the
  image under the mask.
- **VNCCS (a host's page for someone else's tool) [C36]:** sheet, faces, expressions and sprites from one reference.
  Read the steps; don't install without a dependency review.
- **Metadata (standards body; whether games need it is unknown) [C75]:** IPTC Digital Source Type
  `trainedAlgorithmicMedia`, in XMP or C2PA; `compositeSynthetic` for composites with camera material. One optional
  field in the provenance record.

## To test on our own machine: UNTESTED

**Nothing below has been run** (as of 2026-11-06), so no rule rests on it yet. Each needs a free GPU, models whose
licences you've checked, and the owner's time where marked. The list is the research author's; the steps and order are
inference (editor).

To run one:

1. Do the live query. Take the project's GPU lock: one job at a time.
2. Write the pass line from the table down first, and don't move it after seeing results.
3. Plant the fault or run the control. If it doesn't fail, the check proves nothing: fix that first.
4. Run it small. Save outputs, seeds and versions in the project's scratch folder, not in this repo.
5. Replace "UNTESTED" on that row with the date, exact model and result, and edit any rule it contradicts.

**Start with** T4, then T2 and T1 (no owner time, and they decide what later prompts mean; a byte-compare means little
before T4 shows determinism), then T13 (no verdict means much without it). Pass lines marked "proposal" are the
editor's and the review's, for the owner to confirm before the test runs.

| # | Question | Test | Pass, or what decides it | State |
|---|---|---|---|---|
| T1 | Does a light-source phrase paint the source on Klein, and is C1's advice safe? | 8 seeds: "light from the left, hard" against "lit sign on the left, light from it"; count painted sources | Lower painted count wins; compare with `../game-assets/NOTES.md`'s earlier result | UNTESTED |
| T2 | Are negatives and guidance actually read? | Klein 4B, Z-Anime distill-8 and base, Animagine: same seed with and without a negative, at guidance 0, 1, 1.5, 4. Byte-compare | Identical output means ignored. Records the real scale per front end | UNTESTED |
| T3 | Does a same-seed trick hold a character? | 3 prompts changing pose and wardrobe, 8 seeds; compare CCIP distance between prompts sharing a seed with that between prompts on different seeds | Proposal: a trick only if the median within-seed distance is below the 25th percentile of different-seed distances | UNTESTED |
| T4 | Reproducibility | Same workflow and seed twice, once after restart, once with offload on | Pixel diff 0, or record the tolerance | UNTESTED |
| T5 | Which wording gets the target look, per model? | 6 wordings, traits only, no names, on Z-Anime, Klein, Animagine, 8 seeds; score with `anime_style_ages`; owner blind-ranks contact sheets | Proposal: Spearman above 0.5 keeps the classifier; the wording is chosen by the owner's rank. A known off-target set is the control | UNTESTED |
| T6 | What does CCIP catch? | 6 characters in 20 approved poses as positives. Plants: same costume different face, same face different costume, wrong hair colour, missing prop | Report which plants pass. Set the threshold from your data, not the card | UNTESTED |
| T7 | Coloured light read as drift | Relight one approved character in the stage (strong coloured rim), then score against the master by CCIP, CLIP | If lighting alone crosses the threshold, score only neutral-lit crops | UNTESTED |
| T8 | Which edge survives coloured light? | One character on flat grey, green, black, and in-scene with rim light; BiRefNet General, Matting and HR-matting, BEN2 base, CorridorKey; composite on white, black, a saturated colour | Proposal: fringe is pixels with alpha 5 to 95% at the edge; report its width and hue. Pick the lowest alpha error on a synthetic control with known alpha over a saturated plate. Owner sees the three worst | UNTESTED |
| T9 | Can one face give mouth and blink frames? | 6 mouths and a blink by mask inpaint on Z-Image and Klein, composited over the master; also the same by unmasked edit | Pixels outside the mask unchanged (diff 0), CCIP and skin class against the master; flipbook for the owner. Plant a 2-pixel offset to prove the diff can fail | UNTESTED |
| T10 | Lighting match | Same character over a plate: stage tint and rim sprites against IC-Light | Identity score, line damage (edge map diff), owner's choice | UNTESTED |
| T11 | Do descriptors hold? | 8 cast descriptions, 16 seeds each, on each permitted model, neutral light; owner and `anime_ch_skin_color` check. Repeat for each expression | Share of images holding skin, gender presentation and age. Proposal: under 80% holding on any attribute rules the model out for that character. Worst model and worst expression named | UNTESTED |
| T12 | Adult read and drift, **adults only** | Portraits of adult-designed cast, fully clothed, scored by `anime_teen`, tags by WD. Generate 100 of a neutral scene per character and trend clothing and framing tags. **Never build a positive control combining young-looking characters with sexual or suggestive content;** for sensitivity use a non-sexual control only (adult in swimwear against adult in coat). Teen classifier sensitivity then stays unknown on your art, and it's reported as such | Flag rate on adults; trend per character. Proposal: a clothing or framing tag's share rising 10 points above that character's master sends the batch to a person. Owner reviews every flagged image and a random sample of unflagged ones. This sampling is the test's; it doesn't replace the look at every image with a person | UNTESTED |
| T13 | Which judge can we trust? | 40 images, 10 with planted faults (six-finger edit, wrong costume, mirrored insignia, swapped eye colour, garbled sign). Judges: the generating session; a fresh session of the same model, with and without the prompt; another vendor's model, with and without. A person labels the 30 unplanted images first | Counts, not just rates: 10 of 10 still has a lower 95% bound near 69%. Proposal: a judge is used for flags only if it catches at least 9 of 10 plants and false-alarms on at most 3 of the 30. Publish beside any later verdict. Expect the prompt-aware and self-judging settings to look kinder (C46); this tests it. Says nothing about adult appearance | UNTESTED |
| T14 | Are scorers any use for your look? | LAION, PickScore, `anime_aesthetic` on 30 images the owner has ranked blind | Keep only if Spearman is above 0.5 and stable across a second batch | UNTESTED |
| T15 | LoRA on your card | 15, 30, 60 images of one character from your own approved sheets (no BFL API images), on Klein 4B base and Z-Image base. Vary outfit in training; ask for a new outfit and a new pose; try other checkpoints | Peak VRAM; CCIP on held-out poses; whether outfit follows the prompt; portability. Proposal: keep the smallest set that fits the card, beats a shuffled-caption control on held-out poses, and follows a new outfit in 8 of 10. Only after the look is settled | UNTESTED |
| T16 | Cost per approved image | 20 briefs: 16-image batch, then a pre-sort, against 4 careful prompts. Log GPU minutes and owner minutes | Owner-approved images per owner minute. Plant 2 bad images per batch to confirm the pre-sort removes them | UNTESTED |
| T17 | Spread across seeds | Z-Anime distill-8 and base, 16 seeds, one prompt: CCIP and composition spread | Proposal: distilled varies less if its median pairwise CCIP distance is below base's. Buy more seeds only on the wider variant | UNTESTED |
| T18 | Provenance survives | Run an image through matte, upscale and engine import; read the metadata at each step | Lost fields must be in the sidecar | UNTESTED |
| T19 | Signage | Ask for short sign text on Klein, Z-Anime, Gemini; OCR against the wanted string | If under 90% exact, composite all text in the stage | UNTESTED |
| T20 | Edit chains | 10 chained edits against 10 edits each from the master; CCIP to master, palette drift | Proposal: chaining is allowed only if CCIP to master and palette drift after 10 chained edits stay within the range of the 10 edits from the master | UNTESTED |

## Single sightings

Moved from the library's candidate list on 2026-11-13: true of this skill's domain, not yet seen twice.

- **2026-11-07, mystery-game - Compare a generated person with strangers from the same words, not with other people.** Across different test people both face tools separated them easily, but against sheets from the same description an anime-trained tool scored strangers as close as the real frames, and only a line-up (which same-words sheet is nearest) moved above chance, on 2 of 3 people. Give the no-reference frames as the control. Target: generated-art.
- **2026-11-07, mystery-game - A reference image can leave a model's body proportions unchanged.** On one fast image model a plain proportion figure given as a reference carried about 15% of a deliberately different body, whatever the order or number of references; starting the image from the figure carried about 95%. Plant a different figure before believing any "reference controls X" claim. Target: generated-art.
- **2026-11-07, mystery-game - Steady isn't correct.** A character method held the same proportions across outfits, and those proportions were unlike the stated ones (head about 1.4 times the target). A spread alone would have passed it; report the gap to the target beside the spread. Target: generated-art.
- **2026-11-07, mystery-game - Front-on outlines can't see a bust.** Body-model bust size changes depth, so mask widths from the front were identical across builds. Measure side-on. Target: generated-art.
- **2026-11-07, mystery-game - Start-image strength has steps, and low values copy.** On a 6-step schedule denoise .65 copied the mannequin, and .8 and .9 gave identical images. Check that two settings differ before comparing them. Target: generated-art.
- **2026-11-07, mystery-game - `rtmlib` pulls in GUI OpenCV.** In a slim container it fails on libxcb, and a measuring run that caught the error reported a count of 0. Install `opencv-python-headless` with `--no-deps`, and treat a zero count as a failure until looked at. Target: generated-art NOTES.
- **2026-11-07, mystery-game - To change a generated frame's look, edit its own plate; and state the goal, not a means.** Three frames came out in a flatter look than the rest. Fresh prompts had taken 3 to 6 attempts to get their stair geometry. An edit call on each frame's own plate, with a matching frame as the look reference, kept the geometry and fixed the look in 2 attempts. A wording rule for one object's path (a handrail "from the top step to the door") failed on 6 of 6 attempts, while the goal behind it, no geometry error, was met by a short rail. Target: generated-art.

## Moved from SKILL.md (2026-11-13)

Most numbers cut from `SKILL.md` already live in "Check cards" above or in `EVIDENCE-GENERATION.md` under the cited
tag, so they were cut, not copied. These were in neither:

- **Before the first prompt.** The most downloaded model family on 2026-11-06 was one the research lists as
  research-only [C72]. Examples of variant differences [C5, C6, C11]: Z-Image-Turbo takes guidance 0 and ignores
  negatives, Z-Image base takes CFG 3 to 5 and uses them; Qwen-Image-Edit-2511's example sets `true_cfg_scale` and
  `guidance_scale` apart. The licence example [C33]: Anima-RGBA is tagged apache-2.0, but its LoRA derives from Anima,
  whose licence names LoRAs as derivatives and bars revenue-generating use, while its clause 2(e) lets Outputs be used
  commercially except as prohibited; unresolved. Pinning [C85]: one forum thread reports replacing old art after a
  model's style shifted.
- **Prompting.** Prose for FLUX.2 Klein 4B and 9B and Z-Anime; ordered tags for Animagine XL 4.0 [C1, C7, C8]. Negative
  prompts [C2, C4, C7]: diffusers has no text negative for distilled FLUX.2 Klein, Z-Anime's card says limited, a
  practitioner guide advises one anyway. Positive wording [C3, C10, C12]: BFL and Google advise it (FLUX.2 pro and max,
  FLUX 3 Image, Gemini image models); on Stable Diffusion v2 at 30 steps, inpainting removal averaged about 80% by
  human judges and 63% by GPT-4V. Token budgets [C9]: CLIP-era SDXL's standard pipeline cuts at 77 tokens, Animagine's
  card uses a long-prompt pipeline, `max_sequence_length` is 512 in the diffusers Klein and Z-Image pipelines.
- **Who scores an image.** Planted faults: ten in forty images. Self-preference [C46]: in one paper, judges were over
  50% more likely to pass their own rubric failures.
- **Adult appearance.** Age following [C57]: error 3.0 to 5.3 years on photoreal models; SD 3.5 skewed women younger by
  1.10 years.
- **Bias** [C51, C52, C54]: open models (Flux and SD 3 family) gave 41% women against 52% in matched data (one study);
  Gemini Flash 2.5 Image gave 93.7% women, GPT Image 1.5 29.4%, both about 96% classified white (one preprint). Across
  eight models, Anger moved the 20-to-39 share from 80.3% to 40.4%; Disgust moved White from 49.0% to 81.4% and Asian
  from 26.3% to 2.1%. Young, female and Black came out at 1.3% against 5.27% expected, none in four of eight models.
  Anime imbalance [C56] was on SD 3.5, Illustrious and two others.
- **Provenance, rights and disclosure.** Allen v. Perlmutter was pending at 2026-06-01: check its outcome [C68, C69,
  C70]. Disclosure [C73, C78]: Steam's doc (opened 2026-11-06) covers content that ships and players consume; one report
  adds store-page marketing.
