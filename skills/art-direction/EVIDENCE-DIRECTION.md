<!-- Research notes from 2026-11-06, edited into citable form the same day. Rules are in SKILL.md. Editing changed no claim number, kind, status mark
or limit. It generalised inference lines written about one project, turned quoted source wording into paraphrase, dropped one artist's name from a
tutorial that imitates that artist, moved the owner's questions to SKILL.md, and added one editor's check at #60. Corrections an independent review made at the source on 2026-11-06, at #59 and #60, are marked as such. "I" and "my" mean the
research author. Cite an entry as [#12]. -->

# Art direction, visual storytelling and panel critique: evidence file

Collected 2026-11-06. No rules or skill text here. Findings are meant to hold for comics, visual novels and game art, and say
so where they depend on the form. Period and genre entries are about those periods and genres, not a target look.

## How to read this file

**Search budget:** all 20 searches were spent (list at the end). Later reading only followed URLs found by those
searches, or links on pages I had opened. Where the budget ran out, the question says so.

**Status of each source**
- `opened`: I downloaded the raw page text and read the cited passage myself. Not a claim that I read every page
  of a long paper. Source wording has since been paraphrased; what stays in quotation marks is a term, a title or this file's own wording.
- `extract`: seen through a summarising fetch. **In practice no claim uses this status.** All five WebFetch calls
  returned 403, so everything I read went through raw download.
- `not opened`: known only from the search tool's summary of the result, or a page that blocked me. The search tool
  itself summarises, so treat these as leads with paraphrased content. Never a checked quote.

**Kinds**
- `practitioner`: someone who does the work, speaking about it.
- `demonstrated`: a work that does the thing. This shows it can be done, not that it caused success.
- `measured`: an experiment or corpus result.
- `critic/scholar`: added as a fifth label. Interpretive argument by a non-practitioner. Merging these into
  "practitioner" would overstate them.
- `inference`: mine. Every "Would change" line is inference, as requested.

**Corroboration** counts independent sources within this pass only. "None here" means I found none in the budget,
not that none exists. Craft advice is rated by the source's standing and agreement, and that is not evidence it
works.

**Entries headed GAP** are not claims. They record that a sub-question has no source here, what the search returned,
and any reasoning of mine, which is `inference` throughout. The claim fields don't apply to them.

**Second-hand warnings that recur**
- The Makko post (#28, #29) is a vendor blog selling a generated-art constraint product. It quotes four public art
  bibles. I did not open the bibles themselves, so those quotes are second-hand.
- Hintze et al. (#62) was not opened. The Elsevier link only redirected. I read two reports of it.
- Valve's material dates from 2007-08, and is written for a multiplayer shooter at speed. A still panel has no such
  time pressure.

---

## Numbered claims

### Q1. Composition and reading a panel

**1. The eye jumps. It does not flow along lines, though salient items reliably catch it.**
Beelders & Bergh 2020, J. Eye Movement Research, three landscape paintings analysed in depth, each with a known
intended compositional line, convenience sample n=65, free viewing. Above roughly 50% similarity on *where* people looked, low
similarity on *order*; a random path showed the same pattern. The authors conclude standout elements work and
guiding elements less so, and say they cannot yet separate composition from plain bottom-up selection.
https://pmc.ncbi.nlm.nih.gov/articles/PMC7963460/ . `opened`. `measured`.
Corroboration: #2 partly contradicts on lines; #3 agrees; the same paper's background section cites Buswell 1935 and a
further study finding focal points worked while entry and exit points and the compositional line did not.
Limits: three paintings picked because they had a clear intended line, one genre, convenience sample, no comics, no
story task.
Would change (inference): review should ask "what do people land on" and stop asking whether a line "leads the eye
to" something. Don't accept a leading line as the fix for a focal point nobody hits.

**2. Against #1: saccades do align with composition lines when the composition is clear.**
Sancarlo, Dare, Arato, Rosenberg 2020, J. Eye Movement Research 13(2):7. Fourteen Last Supper pictures across four
centuries; 40 participants, 8 excluded, 32 analysed. Saccades between viewers were more alike than chance on all fourteen; participants' drawn
composition lines also agreed; saccades matched the drawn lines on twelve of fourteen, most on the clearest
compositions. The authors note Garbutt & Spehar 2014 and Kirtley 2018 found no sequential, linear path.
https://bop.unibe.ch/JEMR/article/download/JEMR.13.2.7/10079/26653 . `opened`. `measured`.
Corroboration: partial, see "Where practitioners disagree". Limits: one subject with a known horizontal structure of
heads and table; many saccades simply ran along the row of faces; all participants female students familiar with
composition, by design. Direction alignment is not a path followed in order.
Would change (inference): rows of faces and strong axes give direction of scanning; don't expect them to set an
order. Clearer structure means viewers agree more, which is a usable target even if "the path" isn't.

**3. Faces draw attention wherever you put them; placement on a golden-section line alone doesn't.**
James Gurney (illustrator, Dinotopia), 2009, an informal eye-tracking demo with Eyetools on his own painting. His
conclusions: the eye leaps and doesn't follow contours; golden-section placement doesn't by itself draw attention; a
face gathers attention wherever placed; two people don't scan along the same route but share a strategy of
alternating context and detail. Three faces, including a dinosaur's, took nearly everyone's attention within five seconds.
https://gurneyjourney.blogspot.com/2009/09/eye-tracking-and-composition-part-3.html . `opened`.
`practitioner` reporting informal `measured`. Corroboration: agrees with #1 on leaps and order. Limits: one painting,
small unreported sample, vendor demo, no statistics in the post.
Would change (inference): every face in a panel is a claimed focal point. A crowd scene needs its background faces
dimmed, turned away or cropped, or they'll compete with the speaker. Don't spend a note on thirds placement.

**4. Readers navigate comic pages mainly by panel borders, and content decides ambiguous cases.**
Kirtley, Murray, Vaughan, Tatler 2022, Applied Cognitive Psychology, eye tracking. Six layout variations; external
structure replicated as the major cue; text location mattered for one layout; panel content was a consistent effect
across variations of that ambiguous layout.
https://discovery.dundee.ac.uk/en/publications/navigating-the-narrative-an-eye-tracking-study-of-readers-strateg/ .
`opened` (abstract only). `measured`. Corroboration: #5. Limits: abstract only, sample size not seen; page layouts,
not single panels.
Would change (inference): applies to page or screen-with-several-panels forms. For a full-frame panel sequence this
question largely disappears, and the reading order inside a panel falls to faces and speech. Text location is a real
order cue.

**5. Reading order is partly learned. Experienced readers and manga readers differ from novices.**
Cohn 2013, Frontiers in Psychology, 145 participants at a 2004 convention numbered blank panels in 12 pages. Readers
preferred the blockage path over the Z-path; manga reading reduced left-to-right entry; older participants preferred
left-to-right more. Cohn & Campbell 2015 extended this with manipulated layouts. The same paper cites Omori et al. 2004: changing layouts
changed eye movements but did not appear to significantly change comprehension, and argues layout and content are
independent structures, which cuts against craft claims that layout carries meaning.
https://pmc.ncbi.nlm.nih.gov/articles/PMC3629985/ (`opened`); https://www.aip.org/inside-science/the-visual-language-of-comics
(`opened`, a press report); Navigating Comics II https://research.tilburguniversity.edu/en/publications/navigating-comics-ii-constraints-on-the-reading-order-of-comic-pa/ (`not opened`).
`measured`. Corroboration: Omori et al. 2004 eye tracking, as cited by Cohn, found readers skipping blockage panels; Cohn
attributes the contrast to expertise, which is his interpretation. Limits: blank panels, self-reported expertise,
convention sample skewed towards readers, numbering task rather than natural reading.
Would change (inference): don't assume a player reads panels the way a comics reader does. The owner, if a comics
reader, is a poor test of novice reading order.

**6. Story order changes where people look and how fast they understand.**
Foulsham, Wybrow, Cohn 2016, Applied Cognitive Psychology 30(4). Eye tracking on comic strips, panels one at a time and
all together. In original order, pictures were understood faster with fewer fixations; randomised, they took more
attention and more regressions. Fixation distributions differed, so context affects where people look.
https://repository.essex.ac.uk/16471/ . `opened` (abstract). `measured`. Corroboration: consistent with Cohn's broader programme,
not checked further. Limits: wordless strips; abstract only.
Would change (inference): judge a panel in sequence as well as alone. A panel that looks unfocused alone may read
fine after its predecessor, and the reverse. Review contact sheets, not only single frames. Hold shorter once context does
the work.

**7. Eye level is the fastest shot to grasp, and an establishing shot should say where we are.**
Jim Shooter (Marvel editor-in-chief from 1978, per his own site), edited transcript of a 1994 seminar, Storytelling Lecture parts 9-11. Eye level
is the most common view and easiest to read at once; a shot should be clear at a glance; he notes a Kirby panel forced
to do two jobs because of a panel budget, and a colourist error that made the character harder to find. Introduce who, what, when, where.
https://jimshooter.com/category/04-storytelling-lecture/page/2/?order=asc and https://jimshooter.com/category/04-storytelling-lecture/?order=asc .
`opened`. `practitioner`, high standing in US comics. Corroboration: #8 for clarity-first. Limits: single-tradition, superhero
newsstand comics, one man's view; I read parts through category pages, not every lecture.
Would change (inference): helpful news for first person, which is eye level by default. It also suggests the opposite problem:
eye-level clarity is the default, so dramatic angles have to be chosen for a reason (see #14 monotony).

**8. Silhouette first, then interior shapes in shadow; test with no interior detail at all.**
Valve: Mitchell, Francke, Eng 2007, Illustrative Rendering in Team Fortress 2 (NPAR); Mitchell, GDC 2008 slides;
Francke & Lundeen, Gamefest 2008 talk. Characters were validated at concept phase in silhouette with no internal shading. Character steps: silhouette,
interior shapes solved with shadow shapes, model sheet, model, skin, in-game. Value patterns accentuate internal shape.
https://www.cs.princeton.edu/courses/archive/fall07/cos597B/papers/mitchell-team-fortress.pdf (`opened`);
https://cdn.fastly.steamstatic.com/apps/valve/2008/GDC2008_StylizationWithAPurpose_TF2.pdf (`opened`);
https://gamedeveloper.com/art/in-depth-how-valve-makes-art-to-enhance-gameplay (`opened`, report of the talk).
`practitioner` plus `demonstrated`. Corroboration: #9, and #43. Limits: a shooter's need to identify class at speed and at distance.
Valve says characters never appear this way in game, so it's a design test, not a look. No measured readability result given.
Would change (inference): a "black-fill silhouette test" is cheap and can fail, so it's a good gate for characters and key
props. It suits a talking head less well (head-and-shoulders silhouettes converge), where the test should be at the size of the
panel on screen and include hair and collar.

**9. Rank what must be read, then give each level its own channel.**
Valve read hierarchy: team through colour, class through silhouette, then fine detail at the chest with dark lower
body gradating to a contrasting upper torso. Same sources as #8 (https://gamedeveloper.com/art/in-depth-how-valve-makes-art-to-enhance-gameplay and the GDC 2008 slides). `opened`. `practitioner`.
Corroboration: Riot VFX guide's primary and secondary element rule, second-hand via #29. Limits: gameplay-driven.
Would change (inference): for a panel, write the ranked list before asking for it: who is speaking, how they feel, where we
are, what else. Assign each to a channel. Note that the highest-contrast detail region is a choice with consequences; see #47.

**10. GAP: the 180-degree rule and eyelines.**
No search targeted this; the Q1 searches went to measured reading and the budget ran out. No practitioner source on 180-degree
or eyeline matching was opened. Status: `unanswered`.
My reasoning, `inference` only: a true first-person sequence has one observer, so there is no axis to cross between the viewer
and a speaker, and no shot/reverse-shot. The axis still exists between two *other* characters in frame, and a turn of the viewer's
head is a continuous pan, not a cut. A cut in first person is a time jump or a change of gaze, and needs a rule about which.
Screen direction of a speaker on repeated panels (always left of centre when seated in one spot) does the job screen geography did.
None of that is sourced; test it against film editing texts before using it.

### Q2. First-person framing

**11. Whole-film first person was tried and largely judged a gimmick: Lady in the Lake (1947).**
Wikipedia article citing contemporary reviews and American Cinematographer 1946: Marlowe seen only in mirrors and in direct
addresses; other characters talk directly to camera; custom dolly walked through doors and up stairs; Montgomery sat on the dolly so
actors could play to him; MGM objected to hiding its star. Pryor (NYT): after a few minutes of a hand reaching for a doorknob, or
lifting a glass, novelty wears thin. Schallert (LA Times) praised it as ingenious, so reception wasn't uniform.
https://en.wikipedia.org/wiki/Lady_in_the_Lake . `opened`. `demonstrated`, with `critic/scholar` reception.
Corroboration: several reviews among search results (e.g. https://varley.net/?p=10805, https://first-draft.com/2025/06/29/lady-in-the-lake-1947/ , `not opened`); one result, not pinned to a URL, described a handshake with an
arm appearing a few feet from the lens. Limits: a 1947 studio film with live actors. Reviews are opinion, and whether the technique
or the script failed is not separable.
Would change (inference): bare hand-doing-a-thing panels burn out fast; use them when the action matters. Actors playing to a
person rather than a lens has an analogue in the prompt: name who they're looking at and their reason.

**12. Crowther's diagnosis: the camera-character shouldn't talk much, and being addressed all the time gets monotonous.**
Bosley Crowther, NYT, 9 Feb 1947, quoted at length in the same Wikipedia article. A voice from the camera doesn't match what
the audience would say and becomes a third-person presence beside you. Constant direct address becomes monotonous; better if
characters could go about their business while the camera observes.
https://en.wikipedia.org/wiki/Lady_in_the_Lake . `opened` (quotation inside a tertiary source). `critic/scholar`.
Corroboration: #14 from a game reviewer, 76 years later, with the same complaint about stare-downs. Limits: critic's theory, one film,
and games with voiced protagonists are a counter-case.
Would change (inference): the strongest single idea against the main risk of sustained first-person framing. Vary the stage: speakers doing something else, looking away,
talking to a third person, working at their task. Treat eye contact as a rationed event, so that it means something when it comes.

**13. Partial first person with a story reason exists as an alternative.**
Dark Passage (1947): only the first portion is subjective, concealing the star's face until plastic surgery in the plot. The reason for hiding
the face is built into the story.
https://en.wikipedia.org/wiki/Dark_Passage_(film) . `opened`. `demonstrated`. Corroboration: a review in the search summary said it learned from the subjective approach and handled it better
(not pinned to a URL, `not opened`), so weak. Limits: one comparison; no evidence that "partial" is what made it better.
Would change (inference): consider whether first person has a story reason. Mirrors and reflections as a treat, or a
rule that the viewer is never shown, should be decided once and stated in the style guide.

**14. Games: first-person talking has no shot/reverse-shot, and the fix games use is movement, which a motion comic doesn't have.**
Morgan Park, PC Gamer, 2023. First-person games lack the shot/reverse-shot that keeps a conversation flowing. Deus Ex avoided it with a
third-person dialogue view; Fallout 4 tried a third-person view and fans preferred the older way; Starfield's locked close-up is described
as jarring and creepy, since nobody holds a fixed stare while talking. Cyberpunk 2077 lets you roam, look away, read, walk off.
https://pcgamer.com/cyberpunk-2077-has-a-secret-weapon-that-makes-talking-fun-and-i-wish-starfield-would-steal-it . `opened`.
`critic/scholar` (journalist) describing `demonstrated` works. Corroboration: #12; #15 for CDPR's stated intent. Limits: one
reviewer's taste; a CDPR designer, in a search summary (`not opened`), called such criticism of Starfield generally ignorant of design
differences. Would change (inference): the movement fix isn't available in fixed panels, so the variety must come from staging in the art:
the speaker moves within the sequence, a third person enters, an object is handed over, the view drops to a table or a hand. A rule against the
frontal centred stare would be justified on this evidence, and also by #12.

**15. Developer intent for fully first-person conversation: control and threat, at high cost.**
CD Projekt Red. Pietras, lead cinematic animator: first person matters because who you are and how you dress matters; scripted scenes can be
interrupted, e.g. you pull a gun, which he calls very hard to do. Pears, level designer: having a gun pulled on your face wouldn't have the same impact in third person. https://www.vgr.com/?p=7680
(`opened`); https://www.videogameschronicle.com/news/cyberpunk-2077s-first-person-focus-is-the-right-choice-says-designer (`opened`);
GDC session page 404, title seen only in search result, `not opened`. `practitioner`, pre-release statements. Corroboration: #14 on what shipped.
Limits: marketing-era statements defending a decision fans disliked. Pietras's dress point is odd in first person, since you seldom see yourself.
Would change (inference): first person's best dramatic asset is being threatened, flirted with or lied to in person. Put panels there, and don't
spend them on exposition. Dress for the viewer's character has to appear through hands, reflection or other people's reactions.

**16. Even a first-person comic doesn't draw most panels subjectively.**
Mikkonen, chapter "Graphic Style, Subjectivity, and Narration", The Narratology of Comic Art, Routledge 2017. Close reading of a first-person
graphic novel by Taniguchi: at the visual level, impersonal perspective is the main mode, and subjective view is a local intervention.
https://www.taylorfrancis.com/books/9781315410135/chapters/10.4324/9781315410135-6 . `opened` (abstract). `critic/scholar`. Corroboration: #17, and a search-summary
corpus study of 300+ Asian comics on point-of-view panels (https://ebusca.uv.mx/Record/pubmed-10259188 , returned 404, `not opened`; do not rely).
Limits: first-person narration differs from first-person framing; one work.
Would change (inference): comics that say "I" mostly don't show "I see". A sustained first-person-*drawn* comic is unusual, so there's little tradition to copy,
and it makes the case for planned exceptions (a cutaway, a memory, a security feed) to break up long stretches. A project whose premise is sustained first person should put that premise to the same test.

**17. A subjective panel can show what a character perceives without being from their eye.**
Derik Badman, comics blogger, on Hergé's Secret of the Unicorn: seeing Snowy and seeing what Snowy sees, double, in one panel. Refers to Jost's ocularization, and
to Gaudreault and Jost on subjective deformations such as blur or partial masking.
https://madinkbeard.com/archives/snowy-sees-double . `opened`. Badman's longer essay on first-person comics (https://madinkbeard.com/archives/points-of-view-first-person-in-comics) returned 404.
`critic/scholar`. Corroboration: None here. Limits: blog, one example.
Would change (inference): blur, doubled vision, partial masking and eyelids are tools for showing state without a voiceover. Useful for
drunk, tired or hurt states, and cheap in layered stills.

**18. Hands in first person: the game convention is hands or tools visible, body not.**
Wikipedia, First-person (video games): players typically can't see the avatar's body though they may see weapons or hands; the absence of an avatar makes
platform timing harder and may cause motion sickness in some players. Fortnite docs says the same in search summary (`not opened`). https://en.wikipedia.org/wiki/First-person_(video_games) . `opened`. `demonstrated`. Corroboration: #11 for hands in film.
Limits: tertiary; written about real-time control, where hands carry weapon feedback. **No practitioner source on how to compose or draw viewer hands in stills was found.** Recommendation below is mine.
Would change (inference): in stills hands should appear when they do something (offering, refusing, holding a drink, flinching). Treat them as an acting channel with their own consistent
skin, sleeve, age and ring. Hand drawing is a known weak spot for generated images, but no source opened here tested that.

**Q2 unanswered:** visual-novel first-person staging. My search returned nothing usable, so sprite conventions, and what visual novels do about monotony, have no source here. Film examples beyond the two above (for example long POV sequences, direct address close-ups) were requested in one search that returned only Lady in the Lake.

### Q3. Colour and light

**19. A colour script maps emotional beats over the whole story, and started as small, crude sketches.**
Hyperallergic on The Art of Pixar (2020 ed.), quoting Eggleston's description: long strips of black paper with chalk pastel, a stream-of-consciousness map of colour,
value and visual drama, used to help everyone see the whole. Not invented by Eggleston or Pixar. Later digital scripts by Tsutsumi (Toy Story 3) and Romano (Incredibles, Up). Bleak, muddy colour marks sinister
moments. https://hyperallergic.com/the-art-of-pixar-chronicle-books . `opened`. MoMA audio transcript `not opened` (403): reported to say Eggleston made small pastels of each scene. `practitioner` quoted through a reviewer, and `demonstrated`.
Corroboration: MoMA, Slashfilm (`not opened`). Limits: feature animation with big crews; Pixar's own PR around it; review is not process documentation. The book's interviews weren't opened.
Would change (inference): plan the palette as a strip for the whole story before any final image, with one swatch per scene and a note on the emotion. It's cheap and can fail: laid out, a monotonous story shows immediately.

**20. GAP: "value before hue" has no direct sourced statement, only indirect.**
Search for process-level support found Eggleston's mention of value (#19), Valve's patterns of value (#8), and the 80s airbrush walkthrough moving from mid-values to darks and lights (#35).
None is a test. Status: `unanswered as a tested claim`, widely repeated as far as I know, listed under weakly supported. Would change (inference): a greyscale check is cheap, so it is still worth doing as a test that can fail; just don't call it proven.

**21. Light the scene plainly, then bring in the palette through neon, signs and streetlights.**
Art Direction Guide, Carmageddon game production document, on a website archiving unreleased games. Lighting the entire environment with one colour wash is too simplistic and soon boring to the eye; light naturalistically, perhaps tinting moon or sun, then apply palette colours through neon, billboards, street lights, fill lights down alleys and in front of stores.
https://www.gamesthatwerent.com/wp-content/uploads/2020/12/Art-Direction-Carma-guide.pdf . `opened`. `practitioner` (internal document; author and date not stated in what I read). Corroboration: #22 in spirit. Limits: real-time car game; the document's age and whether it was followed are unknown.
Would change (inference): separates base exposure from accent colour, which matches layered stills: a neutral-ish lit plate plus coloured light layers. Ask for "where does the coloured light physically come from" in every panel.

**22. Coloured light used on dark skin and for emotion, with colour planned with the colourist in advance.**
Laxton, cinematographer of Moonlight (ARRI interview): skin tone of incredible importance; aimed for natural, more realistic than flattering, warm and not harsh; palette of magentas, lime green, ocean blues taken from Liberty City and the beaches; warmed gels and some pinks and greens at night; a beach scene's light was 100% artificial.
https://arri.com/news-en/-moonlight-dp-james-laxton-creates-poetic-look-on-alexa . `opened` (a camera maker's interview, so the Alexa praise is promotional). `practitioner`, `demonstrated`. Colourist-preproduction detail and a pink-light-for-emotion quote seen only in search summaries (e.g. https://britishcinematographer.co.uk/james-laxton-moonlight/ , https://psuvanguard.com/?p=116959 ; `not opened`).
Corroboration: The Guardian piece via inkl (https://www.inkl.com/news/it-s-lit-how-film-finally-learned-how-to-light-black-skin) was paywalled after two paragraphs; Insecure's lighting not verified. Limits: one film, one DP; film sensors, not paint.
Would change (inference): saturated pink and green on dark skin is documented and praised, so coloured light doesn't require lightening skin. Palette drawn from a real place beat a generic mood, by Laxton's account.

**23. Saturation can be a deliberate stance, working at the midtones, with palette types mapped to spaces.**
Massé, artist on Dead Cells: pillars of saturated colour, Celtic architecture, alchemy. Saturated colour keeps the player alert and pulls the eye to new elements; saturation pushed mostly in midtones; complementary palettes make interiors feel confined; analogous palettes for depth outdoors; a deliberate refusal of the low-saturation convention.
https://gamedeveloper.com/production/art-design-deep-dive-giving-back-colors-to-cryptic-worlds-in-i-dead-cells-i- . `opened`. `practitioner`, `demonstrated`. Corroboration: Digital Futurism devs (#24). Limits: fast 2D action game; the "alert" claim isn't measured; survivor bias from a hit.
Would change (inference): "saturate only the midtones" and "complementary for confinement, analogous for depth" are concrete things to try in a brief. Treat as hypotheses, since this is one team's account.

**24. Restraint makes colour stronger: a rare colour has more effect.**
San Filippo, Race the Sun, quoted in GamesBeat's Digital Futurism piece: world mostly grey; when coloured objects appear, they strike harder. In the same piece, Righi Riva and Flanagan use saturated colour for different reasons; the piece names saturated glow on dark as a defining trait. https://gamesbeat.com/digital-futurism-part-1-a-discussion-about-a-popular-video-game-art-style/2 . `opened`. `practitioner`. Corroboration: Riot's advice to avoid extremes (#29). Limits: small team anecdotes, about the same style's variants.
Would change (inference): for a long saturated story, reserve the top of the saturation range so a key moment has somewhere to go. Compare to #23: same evidence level, opposite instinct, reconcile by story position.

**25. GAP: saturation eye strain has only forum and weak sources in this pass.**
Search results named indie developers reporting eye strain from saturated colours and fatigue from bright backgrounds in long sessions (https://itch.io/post/1340549 and similar, `not opened`; which post says what wasn't verified), and a low-quality study guide. No vision-science source appeared; chromostereopsis search returned nothing. Status: `unanswered as measured`.
Would change (inference): treat this as a risk to check in play, on a real display, not a proven threshold. A follow-up should look for measured visual-fatigue work.

**26. Sameness of neon as a look: critics say it, and there's a measured neighbour.**
PC Gamer opinion: focus shifted to oversaturated neon visuals, an '80s nostalgia trend, not true retrofuturism (https://pcgamer.com/enough-with-the-cyberpunk-aesthetic-bring-back-retrofuturism, `opened`). Visual Movements site: rain, neon, night as the forty-year default, magenta and cyan against darkness; unsigned reference site (https://visual-movements.pages.dev/movements/cyberpunk/ , `opened`). The Neon Graveyard essay: "cyberpunk style" among the best-understood prompts, so neon and rain are the easy path (https://b4theaiyellscut.substack.com/p/the-neon-graveyard , `opened`, polemic, unsupported on that claim).
`critic/scholar`. Corroboration: three opinion pieces of varying weight; #62's motif list includes rainy Parisian nights, which is a loose link at best. Limits: no measure of audience fatigue with neon.
Would change (inference): neon and rain together are the genre's default, so they establish genre and identify nothing. Specificity must come from elsewhere: #41.

### Q4. Style definition

**27. Consistency can come from small enforced decisions a viewer never notices.**
Xavier Coelho-Kostolny, character artist, thread transcribed at 80.lv: TF2 nose-to-forehead angle is nearly constant across characters; a tightly restricted palette covers skin, team colours, secondary, tertiary and metals; it spans characters, weapons and environment; a limit forces shape and material to separate areas.
https://80.lv/articles/comparing-team-fortress-2-and-overwatch-art-direction . `opened`. `practitioner` analysing a third party's work. His reading, not Valve's statement. Corroboration: #8 for the palette in part; #28. Limits: reverse engineering.
Would change (inference): a style guide should include a few checkable facial or construction constants. Watch for the tension with #45: constants that make everyone look alike.

**28. What usable art bibles have in common: a tie-breaker, disambiguated light direction, numeric shadow, a detail floor, a named mistakes list.**
Tony Valcarcel, Makko blog, on 0 A.D.'s Art Design Document, Liberated Pixel Cup guide, Battle for Wesnoth's Creating Unit Art, Riot's LoL VFX guide. Details reported: gameplay wins when it disagrees with realism; don't model anything smaller than a human hand; camera about 60 degrees orthographic, 32x32 grid; feet 55 px down on a 72x72 canvas; shadows towards purple and highlights towards yellow; outlines darker than local colour except black for characters; light from the upper right as the artist sees it, not as the unit does. https://blog.makko.ai/what-public-game-art-bibles-say/ . `opened`, but all four bibles `not opened`; these details are second-hand from a vendor blog. `practitioner` documents, reported. Corroboration: none independent here, though the specifics can be verified at source. Limits: sprite-oriented; three of four are volunteer or open projects, and these are the ones that happen to be public, not a sample of good ones. No evidence these documents worked except that the projects shipped.
Would change (inference): a style guide should be checkable: numbers and frames of reference. Also needs a stated tie-breaker. Example candidates: reads at game size beats pretty rendering; face over environment.

**29. In a generated pipeline, the failure is drift between generations, not disagreement between people.**
Same Makko post, https://blog.makko.ai/what-public-game-art-bibles-say/ . Art bibles were written for artists who disagree; a generator is internally consistent per image while trim creeps warmer, outlines thin, light wanders. Proposed locks: reserved colour per character, silhouette envelope, canvas and baseline, light direction, outline treatment, frame count. Riot details: avoid the extremes of 0 or 100, use mid-range to define palette; within one effect one element is primary; when complements appear together, one acts as secondary.
`opened`. `practitioner` with a commercial interest (it sells this constraint layer). Corroboration: None here, but plausible; `EVIDENCE-GENERATION.md` bears on it without testing it. Limits: vendor framing, no data, and sprite-focused.
Would change (inference): review a panel beside previous panels, side by side, against a short list of locks. Drift is invisible one image at a time, so a contact-sheet check is the gate. See #6.

**30. GAP: approved and rejected examples, weakly sourced.**
Search summary said good guides show what not to do (likely https://minnow-oarfish-wg2d.squarespace.com/style-guide-art-bible or https://sites.google.com/view/demetrius-leal/art-bible-art-plans-and-style-guides , `not opened`), and said a guide is law until amended (from an agent-skill outline, https://tessl.io/registry/skills/github/Donchitos/Claude-Code-Game-Studios/art-bible , `not opened`, itself generated advice, low standing). Liberated Pixel Cup's closing mistakes list via #28. Status: partly answered, weak.
Would change (inference): rejected examples with the reason named. Still unverified as better than rules alone; no source tests it.

**31. Reference can weaken as well as strengthen drawing, and learned "glyphs" creep in.**
Shooter, Storytelling Lecture Part 9 and 10: reference is important, but even good draughtsmen fake wrinkles with a memorised symbol, draw window glyphs instead of windows, hair glyphs on a right face. Measure elements against one another; draw the actual object.
https://jimshooter.com/category/04-storytelling-lecture/page/2/?order=asc . `opened`. `practitioner`. Corroboration: conceptually with #62. Limits: pencilling advice from an editor, not a teacher of drawing.
Would change (inference): "glyph" is a useful review word for generated art: generic window, generic hair, generic wrinkle. Ask for the specific object, in the specific building.

### Q5. Period and genre

**32. The 80s anime look is largely a set of physical process artefacts, many unintended.**
AnimeNation "Ask John" column (2011): hand-painted cels on acetate photographed frame by frame; frames can shift out of register; dust, scratches on cels, film stock and developing flaws, exposure errors; limited paint colours; digital brought vastly more colours; cost-saving became style. https://www.animenation.net/blog/wp-json/wp/v2/posts/26264 . `opened`. `critic/scholar` (columnist, no process citations). Corroboration: #33; Krita forum (https://krita-artists.org/t/80-90s-anime-aesthestic/9145 , `opened`) where artists guess at yellow tint and limited saturation but admit they need an expert. Unreal Engine's Orbitals post on photographed grain, halation and chromatic aberration (`not opened`, 403). Limits: I found no cel-era animator or studio technical account. **The strongest question here is under-sourced.**
Would change (inference): ask for materials and their results: paint-flat colour with limited palette, slight misregistration of foreground on background, a separate soft painted background, and the optical softness of being photographed. My guess, unsourced: grain alone is one of the weaker markers.

**33. Painted backgrounds in poster colour, and what filters can and can't recreate.**
vghpe blog on Gunbuster (1988-89) starfields: backgrounds, by the author's guess, opaque poster colour (Nicker), stars dotted with brush, nebula sprayed; blues shift right, reds bleed outward, grain and haloing visible in captures; the digital challenge is recreating lenses, cameras, film; fairly close with blurs, aberration, fake grain. https://vghpe.github.io/posts/gunbuster/ . `opened`. `practitioner` (hobbyist developer), and its materials claims are explicit guesses. The search summary reports a forum poster saying generic digital noise reads as static while film grain responds to scene light (`not opened`, unverified, low standing). Corroboration: #32 on film-stage artefacts. Limits: one effect; captures may be remasters; the author is a modern hobbyist, not a period witness.
Would change (inference): what's faked is usually a uniform overlay across the frame. Reasonable hypothesis to test: artefacts should differ by layer and by luminance. Unproven.

**34. Display and transmission are confused with production.**
Clip Studio Tips tutorial by LizStaley lists film grain and the off colours of VHS and CRT together, and attributes chromatic aberration to old TVs and VHS, then adds filters; recommends downscaling first so filters show. https://tips.clip-studio.com/de-de/articles/9163?org=1 . `opened`. `practitioner` (tutorial writer). Set beside #32 and #33, which put such effects at the film stage. Corroboration: None here, and it conflicts with #33. Limits: a hobby tutorial on a filter. My reading, `inference`: a film-print cel look and a VHS look are two different targets, and many "retro anime" pictures mix them.
Would change (inference): the style guide should choose: theatrical film print, TV broadcast, or home VHS. Each has different softness, colour and artefacts. Ask for one.

**35. 80s airbrush: mid-values outward, physical masks for hard edges, thin seam lines, glow, grain.**
ImagineFX tutorial at Creative Bloq, recreating a named illustrator's chrome robot work (the name is left out here on purpose): uses soft brushes only and moves from mid-values to darks and lights; emulates masks by selection for hard edges; seam lines break up large shapes; adds grain and imperfection at the end.
https://creativebloq.com/advice/painting-in-the-80s-airbrush-style . `opened`. `practitioner`. Limits: an explicit imitation of a named artist, which a style brief should avoid; useful for the process facts only. Corroboration: None here.
Would change (inference): the *technique* is expressible without the name: soft gradient plus cut-mask hard edge, seam lines. The artist's name adds imitation, not information.

**36. GAP: 80s comics materials.**
No search was left after higher-priority questions. Nothing on colour separation, newsprint, Ben-Day or painted European albums was opened. Status: `unanswered`. Would change: nothing until sourced. See leads at the end.

**37. Noir's defining definition: low-key, high ratio of key to fill, rich shadow.**
Place & Peterson, "Some Visual Motifs of Film Noir" (1974): quoted in reviews and notes. https://brightlightsfilm.com/?p=33485 quotes them on silhouetted figures (`opened`); definition itself seen via search summary of a scanned reader (`not opened`) and listed in notes https://www.broadway.org.uk/sites/default/files/attachments/Film%20Noir%20Notes%20%26%20References%20%282%29.pdf (`opened`, bibliography). `critic/scholar`, widely cited. Corroboration: #38. Limits: primary essay not opened.
Would change (inference): usable as a value specification: the shape of the shadow rather than the amount of darkness, and the ratio between lit and unlit sides.

**38. Alton: shadows as staging and story, fog and smoke as tools, and short schedules.**
ASC article on John Alton: T-Men opens with a statuette casting an exaggerated shadow that undercuts the speaker; lit fog, mist, smoke; Alton on mysteries calling for natural light, and on night as when interesting things happen; T-Men made in about six weeks, Raw Deal in half that. https://theasc.com/articles/john-alton-master-of-the-film-noir-mood . `opened`. `practitioner` quoted, by a trade body with interest in celebrating him. Corroboration: Bright Lights review (#37). His remark that what you leave unlit matters more than what you light was seen only in search summary (`not opened`). Time's account of cost saving returned 404, `not opened`. Limits: a hagiographic piece.
Would change (inference): a shadow can carry a story beat. In a first-person panel a shadow can stand for a person off-frame or show a threat approaching, which suits the framing. Fog and rain mean cheap depth layers. A short schedule as cause of the style is suggestive only.

**39. Not all canonical noir has those traits.**
James Naremore, More Than Night, quoted by a film blog: Out of the Past has no night-for-night, distorting lenses, extreme deep focus, choker close-ups, few radical angles, so it manifests almost none of the traits Place & Peterson call essential. Same blog: harsh low light, practicals, low angles are indicative of trends; flashback structure, femme fatale and gender-asymmetric lighting also mark it; Naremore estimates about 12% of 1947 US films were in colour. https://categoryd.blogspot.com/2009/02/out-of-past.html . `opened`, second-hand quote. `critic/scholar`. Corroboration: None here beyond the blog, but Naremore is a standard authority. Limits: a blog quoting a book.
Would change (inference): "noir" is a family of choices, and low-key is not the only marker. Don't let "noir" in a prompt collapse to Venetian blinds and hard shadows. Those specific clichés weren't sourced; flagging from general knowledge.

**40. Techno-orientalism: neon Asian signage reads as a Western view of Japan, 1980s-specific.**
Sabukaru essay ties the genre to 1980s Western anxiety about Japanese economic rise; beyond the LEDs lie bureaucracy and tradition. https://sabukaru.online/articles/techno-orientalism-decoding-japans-misrepresentation-as-a-cyberpunk-utopia . `opened`. A 2024 paper says Japanoid imagery in Blade Runner, Cyberpunk 2077 and Edgerunners stays condescending (https://doaj.org/article/97e8cd88b16744d489342e0e7b60c245 , 403, `not opened`); AHFE paper on Oriental elements in cyberpunk games (https://openaccess.cms-conferences.org/publications/book/978-1-958651-45-2/article/978-1-958651-45-2_79 , opened but abstract not captured). `critic/scholar`. Corroboration: moderate. Counter: The Neon Graveyard (`opened`) argues Japanese creators were documenting their real bubble Tokyo, unsupported assertion; the critique isn't uniform. Limits: essay and two unread papers; no measure of how players of any background read this imagery.
Would change (inference): choose a real or invented place with its own script, food, work and bureaucracy. Don't use Asian text as wallpaper. If you use real languages, someone must be able to read them.

**41. GAP: keeping it specific, unanswered as a practitioner method.**
My search asked for this directly and found only opinion that it should be done (#26, #40), plus #22's palette from a real neighbourhood, #31's "draw the actual object", #62's motif list. No concept artist or production designer on specificity was opened; Syd Mead's process wasn't found. Status: `partly answered by inference`.
Would change (inference): ask for the local cause of everything: who pays for this sign, what it sells, what the rain has damaged, the brand of noodles. Make one setting's facts the source of its look.

**42. Avoiding imitating a single work or artist: no source tackles it directly, but demonstrations of triangulating do exist.**
Valve drew on three named illustrators plus 1960s industrial design and its gameplay needs (#8, https://www.cs.princeton.edu/courses/archive/fall07/cos597B/papers/mitchell-team-fortress.pdf ). Moonlight's reference folder drew on Clockers, Happy Together, Wuthering Heights, Ginger & Rosa and Tumblr photographers (#22, https://arri.com/news-en/-moonlight-dp-james-laxton-creates-poetic-look-on-alexa ). Against that, #35 is plain single-artist imitation. `demonstrated`, source statuses as in those entries. Corroboration: two demonstrations. Limits: neither says it was done to avoid imitation; reference gathering by people; a generator may react differently. Status: partly answered.
Would change (inference): several references from different media, each named for one borrowed property (this film's practicals, that illustrator's edge). State the material process and purpose, and drop a named-artist shortcut.

### Q6. Characters

**43. A cast reads apart at a glance through silhouette, proportions and costume, deliberately exaggerated.**
Valve as in #8 (https://www.cs.princeton.edu/courses/archive/fall07/cos597B/papers/mitchell-team-fortress.pdf , https://gamedeveloper.com/art/in-depth-how-valve-makes-art-to-enhance-gameplay ): body proportions, weapons, footwear, hats and clothing folds designed to give each character a unique silhouette, with folds echoing silhouette. Medic patch on a sleeve failed in playtest as an identifier, so they abandoned tiny marks for gross shapes (gamedeveloper report). Coelho-Kostolny (#27, https://80.lv/articles/comparing-team-fortress-2-and-overwatch-art-direction ) credits Overwatch with silhouettes and recognisability too, while criticising its lack of team colours. `opened`. `practitioner`, `demonstrated`. Corroboration: two, both shooters. Limits: full-figure shooter at distance; here figures are cropped close.
Would change (inference): at bust crop silhouette is hair, hat, collar, shoulders. Costume marks must be large. The sleeve patch story is a good reminder: small marks don't read as identity at game size, and that can be tested.

**44. Generated faces collapse variety inside a group: measured.**
AlDahoul, Rahwan, Zaki, arXiv 2402.01002 on Stable Diffusion: significant bias across six races, two genders, 32 professions and eight attributes; significant racial homogenisation, e.g. nearly all Middle Eastern men shown dark-skinned, bearded, with traditional headdress. Preregistered experiment: exposure to such faces affected viewers' biases. https://arxiv.org/abs/2402.01002v2 . `opened` (abstract). `measured`. Corroboration: #62 in spirit. Limits: one model, a preprint version, abstract only.
Would change (inference): the default output for a named culture is a caricature bundle. So the brief for a character specifies a person (job, age, what they wear today, how they cut their hair) and not an ethnicity plus a costume. Review a group shot for sameness within a group. Note that I found no practitioner source on hair and dress by culture; **that sub-question is unanswered.**

**45. GAP: face consistency vs. face variety.**
Only `inference`, from #27 versus #44: fixed construction constants unify a style, and also push all faces to one template. No source addresses it, and "drawing different faces" wasn't found. Status: `unanswered`. Would change (inference): if a guide has face constants, it should also list what must vary: jaw, nose bridge, eye spacing, age marks.

**46. GAP: skin under coloured light beyond #22.**
See #22. No technical source on skin hue under coloured light opened. Status: partly answered. Practical inference, unsourced: the base skin colour must be stated separately from the light colour in the brief, or the character's skin becomes the neon.

**47. Sexualisation: pose and framing that don't match the moment is the working test, and context beats skin count.**
Nuclearpasta, webcomic artist, Patreon essay: objectification is a matter of context, not exposure; ask whether undress is justified by the story, and what the character's purpose is beyond looking nice; a fight scene framed like softcore is the fault; own rules: no sexy poses; framing follows the story, not the underwear; no overfocus (a body drawn loosely with lavished breasts and buttocks shows where the attention went; jiggle in animation is the same fault); note when women are the only ones undressed. Admits a failure in the artist's own comic. https://www.patreon.com/posts/35392080 . `opened`. `practitioner` of modest standing, unusually concrete. Corroboration: #48; #49. Limits: one artist's framework; states as fact that authors' intent determines sexualisation, which #48 disputes.
Would change (inference): review question: "does the camera's interest in this body match what the scene is about?" Overfocus gives a checkable sign: compare rendering detail on the body with detail on the face and hands. Also a contact-sheet count of who's undressed and whose body the frame lingers on, across the cast and across genders.

**48. Gaze: where the character's eyes go, and what they ask of the viewer, can matter more than the outfit.**
WWAC on Jenny Frison's Red Sonja covers: same flimsy costume, but she looks past the viewer, no invitation, and the piece credits that. Sets a three-way relationship of character, creator, viewer. Names brokeback pose as a marker. Frison is reported as aiming for the strongest possible effect on the viewer. https://womenwriteaboutcomics.com/?p=41526 . `opened`. `critic/scholar` on a `demonstrated` work. Corroboration: Begley, Works and Days 2014, argues Simone's Red Sonja and de Campi's Grindhouse negate the male gaze (https://www.worksanddays2.net/2014/File13.Begley.pdf , `opened`, opening pages). Limits: critics' readings; a critic's one example chosen because it succeeded.
Would change (inference): this is a direct issue in first person: every character looks at the viewer, so each look is an invitation or isn't. Default gaze and expression should be about the conversation. Adult seductive looks need story justification. A character who ignores the viewer can't read as available.

**49. Men: power fantasy and sexual fantasy overlap; the double standard shows up as asymmetry.**
Nuclearpasta (#47, https://www.patreon.com/posts/35392080 ) on Aquaman vs. Carol Marcus: male power fantasy for men can be a sexual fantasy for women; the problem is objectification and who's the assumed audience; Witcher criticised for asymmetric nudity. `opened`. `practitioner`. Mulvey's claim (male figure can't bear sexual objectification) seen via a search summary paper (`not opened`), `critic/scholar`. The Hawkeye Initiative, which redraws poses on a male hero, seen only via TV Tropes search summary (`not opened`). Corroboration: weak, one artist plus fan practice. Limits: measured content analysis of games was searched for and nothing returned, so `unanswered`.
Would change (inference): the swap test (same pose and framing on a man of the same role and age: does it now look ridiculous?) is cheap and applies equally. Its origin is fan practice, unmeasured. Don't sexualise men by default either; equal treatment of skin isn't the goal, matching the scene is.

**50. GAP: adult faces shown clearly.**
Status: `unanswered`. From #3 and #9 only, by inference: faces take attention anyway, so put highest contrast at the face. Keep age markers (lines, jaw, neck, hands), which also bears on not producing adults who read as children. No practitioner source was found for that, and it is too important to leave resting on my reasoning.

**51. GAP: costume as character, and costume by setting.**
Not searched separately; budget ran out. Only Pietras's remark (#15) touches it. Status: `unanswered`. Would change: nothing until sourced.

### Q7. Motion comic and limited animation

**52. The main diagnosed failure of motion comics is the loss of reader control of pacing.**
Jim Lee (then DC co-publisher, Kotaku, June 2013, launching DC2): earlier motion comics took the control and pace out of the viewer's hands, a passive experience like a low-budget cartoon. https://kotaku.com/here-s-how-the-video-game-comics-of-the-future-will-pro-511727593 (`opened`, promoting DC's own interactive product). Goodbrey (comics scholar and maker) via Loyer: fixed-duration animations act like cutscenes, and erode the reader's agency (https://thedigitalreview.com/issue01/timeframing/timeframing-script.pdf , `opened`, Goodbrey 2017 quoted there). McCloud via Drew Morton: readers stop and start being active collaborators, amid a mix of sensations (https://mediacommons.org/imr/node/1505 , `opened`, second-hand). iFanboy: comics fans read to be active, feel their time wasted (https://ifanboy.com/articles/pop-up-comics-and-technological-revolutions/ , `opened`).
`practitioner` + `critic/scholar`. Corroboration: high, among comics people. Limits: all from print-comics voices; no measured reader data found; these are people who value comics' control, on works sold as comics. A game audience may have different expectations (cutscenes are normal), as Loyer notes.
Would change (inference): advance by player input. Loops run while waiting; no animation should block text or hold back a click. Any non-skippable timed move is a design choice needing a reason.

**53. Case: Watchmen Motion Comic keeps 2.5 of Goodbrey's 7 characteristics.**
Erik Loyer, Timeframing (Digital Review, 2020), https://thedigitalreview.com/issue01/timeframing/timeframing-script.pdf : space as time, juxtaposition, closure, reader pacing gone; spatial network partly; tablodic images and word/image blending intact. Viewer can only pause. Loyer says this is typical of US works marketed as motion comics, and links it to fans' negative response.
`opened`. `practitioner` (digital comics maker) using a scholar's framework. Corroboration: search summary's reviewer: more an audio book with pictures (`not opened`). Limits: framework counts properties of "comics", which defines the problem in comics' favour. Being "not a comic" doesn't mean it failed for its own audience; no sales or retention data.
Would change (inference): deciding whether this form is a comic or a game cutscene sets which complaint applies. If the panel fills the frame and the text is voiced, judge it as limited animation.

**54. Commercial failure has other causes too: Madefire.**
Gutternaut on Madefire (2021): tap-driven Motion Books kept word balloons and reader pacing, won an Apple Editor's Choice, partnered with DC and Blizzard, then liquidated after failing to find an audience, store competition, a bad film investment, Covid. Author says reasons weren't public; his guesses. https://gutternaut.substack.com/p/madefire-how-an-innovative-gimmick-couldnt-keep-up . `opened`. `critic/scholar` (blog). Corroboration: None here. Limits: speculation by the writer's own admission.
Would change (inference): reader control doesn't save a product; don't credit it for commercial results. The evidence above is about reception among comics readers.

**55. Print comics also control the reader, so the contrast is overstated.**
Nichols, Comics and Control: Leading the Reading (Writing Visual Culture, 2015): layouts and page turns already control what's seen and when; digital adds other controls. https://researchprofiles.herts.ac.uk/en/publications/comics-and-control-leading-the-reading/ . `opened` (abstract). `critic/scholar`. Corroboration: None here. Limits: abstract only.
Would change (inference): a panel reveal on a click is the digital page turn, and the strongest place for a surprise.

**56. Small loops are a recognised form: cinemagraphs, idle loops, overlapping loops.**
Loyer on Hobo Lobo of Hamelin's overlapping subtle loops; cinemagraphs and game idle animations as bounded "vignettes", some with jarring loop points, others subtle. Timeframing script. `opened`. `practitioner` plus `demonstrated`. Freaksugar and a student site conclude animation can feel gimmicky unless it serves the narrative (https://www.freaksugar.com/webcomics-wednesday-animation , https://beli.hotglue.me/?Conclusion , `opened`, low standing). Corroboration: weak, these two. Limits: taxonomy, not effectiveness.
Would change (inference): check loop points: a visible seam or sync between layers looks cheap. Overlap unequal loop lengths. **No source gives a numeric limit on how much movement is too much, or on hold length. Timing is unanswered.**

**57. Anime's limited animation is rooted in economy, then became vocabulary.**
Wrong Every Time (critic) on Tezuka: low-image-count choices driven by cut-throat TV pricing; anime's visual vocabulary built from necessity. https://wrongeverytime.com/tag/belladonna-of-sadness/ (`opened`). AnimeNation (#32) says the same on reused backgrounds, fewer frames. Morton (#52): The Marvel Superheroes (1966) repurposed comics art, partly for economic reasons (Kirby and others unpaid), and he treats it as the form's origin. Search summary: Steinberg's "economy of motion", Tsugata's *ugokanai animation* ("animation that doesn't move") (`not opened`). `critic/scholar`. Lamarre's Anime Machine not found.
Corroboration: three independent sources here on economy. Limits: no practitioner account or production document opened on how a director times a hold. Dezaki-style held stills weren't found.
Would change (inference): a hold is a respectable tradition, and motion isn't owed. But the tradition rests on strong stills, which is the point to carry over.

**58. An extreme: Belladonna of Sadness tells a feature largely by panning over still watercolours. Reception divides.**
Moria review: limited animation, often static watercolour or pencil, a hard watch through stationary shots; premiered at Cannes; cult revival. https://moriareviews.com/fantasy/belladonna-of-sadness-1973.htm (`opened`). Rolling Stone: virtually ignored on release, helped bankrupt Mushi, now reappreciated; called a seed for Dezaki and Sugii (https://www.rollingstone.com/culture/culture-news/inside-the-greatest-x-rated-animated-film-youve-never-heard-of-162880/2/ , `opened`). `demonstrated`, `critic/scholar`. Corroboration: two reviews. Limits: an adult X-rated film, cited for technique only, and not a character reference; reviews, no measure of holding attention.
Would change (inference): pan-over-still can sustain feature length for some audiences and is a proven strain for others. Long pans need something to find along the way.

**59. WCAG 2.3.1 Level A: three flashes per second, or below thresholds.**
W3C Understanding 2.3.1 (WCAG 2.2): nothing flashes more than three times in any one second unless below general and red thresholds. General flash: opposing changes in relative luminance of 10% or more of max, where the darker is below 0.80. Red flash: opposing transitions involving saturated red, working definition R/(R+G+B) >= 0.8 for a state and a CIE 1976 UCS chromaticity difference > 0.2 (new note in 2.2, replacing an older formula still quoted in other summaries). Area limit: 0.006 steradians within a 10-degree field, i.e. 25% of it, estimated by a 341x256 CSS px rectangle. Analyse at largest size offered, while looping. Turning flashing off isn't an accepted fix; blinking under three per second is a distraction issue, not a seizure issue. People are more sensitive to red flashing than other colours. https://www.w3.org/WAI/WCAG22/Understanding/three-flashes-or-below-threshold.html . `opened`. Normative guidance. Corroboration: #60. Limits: web standard; adapted from broadcast; can't account for viewing distance; a note says viewers closer than assumed are affected by content that passes.
Would change (inference): sign flicker, lightning and muzzle flash need a limit stated in the brief, and the red check matters here especially for a red-heavy palette. Test with a tool. By my reading: a sign flicker of up to three pairs a second stays under the count limit whatever its size, though it may still distract. Saturated red by the 0.8 ratio is narrower than "red-looking": computed by me, pure red (1,0,0) gives 1.0 and a made-up pink (1,0,0.2) gives 0.83, while magenta (1,0,1) gives 0.5, so magenta alone escapes the red test but not the luminance one. Correction (independent review, at the source, 2026-11-06): R, G and B are linear relative-luminance values, so CSS hotpink #FF69B4 is 0.63 and deeppink #FF1493 is 0.77, with #FF0088 about the edge at 0.80. A transition counts to or from a state at or above 0.8, so magenta to red does count.

**60. Harding: same family of test, different area rule, and a duration rule the WCAG wording lacks.**
HardingFPA: transition of at least 20 cd/m² counted per pixel; failure needs flash over 3 Hz and area exceeding 25% **of the video frame**; extended failure when over 80% of frames in the last 5 seconds near failure (warning 0.3 or 0.4). A small change of size or format can push near-failing material over. Spatial patterns are tested too (stripes). https://www.hardingfpa.com/technical-support/how-to-interpret-hardingfpa-results/ . `opened`. Suite covers Ofcom, ITU, NAB-J and ISO; a Games edition exists https://www.hardingfpa.com/hardingfpa-for-games/ (`opened`, navigation only; little text). `practitioner` (test vendor). W3C lists PEAT and Harding as resources. Ofcom's own text `not opened`. Corroboration: #59. Limits: vendor documentation; platform-holder requirements for console games weren't found.
Would change (inference): rain streaks and striped signs are spatial patterns, a risk unrelated to flashing. The area rules differ a lot: computed by me, 25% of a 341x256 window on a 1024x768 screen is about 2.8% of the screen, against Harding's 25% of frame, so a flicker can pass Harding and fail WCAG. State which test applies. A long near-threshold shimmer can fail Harding's extended rule.
Editor's check at the source, 2026-11-06 (W3C page above, opened): the normative text says 0.006 steradians, 25% of any 10-degree field. The Understanding page calls the 341x256 block a 10-degree viewport, and also says the flashing area becomes 341x256 CSS pixels, 87,296 px (about 11.1% of a 1024x768 screen, my arithmetic). Settled by the independent review, 2026-11-06: that page is marked informative, and the sentence drops the normative 25%. The limit is 25% of the field, 21,824 CSS px (2.8% of 1024x768). Don't use 87,296. How a fullscreen game maps to CSS pixels isn't stated, so 2.8% of the frame is the conservative reading (inference).

### Q8. Critique

**61. Separate problem from suggested solution when the reviewer isn't an expert.**
CGMA blog with industry instructors: for non-expert reviewers, ignore the suggested fix (change her outfit's colour) and act on the reported effect (she seems too meek); they're still audience. If a client wants a bad idea, make it and show the problem. https://conceptart.cgmasteracademy.com/blog/how-to-read-minds-and-decode-artistic-feedback.html . `opened`. `practitioner` via a school's marketing. Creative Bloq: critique should ask whether the piece achieves what the artist set out to do; Robinson (Paizo creative director) makes requested changes to show why they fail; Blanché: critique isn't about you. https://creativebloq.com/features/how-to-give-and-get-more-from-art-critiques . `opened`. `practitioner`. Corroboration: mutual, plus search-summary sources (parse.gl, Medium game-art posts blocked, `not opened`). Limits: generic soft advice, no outcome evidence. GDC talk on critique by Jeff Hesser, abstract only (https://gdcvault.com/play/1023293/Maximizing-Critique-Improving-Communication-for , `opened`, abstract only).
Would change (inference): an owner's note should be recorded as a reported effect plus a suspected cause. An art agent should take the effect as data and may challenge the cause by showing it.

**62. Generators converge on a small set of pleasant generic motifs without retraining: measured, in a narrow setup.**
Hintze, Proschinger Åström, Schossau, Patterns (DOI 10.1016/j.patter.2025.101451): SDXL and a captioning model in a loop from diverse prompts; drift to 12 motifs including Gothic cathedrals, pastoral landscapes, rainy Parisian nights, luxurious sitting rooms, snowy houses; bland, background-music imagery; persisted across parameter and model changes; a prime-minister prompt ended in an empty, furnished room. Paper `not opened` (redirect). Read via Elgammal, The Conversation, republished (https://www.thenewsminute.com/news/ai-induced-cultural-stagnation-is-no-longer-speculation-its-already-happening , `opened`) and HyperAI report (https://hyper.ai/en/stories/9012adeef14148114da11dc792fbcd8d , `opened`). `measured`, read second-hand. Corroboration: #44; #63. Limits: **autonomous caption-and-regenerate loops are not how a directed project runs.** The motif drift is the loop's. Commentators stretch this to "cultural stagnation", which it doesn't test. People, drama and specific time and place dropped out: a detail worth noting.
Would change (inference): any step where an image is described in words and regenerated loses specifics. Watch for people vanishing from scenes, and furnished rooms replacing events. Keep the concrete nouns as source of truth rather than re-derive them.

**63. Prompts themselves are uniform.**
De Rosa Palmini & Cetinic, arXiv 2410.06768: three prompt-originality metrics on DiffusionDB and Civiverse; users' reliance on templates contributes to homogenisation, topics and wording repeat. https://export.arxiv.org/pdf/2410.06768 . `opened` (abstract and search summary on findings). `measured`. Corroboration: #62, #44. Limits: public hobbyist datasets; it's correlational on the question of images.
Would change (inference): mostly pipeline territory (`EVIDENCE-GENERATION.md`). For review: phrases copied from a house prompt are a suspect in sameness.

**64. GAP: what practitioners do to get past the generated look.**
My search returned general calls for deviation and nothing concrete. Status: `unanswered`. `EVIDENCE-GENERATION.md` has nothing on it either. Nearest related items: #31 glyphs, #41 local cause. Would change: nothing until sourced.

**65. GAP: telling "technically clean" from "says something".**
Nearest items: Frison's aim of the strongest possible effect (#48); Elgammal's point that generated work can be polished and pleasant and mean nothing (#62); Shooter's clarity first (#7); Massé's insistence on unsettling background elements as a story idea (#23). Status: `partly answered by inference`. Would change (inference): ask what changed from the panel before, and what we now know that we didn't. A panel that could be swapped with another with no loss says nothing, and this can be tested by actually swapping them.

**66. Non-experts see what trained viewers see, broadly, in where they look.**
Beelders & Bergh's background section (https://pmc.ncbi.nlm.nih.gov/articles/PMC7963460/ ) reports Buswell 1935: trained and untrained viewers' gaze patterns didn't differ significantly, and task changes gaze a lot (Yarbus, DeAngelus & Pelz). Sancarlo's students (https://bop.unibe.ch/JEMR/article/download/JEMR.13.2.7/10079/26653 ), familiar with composition but not experts, agreed on it when it was clear. `opened` as secondary citation; Buswell `not opened`. `measured`. Corroboration: mixed: #5 finds expertise matters for page-reading order. Limits: 1935; gaze isn't judgement. Whether non-artists can judge craft wasn't tested by anything here.
Would change (inference): a non-artist owner is a good instrument for what reads and what's seen first, and a weak instrument for how it was done. The form dependency: comics page order is where expertise matters; single images less so.

**67. Tracked objects that changed between frames, in two projects (added 2026-11-13, outside the 20-search pass).**
owlinthebarnai/video-studio-kit @ `fbd31eb` (no licence file of its own; read for ideas, nothing copied), in
`.claude/skills/what-if-animation/references/traps.md` (from kelano86/what-if-animation, MIT): a calendar showed nine
crossed-off days on night one. The library's own a mystery game, 2026-11-07: a plot-critical phone changed type
between frames. `opened`. `practitioner`. No outcome data.
Would change (inference): a frame review checks a written list of tracked objects, not only each frame alone.

**Comics editors' feedback specifically:** only Shooter's lectures, which address creators rather than describe editorial process. Search for editors' notes returned no others. Status: `partly answered`.

---

## Question status

| Q | Status | What's missing, and what was searched |
|---|---|---|
| 1 | Largely answered | Measured reading and gaze: good. Eyeline, 180-degree, shot grammar in craft sources: **unanswered** (#10). Thumbnail size tests: only Valve silhouette. Rule of thirds: only Gurney's related golden-section note. Searches 1, 2, 7. |
| 2 | Partly answered | Film, games: yes. Comics: scholarship, little practice. Visual novels: **unanswered**. Viewer hands in stills: **no craft source**. Searches 3, 8, 20. |
| 3 | Partly answered | Colour scripts at overview level; neon as source thin but real; eye strain unmeasured; cinematographers on neon beyond Laxton not found; chromostereopsis, Deakins, Refn etc. **unanswered**. Searches 4, 19. |
| 4 | Partly answered | Good secondhand on bibles; primary bibles unopened; approved and rejected examples weak; model sheet process from Valve only. Search 5. |
| 5 | Partly answered | Cel anime: only columnists and hobbyists. 80s comics: **unanswered**, unsearched. Noir: reasonably answered. Retro-futurism specificity and avoiding imitation: opinion and demonstrations only. Searches 9, 10, 11. |
| 6 | Partly answered | Silhouette and gaze: answered. Different faces, hair and dress by culture, costume by setting, adult faces: **unanswered**, partly from search limit. Skin tones: one strong demonstration. Searches 12, 14, 15. |
| 7 | Partly answered | Why motion comics failed: yes. Photosensitivity: answered from source. Quantities and timing: **unanswered**. Measured motion-attention: **unanswered**. Sound and image: thin. Searches 6, 13, 16. |
| 8 | Partly answered | Feedback advice: generic. Editors: Shooter only. Sameness measured: yes, narrow. Getting past it: **unanswered**. Searches 17, 18. |

---

## Where practitioners disagree

1. **Do lines lead the eye?** Art-teaching tradition and Sancarlo et al. (#2, on order-free direction) against Beelders, Gurney, and Garbutt & Spehar and Kirtley 2018 as cited (#1, #3). Reconciled best as: salient items and strong axes affect *where* and *which direction*; little supports a set *order* of viewing. Kirtley-the-comics-researcher (#4) is about page navigation, a different question from lines inside an image.
2. **Saturation: asset or fatigue?** Dead Cells pushes it to keep players alert (#23); Race the Sun, Riot and LPC via #24, #28, #29 hold back, and indie reports of strain are weak (#25). Probably settled by position and length of story, but no one has measured that here.
3. **Is reader control the thing?** Lee, Goodbrey, McCloud, Loyer say yes (#52, #53). Nichols says print controls readers too (#55). Madefire kept control and died anyway, for unclear reasons (#54). Loyer also notes that games train people to accept cutscenes.
4. **First person: conviction or compromise?** CDPR "100%" (#15), Deus Ex and Fallout 4 third-person dialogue, Starfield's locked close-up (#14), Dark Passage's partial use (#13), Mikkonen's finding that first-person comics rarely draw from the eye (#16).
5. **Who decides sexualisation?** Nuclearpasta: authorial intent decides (#47). WWAC: viewer's socialised reading, with intent set aside (#48). Mulvey as summarised holds men can't bear the same objectification; Nuclearpasta rejects a clean division between power fantasy and sexual fantasy (#49).
6. **What makes noir?** Place & Peterson's low-key list vs Naremore's counterexample (#37, #39). Alton described lighting mysteries as natural (#38), against an account from German expressionism (SMPTE, search summary, `not opened`) and one of low-budget necessity (Time, search summary, page 404).
7. **Is the retro anime look film or tape?** Gunbuster post and AnimeNation say film; the Clip Studio tutorial says VHS and CRT (#32 to #34). Krita forum members can't settle it.
8. **Is cyberpunk over?** PC Gamer, the Neon Graveyard essay and Visual Movements call it a worn default (#26). No practitioner in this pass defends it directly. My reading, `inference`: Moonlight (#22) and Dead Cells (#23) show saturated palettes still earning praise when tied to a place or an idea, though neither is cyberpunk.
9. **Consistency vs variety.** Constants that hold a style (#27) against what variety of faces needs (#44, #45). No one in this pass addressed the tension directly.

---

## Repeated but weakly supported

Stated carefully: "weakly supported" means weak in what I could open, not false.

1. **"Composition leads the eye along a path."** Tested: mostly fails on sequence, works on destination (#1, #2, #3).
2. **"Golden section or rule-of-thirds placement draws attention."** Only Gurney's note against it, informal. My search returned nothing that tested thirds; the claim also isn't supported by anything opened.
3. **"Value before hue."** A sensible cheap check. I found process mentions, and no test (#20).
4. **"Motion comics failed because of reader control."** Comics-world consensus without data (#52 to #54). All voices come from the print side, and one had a competing product to promote.
5. **"Saturated neon causes eye strain."** Forum reports and a poor study guide (#25). May well be true in specific conditions; nothing opened measured it.
6. **"Silhouette is the key to character readability."** Valve demonstrates it strongly, for one form. No measured result, and extrapolation to bust-length panels is untested (#8, #43).
7. **Grain and chromatic aberration as "the" 80s anime look.** Popular in tutorials, attributed inconsistently (#33, #34).
8. **"A guide needs approved and rejected examples."** Repeated, including by generated "agent-skill" pages, which appear to copy each other. Search result 5 was dominated by near-identical skill files, so this may be an echo. None of those were opened, and I would not count their agreement as corroboration.
9. **Blade Runner's rain was a budget trick**, or conversely a tears metaphor. Neon Graveyard asserts both in one sentence, unsupported.

---

## Questions a non-artist owner can answer about an image

The list, all `inference`, is in `SKILL.md`, shaped by #1, #3, #6, #52, #61, #66.

---

## Leads not used as evidence

From my memory, **not found by search, not opened, not claims**. Listed so a later pass can check them: Tim Smith's attentional theory of cinematic continuity, Hutson and Loschky on "tyranny of film" (searched, not returned), Laubrock on comic eye movements, McCloud's Understanding Comics, Eisner's Comics and Sequential Art, Gurney's Color and Light, Bacher's Dream Worlds, Calahan on storytelling through lighting, Alton's Painting with Light, Lamarre's The Anime Machine, Steinberg's Anime's Media Mix, Mulvey's essay itself, Downs & Smith and Lynch et al. on game character sexualisation, Landis on costume, the DC Guide to Coloring and Lettering, Ofcom's flashing guidance, and first-person works such as Peep Show, Hardcore Henry, Being John Malkovich, Half-Life.

## Searches spent (20 of 20)

1 Cohn eye tracking layouts. 2 Composition, lines, thirds, gaze. 3 POV film, direct address. 4 Colour scripts. 5 Art bibles. 6 WCAG, Harding. 7 Foulsham, attentional synchrony. 8 Cyberpunk 2077 dialogue. 9 Noir lighting. 10 Cyberpunk clichés, techno-orientalism. 11 80s cel materials. 12 TF2 silhouette plus dark-skin lighting. 13 Motion comics failures. 14 Gaze, sexualisation. 15 TF2 silhouette. 16 Limited animation. 17 Art direction feedback. 18 AI sameness. 19 Neon, saturation, fatigue. 20 First-person comics, visual novel sprites.

Blocked: Medium (two critique posts), MoMA, Unreal Engine (Orbitals), DOAJ pages, all 403 and not worked around. Paywalled: Guardian via inkl. Dead: GDC session page, Time on Alton, Badman's first-person essay, the varley review URL I tried, ebusca record.
