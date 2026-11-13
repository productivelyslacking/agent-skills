---
name: production-stages
description: When to commit to what in a game or story production: what each stage must prove, locks, late changes, playtests and tester counts, when final art and voice start. Use when planning milestones, before spending on final assets, or when a test result arrives.
---

# Production stages

Assumes **ground-truth**; **agent-team** runs the work, this says when to commit it. Thesis: **commit to each expensive
thing only after the cheapest test that could change it has run, and finish last.** The failure this prevents: a lot of
finished art around a story that's still moving.

**How far to trust this.** Research-based and unproven: written from a review, not from use (D25 in the library's
`docs/DECISIONS.md`). Nothing found compares production orders under control; the strongest source on order is a volunteer
survey, on story testing one consultant's guide, the rest mostly makers on their own work, much of it second-hand. Nobody
measured overhead at this size or studied an AI studio. The cases, numbers and dates behind the rules are in `NOTES.md`
beside this file, read on demand.

**Reading a rule.** Claim, reason, kind, tag. `[G-C3]`, `[F-C6]` are claims in `EVIDENCE-PRODUCTION.md` beside this file (Part G
games, Part F film and animation), with their limits; `[G-S7]` is a section; `[F-REEL]`, `[F-TABLE]` are Part F's draft reel and stage
table; `[DR-54]` is in `../directing/EVIDENCE-DIRECTING.md`. Kinds: *measured*; *practitioner*; *demonstrated* (a production did it,
which says nothing about cause); *inference*, the research author's, or *inference (editor)*. Read the entry before relying on a rule
in a hard decision.

## The biggest alarm

- **Stop finishing when finished art outruns the resolved story.** Keep one count on the board: scenes with finished assets that
  don't meet "When finishing may start" below (a look test's shots don't count). Above zero, start no more finishing until that
  scene is tested or reverted, and report it. A feature that did this cut finished minutes and still lacked key story.
  Demonstrated, one case through a secondary source; the top-alarm reading is inference, the count inference (editor) [F-C36].
  A cancelled game with polished cutscenes first is close; self-reported [G-C3].
- **Holding back finishing doesn't make the story right:** passing review means coherent, not wanted. Demonstrated; the reading is
  inference [F-C6].
- **A showcase can starve the rest:** budget all planned episodes together before finishing the first. Demonstrated; the rule is
  inference [F-C49, F-C9].

## Stages: what each must prove

**Never put a bare stage name in a brief; write what's frozen and what may be placeholder.** Definitions of alpha and beta
disagree, and no publisher's own guideline was found. Practitioner [G-C1, G-C2]. The order below is inference (editor); skip
what a project doesn't have.

| Stage | Must prove | May be rough | Commits | From |
|---|---|---|---|---|
| Spine | What it's about, where it ends or can stop, each major character's exit | Everything | The spine, not each beat | F-C29, F-C30, G-C38 |
| Slide test | Who wants what, what just happened | Frames | What the reel must fix | G-C20 |
| Story reel | It plays in real time; order and length | Pictures, voice | Order and lengths, still rebuildable | F-C1, F-C2, F-REEL |
| Risky prototype | One question the story or play rests on | All else | That mechanic | G-C6, G-C37 |
| Look test | How the finished look lands | Story content | The style | F-C47, F-C49 |
| Layout | Framing and staging, before any motion | Finish | Composition | F-C7 |
| Scratch or provisional voice rounds | Performance, which can change the story | Other scenes | A tracked as-recorded script; final voice is finishing | G-C8, F-C30 |
| Owner's first play (if story is kept from them) | Whether they're entertained, surprised and want to go on; their call on the story | Picture, motion, mix | Nothing: changes go on the change list | D25 |
| Scene finish | Nothing about story: movement, touch-up, mix | Nothing | That scene | F-TABLE |
| Public release | A separate gate with its own bar | Nothing it shows | The launch moment | G-C4, G-C31 |

**A final-quality vertical slice is not the default:** build one only for a buyer or a named pipeline risk, and only as final as
that question needs. Practitioners disagree and nothing is measured, so this is a pick. Practitioner [G-C6, G-C1, G-C8].

## Tests attach to commitments

- **Name the test before each commitment, not at a milestone** ("before we finish this scene's stills", not "at beta"): tests
  synced to alpha or beta find problems no one can still act on. Practitioner with a consultant's interest [G-C23].
- **Write pass and kill criteria before the test, so nobody moves them afterwards.** No source gives story pass numbers or kill
  criteria: choose per project. Inference [G-C45, F-C33, G-S7].
- **In one game, kill units of story, and cut before characters and art attach; protect named high-risk scenes from the harder
  gate,** which would have cut the hardest ones. Demonstrated, one team's hindsight; the protected list is inference [G-C37, G-C45].
- **Budget several full rebuilds as the job, in short cycles,** without copying any studio's count or cycle length. Practitioner;
  the short cycles are inference [F-C1, F-C2, F-C4].

## Keep text apart from picture and voice

- **Store story text as data keyed by ID, so a line changes without touching a still or a take:** late story change is cheap only
  when decoupled. Demonstrated; the lesson is inference [G-C33, F-C37].
- **Voice brings lock pressure back, so decide per scene what's bound to what.** Record in rounds, scratch voices first, with an
  as-recorded script as the source of truth; voice before or after picture is a choice.
  Practitioner [G-C8, G-C39, F-C1, F-C8]. Keep with each take the text it was made from, so a stale take shows. Inference (editor).

## Cheap tests first

- **Test comprehension from slides, one person at a time, before any still is final:** show beats, ask open questions per beat,
  and repeat later, because format changes results. Practitioner, no data, sells services; the most directly usable source found [G-C20].
- **Then a timed reel of the whole episode, with scratch voice and one placeholder per beat,** so a problem is seen before it's argued.
  Practitioner; the contents are a draft no source describes [F-C2, F-REEL].
- **Rough tests probably answer "can they follow it", not whether "do they feel it":** usability problems survive low fidelity, but
  looks shift emotion. Don't compare scores across finish levels, or call a scene weak or safe from a rough build (owner's play: below). Measured off-domain, practitioner [G-C11, G-C12, G-C7, G-C9, F-C21].

## A separate look test

- **Test the finished look on its own: a couple of finished shots, reviewed apart from the reel,** since a reel can't test how a
  look lands. Demonstrated; the reading is inference [F-C47, F-REEL]. **The owner judges it** (agent-team), on frames with no plot if
  story is kept from them (**directing**).
- **Decide limited motion as a style, early.** Narrow, inference [F-C38].

## Lock the spine, finish scenes on evidence

- **Fix the spine early, and keep scenes and dialogue open until their evidence is in.** Disputed (some makers start without an
  ending); the spine comes first here, for stories resting on planted facts. Demonstrated; the pick is
  inference (editor) [G-C38, F-C30, DR-3, G-C37, F-C11].
- **A pass releases the next scenes' story and rough assets, not their finishing.** Test the hardest scene first: easy ones prove
  nothing. Inference [G-S7, G-C37].
- **When finishing may start: all four, on the board by ID.** (1) The scene's chapter or reel has had a story test against written pass
  criteria, one round per unit, since fresh testers are single-use. AI cold reads alone release rough work, never finishing; with
  no other human test, the owner's play is the story test. (2) The named judge said yes: the owner, who reads the story or, if it's
  kept from them, has played that chapter; the director's yes alone releases rough work. (3) The look test passed. (4) Nothing is open
  on that scene in the change list. "Finished" means movement, touch-up, final voice or mix, the work a story change would redo;
  generated drafts aren't finished. Rough art may hide some weight from the play [G-C7], so the play decides plot, order and pacing,
  and mood stays provisional until finished scenes reach the owner. Inference (editor).
- **A lock is an agreement, not a wall: write what happens when it breaks,** since true locks erode and very late changes are common.
  Practitioner, one analyst's count [F-C12, G-C5].

## The change list

- **After a gate, every change gets one line: what changes, what depends on it, its estimated cost then its measured cost, who agreed.**
  Don't ban late change; rule on the price, and batch changes, since each costs review attention. Practitioner, demonstrated, measured;
  the form and the batching reason are inference [F-C47, F-C52, G-C14, G-C26].
- **Measure the price in this pipeline, and don't cite a curve:** no game or film source measures the slope. One survey ties frequent
  core-design change to worse outcomes, but can't separate "test before committing" from "don't change". Hold both, and count the
  dependents. Measured with those limits [F-C13, G-C15, G-C26].

## Testers: a budget

- **A fresh tester is single-use for story, so budget them like money.** Repeat players are fine for mechanics, not story. Practitioner
  [G-C20, G-C18]. Generation makes options cheap and testing no cheaper, so don't generate more than you can test. Inference [G-S5].
- **About six per round finds problems and sizes nothing.** A clean round isn't proof: run a second fresh round before a costly
  commitment, per chapter, not per scene. Practitioner, measured off-domain, inference [G-C21, G-C22].
- **Ask for retellings and confusions, not scores.** Ask: what just happened, what do they want, what do you expect next, how much do you
  want to know what happens next (asked repeatedly; the drop-off is the finding), and pick words for how you feel, against the intent. Not
  "did you like it" or "any ideas". Report counts and scene IDs, not percentages. Follow up a confusion, curious or lost? Practitioner,
  unvalidated; comprehension fixes have the cleanest stories, all selected [G-C20, F-C14, F-C27, F-C16, DR-47, DR-59].
- **One person at a time, a silent observer, individual answers before any talk.** Read "focus group" as this: groups report what people
  say, not do, and suit early wants, never a choice between story options. Practitioner, partly off-domain; no comparison in games; the
  last clause is inference [G-C17, G-C18, G-C19]. **gamedev-team-practices** has the rest of watching.
- **Where story is kept from the owner,** they may recruit and don't read results. Use a human stand-in if they agree, or a self-run form
  saved to `sealed/` (untested, weaker than moderated); with neither, say the owner's play is the first human story test. Inference (editor).
- **Name who you asked:** first-read testers from comparable games, who recount beats to prove attention; friends, family and industry
  can't give that; experts give craft critique. Practitioner, reported [G-C20, G-C25, DR-48, G-C24, G-C32].
- **Treat a test as a diagnosis, not a forecast:** nothing found shows testing improves a work or how good its diagnosis is. A good
  round predicts nothing; a weak one is a reason to ask why. Practitioner, contested [F-C26, F-C27, F-C17, F-C18, F-C28, DR-50].
- **Fix or taste, by a test written beforehand** (no study found): failure against written intent is a fix; interest falling at one point
  for several testers is a fix or a cut; stated preference is taste; a popular request against the written vision is the decision-holder's
  call, logged. Inference [G-S7, G-C32].
- **An owner who has read or built a thing can't test what depends on not knowing it** (a sealed owner can for story, not for tutorials or
  difficulty). Practitioner; no study of owner-designers was found [G-C24]. Single-use reactions and AI cold readers: **directing**.

## What's specific to generated assets (all inference)

Hypotheses to measure in your own pipeline; no opened source measures them for an AI studio, and no first-hand postmortem of a
generated-image comic was found [G-S5, F-C45].

- **Cheap per piece isn't cheap to change.** What remains: owner attention per review, consistency across a set, regeneration when one
  story change touches many scenes. A beautiful still also anchors people even when it cost little.
- **Rights come before finishing, and aren't settled here.** A US Copyright Office decision recognised a comic's text and arrangement and
  refused its generated images; not legal advice [F-C44]. Clear music before picture finishes [F-C43]. Voice law wasn't researched [G-S5].

## What a small team skips

The skips are inference.

| Skip | Why |
|---|---|
| A score from recruited viewers, research firms, genre norms | Hundreds of viewers make that number; yours can't [F-C14] |
| Choosing a methodology | No correlation with outcome, one self-report survey [G-C26] |
| Long design documents | Nothing measures length; an early document barely tracked outcome, one self-report survey; a designer argues against them, no data. Keep a log tied to the played build [G-C26, G-C44] |

Don't cite a late-change multiplier [G-C15], five testers as enough [G-C22], or "90% of films are tested" [F-C15].

## Not established

Write as unknown: what rough art does to judgement of mood or story; late-change cost in a game; when art should go final (no source gives
a rule); fix versus taste; owner-designer feedback; audience tests of motion comics; how generation changes rework. Each part of the
evidence file ends with its full list.
