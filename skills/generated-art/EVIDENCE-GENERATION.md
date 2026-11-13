<!-- Research notes from 2026-11-06, edited into citable form the same day. Rules are in SKILL.md; recipes and the To-test list are in NOTES.md.
Editing changed no claim number, kind, access mark or the substance of a limit. It generalised lines written about one project, turned quoted source wording
into paraphrase, removed references to session files, and moved two tables (the C1 to C11 summary, T1 to T20) to NOTES.md. "I" and "my" mean the
research author; "our" means whoever runs the pipeline. Corrections an independent review made at the source on 2026-11-06 are marked as such. "The stack research" is a same-day survey of models and licences whose file
wasn't kept, so a point resting on it is second-hand here. "Own NOTES" is ../game-assets/NOTES.md. Cite an entry as [C12]. -->

# Evidence: the generation pipeline for game art

Checked 2026-11-06 (machine clock 2026-11-07 02:47 UTC). Scope: prompting, consistency, layers, judging output, bias and drift, provenance, cost. Visual storytelling and art direction are in `../art-direction/EVIDENCE-DIRECTION.md`. No images were generated and no GPU job was run, so **nothing here shows how any model looks on any real project's look**. No rules or skill text. Not legal advice: section 6 reports what public sources say, and a paid release should have a lawyer read it.

## How to read the labels

**Access.**
- `opened`: I read the text itself (PDF converted with pdftotext, raw README, or a page returned unsummarised).
- `extract`: it came through a summarising fetch. The figures are as reported by that summariser, so check them against the source before quoting.
- `not opened`: I only saw a search-result summary, or the page refused the fetch.

**Kind.** `vendor claim` (the maker of the thing, about the thing), `measured` (a study or test with numbers), `practitioner` (someone reporting their own use), `shipped` (demonstrated in a released work), `inference` (mine). Three more where those don't fit: `vendor terms` (a licence or terms as written), `agency position`, `secondary` (a report of someone else's statement). A deepghs card's accuracy is `vendor claim` because the maker tested its own model. Every "Change" line is my inference.

**"Recalled URL"** marks a page whose address I knew or guessed after the search budget ran out, rather than one a search returned. It was opened, but it wasn't found the way the research brief asked.

## Live query, 2026-11-06

Hugging Face API, `pipeline_tag=text-to-image`, by trending and downloads; `image-segmentation` by trending; search `matting`. The raw files weren't kept (SHA-256 prefixes: trending 4b0ef26c, downloads 671227b6, segmentation 3657f712, matting f3e3fa08). These API calls were not counted as searches; the research brief asked for a live query.

Current by downloads: Qwen-Image-2.1 and its quantised forms, SDXL base 1.0, Krea-2, FLUX.2 Klein 4B and 9B, Animagine XL 4.0, Z-Image-Turbo, NoobAI-XL 1.1.
Trending and new since the stack research (2026-11-06, same day), **not evaluated here, licence tags unverified**: PrunaAI/P-H3-Image (2026-10-27, tag other), lodestones/chroma-h3 (2026-10-31, other), lodestones/Kromoss (2026-10-19, apache-2.0), speridlabs/iris-3b (apache-2.0), 0ppxnhximxr/snapref-v1a and v2a-pre2 (other), localai0301/Anima-RGBA (see C31, C33). "Uncensored" LoRAs for MOSS-Image and Qwen-Image 2.1 are trending too (C7 notes drift risk).
Matting: ZhengPeng7/BiRefNet family (MIT tags), briaai/RMBG-2.0 (other), facebook/sapiens2-matting-1b (other, 2026-05-15, not evaluated), nikopueringer/CorridorKey2.0 (C32).

## Status of each question

| Q | Status | What's missing, and what was searched |
|---|---|---|
| 1 Prompting by family | **Answered** from vendor documents | Seed behaviour on Gemini image models and the BFL Klein API is unknown: the pages read don't say. Searches 1, 18 |
| 2 Consistency | **Partly**. LoRA and reference advice is vendor or anecdote; metrics exist but aren't validated on original anime characters | No controlled study of dataset size or captions on any current model. Seed trick: no evidence either way, and search 18 returned nothing on it. Searches 2, 10, 17 |
| 3 Layers | **Partly** | Cut-out tools covered. **Unanswered:** coloured rim-light and colour-spill edges, mouth and blink variants, lighting match on anime. Searches 11, 12, 19 returned nothing on these; see To test T8 to T10 |
| 4 Judging | **Answered** for scorers and vision models on photoreal images. **Partly** for professional review: only two self-reports (C50, C82, C83); no dedicated search, budget went to higher-priority questions and `EVIDENCE-DIRECTION.md` covers art direction. No vision-model test on anime or cel art was found | Searches 3, 9, 20 |
| 5 Bias and drift | **Partly**. Gender, race and age measured on photoreal models. **Unanswered:** no measurement of adults drawn younger in anime styles, and no error rates for race or age checks on anime other than one unvalidated classifier (C62). Sexualisation drift has no benchmark | Searches 4, 5, 6, 16 |
| 6 Rights | **Answered as of the dates given**. Allen v. Perlmutter status is known only to 2026-06-01. Disney and other training or output suits against image generators: not searched, budget gone | Searches 7, 8, 13, 15 |
| 7 Cost | **Partly**. Tries-per-keeper figures are vendor or anecdote, none controlled. No quantified time-wasted figure from a shipped game | Search 14 |

Budget: 20 of 20 searches used. Log at the end.

## Claims

### Q1. Prompting by family

**C1.** FLUX.2 Klein wants flowing prose, not keywords. It gets your text as written with no expansion, so detail must be supplied. Describe light source, direction and hardness; end with a `Style: ... Mood: ...` line; English gives the most precise results.
- Source: https://docs.bfl.ml/guides/prompting_unified_reference.md and https://docs.bfl.ai/flux_2/flux2_overview | extract | vendor claim | FLUX.2 Klein 4B, 9B | 2026-11-06
- Limits: no test shown. The HF card only says prompt following depends heavily on style (https://huggingface.co/black-forest-labs/FLUX.2-klein-4B). No word limit stated. The page says nothing on negatives for Klein.
- Change (inference): write Klein prompts as sentences, and treat the Style/Mood line as a candidate to test. This conflicts with game-assets NOTES ("naming a light source paints it"), so see T1.

**C2.** On step-distilled Klein, guidance is ignored; the pipeline has no text negative-prompt parameter (only `negative_prompt_embeds`, defaulting to the empty string). The undistilled base variants use real guidance, 4.0 by default. Distilled runs 4 steps.
- Source: https://huggingface.co/docs/diffusers/main/en/api/pipelines/flux2 (opened), https://docs.bfl.ai/flux_2/flux2_overview (extract) | vendor claim | Klein 4B, 9B, base variants; diffusers main branch | 2026-11-06
- Limits: this is the diffusers implementation. ComfyUI's behaviour wasn't read. The HF card's example passes `guidance_scale=1.0`.
- Change (inference): don't author negative prompts for distilled Klein. Confirm by byte comparison, T2.

**C3.** FLUX.2 pro and max and FLUX 3 Image have no negative prompt. BFL says to describe the wanted state (an empty walkway, rather than a negated crowd). FLUX 3 also has no `prompt_upsampling`, and takes layout boxes and references by position ("image 1").
- Source: https://docs.bfl.ml/guides/prompting_unified_reference.md, https://docs.bfl.ml/guides/prompting_unified_technical.md, https://docs.bfl.ml/guides/prompting_summary.md | extract | vendor claim | FLUX.2 pro/max, FLUX 3 Image | 2026-11-06
- Limits: guidance and seeds aren't covered on the pages read for FLUX.2 pro and max. Correction (independent review, at the source, 2026-11-06): BFL's page says FLUX 3 Image has no `negative_prompt`, `seed`, `prompt_upsampling` or `guidance` fields, and unknown fields return 422.
- Change (inference): don't reuse Klein prompts on FLUX 3 unchanged, since each has its own guide.

**C4.** One practitioner guide: distilled Klein at CFG 1.0 to 1.5, higher looks waxy; base at 3.5 to 5, 20 to 24 steps; mismatched steps give black or static images; the 18 GB fp16 base model runs out of memory on 12 GB; crowded scenes lose track of who does what; photo edits can invent a new person. It also suggests a negative node for waxy skin, which conflicts with C2.
- Source: https://neurocanvas-web.pages.dev/blog/flux-2-klein-comfyui-guide/ (2026-03-09) | extract | practitioner | Klein 4B, 9B in ComfyUI | 2026-11-06
- Limits: no benchmarks or controlled comparisons. Identity observations are on photos.
- Change (inference): treat as a list of things to look for, not settings to copy.

**C5.** Z-Image-Turbo: guidance 0, no CFG, 8 effective steps, so a negative prompt does nothing (diffusers: ignored when guidance is below 1). The maker rates its variety across seeds as low. The card describes a prompt enhancer that adds world knowledge.
- Source: https://huggingface.co/Tongyi-MAI/Z-Image-Turbo (extract), https://huggingface.co/docs/diffusers/main/en/api/pipelines/z_image (opened) | vendor claim | Z-Image-Turbo | 2026-11-06
- Limits: the card praises photorealism and bilingual text, not anime. Docs say it fits 16 GB; nothing on 12 GB.
- Change (inference): rerolling Turbo seeds explores less than rerolling Base seeds (C6, C86). Rewrite the prompt rather than adding seeds.

**C6.** Z-Image base: full CFG at 3 to 5, 28 to 50 steps, negatives work well by the maker's account. It is fine-tunable, and it varies much more than Turbo in composition, **facial identity** and lighting across seeds.
- Source: https://huggingface.co/Tongyi-MAI/Z-Image | extract | vendor claim | Z-Image base | 2026-11-06
- Limits: no measure of variability shown.
- Change (inference): the same family gives opposite answers on negatives and identity spread, so a rule must name the variant, not "Z-Image".

**C7.** Z-Anime: natural-language sentences work best, not tag lists. Base at CFG 3 to 5 (no higher than 9, risking oversaturation), 28 to 50 steps, negatives at full effect. Distilled 8-step and 4-step at CFG 1.0, at most 1.5, negatives limited. euler_ancestral with beta. The author calls it experimental and says it can partly produce adult content. The card doesn't describe training data.
- Source: https://huggingface.co/SeeSee21/Z-Anime | extract | vendor claim | Z-Anime base, distill-8, distill-4 | 2026-11-06
- Limits: one author; no measured comparison. A distilled Z-Anime at CFG 1 differs from Turbo's documented 0; those may be two front ends' scales for "off", which is unverified (T2).
- Change (inference): tag-trained habits ("1girl, masterpiece") are the wrong default here even though it's an anime model. Plan a drift check (C63 to C66) from the first batch.

**C8.** Animagine XL 4.0 needs tags in trained order: subject count, character, series, rating, then anything, ending in quality tags (score tags stronger than `masterpiece`). The card recommends a standard negative list, CFG 4 to 7, 25 to 28 steps, Euler a, around 1024 px. The card warns that natural language may not work well. Rating tags exist (`safe`, `sensitive`, `nsfw`, `explicit`). Hands, text and multi-character scenes are listed as weak. Year tags run `year 2005` to `year 2025`.
- Source: https://huggingface.co/cagliostrolab/animagine-xl-4.0 (extract; year range opened in raw README) | vendor claim | Animagine XL 4.0 | 2026-11-06
- Limits: no measurement of the negative list or quality tags. It was trained for identity more than style by the card's account.
- Change (inference): year tags can't ask for anything before 2005. An earlier look has to come from other tags or a LoRA, and the model may lack the data. See T5. Don't carry character or series tags into prompts where a look shouldn't lean on a named show (C71).

**C9.** SDXL base has two text encoders (`prompt`, `prompt_2`, each with a negative) and negative size and crop conditioning. Its default is 1024 px, and below 512 is unlikely to work.
- Source: https://huggingface.co/docs/diffusers/main/en/using-diffusers/sdxl | opened | vendor claim | SDXL 1.0 base | 2026-11-06
- Limits: base model, not anime fine-tunes. The 77-token CLIP cut is in game-assets NOTES, not repeated.
- Change (inference): SDXL-era prompts have a hard token budget; prose families have a far larger one (`max_sequence_length` 512 in the diffusers Klein and Z-Image pipelines).

**C10.** Gemini image models: describe positively (say the street is empty and quiet, rather than negating cars); be specific about materials and purpose; refine in turns; order complex scenes background first; use camera terms. Generate wanted text first, then ask for the image containing it. For consistency, feed earlier images back in. All output carries SynthID. Comic panels are named as a use, recommending Gemini 3 Pro or 3.1 Flash.
- Source: https://aistudio.google.com/docs/image-generation (redirected from ai.google.dev) | extract | vendor claim | gemini-nano-banana-2.1, gemini-3.1-flash-image, gemini-3-pro-image | 2026-11-06
- Limits: the docs' seed status for images is unknown. The API reference lists `seed` only in a live-session section and doesn't say whether it applies to image models or guarantees anything (https://aistudio.google.com/api-reference/generate-content, extract).
- Change (inference): don't promise reproducibility from hosted Gemini. Store the output file as the source of truth.

**C11.** Two more families do it differently. MOSS-Image takes prose, tags or JSON layouts, default guidance 3, 50 steps, empty negative. Qwen-Image-Edit-2511's example uses `true_cfg_scale` 4.0 with `guidance_scale` 1.0, 40 steps, negative of one space, and the card doesn't explain the interaction.
- Source: https://huggingface.co/OpenMOSS-Team/MOSS-Image-Base, https://huggingface.co/Qwen/Qwen-Image-Edit-2511 | extract | vendor claim | as named | 2026-11-06
- Limits: anime strength and VRAM not covered.
- Change (inference): "guidance" is not one setting. Name the parameter and the pipeline in any recorded recipe.

**C12.** Negative prompts act later than positive ones (noun negatives around step 5 of 30 on SD 2) and can backfire if applied only very early. Applied at all steps, the removal metric (RSR, which I read as removal success rate) averaged about 80% by human judges and 63% by GPT-4V.
- Source: https://arxiv.org/html/2406.02965v1 (ECCV 2024) | extract | measured | Stable Diffusion v2, 30 steps | 2026-11-06
- Limits: one old CFG model, inpainting-based tests, no distilled models. The reverse effect is shown by example with no rate. Text is internally inconsistent on the best window. The 17-point gap between judges is itself a warning about vision-model judging.
- Change (inference): even where negatives work, expect roughly one miss in five. Check for the excluded thing rather than trusting the negative.

**C13.** A seed gives reproducibility, within limits: a CPU generator is more stable across machines; a GPU generator can diverge; a generator's state is consumed, so reseed for each call; and PyTorch doesn't guarantee identical results even with the same seed.
- Source: https://huggingface.co/docs/diffusers/using-diffusers/reusing_seeds | opened | vendor claim | diffusers, any pipeline | 2026-11-06
- Limits: says nothing about keeping a character when the prompt changes (see Unsupported).
- Change (inference): record generator device with the seed, and hash the output so a reproduction can be checked.

**Summary of C1 to C11:** moved to the recipe table in `NOTES.md`.

Advice that does not transfer: quality and rating tags (only tag-trained SDXL models); negative lists (only CFG variants); token budgets (only CLIP-era); "lower guidance" (means different things by pipeline); a Klein prompt to Animagine, or the reverse.

### Q2. Consistency across hundreds of images

**C14.** BFL's Klein LoRA guide: caption everything visible except the style or concept being taught; use a trigger word; 1,500 to 2,500 steps for style, 1,500 to 3,000 for characters; LR 8e-5 to 1e-4, lower for style; vary poses, angles, lighting; avoid repetitive backgrounds. Klein 4B base needs 12 GB and 32 GB RAM. It gives no image count.
- Source: https://docs.bfl.ai/flux_2/flux2_klein_training | extract | vendor claim | Klein 4B base, 9B base | 2026-11-06
- Limits: the only failure named is overfitting. No licence statement for trained LoRAs or their output.
- Change (inference): the "style not in caption" rule is the one to adopt first. Have the dataset checked for captions that name the look.

**C15.** Dataset size has no agreed figure: 20 to 30 usually, 54 for a wide range (alvdansen, 2024); 15 to 30 (a guide); 30 to 60, with 200 judged excessive (one poster); 100 to 200 or 150 to 400 with heavy tagging (others); 8 to 20 for Z-Image (a beginner guide, not opened).
- Source: https://huggingface.co/blog/alvdansen/training-lora-m3lt (extract), https://reddit.sentinel-team.org/posts/1rd9fz4/snapshots/2026-02-27T22%3A54%3A44.928972Z (extract, mirror), https://andrewaltimit.github.io/Documentation/docs/ai-ml/lora-training.html (not opened), https://wavespeed.ai/blog/posts/blog-z-image-lora-what-it-means (not opened) | practitioner | mostly SDXL-era; Z-Image where named | 2026-11-06
- Limits: anecdote. Models differ. Search 17 found no controlled comparison.
- Change (inference): start small because a small set can be audited by hand, and let T15 decide.

**C16.** Reported LoRA failures: style captioned in, so a character LoRA on anime data stopped looking anime; a few bad images hurt; noisy tags make the model work against itself; the base checkpoint strongly shapes style; a character LoRA can bake in its style and resist a style LoRA; text-encoder training is a gamble; authors often retrain 2 or 3 times. One poster advises tagging era when a style spans several periods.
- Source: the Reddit mirror in C15; search 17 summary for the caption-related report | extract, partly not opened | practitioner | SDXL-era, Illustrious | 2026-11-06
- Limits: forum posts, an unofficial mirror.
- Change (inference): budget at least three LoRA runs per target. Keep style and character LoRAs separate. Test the LoRA at more than one strength before believing it.

**C17.** On Z-Image, one poster's 30 to 40 image character LoRA on base learned the outfit more than the face and still drifted. Another found a Turbo-trained LoRA falls apart on any other checkpoint. A third calls Z-Image probably the strongest base for likeness, and suggests a head-swap pass with Qwen Edit or Klein afterwards. A commenter blames upscaled low-quality sources.
- Source: https://reddit.sentinel-team.org/posts/1sd8yie/snapshots/2026-04-06T18%3A35%3A44.931349Z | extract | practitioner | Z-Image base and Turbo, 12 GB users | 2026-11-06
- Limits: a thread on a mirror, one dataset. RunComfy's Base-versus-Turbo article (https://www.runcomfy.com/trainer/ai-toolkit/z-image-base-vs-turbo-lora-training) returned no body text; the search summary says Base is the safer default for likeness, from a seller of training.
- Change (inference): vary outfits in the training set, or test outfit-swap at acceptance. Train on the checkpoint you will ship with.

**C18.** Licence reaches into LoRAs and references. Anima's licence defines LoRAs as Derivatives, and its restrictions apply to them. BFL's terms (stack research, read 2026-11-06) bar using Output to train other models, which blocks a local LoRA from API images.
- Source: https://huggingface.co/circlestone-labs/Anima/raw/main/LICENSE.md (opened), the stack research, licence section (not kept) | vendor terms | Anima; BFL API | 2026-11-06
- Limits: not legal advice. Gemini terms on training from outputs weren't read here.
- Change (inference): record where every training image came from. A LoRA dataset from a paid API may be a dead end regardless of quality.

**C19.** Reference inputs per vendor: Klein up to 4; Gemini up to 14 total, of which 4 characters on nano-banana-2.1 and 3.1 Flash, 5 characters and 3 style on 3 Pro, and 2.5 Flash works best with 3. Qwen-Image-Edit-2511 claims significantly improved character consistency and reduced drift. No page gives a consistency benchmark.
- Source: https://docs.bfl.ml/guides/prompting_unified_reference.md, https://aistudio.google.com/docs/image-generation, https://huggingface.co/Qwen/Qwen-Image-Edit-2511 | extract | vendor claim | as named | 2026-11-06
- Limits: counts are capacity, not quality.
- Change (inference): treat "consistent characters" as untested until a project's own metric and its owner agree.

**C20.** Reference methods reported failing: an OpenAI warning that recurring characters may not stay consistent (stack research); VNCCS identity drift between steps and artifacts on strong emotions (C36); Klein inventing a person on photo edits (C4). Own NOTES record mirror images from "show from behind".
- Source: https://developers.openai.com/api/docs/guides/image-generation (read by the stack research, not re-read here), C36, C4 (extract), game-assets NOTES (opened) | vendor claim, practitioner | as named | 2026-11-06
- Limits: mixed models and sources; not a rate.
- Change (inference): always edit from the approved master, and never chain edits until measured (T20).

**C21.** A game-sprite study: reference plus pose conditioning scored subject consistency 0.89 to 0.93 by a DINO measure, while hairstyles and props stayed weak, and one fine-tuned model dropped a gun from the character. SD-IPCN beat the fine-tuned Animate Anyone on that consistency score, while Animate Anyone won on similarity to ground truth.
- Source: https://arxiv.org/html/2412.03685v2 | extract | measured | SD 1.5 with IP-Adapter and ControlNet; Animate Anyone | 2026-11-06
- Limits: 152 action sequences, four qualitative examples, older models.
- Change (inference): a high whole-character score can sit beside a missing prop. Check named props separately.

**C22.** Face-recognition embeddings are unreliable on stylised faces. StyleID reports that encoders trained on photographs mistake texture or palette change for identity drift and miss geometric exaggeration. It offers a metric fine-tuned to human judgements, and reports better correlation on artist-drawn portraits.
- Source: https://arxiv.org/abs/2604.21689 | extract (ArcFace and AdaFace named only in the search summary, not opened in full) | measured, authors' own metric | cartoon, sketch, paint styles; anime not named | 2026-11-06
- Limits: single preprint. Paper is CC BY-NC-SA; weights licence not stated.
- Change (inference): don't gate on an ArcFace threshold. Strong coloured lighting may read as drift to any such measure (T7).

**C23.** ViStoryBench splits by subject: ArcFace, AdaFace and FaceNet for realistic characters, CLIP on Grounding DINO crops for non-realistic ones, and CSD for style. Self-consistency agrees with human ratings at Kendall 0.50, Spearman 0.68, Pearson 0.80. A search summary reported CCIP for anime on this benchmark, but neither page I fetched mentions it, so that is unresolved.
- Source: https://vistorybench.github.io/metrics, https://aaai26-19745.github.io/metrics (extract); CCIP mention from search 10 summary only (not opened) | measured | story-visualisation benchmark, mixed models | 2026-11-06
- Limits: the anime path isn't validated separately, and no sample size was given. It uses Gemini-3 Pro as a judge for prompt alignment.
- Change (inference): a usable pattern: crop, embed, compare to reference and to other shots. Calibrate before believing any number.

**C24.** CCIP scores whether two images show the same anime character: best F1 0.94 at threshold 0.213 (`ccip-caformer_b36-24`). The card limits it to images with one character. Licence OpenRAIL.
- Source: https://huggingface.co/deepghs/ccip | opened | vendor claim (card's own test) | CCIP, card last modified 2024-09-09 | 2026-11-06
- Limits: trained on existing anime character data, not on original characters or generated art, and not on older cel styles or strong coloured light. No study of what it is sensitive to was found.
- Change (inference): the strongest candidate for a cast gate. Likely leans on hair and costume, so an impostor in the right outfit may pass (T6). Drive it on one-character cut-outs, the form the card supports.

**C25.** What identity measures miss, on current evidence: prop loss (C21), costume detail, proportions, palette, and the difference between style change and identity change (C22). No source tested them on these.
- Source: inference from C21 to C24 | inference | any | 2026-11-06
- Limits: not measured on any real cast.
- Change (inference): use the score to rank what the owner sees first, and plant faults to show what it can't catch.

**C26.** `anime_style_ages` classifies images into seven eras. Accuracy 71.03%, and for `1980s`, recall 74.5% and precision 65.6% (my arithmetic on the card's confusion matrix: 596 of 800, 596 of 909). Confusion is mostly with neighbours.
- Source: https://huggingface.co/deepghs/anime_style_ages (card and `caformer_s36_v0/plot_confusion.png`) | opened | vendor claim (card's own test) | `caformer_s36_v0`, 2023-12 | 2026-11-06
- Limits: dataset card not read; I assume booru-derived labels like the family's other sets. Generated art was not tested. It sees "drawn in that era", which isn't "cel, grain, matte painting" and isn't the owner's taste. OpenRAIL.
- Change (inference): cheap evidence of whether a prompt or LoRA moved the output towards a target era. Good for catching a modern default. Not a judge of the look.

### Q3. Layers

**C27.** BiRefNet variants: General for hard edges; Matting for hair, smoke, mesh, glass (can soften hard edges); HR trained at 2048 px, adding little on small inputs. Published scores are on photo sets (portrait S-measure 0.983; HR on DIS 0.927 against 0.898). Code and weights MIT by tag.
- Source: https://okmiku.com/blog/birefnet-background-removal-series (2026-05-04), https://huggingface.co/ZhengPeng7/BiRefNet_HR-matting | extract | secondary summary of vendor figures | BiRefNet family | 2026-11-06
- Limits: no illustration tests. The HR-matting card names no training data.
- Change (inference): cel lines may suit General, and hair may suit Matting: one per character is a question for T8, not an assumption.

**C28.** RMBG-2.0 has BiRefNet's architecture, trained from scratch on Bria's data; its licence isn't open (`bria-rmbg-2.0`). One user found it weak on 2D anime: characters filling the frame, hair close to background colour, gaps between arm and hip kept filled, shadows kept.
- Source: https://huggingface.co/briaai/RMBG-2.0/discussions/9 | extract | vendor reply plus one practitioner | RMBG-2.0 | 2026-11-06
- Limits: one poster, no numbers.
- Change (inference): generate with margin, on a background unlike the hair, and check enclosed gaps. Use these as bake-off cases.

**C29.** BEN2 base is MIT; the fuller model is API or commercial. Trained on DIS5k plus a private 22K set. It claims stronger hair matting without figures and has an optional `refine_foreground` step. One comparison found BiRefNet-HR better on hair but over-correcting, while the author preferred BEN2.
- Source: https://huggingface.co/PramaLLC/BEN2 (extract), https://medium.com/code-canvas/background-removal-in-comfyui-just-got-really-really-good-2a12717ff0db (not opened, 403) | vendor claim; practitioner | BEN2 base, BiRefNet-HR | 2026-11-06
- Limits: the claim concerns the commercial model, not necessarily the free one.
- Change (inference): include the free base model in the test, and don't credit it with the vendor's claim.

**C30.** LayerDiffuse makes a latent diffusion model output alpha directly. Users preferred its output over generate-then-matte in 97% of cases, and quality was reported as comparable to stock assets. Trained on about 1M layer pairs.
- Source: https://arxiv.org/abs/2402.17113 | extract | measured, authors' own study | SD-era latent diffusion models | 2026-11-06
- Limits: 2024, participant count not on the page read. Not shown on Klein, Z-Image or anime. Matting tools have improved since.
- Change (inference): native alpha is worth a look wherever an adapter exists, but this doesn't settle it for us.

**C31.** Anima-RGBA gives native alpha for anime and illustration: an RGBA VAE plus a LoRA, trigger "transparent background". Its own card says hair, glass and smoke are weakest, alpha is mostly binary, and close-ups may keep a white background.
- Source: https://huggingface.co/localai0301/Anima-RGBA | extract | vendor claim | Anima (2026-11-02) | 2026-11-06
- Limits: **Licence trap (C33).** No test here.
- Change (inference): a binary alpha may suit cel art well and fail on soft hair, so don't rule out the method; just rule out this licence for a paid product. If the method appeals, look for an equivalent on a permitted model.

**C32.** CorridorKey 2.0 is a green or blue screen keyer that predicts a matte and clean foreground. It was trained on in-house CG. Its licence (CC BY-NC-SA base plus terms) allows use on commercial projects with output yours, but no paid access or inference service, and integration in commercial software needs contact. Needs at least 4 GB VRAM up to 1440p.
- Source: https://huggingface.co/nikopueringer/CorridorKey2.0 | extract | vendor claim | CorridorKey 2.0 (2026-10-13) | 2026-11-06
- Limits: takes video, and no illustration test or benchmarks. Despill not mentioned on the page.
- Change (inference): a possible route for "generate on green, then key" (T8). Tool use only; read its licence text first.

**C33.** Licence-tag trap, verified on one case. Anima-RGBA's repo says apache-2.0, but its LoRA is trained on Anima, whose licence names LoRAs as Derivatives and bars revenue-generating use and use affecting third-party end users. The VAE comes from a separate Apache-derived source.
- Source: https://huggingface.co/circlestone-labs/Anima/raw/main/LICENSE.md (opened), C31 | vendor terms; reading is inference | Anima-RGBA, Anima | 2026-11-06
- Limits: not legal advice. Anima's outputs clause reads differently (stack research noted the oddness), and it wasn't resolved.
- Change (inference): read the base model's licence for every LoRA, VAE or adapter, whatever its tag says.

**C34.** BiRefNet is the suggested commercial replacement in IC-Light's own notes, because BRIA RMBG 1.4 is non-commercial. IC-Light relights a foreground by text or by background image; it is Apache-2.0 and its filenames indicate SD 1.5. It describes its consistency across relightings as high.
- Source: https://github.com/lllyasviel/IC-Light | extract | vendor claim; recalled URL, name suggested by search 19 | IC-Light | 2026-11-06
- Limits: the search returned nothing on lighting matches for anime. It repaints the foreground, so it may change a cel character's line and face (inference). SD 1.5 era.
- Change (inference): for layered art, first consider tinting the cut-out in the stage with coloured rim sprites or grading (no AI), and only then a relight, with identity measured (T10).

**C35.** Z-Image has an inpaint pipeline (white is repainted, black preserved), and at strength 1 ignores the image under the mask. Own NOTES warn that inpainting a seam invents objects.
- Source: https://huggingface.co/docs/diffusers/main/en/api/pipelines/z_image | opened | vendor claim | Z-Image-Turbo, diffusers | 2026-11-06
- Limits: nothing on mouth or blink use.
- Change (inference): for variants, composite the masked result over the original so pixels outside the mask are provably unchanged (T9).

**C36.** VNCCS (ComfyUI nodes) builds a body sheet, face set, expression packs and transparent sprites from one reference, using Qwen Image components, SDXL helpers and its own LoRAs. Reports say identity can drift between steps and strong emotions add artifacts; a Face Detailer is the suggested fix. It works best from a single, well-lit image on a plain background.
- Source: https://www.runcomfy.com/comfyui-workflows/comfyui-vnccs-character-workflow-qwen-image-seedvr2 | extract | a host's vendor page for someone else's tool | VNCCS | 2026-11-06
- Limits: no results measured. Licence not stated. Whether its parts permit commercial use is unknown. Qwen-Image 2.1 is research-only per stack research; which Qwen version this uses wasn't confirmed.
- Change (inference): the closest published recipe for sheet-to-sprite. Read the steps; don't install without a dependency review.

**C37.** Mouth shapes, blink frames and per-viseme masks: **no source found.** Searches 12 and 19 returned general expression sheets (Morphic's commercial page, not opened) and nothing else. Coloured rim-light and colour-spill handling: **no source found** either.
- Source: search log | n/a | n/a | 2026-11-06
- Limits: a failed search isn't evidence the technique fails.
- Change (inference): don't write rules here until T8 and T9 have been run.

### Q4. Judging output

**C38.** Aesthetic and CLIP scores predict human preference weakly. Pairwise accuracy, where 50% is chance: LAION aesthetic 55.3% (Picsart), 56.8% (Pick-a-Pic), 72.6% (HPD v2), 57.35% (ImageReward); CLIP alignment 51.9%, 60.8%, 62.5%, 54.82%. On Picsart: PickScore 62.6%, HPS v2 59.4%, ImageReward 60.48%, the authors' own Social Reward 69.7%.
- Source: https://ar5iv.labs.arxiv.org/html/2402.09872 | extract | measured | generated images from several SD-era models | 2026-11-06
- Limits: authors are promoting their own metric, from a company with the dataset. Implicit "remix" behaviour isn't taste. Nothing specific to anime.
- Change (inference): a scorer can't decide between two candidates. Don't filter with it before the owner.

**C39.** LAION's predictor behaves more like a photorealism measure. It kept images with women in the caption more than men or LGBTQ+ ones; on WikiArt, cityscapes, landscapes and portraits are 39% of images but 73% of those at 6.5 or above; on the Met set, almost no African, Oceanian, Native American, Egyptian or Islamic art scored 6.5 or above. Its training data mixed scales and came from a few raters.
- Source: https://arxiv.org/html/2601.09896v3 (FAccT 2026) | extract | measured, with ethnography | LAION-Aesthetics Predictor | 2026-11-06
- Limits: read to 100k of 141k characters. Art datasets, not generated cel art. No cartoon or anime result in what I read.
- Change (inference): expect it to mark flat-colour styles down, and possibly reward sexualised images. Using it could steer against both a flat period look and a project's content rules.

**C40.** A 2026 audit of LAION-Aesthetics, PickScore, ImageReward and HPSv2: edits to skin lightness in either direction lower scores, the same as such edits elsewhere in the image, so the scorers punish fidelity loss rather than a demographic. Bias found on synthetic faces reversed or weakened on 1,470 real faces.
- Source: https://arxiv.org/abs/2608.23593 | extract | measured | those four scorers | 2026-11-06
- Limits: a preprint, one author. Group results mostly not robust after correction.
- Change (inference): it disagrees in emphasis with C39. Either way these measure image cleanness at most, so they may catch a broken image but not a look. An audit on synthetic images alone can mislead, and our checks must be validated on labelled samples.

**C41.** `anime_aesthetic`, a classifier of seven community-score bands, reaches 40.88% accuracy (AUC 0.82), best model.
- Source: https://huggingface.co/deepghs/anime_aesthetic | opened | vendor claim (card's own test) | swinv2pv3_v0_448_ls0.2_x, 2024-03 | 2026-11-06
- Limits: labels likely reflect community score (assumption from the label names; dataset not read). Not validated against art direction.
- Change (inference): can't tell whether a piece meets our brief. Only a test could justify any use (T14).

**C42.** Generic image-quality scores see almost nothing in hands. Correlation with raters: BRISQUE 0.006, NIQE 0.15, HyperIQA 0.49, MUSIQ 0.52, Q-Align 0.52, DeQA-Score 0.55, HandEval 0.67.
- Source: https://arxiv.org/html/2510.08978v1 | extract | measured | 10 text-to-image models, realistic hands | 2026-11-06
- Limits: 100 test images, about 8 raters. The best is still far from solved, and weights aren't confirmed released.
- Change (inference): don't use a generic score as a hand check. Crop and count (C47), and let a person look at hands that matter.

**C43.** Nearly half of generated human images contain distortions. Across SD 3.5, Flux.1-dev, Recraft v3 and Hunyuan, only one model is above 50% undistorted, by the study's reading. A dedicated detector (ViT-HD) got image-level F1 0.884. GPT-4o miscounted a six-fingered hand as five, and Qwen2-VL-7B flagged almost everything. Defects: extra hands, missing fingers, deformed feet, fused body parts.
- Source: https://arxiv.org/html/2503.00811v1 | extract | measured | those models, 500 prompts, 1024 px | 2026-11-06
- Limits: photoreal-leaning. Expert review of 50 images per model agreed with the detector about 80% of the time. About a third of regions had no clear type. The summary's model ranking is inconsistent; check Figure 5. Independent review, at the source, 2026-11-06: the abstract says nearly 50% of images had distortions; its text says only SD 3.5 was above 50% undistorted, by the study's own detector.
- Change (inference): plan for about half of people-images having a defect on the older models, until our own rate is known. Budget review accordingly. Reuse approved cut-outs to reduce exposure.

**C44.** No vision model is both sensitive and calibrated at spotting artifacts. Share of artifact images flagged / false-claim rate on real images (derived in the extract): Gemini 3.1 Pro 99.37 / 49.72; Gemini 3.1 Flash Lite 83.37 / 6.74; Gemma-4-31B 86.32 / 31.74; Claude 4.6 Opus 47.58 / 0.00; GPT-5.4 4.63 / 0.00; most open models below 25. The best model answered all four questions right on just 53.26% of artifact images. Humans scored near 100%.
- Source: https://arxiv.org/html/2606.12671 | extract | measured | 20 named vision models; Imagen 4, Midjourney, FLUX.2 Klein defects | 2026-11-06
- Limits: **photorealistic only; non-photoreal images were removed.** 475 artifact images, multiple choice, single turn. The false-claim rate is on real photographs only. Independent review, at Table 1, 2026-11-06: on generated references with the defect removed (Ref-PG), share rejecting it on every follow-up is Gemini 3.1 Pro 0.00, Flash Lite 0.00, Gemma-4-31B 0.00, Claude 4.6 Opus 0.84, GPT-5.4 20.17, so a 0.00 false-claim figure doesn't carry over to generated images. No anime or cel result. Claude Opus 5.5, the model that wrote this research, is not in the table. Check the figures against the paper's Table 1.
- Change (inference): a clean verdict from a conservative model means little (could miss half or more), and a defect report from a sensitive one means little too. No false-alarm rate here describes generated art, so measure the judge on our art (T13).

**C45.** Two papers disagree on how close vision models are. ArtifactLens: pretrained models need only a few hundred labelled examples per category plus scaffolding, reaching state of the art on five benchmarks. Human Distortion (C43): detection is purely visual and the language part doesn't help. MagicMirror: 340K annotated images, and even GPT-image-1 is reported plagued with artifacts.
- Source: https://arxiv.org/abs/2602.09475, https://arxiv.org/abs/2509.10260 | extract | measured, abstract only | human artifact benchmarks | 2026-11-06
- Limits: abstracts; no figures read for either.
- Change (inference): a few hundred labelled images from our own pipeline may be worth collecting later, and only if the check keeps being needed.

**C46.** Judges favour their own output, shown on text. LLM evaluators scored their own summaries higher than humans judged them, tracking how well they recognise their own text (GPT-4, Llama 2). Where output failed an objective rubric, judges were over 50% more likely to wrongly pass their own. Ensembles reduced it but didn't remove it. Harmful preference persisted when the evaluator was wrong (Qwen2.5-72B 86% on MATH500); longer reasoning reduced it.
- Source: https://arxiv.org/abs/2404.13076, https://arxiv.org/abs/2604.06996, https://arxiv.org/html/2504.03846v3 | extract | measured | LLMs on text; **no image study found** | 2026-11-06
- Limits: text only. Transfer to an agent judging images it prompted is my inference, and that agent also knows the intent, which is a separate bias.
- Change (inference): the agent that wrote the prompt doesn't score the result. The judge gets the image and a defect list, not the prompt, with planted-fault images mixed in. Report the judge's hit and false-alarm rates on the plants beside its verdict (T13). Any rating is bounded by those rates.

**C47.** Anime-specific detectors exist for pre-sorting: hand detection F1 0.75 at the tiny size shown; a face, head, person and eye set in the same family. Licences vary (OpenRAIL, MIT).
- Source: https://huggingface.co/deepghs/anime_hand_detection and live query | opened | vendor claim (card's own test) | deepghs models | 2026-11-06
- Limits: test data not read, probably booru images (assumption); these find a hand, they don't judge it.
- Change (inference): crop hands and faces for the review sheet so the owner spends seconds, not minutes. A detector finding three hands on one character is a cheap flag.

**C48.** Checks that can fail and need no taste (mostly inference, based on own NOTES): near-black or NaN output; size and aspect; alpha coverage and fringe; hue and luminance of a plate against a palette target; duplicate detection by perceptual hash; OCR on any region meant to be blank; face and hand counts; CCIP against master.
- Source: game-assets NOTES (black output, measure hue); the rest inference | inference | any | 2026-11-06
- Limits: none measured here. Each needs a planted fault first.
- Change (inference): this is the "before the owner" list. Output it as flags and ranking, with no overall quality score.

**C49.** Common defect list across sources: count (fingers, limbs), topology (fusion), local render, anatomy, plausibility including physics, reflections, identity and text. Vendor cards add hands and text as known weaknesses on Klein and Animagine. Identity and symmetry drift are covered only by the consistency sources.
- Source: C43, C44 (taxonomy), Klein and Animagine cards | extract | measured and vendor claim | photoreal-leaning | 2026-11-06
- Limits: **cel-specific defects (line weight drift, colour holds, flat areas gone gradient, mixed line styles) appear in no source I read**; that is my own guess at the list.
- Change (inference): keep a project defect list that grows from real rejects. A generic one misses the look.

**C50.** How professionals review: thin evidence. Nexters' art producer describes AI output as a sketch to refine; designers oversee; backgrounds almost never kept as generated; manual work still takes most of the time, by his account. Room 8 tested tools inside a pipeline against quality, control, legal and cost.
- Source: https://gameworldobserver.com/2023/07/31/midjourney-game-development-art-nexters-hero-wars, https://80.lv/articles/room-8-group-analyzed-34-ai-tools-for-2d-game-art-only-2-were-viable | extract | practitioner, partly shipped | Midjourney v5 (2023); unnamed tools (2025) | 2026-11-06
- Limits: self-reports. No search was spent on general art-review practice; `EVIDENCE-DIRECTION.md` covers art direction. **Otherwise unanswered.**
- Change (inference): don't write review-process rules from this alone.

### Q5. Bias and drift

**C51.** Open models default to men on gender-neutral prompts. Average female share 41% in generated images against 52% in matched LAION-400M activities, on 2.29 million images kept from 3.2 million. Occupations polarise strongly.
- Source: https://arxiv.org/html/2503.23398v2 | extract | measured | Flux, Flux-Schnell, SD 3.5 Large and Medium, SD 3 Medium | 2026-11-06
- Limits: binary perceived gender, classified by an LLM. No Klein, Z-Image or anime.
- Change (inference): never leave gender to the model on background characters. Assign the cast's gender in the brief.

**C52.** Direction can flip between models. On four neutral prompts (3,200 images), Gemini Flash 2.5 Image gave 93.7% women and GPT Image 1.5 gave 29.4%. About 96% were classified white in both. Wording matters: GPT's men share was 99.2% for "human being" and 27.5% for "someone".
- Source: https://arxiv.org/html/2602.12133v1 | extract | measured | those models, 2026-01-28 | 2026-11-06
- Limits: single author, v1 preprint, photorealistic prompts only, no explicit diversity prompts. Automated perceived labels.
- Change (inference): measure each model we adopt; don't carry over a general "models favour X". Synonyms for "person" can change the demographics.

**C53.** Skin-tone readings shift with light and colour grading. The audit uses CIELAB with landmark masks and normalisation, and says these reduce but don't remove the problem.
- Source: C52's paper | extract | measured method, effect not quantified | any | 2026-11-06
- Limits: no before-and-after numbers given.
- Change (inference): **under strong coloured light, a skin measure is meaningless.** Measure cast skin tone on the neutral-lit master sheet, and hold that master as the reference for what the character looks like.

**C54.** Eight models: faces aged 20 to 39 exceeded 80% in six, older adults under-represented. Expression shifts demographics: Anger moved the 20-39 share from 80.3% to 40.4%; Disgust moved White from 49.0% to 81.4% and Asian from 26.3% to 2.1%. The young, female and Black intersection was 1.3% against about 5.27% expected, with none in four models.
- Source: https://arxiv.org/html/2602.00032 | extract | measured | FLUX-Schnell, Proteus V0.3, SD 3.5 medium, SANA 1.5, Hunyuan-DiT, Qwen-Image, Kolors, Wan2.1 | 2026-11-06
- Limits: preprint; FairFace labels; read to 100k of 258k characters; prompts were not character-locked. Attractiveness part is less reliable.
- Change (inference): expressions may change who a character seems to be. Check each expression variant against the master for skin tone, age and identity (T9). Generating a character from words per expression is the wrong approach; edit from an approved face.

**C55.** Stable Diffusion 2.1 flagged Latin American, Mexican, Indian and Egyptian women as sexualised more than others on plain prompts, confirmed by manual review. "A person" read as a light-skinned Western man.
- Source: https://arxiv.org/abs/2310.19981 (EMNLP Findings 2023) | extract | measured | SD 2.1, 136 prompts by 50 images | 2026-11-06
- Limits: old model. Non-binary and skin detail only partly in the abstract.
- Change (inference): drift checks must run across the whole cast, because a rate averaged over the cast could hide one character's problem. Compare per character.

**C56.** Anime-style output shows stronger gender imbalance and stereotyping than realistic output across SD 3.5, Illustrious, ChatGPT-5 and Gemini 2.5 Pro.
- Source: https://neurips.cc/virtual/2025/128294 (workshop poster) | extract | measured | those models | 2026-11-06
- Limits: ten occupations; labelling method not stated in the abstract; workshop poster only.
- Change (inference): the only anime-specific bias measure found. It suggests the anime look may need more checking, not less.

**C57.** When an age is stated, photoreal models come close: mean absolute error 3.0 to 5.3 years, correlation 0.96 to 0.99. Offsets are small and mixed in direction (Flux men +2.18, SD 3.5 women -1.10). Errors grow with age, and outliers beyond 11 years run 2 to 10%, by estimator. Elsewhere, diffusion models amplified a young skew in the training data.
- Source: https://arxiv.org/html/2502.03420v1 (extract), https://arxiv.org/abs/2305.06402 (abstract extract; youth point from search 5, not opened) | measured | Flux, SD 3.5, SDXL Epic Realism | 2026-11-06
- Limits: **photoreal only, using photo-trained estimators**, and estimator and generator error aren't separated. Its dataset includes young prompted ages, which an art pipeline shouldn't copy.
- Change (inference): stating an age in words is likely useful, not sufficient. Anime proportions can undo it (unmeasured). Don't use these age estimators on anime.

**C58.** "Adults drawn younger in anime": **no measurement found.** Searches 4, 5 and 16 asked directly and returned nothing on it.
- Source: search log | n/a | n/a | 2026-11-06
- Limits: absence of a study. The claim may well be true; no number supports it.
- Change (inference): don't quote any rate. A project's binding rule on clearly adult characters still stands, and is enforced by design choices (C60) and human review.

**C59.** Explicit prompts don't reliably defeat stereotype: counter-stereotype requests and vendor guardrails left stereotypes in place.
- Source: https://arxiv.org/abs/2211.03759 | extract, abstract | measured; recalled URL | models not named in the abstract read; paper dated 2022 to 2023 | 2026-11-06
- Limits: 2022 to 2023, old models. Effect sizes not read. Newer prose models may hold descriptors better: unknown.
- Change (inference): test descriptor-holding per model (T11). The robust path is to lock an approved master sheet per character and reuse it, rather than re-describe people in every prompt.

**C60.** What works for a diverse, clearly adult cast: **no study compares methods on stylised models.** From C51 to C59, my inference is: assign demographics per character in writing; approve a neutral-lit master; edit from it; adult markers in the design itself (proportions, facial structure, wrinkles or grey where fitting, clothing, occupation); human sign-off per character before any scene; never generate a character "young" and then "fix" it.
- Source: inference from C51 to C59 | inference | any | 2026-11-06
- Limits: untested.
- Change (inference): consistency and bias control become the same job: fewer fresh generations of people.

**C61.** `anime_ch_skin_color`, 4 classes: accuracy 79.26%. `dark` recall 88.0%, precision 86.7%; `pale` recall only 60.7% (250 of 840 called `light`).
- Source: https://huggingface.co/deepghs/anime_ch_skin_color (card and confusion plot; arithmetic mine) | opened | vendor claim (card's own test) | `caformer_s36`, 2023-06, MIT | 2026-11-06
- Limits: dataset not read, probably booru-labelled art (assumption), not generated, not under coloured light. Four bins can't represent a range of skin tones.
- Change (inference): a rough cast-sheet check that a dark-skinned character didn't lighten. Not a measure of diversity.

**C62.** `anime_teen`, three classes (`contentious`, `safe_teen`, `non_teen`): accuracy 77.97%. Of 1,319 images labelled teen or contentious, 220 (16.7%) were passed as `non_teen`; of 1,037 `non_teen`, 207 (20.0%) were flagged. Predicted `non_teen` is right 79.0% of the time.
- Source: https://huggingface.co/deepghs/anime_teen (card and confusion plot; arithmetic mine), https://dghs-imgutils.deepghs.org/main/api_doc/validate/teen.html (extract) | opened | vendor claim (card's own test) | `caformer_s36_v0`, 2023-08, MIT | 2026-11-06
- Limits: **labels aren't defined in the docs, and the dataset card wasn't reachable (returned an auth error).** Not tested on generated art. By label (independent review, at the confusion plot, 2026-11-06): safe_teen 26.9% passed, contentious 9.8%; imgutils defaults to the weaker `mobilenetv3_v0_dist`. About one in six missed, so it **cannot be an automated pass** for a binding rule.
- Change (inference): at most a flag that sends an image to the owner sooner. An image passing it hasn't been shown to be clearly adult. See the safety note in T12.

**C63.** Safety classifiers on sexual content, F1 on real / AI-generated: GPT-4V 0.866 / 0.827; LLaVA 0.674 / 0.866; SD_Filter 0.833 / 0.727; MultiHeaded 0.692 / 0.815; NSFW_Detector 0.783 / 0.678; NudeNet 0.650 / 0.596. **Artistic rendering of nudity is often classed safe**; accuracy falls as artistic strength rises.
- Source: https://arxiv.org/html/2405.03486v3 (UnsafeBench) | extract | measured | classifiers on LAION-5B and Lexica (mostly SD) | 2026-11-06
- Limits: borderline-by-design samples; author labels, kappa 0.697; no false-positive rates for sexual content; no anime. VLM results vary by prompt. GPT-4V about $20 per 1K images.
- Change (inference): don't rely on photo-trained detectors on cel. Stylisation is the known weak spot.

**C64.** NudeNet false negatives of 4.4% to 14.4% on jailbroken generated images, often on low quality or small parts. Its developer claims over 90% on real photos.
- Source: https://arxiv.org/pdf/2504.05838 | not opened | measured, reported in search summary | NudeNet | 2026-11-06
- Limits: adversarial setting, not ordinary drift.
- Change (inference): another reason not to treat it as a gate.

**C65.** Anime-trained ratings are noisier than they look but have useful edges. `anime_rating`'s card says there's no objective ground truth for safe, r15, r18 and that keypoint detection is better for accurate R18 work. `anime_dbrating` 4 classes (best model 84.16%): `explicit` read as `general` or `sensitive` 0.4% of the time (225 of 55,675); `questionable` read as those 10% (6,357 of 63,884); `sensitive` read as `general` about 18% (arithmetic mine; diagonal shown rounded). `anime_censor_detection` F1 0.80 to 0.83 at the sizes shown (labels `nipple_f`, `penis`, `pussy`).
- Source: https://huggingface.co/deepghs/anime_rating, https://huggingface.co/deepghs/anime_dbrating (swinv2pv3_v0_ls0.2), https://huggingface.co/deepghs/anime_censor_detection | opened | vendor claim (cards' own tests) | 2024 versions | 2026-11-06
- Limits: Danbooru-style user ratings, not generated art, and no coloured light. Licences differ.
- Change (inference): gross nudity may be catchable; **the likely drift, gradual sexualisation in `sensitive` territory, is where these are weakest.** Tags (C66) may help. Keep a person looking at the whole cast's sheets at intervals.

**C66.** WD taggers give ratings and general and character tags from anime images, trained on Danbooru. Apache-2.0; tags to 2024-02-28; F1 0.4772 at threshold 0.5296 for the v1.0 EVA02 large.
- Source: https://huggingface.co/SmilingWolf/wd-eva02-large-tagger-v3 | extract | vendor claim | wd-eva02-large-tagger-v3 | 2026-11-06
- Limits: tag vocabulary is booru and can itself be sexualised; a tag isn't a judgement. Precision per tag not read.
- Change (inference): a plausible drift detector: count clothing and framing tags (`cleavage`, `midriff`, close crops) per character over time, and compare against that character's master. Trend across the batch, not a per-image verdict. To test, T12.

**C67.** No benchmark targets gradual sexualisation drift in text-to-image output. Searches 6 and 16 asked and found none.
- Source: search log | n/a | n/a | 2026-11-06
- Limits: absence of a study.
- Change (inference): this needs a homegrown measure and a human.

### Q6. Provenance and rights (not legal advice)

**C68.** US Copyright Office, Part 2 (January 2025): AI used to assist doesn't affect protection; purely AI-generated material isn't protected; sufficiency is case by case; prompts alone don't give enough control under current general technology. Repeated revision doesn't change that: effort is irrelevant, and it describes re-rolling and accepting the system's interpretation. Humans are entitled to their authorship that is perceptible in outputs, to creative selection, coordination or arrangement, and to creative modifications.
- Source: https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-2-Copyrightability-Report.pdf (conclusions, sections on prompts and modifications) | opened | agency position | any | 2026-11-06
- Limits: the Office's view, not a court ruling. US only. The Office said it would give further registration guidance; none newer is listed on https://www.copyright.gov/ai/ (extract).
- Change (inference): tell the owner plainly that individual generated images likely have no protection on their own. The project's protectable material is writing, arrangement, hand edits and any human art used as input. Keep records of these (C74).

**C69.** Zarya of the Dawn, a comic, is the closest precedent. Registration covers the text and the selection and arrangement of images and text, not the Midjourney images. Selecting two or three elements isn't generally enough. A film with AI effects or backgrounds is copyrightable as a whole even if they aren't.
- Source: Part 2 report as C68, https://www.copyright.gov/docs/zarya-of-the-dawn.pdf (cited there, not opened itself) | opened (report) | agency position | Midjourney, 2023 | 2026-11-06
- Limits: registration decision, not a ruling. A layered, animated work may differ.
- Change (inference): record the panel-level sequencing and layout decisions as the owner's. That fits any work built from sequenced panels.

**C70.** Thaler v. Perlmutter: D.C. Circuit held in March 2025 that authors must be human; certiorari was denied 2026-03-02. It didn't decide how much human input suffices. Allen v. Perlmutter (D. Colo.): over 600 Midjourney prompts plus Photoshop; summary judgment was fully briefed and pending at 2026-06-01. The government says he could have registered his Photoshop contribution with the AI parts disclaimed. Suryast v. Perlmutter (C.D. Cal., filed 2026-05-08): refusal for an AI style applied to the applicant's own photograph.
- Source: https://www.bakerdonelson.com/supreme-court-denies-certiorari-in-thaler-v-perlmutter-ai-cannot-be-an-author-under-the-copyright-act, https://ipandmedialaw.fkks.com/post/102mycg/copyrighting-ai-and-art-recent-cases-ask-courts-to-draw-the-line (2026-06-01) | extract | secondary, law firms | n/a | 2026-11-06
- Limits: **no check after 2026-06-01; five months stale.** Check the Colorado docket before relying on this.
- Change (inference): the law on prompt-heavy work could move soon. Note the date beside any statement made to a third party.

**C71.** Part 3 (pre-publication, May 2025): copyright generally doesn't protect style, though some replication of "style" may capture protected expression. Output imitating a creator's style counts in the fair use market-harm discussion. It cites "in the style of" prompting and the Ghibli episode, and notes some vendors' system prompts refuse to imitate living artists.
- Source: https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-3-Generative-AI-Training-Report-Pre-Publication-Version.pdf | opened (passages found by search on "style") | agency position | any | 2026-11-06
- Limits: pre-publication; concerns training analysis. Trademark, publicity and foreign law not read. Suits against generators weren't searched.
- Change (inference): supports a deny-list of named artists, shows and studios as a reputational and risk choice, not a statement that style is unlawful. Describe the look's traits (materials and process) rather than naming sources.

**C72.** Licence traps found: the stack research lists NoobAI (tag FAIPL, card bans commercial), Qwen-Image 2.1 (research only; a repackager tags apache-2.0), Klein 9B and FLUX.1 dev (non-commercial), revenue thresholds on Krea 2 and FLUX 3 Klein, Anima (non-commercial). New here: Anima-RGBA (C33), VNCCS parts (C36), CorridorKey (C32), `other` tags in the live list.
- Source: the stack research, licence section (not kept), C33, C32, live query | opened | vendor terms | as named | 2026-11-06
- Limits: tags in the live list not checked. Not legal advice.
- Change (inference): check base model licence through every link of the chain, per image, from the record.

**C73.** Steam: disclosure covers generative AI in content that ships and is consumed by players, plus store-page and marketing assets, split into pre-generated and live-generated. Developers write a statement shown on the store page. Efficiency tools like code helpers are out of scope. Changed January 2026, disclosure in place since January 2024.
- Source: https://www.gamingonlinux.com/2026/01/valve-tweak-steam-ai-disclosure-form-for-developers-to-clarify-its-for-content-consumed-by-players/ (extract), https://games.slashdot.org/story/26/01/19/1735231/valve-has-significantly-rewritten-steams-rules-for-how-developers-must-disclose-ai-use (extract), https://videogameschronicle.com/news/epic-games-ceo-says-its-really-irresponsible-of-steam-to-make-studios-disclose-ai-use (extract) | secondary, quoting Valve's form | Steam | 2026-11-06
- Limits: Valve's own post returned navigation only: https://store.steampowered.com/news/group/4145017/view/3862463747997849618. Read the Steamworks form before filing. Independent review, at the source, 2026-11-06: https://partner.steamgames.com/doc/gettingstarted/contentsurvey covers content that ships and players consume; store-page coverage is the secondary report's reading.
- Change (inference): every shipped generated image counts for disclosure, placeholders included. Generate the statement's facts from the manifest.

**C74.** Provenance record for each image (my inference, from C13, C18, C33, C68, C70, C73, C75): asset id; role and placeholder status; full prompt, negative and references with their own ids and licences; seed and generator device; output SHA-256; model, VAE, encoder and LoRA names, revisions, SHA-256 and strengths; sampler, scheduler, steps, each guidance parameter by name; size; tool version and workflow JSON; for APIs the model ID, date and terms snapshot; matte tool and version; every human edit and who made it; who selected it, when, from how many; licence-text hash; disclosure class; IPTC source type.
- Source: inference; game-assets covers the manifest, this extends it | inference | any | 2026-11-06
- Limits: not a legal standard. ComfyUI's embedded PNG data may not survive matte or upscale (T18).
- Change (inference): write it at generation time, in a sidecar, so credits and disclosure are generated (ground-truth rule 5).

**C75.** IPTC's marker is Digital Source Type `trainedAlgorithmicMedia`, embeddable in XMP or a C2PA manifest; `compositeSynthetic` covers composites with camera material.
- Source: https://iptc.org/news/iptc-publishes-metadata-guidance-for-ai-generated-synthetic-media/ | extract | standards body; recalled URL | any | 2026-11-06
- Limits: the page points to a user guide I didn't read. Whether games need this at all is unknown.
- Change (inference): low-cost and optional; a single field if exports go beyond the store.

**C76.** EU AI Act Article 50, by the site's text, applies from 2026-08-02: providers mark synthetic output machine-readably; deployers disclose deep fakes, with a lighter duty for evidently artistic or fictional work.
- Source: https://artificialintelligenceact.eu/article/50/ | extract | law, third-party site; recalled URL | any | 2026-11-06
- Limits: **the page links a Digital Omnibus and carries an amendment marker; I couldn't verify the current timing.** Who counts as provider when running open weights locally: not read. Not legal advice.
- Change (inference): a question for a lawyer before any EU release. Keep metadata (C75) in the record in case.

**C77.** Other stores, per an academic overview: itch.io has a searchable AI tag and doesn't require it; Epic, GOG, Nintendo, PlayStation, Xbox and mobile stores have no clear AI disclosure. Steam's disclosure is free text, not a filterable tag, and SteamDB counts over 15,000 titles.
- Source: https://stuff.co.za/2026/02/12/are-video-game-developers-using-ai-players-want-to-know-but-the-rules-are-patchy/ (The Conversation, republished) | extract | secondary | February 2026 | 2026-11-06
- Limits: nine months old; store terms not read directly. Other pages' "one in five" share is unverified.
- Change (inference): re-check per store at release. Consider disclosing voluntarily where nothing is required, given C78.

**C78.** Clair Obscur: Expedition 33 lost Game of the Year and Debut Game at the Indie Game Awards in December 2025. The awards bar any generative AI in development; the studio had said none was used; AI textures, described as placeholders, had shipped and were patched out; patching didn't save the awards. It had been flagged publicly since April 2025.
- Source: https://www.engadget.com/gaming/the-indie-game-awards-snatches-back-two-trophies-from-clair-obscur-over-its-use-of-generative-ai-164730842.html | extract | shipped case, news | 2025 | 2026-11-06
- Limits: one awards body's rule. It says nothing about sales.
- Change (inference): placeholders are generated art. The manifest's placeholder list must be empty, or disclosed, at release. Check each award's or event's rules before entering.

**C79.** Other cases named: Jurassic World Evolution 3 removed AI portraits after fan backlash; Activision admitted AI assets in Black Ops 6; The Nameless City replaced its AI content with human work after release, in a published devlog. Also the reverse: developers accused of using AI on human-made art. A search summary says Larian drew backlash after confirming generative AI in early concept exploration, about a week before Valve's January 2026 rewrite; no primary report was opened.
- Source: C77's article (extract), https://itch.io/devlog/663959/why-and-how-we-used-ai-generative-tools.amp (extract), https://www.comicsbeat.com/indie-game-awards-rescind-clair-obscur-expedition-33s-wins-for-gen-ai-use and search 8 summary (not opened) | shipped cases, secondary | as named | 2026-11-06
- Limits: secondary; no effect sizes.
- Change (inference): keep the ability to swap any image (game-assets already arranges this). Portraits and character art draw notice.

**C80.** Player surveys disagree. Circana (US, December 2025): just over 25% less likely to buy, up from about 22%; over 50% neutral; under 10% more interested. GameDiscover (about 3,800 Steam users, reported July 2026): 8% wouldn't buy under any circumstance; 31% negative by search summary. MIDiA (end of 2024, n=6,300): 60% neutral if the game is good, 20% positive, 19% negative. Quantic Foundry (December 2025, n=1,799): 85% below neutral, 63% most negative.
- Source: https://thegeek.games/?p=126020, https://respawn.outlookindia.com/gaming/gaming-news/do-gamers-care-about-genai-new-data-reveals-a-silent-majority, https://www.gamereactor.eu/?p=126292, https://www.midiaresearch.com/blog/new-research-what-do-gamers-really-think-about-generative-ai-in-games, https://pixelpnl.beehiiv.com/p/pixel-p-l-85-of-gamers-reject-generative-ai-in-video-games-survey-finds | extract | measured surveys, all reported second-hand | n/a | 2026-11-06
- Limits: different wording, samples and recruitment. Quantic's sample reported as self-selected (search summary only). All stated attitudes; **no study measures a disclosure's effect on sales.** A claim that controversy didn't hurt sales (Gamereactor) is unsourced.
- Change (inference): plan for a vocal minority and an indifferent middle, and don't let either number decide the plan. A project's own audience may differ from any of these.

**C81.** Epic's CEO calls Valve's disclosure irresponsible: to him it stigmatises a game and invites attacks.
- Source: VGC, as C73 (2026-06-25) | extract | vendor opinion, from a store competitor | n/a | 2026-11-06
- Limits: opinion, from a rival store.
- Change (inference): none for rules. Shows the disclosure question is contested, not settled.

### Q7. Cost and throughput

**C82.** Nexters on Hero Wars: a pack of 10 images takes about 400 prompts and variations, 4 to 5 hours, against weeks per artwork earlier. Effort on characters fell 40% with Midjourney v5. Manual work still takes most of the time for AI-assisted parts. Animation and UI slicing aren't suited.
- Source: https://gameworldobserver.com/2023/07/31/midjourney-game-development-art-nexters-hero-wars | extract | practitioner, shipped game | Midjourney v5, 2023 | 2026-11-06
- Limits: self-report from an art producer. The images' use wasn't stated in what I read; not a consistent comic. 2023 tools.
- Change (inference): about 40 tries per delivered image is the most concrete professional figure I found. Even at that rate most of the time wasn't generation.

**C83.** Room 8 tried 34 tools for 2D game art: 4 had potential, 2 were viable; no tool made game-ready art by itself. It reports 30 to 50% saved on character illustration and over 40% on environment concepts. GenAI wasn't suited to polish.
- Source: https://80.lv/articles/room-8-group-analyzed-34-ai-tools-for-2d-game-art-only-2-were-viable (2025-03-11) | extract | practitioner, studio's own article | tools unnamed | 2026-11-06
- Limits: self-report, tools unnamed, licence and privacy weighed heavily in screening.
- Change (inference): plan human or scripted finishing, and don't assume the last step comes from the generator.

**C84.** Tries per kept image, weakest evidence: Magnific's blog, about 4 generations per kept image over Feb to Aug 2026 (a median 6 per download per user, over 1,085,259 users); a game dev, 10 to 20 per image; one poster, 50 to 100 on Midjourney and Flux.
- Source: https://www.magnific.com/blog/cost-of-a-kept-image/ (403), https://www.moddb.com/news/button-and-portrait (403), RPGdesign post on a dead mirror | **not opened**, search summary only | vendor claim; practitioner | general use | 2026-11-06
- Limits: "kept" means different things. The vendor's 4 is general consumer use, not a consistent production bar.
- Change (inference): expect 4 at a loose bar and 40 or more at a consistent bar, until our keeper rate is known (T16). Don't promise a number.

**C85.** Where time went in published reports: consistency across tilesets, enemies and UI; replacing old art when a model's style shifted; reworking backgrounds; animation. Reference-sheet "bible" fed into every generation: tedious but works.
- Source: https://reddit.sentinel-team.org/posts/1sf8r2b/snapshots/2026-04-09T20%3A33%3A34.459213Z (extract), C82 | practitioner | mostly hosted tools | 2026-11-06
- Limits: the thread's opener appears to represent a tool vendor (name inference). **No quantified time-wasted figure found in any shipped-work report.**
- Change (inference): pin model and revision on day one. A silent model change forces rework (stack research on pinning).

**C86.** Batch-then-select versus careful single prompts: no study compares them. Evidence around it: distilled models give batches cheaply (FLUX schnell 6 s at 1024 px, measured in the stack research), Turbo varies less (C5), Base varies identity more (C6), the owner's attention is the real bottleneck (ground-truth rule 10).
- Source: inference from C5, C6, the stack research (not kept) | inference | Z-Image family, FLUX schnell | 2026-11-06
- Limits: no measurement.
- Change (inference): explore with prose changes and small batches; when a direction is liked, spend seeds. Report cost per owner-approved image, measured against owner minutes, not GPU minutes alone (T16).

## Where sources disagree

1. **Native alpha or matting.** LayerDiffuse: users preferred native 97% of the time (2024). Anima-RGBA's own card: hair, glass and smoke weakest, alpha mostly binary. BiRefNet Matting is aimed at those very areas. Nobody tests anime under strong coloured light. T8.
2. **Which metric for anime identity.** ViStoryBench's pages say CLIP while a search summary says CCIP; SerialGen still uses ArcFace on anime (not opened); StyleID says photo encoders are brittle. T6.
3. **Is a vision model a usable artifact judge.** ArtifactLens says yes with scaffolding; Human Distortion says the language part doesn't help; SalArt-VQA shows a trade-off between missing and inventing. All photoreal-only. T13.
4. **Which demographic the default favours.** Girrbach: men on open models. Balestri: 93.7% women on Gemini Flash 2.5, 70.6% men on GPT Image 1.5. Also varies with the word chosen for "person". Measure per model.
5. **What aesthetic scorers measure.** Taylor: photorealism and a Western male gaze. Xu: mainly a preference for unedited fidelity, group effects not robust. TU Delft thesis (not opened): partly aligned with human liking. HPD v2 shows 72.6% accuracy for LAION against 55.3% on Picsart, a large gap by dataset.
6. **Negative prompts on distilled models.** diffusers: ignored. Z-Anime card: limited effect at CFG 1 to 1.5. A practitioner guide advises using them on Klein. T2 settles it for our tools.
7. **Z-Image for character LoRA.** Strongest base for likeness (one poster), outfit lock and drift (another), a seller's page says Base is safer, a Turbo LoRA portability failure. T15.
8. **Tries per kept image.** 4 (vendor), 10 to 20, 40 (Nexters), 50 to 100. Different bars, different eras. T16.
9. **Player opposition.** 8% refuse (GameDiscover), about 25% less likely (Circana), 19% negative (MIDiA), 85% negative (Quantic). Sample and wording account for much of it.
10. **Case-by-case in principle or refusal in practice.** The Office says human selection and creative input count; critics say any AI in the expressive elements defeats registration in practice, and Suryast challenges a refusal on the applicant's own photograph. Courts haven't settled it.
11. **Age from words.** Photoreal models follow a stated age closely (C57); explicit counter-stereotype prompts left stereotypes in place (C59); older models, different attribute. Unknown on anime.
12. **Dataset size.** 8 to 20 up to 150 to 400. Different models, goals and tagging effort.

## Common advice that's unsupported

Status given as of what was searched. "Unsupported" means I found no measurement, not that it's false.

- **"Use the same seed to keep a character."** No source measured it. Docs treat seeds as reproducibility only (C13). Search 18 returned nothing on it. Z-Image base's maker says identity varies across seeds, and nothing says it holds across prompts. T3.
- **"Add `bad hands, extra fingers` to the negative."** Recommended by cards; no measurement of a reduction found. Mechanically nothing on distilled models (C2, C5), and about one miss in five even where negatives work, on SD 2 (C12).
- **"`masterpiece, best quality` improves images."** Animagine says its score tags work; no independent test. Nothing suggests it transfers to prose models, whose makers advise against keyword lists.
- **"Filter with an aesthetic or CLIP score."** Near-chance on the most realistic data (C38), biased towards photorealism (C39). Negative evidence, not just absence.
- **"Face similarity above a threshold means same character."** Photo encoders are unreliable on stylised faces (C22), and no threshold was validated on anime.
- **"Ask a vision model whether the hands are right."** On photoreal tests, conservative models miss most artifacts and sensitive ones invent them (C44, C43).
- **"Vendor says improved character consistency."** Qwen, Morphic, Gemini and similar: no benchmark shown (C19).
- **"Lots of prompts means I own it."** The Office says no (C68). Allen could change that.
- **"Placeholders don't count."** They counted in C78.
- **"A licence tag settles it."** It doesn't (C33, C72).
- **"Long, detailed prompts are better."** BFL recommends detail, but no test seen; own NOTES show framing lost when a CLIP prompt grew too long.
- **"Adults are drawn younger in anime by X%."** No number found (C58). The rule is worth keeping; the figure isn't known.
- **"An NSFW classifier keeps it clean."** NudeNet F1 0.596 on generated images, and art styles evade detectors (C63).

## To test on our own machine

T1 to T20, with the runnable steps, are in `NOTES.md` beside this file. **Nothing there has been run.**

## Search log (20 of 20)

1. FLUX.2 klein prompting guide, negative, guidance. 2. Z-Image Turbo LoRA, dataset, captioning. 3. LAION aesthetic predictor reliability. 4. Measured bias by gender, race, age, skin tone, anime younger. 5. Age bias, anime neoteny, age estimation. 6. Sexualisation, NudeNet error rate, anime NSFW. 7. Copyright Office, Allen, Thaler. 8. Steam disclosure, Clair Obscur, reception. 9. Vision models judging defects. 10. Face embedding on anime, consistency benchmark. 11. BiRefNet, RMBG, BEN2 on anime and rim light. 12. Native-alpha, LayerDiffuse, relight (only LayerDiffuse returned). 13. Clair Obscur, Larian, player surveys. 14. Generations per usable image, postmortems. 15. Player survey percentages, disclosure effect on sales. 16. Sexualisation in anime, childlike adult detection. 17. Style LoRA on own art, caption comparisons. 18. Negative prompts studies, same seed consistency. 19. Mouth and blink variants, relighting cut-outs. 20. LLM self-preference.

Failed fetches: docs.bfl.ai/guides/prompting_guide_flux2_klein, help.bfl.ai article 8642316687 (both 404); magnific.com, moddb.com, medium.com (403); redlib.hackliberty.org (DNS); runcomfy trainer article (no body); store.steampowered.com post (navigation only); Defold forum thread (links out, no figures); dataset card deepghs/anime_teen (auth error); arxiv.org/pdf/2402.09872 (too large; used ar5iv).

Not done for lack of budget: general art-review practice; Disney and other suits against generators; Allen after June 2026; Digital Omnibus effect on Article 50; independent tests of Gemini or Klein reference consistency.
