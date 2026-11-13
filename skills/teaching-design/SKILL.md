---
name: teaching-design
description: Teaching a skill so it lasts: courses, lessons, onboarding, practice and review, quizzes, feedback, hints, mastery gates, AI tutors. Use when designing or reviewing learning material or a learning product. Programming: also teaching-programming.
---

# Teaching design

Assumes **ground-truth**. Thesis: **design for what the learner can do later, alone, and judge the design by a test of
exactly that.** The failure this prevents: a lesson that feels good, gets finished and teaches little, which passes
every check that measures enjoyment or assisted success.

**How far to trust this.** From a literature review, not from use (D22 in the library's `docs/DECISIONS.md`), mostly read
as abstracts; almost no source studied an adult learning alone and unpaid, so effects give direction, not size. Each rule
shows its rating and entry: `[L-C3]` is C3 in `EVIDENCE-LEARNING.md`, `[G-C1]` is C1 in `EVIDENCE-CODE-GAMES-AI.md`, both
beside this file; `[Pn]` is in `../psychology-review/EVIDENCE.md`. A rule that is reasoning, not a result, says so here or in
its entry. Read the entry before relying on a rule in a hard decision, and quote a number only with its population. Don't
add papers from memory: confirm one exists and read it first. Effect sizes, samples and dates are in `NOTES.md` beside this
file, read on demand.

## What counts as learned

- **An assisted solve is not skill.** Check the same skill with help off, on a task with a changed surface, and at least
  once after a delay. Strong that task performance and learning come apart. Moderate that unguarded AI lowers learning below
  no AI: one large trial found AI raised practice and cut the unaided exam, one small trial agreed, two found no difference
  [G-C1, G-C13].
- **Never count ease, speed, satisfaction or self-rating as learning:** active classes felt less effective and tested higher.
  "Ready to move on?" never unlocks anything; a skip is a test. Moderate [L-C16, L-C18, G-C7].
- **Report engagement and learning as two numbers:** an easy, well-liked design may be the failure. Moderate [G-B7].
- **Test late.** Retrieval and spacing can tie or lose on an immediate test and win at days or weeks, so a check run straight
  after the lesson can pick the wrong design [L-C1, L-C3].

## Practice

- **Make the learner produce it from memory, rather than re-reading.** Strong for retention, moderate for complex material
  [L-C1]. If first attempts would mostly fail, shrink the cues rather than drop the attempt: moderate that scaffolding helps,
  weak for any specific ladder [L-C2].
- **Space across days by the clock, not by unit,** since a binge gets almost no spacing. On return, start with a short cold
  recall from earlier units (inference). Gap: about 20-40% of a week's target, 5-10% of a year's. Strong that spacing helps; moderate on the numbers, which rest largely on one large study of facts [L-C3].
- **Don't build expanding-interval machinery:** expanding gaps didn't beat equal ones. Adaptive schedules beat fixed ones in some
  studies, on many small items; a short course may have too few to adapt on (inference). Moderate [L-C4].
- **About three correct recalls in a sitting, then come back; plan about seven practice chances per skill across the course,**
  not seven in a row. Moderate, from concept and maths material; the seven rests on a disputed model and more practice isn't
  worthless, so treat these as starting points [L-C5].
- **Interleave only what a learner must choose between:** topic-per-unit at first contact, then later units make the learner pick
  among earlier tools with no label. Mixing unrelated topics showed no reliable effect. Moderate; none of it tests code [L-C7].
- **Vary the surface and test on new problems.** Near transfer can be taught through varied practice and comparing cases; far
  transfer rarely happens, so don't promise general thinking skills. Moderate [L-C17].
- **Guessing before study is worth doing; struggling first is contested.** A wrong guess followed by correction helps, moderate;
  whether early failure drives voluntary learners away is unknown, so measure it [L-C15]. A try-first task suits concepts, not bare
  syntax, and works only if short, supported and built on afterwards; plan on the review's unadjusted effect (the evidence author's
  judgement). Unassisted discovery loses to explicit teaching [L-C14].

## Guidance

- **Novices get heavy guidance, checked per topic, not per person;** experts do better with less. Withholding costs a novice more
  than giving costs an expert, so when unsure, give the help. Skipping must be a test on that topic. Strong, weighted to maths and science [L-C8].
- **Show correct worked examples, then a similar problem.** Strong [L-C8]. Don't append "explain why" after every example: added
  prompts had a negative effect in maths. Contested [L-C10]. Blanking the last step is cheap; adaptive fading isn't justified.
  Contested [L-C9].
- **Gate only true prerequisites, and watch every gate,** since mastery gates often cut completion. Separate progress from recorded
  mastery, so a stuck learner carries on with a marked gap. Moderate for the
  trade-off, from old college data; the soft gate is inference and untested [L-C6, G-B9].
- **Bloom's 2 sigma is not a planning number.** It comes from two dissertations [L-C6].
- **Expect to lose people early,** self-paced more than scheduled. Moderate to strong; MOOC learners may have other goals [G-A12].
  A first unit finishable in one sitting with a real result is the evidence author's reasoning, not a tested remedy [G-A12].
- **Don't rely on prompts to plan or set goals:** they didn't raise completion. Strong for one-off prompts in MOOCs. Sustained
  self-regulation training is a different case and helped university students: moderate [L-C19].

## Feedback and hints

- **Say why, on every wrong answer:** elaborated feedback beats the correct answer, which beats right/wrong. Budget written
  explanations per task, specific to the wrong answer. Keep it about the task, since effects fall as attention moves to the self.
  Strong [L-C12]. So praise like "you're a natural" probably weakens it (inference) [L-C12].
- **Respond when an attempt is finished.** Don't build artificial delay; revisiting later gives the spacing. Contested [L-C13].
- **Don't assume hints help, and don't treat "abstract to concrete" as established:** results run both ways, and no randomised
  test of programming hint ladders was found. Moderate that hints aren't reliably helpful [G-C10]. A concrete hint earlier, then
  applying it to a changed task, and reacting to rapid hint clicks, is the evidence author's suggestion: weak or unknown [G-C10].

## Confidence and motivation

- **Build confidence with a real, checked success, not by asserting it:** past performance predicts later self-efficacy more than
  the reverse. Moderate to strong on direction, for performance; no evidence on quitting; that reassuring lines do less is
  inference [P6]. Flag a line claiming talent or standing in for a success, not a belief tied to a standard, and keep that belief
  about the work [L-C12].
- **In critical feedback, state the standard and that you believe this learner can meet it.** It beat buffering with praise or
  standards alone among Black students; among White students, effects were small or absent. Moderate in that setting, one
  research line; nothing for adult beginners or a tutor. A cheap default, not a measured lever (inference) [P19].

## AI tutors

- **A teaching prompt won't produce learning:** a large preregistered trial found no effect (read through a summary), and
  hint-only tutors only removed harm. Moderate, contested: the main positive trial ran a whole structured lesson [G-C2].
- **Give the tutor this task's solution and known mistakes,** which offline hints also need, so author it once [G-C2].
- **Enforce withholding in code, not by prompt:** refuse the full solution and code filling the learner's blanks, since a pressed
  model may not withhold on a prompt alone. Weak, inference [G-C12].
- **Handle two cases differently.** Syntax and reading the learner's own error get a direct answer; plan and logic get guidance.
  Socratic refusal of syntax help is the likely failure. Inference from a small study [G-C5].
- **Ask for the next step before showing code:** it improved self-judgement and unaided use. Moderate to weak, short lab tasks with
  undergraduates [G-C4].
- **No insert button and no copyable solution:** paste raised solution requests, many with no attempt. The cheapest supported
  change, moderate, though paste wasn't randomised [G-C3].
- **Hand-written help is the reference, not the fallback;** LLM help failed quality checks on some problems. Check LLM output
  before the learner sees it. Moderate, older models [G-C11].
- **Prefer checks on the learner's own step over free chat:** step-based tutors' evidence doesn't transfer automatically to chat.
  Strong for classic tutors, weak for LLMs [G-C9].
- **Don't assume a tutor retains anyone,** and make sure a learner who never opens it still succeeds. Moderate, one course [G-C6].
- **Assume a chatbot is one tab away.** Withholding works only if the learner chooses it, so explain why. Weak to moderate [G-C5].
- **Don't cite a pooled "AI improves learning" number:** a preprint audit finds severe publication bias, and one was retracted.
  Ask what the treatment and controls were, and whether the outcome was assisted [G-C8]. These results age fast.

## Story, rewards and games

Name the job. Story in a learning product is there for persistence, which is a hypothesis to test, not a teaching method.

- **Assume story adds no learning; give it a budget and test a thinner version.** Moderate on average, contested for engagement
  and long play; almost no adult evidence [G-B3].
- **A story wrapper doesn't appear to hurt task performance,** so write it freely and keep the task clear. Moderate, university
  novices, performance rather than learning over time [G-B4].
- **Make the task the mechanic:** if story and task could be swapped independently, integration has failed. Moderate from
  children's evidence, weak for adults, not independently replicated; that alternating cutscene and exercise is the weaker design
  is inference [G-B6].
- **During work, hide everything the step doesn't need:** irrelevant detail costs learning, persistent detail most. Moderate in
  text and multimedia, weak when applied to a game with pauses [L-C23, G-B5].
- **Default to no points, badges or leaderboards, and test any you add:** pooled effects are small, positive and very mixed, and
  leaderboards and badges have backfired. Moderate [G-B1].
- **Default to no side objectives unless they reinforce the main goal;** others hurt player retention. Moderate, from commercial
  casual games with no learning measure [G-B10].
- **Rewards are contested:** avoid rewards for merely showing up. Whether a story reveal counts as a reward is unknown [L-C21, G-B2].
- **Explain why each skill matters, and offer small choices.** Moderate for association; causal evidence is thin [L-C21]. Trials
  had students write the connection themselves [P9] or gave a rationale for a dull lab task [P2]; a character is untested.

## Voice, text and motion

"Don't narrate on-screen text" merges different cases [L-C24]. Keep them apart:

| Case | Evidence | Do |
|---|---|---|
| Text leads, voice is added | No gain | Add voice for atmosphere or access, not learning (motivation untested: measure it); it can be turned off, and text never waits on it |
| Voice leads, text is added | Gain on average | Add text, but see the next rows |
| A picture or animation is also on screen, or the learner sets the pace | Benefit disappears (moderator analyses, mixed) | A transcript adds little here |
| Code or a diagram needs attention | Key terms usually beat full text (a mixed moderator from one thesis); applying this to code is inference | Show 2-3 word labels beside it; no transcript while they're working |
| Subtitles | Thin for native speakers; non-native evidence is mixed | Always offer the toggle; don't remove them on the strength of the redundancy principle |

Also:
- **Spoken vs on-screen tutor help is contested** [G-B5, L-C23].
- **Signal the current step, and keep explanation beside what it explains.** Strong, both through one overview; smaller when
  learner-paced [L-C23].
- **Segment into meaningful chunks.** Moderate. Putting something to do between them is the evidence author's suggestion for code,
  not a tested result [L-C23].
- **Motion earns its place by showing something:** meaningful animation helps, decorative doesn't [L-C26].

## Don't design around

| Idea | Why not |
|---|---|
| Learning styles | Few direct tests, all null [L-C25] |
| The learning pyramid ("90% of what you teach") | Its numbers aren't from research [L-C25] |
| Growth-mindset lessons | Not significant after bias correction [L-C22] |
| 85% correct as the ideal difficulty | Derived for machine learners on binary tasks; no human trial seen [L-C25, G-B7] |
| Learner control as a learning feature | No overall effect; stop, replay and step-through helped, in limited evidence [L-C20] |
| A 10-15 minute attention limit | Primary data don't support the number [L-C25] |
| A "how hard was that?" rating as success metric | Load scales are poor measures; decide on delayed tests [L-C11] |

## Not established

Write these as unknown rather than filling them in: voiced motion comics; in-character AI tutors; hint ladders; story gated
on mastery; any narration or subtitle study with code as the visual; months-later retention with AI tutors; voluntary adult
self-learners generally. The evidence files end with the full list.
