<!-- Research notes from 2026-11-06, kept as written apart from this note and removed references to the session's scratch files.
Rules and how to use them are in SKILL.md. "The game" throughout means the project that prompted the review: a self-paced web
game teaching Python to an adult who knows some scripting, told as a voiced detective story with an AI tutor. "The other agent"
means the author of the sibling evidence file. The citation-check script was not kept; its results are stated here (D22). -->

# Teaching programming, games and story, AI tutors: evidence base

Date of research: 2026-11-06. Search budget used: 30 of 30 web searches, plus Crossref, OpenAlex, arXiv and ERIC API lookups.

## How to read this

**Read levels.** `full` = I obtained the full text and read the methods, results and limits sections directly (not every page), except [clark2016], read through a fetch tool's extraction of the page, and [bastani2025], whose full text I read in the SSRN preprint version; the PNAS abstract states the same headline numbers. `abstract` = abstract only (some through ERIC or OpenAlex). `secondary` = a search summary or index page, not the paper. Numbers appear only where read in a paper or abstract, unless marked secondary.

**Ratings.** strong = several good studies or a meta-analysis, consistent. moderate = some good evidence with real limits. weak = thin, small, or only observational. contested = good evidence on both sides. A rule marked *inference* is my reasoning from the evidence, not something a study tested.

**Population warning.** Almost nothing here tested an adult self-learner in a story game. Most data is university students, school children, or crowd workers. The closest to the target learner are [lee2015] (adults on Mechanical Turk, median age 23 to 25), [lehmann2024] (lab, 78% no Python, university setting) and [nie2024] (free online course, 146 countries).

## Findings that argue against the current design

1. **Unrestricted help.** No trial I read shows unrestricted AI help significantly raising later unaided skill. Unguarded GPT-4 cut later exam scores 17% in a trial of about 1,000 students [bastani2025]. Other trials found gains in task score and none in learning ([bassner2026], [lehmann2024]). The nearest to neutral is children using Codex: no harm, no significant gain [kazemitabaar2023]. See C1.
2. **The tutor prompt will not solve it.** Hint-only tutors removed harm but did not beat no AI at all ([bastani2025], [bassner2026]). A preregistered 1,059-student trial of pedagogy written into system prompts found no effect on any confirmatory measure [barth2026]. See C2.
3. **Offering the tutor may lose players.** Offering GPT-4 in a free online coding course cut exam participation 4.3 points overall, though only 14.2% used it [nie2024]. See C6.
4. **Story did not improve learning.** Removing a detective story from a learning game changed nothing significant (d = -0.16) [adams2012]. Medium-depth story had the lowest effect in the K-16 meta-analysis (g = -0.03) [clark2016]. Comic cutscenes changed nothing for children, on learning, enjoyment or time [sykora2020]. See B3.
5. **Alternating story and code is the weaker structure.** The design "story pauses, player writes code" risks being the extrinsic variant that lost to intrinsic integration [habgood2011]. See B6. This is my reading of the structure; nobody has tested this game.
6. **Voiced characters.** Pedagogical agents that communicated through on-screen text beat narrating agents, and agents helped post-secondary learners less than K-12 [schroeder2013]. No study of a voiced motion comic was found. See B5.
7. **In-game hints.** All four hint designs lowered performance against no hints in a 50,000-child game study (small effects) [orourke2014]. See C10.
8. **Self-paced and mastery-gated.** Same programming MOOC: 45% retained on a schedule, 13% self-paced (not randomised) [ihantola2020]. Self-paced mastery programmes "often reduce the completion rates" [kulik1990]. See A12, B9.

## Top rules

| Rule | Rating | Entry |
|---|---|---|
| Never count an assisted solve as proof of skill; check the same skill with the tutor off | strong (dissociation) | C1, C13 |
| Don't tune on playtime, completion or self-report; A/B on unaided score | moderate | B7, C7 |
| Assume the story adds no learning; give it a budget and test a story-off variant | moderate | B3 |
| Make the code the investigation, so output changes the case | moderate, children only | B6 |
| Put the solution and common errors in the tutor's context, and enforce withholding in code, not by prompt | moderate | C2, C12 |
| Ask the learner for the next step before showing code | moderate to weak | C4 |
| Keep hand-written hints as the reference, not the fallback | moderate | C11 |
| Predict the output before writing, in every case | moderate to weak | A1, A2 |
| Name false friends from the player's own prior language | moderate | A10 |
| Make case 1 finishable in the first sitting; expect dropout early | moderate | A12 |

---

# C. AI tutors

## C1. Unguarded AI raises task performance without raising, and sometimes lowering, later unaided performance

- **Rule.** Never treat a solve done with tutor access as evidence of skill. Testable: for each case, compare assisted score with score on an isomorphic task with the tutor off. A gap means the tutor did the work.
- **Sources.** [bastani2025] full; [shen2026] full; [lehmann2024] full; [bassner2026] abstract; [chen2025] abstract; [fan2024] abstract; contrary [kazemitabaar2023] abstract, [lyu2024] abstract, [nie2024] full.
- **Design, population, model.**
  - [bastani2025]: preregistered RCT, about 1,000 Turkish high school students, four 90-minute sessions, autumn 2023, GPT-4, maths, one school.
  - [shen2026]: randomised, preregistered, preprint, **vendor flag: Anthropic authors**, testing GPT-4o; 52 crowd-worker developers with more than a year of Python learning the Trio library; quiz right after the task. The result runs against the vendor's interest.
  - [lehmann2024]: preprint, two preregistered lab experiments (N = 108; N = 69), 78% no Python experience, 45-minute learning phase, gpt-3.5-turbo-0125, June 2024.
  - [bassner2026]: three-arm RCT, N = 275, CS1 at TUM, one 90-minute concurrency exercise; **probably developer-run** (Iris and the study are both from TUM; not confirmed in the abstract); versions of Iris and ChatGPT not in the abstract.
  - [chen2025]: preprint, N = 24, ChatGPT. [fan2024]: N = 117 university students, writing, ChatGPT version not stated in the abstract.
- **Effect as stated.**
  - [bastani2025]: practice +48% (GPT Base), +127% (GPT Tutor). Exam without AI: GPT Base -0.054 on a 0 to 1 scale, "17% reduction"; GPT Tutor -0.004, not distinguishable from control.
  - [shen2026]: quiz lower by 4.15 of 27 points, "17%", d = 0.738, p = 0.010; task time not significantly different (p = 0.391).
  - [lehmann2024]: "no effect of LLMs on overall learning outcomes". Pre to post gain, control vs LLM: 4.8 vs 5.4, then 4.2 vs 5.0.
  - [bassner2026]: both AI arms "substantially higher" exercise scores; neither "produced greater pre–post knowledge gains or code-comprehension advantages".
  - [fan2024]: essay scores improved; knowledge gain and transfer "not significantly different".
- **Rating.** Strong that task performance and learning come apart. Moderate that unguarded AI lowers learning below no AI: one large trial and one small one say yes, two say no difference.
- **Limits and contrary.**
  - [kazemitabaar2023] found Codex raised authoring (1.8x scores) without lowering manual modification, and one-week retention was slightly better, not significant: 69 learners aged 10 to 17, Codex.
  - [lyu2024] found higher final scores with CodeTutor: 50 students, semester, preregistration not stated, **developer-run**, and final scores may include tutor-assisted work (the abstract does not say).
  - [nie2024] estimated +6.8 points for adopters, a modelled complier effect from an optional exam.
  - Bastani was children doing maths in class. Shen's quiz was immediate. No trial measured months-later retention in adult self-learners.
- **What it changes.** "Allowed to help anywhere" can stay only if progress and any record of skill come from tutor-off checks. Without those the game cannot tell whether the player learned.

## C2. Hint-only guardrails remove harm but have not shown gain over no AI; prompts alone steer weakly

- **Rule.** Don't expect a pedagogical system prompt to produce learning. Give the tutor the solution and known mistakes for this exact task. Test the tutor against a no-tutor arm, not only a chatbot arm.
- **Sources.** [bastani2025] full; [bassner2026] abstract; [barth2026] secondary (the abstract, via the ICER page's summary and short quotes); [kestin2025] full; [nie2024] full.
- **Design.** Barth: preregistered three-arm crossover, 1,059 CS1 students, six weeks; prompts built on Zimmerman's self-regulation model and Chi's ICAP; model not read. Kestin: RCT crossover, N = 194, Harvard physics, GPT-4, 2023, median 49 minutes, tutor prompts carried expert step-by-step solutions, compared with an in-class active learning lesson.
- **Effect.** Barth: "no statistically significant differences between conditions" on four confirmatory measures; exploratory, more time on task and longer messages. Kestin: linear regression effect 0.63; quantile regression "0.73 to 1.3 standard deviations", post-test median 4.5 vs 3.5. Bastani GPT Tutor exam: -0.004.
- **Rating.** Moderate; contested on whether AI tutors can beat good instruction.
- **Limits and contrary.** Kestin is the main positive result. The tutor was a whole structured lesson with hand-authored solutions, first exposure, immediate post-test, no retention measure, elite students. Authors say effects "may also depend on" expert prompts and warn against use "as a crutch". Bastani's practice gain shows hand-given solutions in the prompt matter (they attribute the Tutor-vs-Base gap to them). Bassner: Iris alone raised intrinsic motivation. [nie2024] had prompts "to prevent students from seeking direct solutions" and still lost engagement.
- **What it changes.** Each case needs authored solution, misconceptions and hint material in the tutor's context. A persona prompt is not a teaching design. Budget for authored data per case, which is also what offline hints need.

## C3. Asking for explanations and asking for solutions have different effects, but the evidence is exploratory

- **Rule.** Make explaining the easy path and getting code the hard one. Testable: log the share of tutor requests that ask for a solution, and watch it against unaided score. Block paste between tutor and editor.
- **Sources.** [lehmann2024] full; [shen2026] full; [chen2025] abstract; [bastani2025] full.
- **Effect.** Lehmann: substitution raised topic volume and lowered understanding; complements raised understanding. Enabling copy-paste raised messages from 4.45 to 7.71 (p = 0.002) and solution requests (p < 0.001). "42% of messages asking for a solution were sent without a single attempt". Shen: six usage patterns, three preserved learning. Bastani: the most common message to GPT Base was "What is the answer?".
- **Rating.** Moderate for the friction effect (Study 3 ran three weeks after Study 2 with paste enabled; paste was not randomised and Study 2's block was accidental). Weak for causal claims on usage patterns, which are exploratory and self-selected. Chen also reports that minimal use gave weak gains, so avoidance isn't the goal.
- **What it changes.** No "insert this code" button. The tutor offers no copyable solution block. Costs almost nothing and is the cheapest supported change.

## C4. Making learners state the next step before seeing code helps calibration and unaided application

- **Rule.** Before revealing any code, require the learner to say what should happen next. Testable: A/B lead-and-reveal vs direct reveal, measure tutor-off isomorphic task and perceived vs actual ability.
- **Sources.** [kazemitabaar2025] full; [tranle2026] secondary; [marwan2019] abstract.
- **Design.** Kazemitabaar: between-subjects N = 82 then within-subjects N = 42, undergraduates in a data-structures course aged 18 to 23, GPT-4, 2024 to 2025. Tran-Le: AAAI 2026 pilot, college programmers, LeetCode-style tasks, N not seen; abstract says novices had "substantial post-test gains" (via a page summary). Marwan: randomised, MTurk novices, block-based.
- **Effect.** Kazemitabaar: the abstract names step-by-step dialog as "the most effective technique"; it "significantly improves alignment between perceived and actual coding ability without increasing cognitive load". Learners answered 58.0% of its questions correctly. Some reported frustration. Marwan: textual code hints raised immediate performance, and improved a later task only "when they were combined with self-explanation prompts".
- **Rating.** Moderate to weak. Short lab tasks, university students, one group, no long-term measure.
- **What it changes.** Gives the in-character tutor a shape: the partner asks "what would you check first?" before showing anything. In-character delivery is *inference*, untested.

## C5. Strict guardrails cost goodwill, and a self-learner can walk away to any chatbot

- **Rule.** Assume ChatGPT is one tab away. Withholding only works if the learner chooses it, so explain why and let a fair attempt unlock more. Testable: ask at exit, and track tutor abandonment by case.
- **Sources.** [eastwood2026] full; [bassner2026] abstract; [lyu2024] abstract; [xiao2024] abstract; [barth2026] secondary.
- **Design.** Eastwood: preprint, RCT, 132 intro students, four GPT-4o arms, 2026, three tasks. Xiao: think-aloud with 12 novices, GPT model family, 2024.
- **Effect.** Eastwood: Socratic with full context rated least supportive (significant); it also had highest external LLM use (23%, 7 of 30) and lowest full-comprehension answers, but those differences were "not statistically significant" (p = .48 for external use). Bassner: students rated unrestricted ChatGPT easier and more helpful, the authors' "comfort trap". Xiao: high-level hints alone "can be helpless or even misleading, especially" for next-step or syntax requests.
- **Rating.** Weak to moderate. Small, short, and mostly perception. No trial has measured bypass in self-learners.
- **What it changes.** Name two cases and handle them differently (*inference* from Xiao, n = 12): syntax and error-reading questions get a direct answer; plan and logic for the current evidence get guidance. Socratic refusal of syntax help is the likely failure.

## C6. Offering an LLM can reduce participation, and most people won't use it

- **Rule.** Don't assume the tutor is a retention feature. Testable: randomise tutor prominence in early playtests and compare case completion. Design so a player who never opens the tutor still succeeds.
- **Sources.** [nie2024] full (preprint; a search summary says L@S 2025, not confirmed by me).
- **Design.** RCT, 5,831 active students, 146 countries, free online coding course, GPT-4 with prompts against direct solutions, offered at week 4. Cohort course with sections, not self-paced.
- **Effect.** Exam participation -4.3 points (44.1% vs 48.4% raw), with falls in homework and section attendance. Only 14.2% adopted. Adopters' estimated exam gain +6.8 points. Students from low-HDI countries +14.8 points in participation. The authors' email discussed benefits and harms, so the advertisement itself may be the cause.
- **Rating.** Moderate. Large and randomised, but one course, and the mechanism is unknown.
- **What it changes.** Hand-written hints are the main help channel for most players. Frame the tutor as optional.

## C7. Learners overestimate how much they learned with AI, and weaker learners suffer more

- **Rule.** Never use self-report or enjoyment as a learning measure. Show the player their tutor-off result.
- **Sources.** [bastani2025] full; [prather2024] abstract; [lehmann2024] full; [kazemitabaar2025] full; [darvishi2024] abstract.
- **Effect.** Bastani: GPT Base students performed worse and "did not perceive" it; GPT Tutor students perceived gains they didn't get. Prather: 21 lab sessions; struggling students "finished with an illusion of competence". Lehmann: LLMs "widen the gap" by prior knowledge (exploratory). Darvishi: 1,625 students, peer review, "tended to rely on rather than learn from AI assistance" (non-generative feedback AI).
- **Rating.** Moderate to strong on overconfidence (independent settings agree). Weak on gap-widening. Contrary: [bastani2025] found "limited to no support" for preregistered heterogeneous effects, and [kazemitabaar2023] found prior Scratch skill helped.
- **What it changes.** The target adult "knows some scripting", which may put them on the better side, but they are still novices in Python. Whether this holds is unknown. A case-end "no partner this time" check is also the honest feedback the player lacks.

## C8. Pooled generative-AI effect sizes are not a safe basis for design

- **Rule.** Don't cite a pooled "ChatGPT improves learning" number. Ask of each study: what was the treatment, what did controls do, and was the outcome assisted?
- **Sources.** [bartos2026] abstract (preprint); [weidlich2025] abstract (preprint record); [deng2025] abstract; [wangfan2026retract] abstract (a one-line note); [huang2025] abstract (preprint).
- **Effect.** Bartoš: 1,840 effects from 67 meta-analyses, "severe publication bias"; adjusted SMD = 0.196, 95% credible interval 0.000 to 0.323, prediction interval -1.521 to 1.908. Deng: positive overall, warns of no power analysis and post-tests that may reflect output quality. Wang and Fan's meta-analysis was retracted in 2026; reason not in the note I read (a secondary source cites "discrepancies"). Huang: 133 studies, "positive but uneven".
- **Rating.** Moderate: the critique is largely preprints, but the retraction is a fact.
- **What it changes.** Decisions about the tutor should rest on the specific trials in C1 to C6.

## C9. Step-based intelligent tutors work, but this does not transfer automatically to LLM chat

- **Rule.** Give feedback on the learner's own step, not a free conversation about the problem. Measure on a test you didn't align to the tutor's script.
- **Sources.** [ma2014], [kulik2016], [steenbergen2014], [vanlehn2011], [nesbit2014], [crow2018], [pane2014], all abstract.
- **Effect.** Ma: 107 effects, 14,321 participants; vs large-group g = .42, vs other computer instruction g = .57, vs books g = .35, vs human tutoring g = -.11 (n.s.). Steenbergen-Hu: college, g = .32 to .37, earlier studies larger than recent. Kulik: median 0.66 SD, strongly dependent on locally developed vs standardised tests. VanLehn: ITS d = 0.76, human d = 0.79. Nesbit: 22 effects in CS, significant, no number in abstract. Pane: schools randomised in matched pairs; no first-year effect; in year two significant for high schools, not middle schools, about 8 percentile points.
- **Rating.** Strong for classic ITS against conventional teaching. Weak as evidence for LLM tutors.
- **Limits.** Mostly school and college, mostly maths. Effects shrink with standardised tests and fair controls. Crow is descriptive (features of programming tutors), no effect size.
- **What it changes.** A cheap non-LLM layer that checks steps (tests, output comparison, known-misconception matching) has more evidence behind it than free chat.

## C10. On-demand and in-game hints help less than expected, and how much escalation helps is unknown

- **Rule.** Don't assume hints help. Watch for rapid hint requests and respond to them. Testable: A/B hints on and off for one case on tutor-off score. **Do not treat "escalate abstract to concrete" as established.**
- **Sources.** [aleven2016] abstract; [roll2011] abstract; [baker2004] abstract; [orourke2014] full; [marwan2019] abstract; [xiao2024] abstract; [shih2010] secondary; [price2017] abstract.
- **Design.** O'Rourke: 50,000 children on BrainPOP, the fractions game Refraction, four hint designs (embedded or earned, abstract or concrete); play lasts a few minutes. Baker: classroom Cognitive Tutor users. Roll: 58 and 67 students, Geometry Cognitive Tutor. Price: 15 interviews.
- **Effect.** O'Rourke: "all four designs negatively impacted performance", "the size of these effects is small"; concrete hints got used more and helped win levels more than abstract ones; earned hints were hoarded and players persisted longer. Aleven: feedback on help seeking changed behaviour "but not" learning outcomes; "Help helps, but only so much". Roll: improved help-seeking transferred a month later. Baker: gaming the system correlated with post-test scores as strongly as prior knowledge. Shih: secondary only, bottom-out hints may act as worked examples. Xiao: lower-level hints with code examples helped.
- **Rating.** Moderate that hints aren't reliably helpful. Weak or unknown on the best escalation ladder: I found no randomised test comparing numbers of hint levels for programming.
- **Limits.** O'Rourke's hints were not on-demand tutoring, players were children, sessions were minutes. Pardos ([pardos2024]) found help beat no help in algebra and statistics.
- **What it changes.** Use the concrete hint earlier than doctrine suggests, then require the learner to apply it to a changed task. Log and react to rapid clicks in character.

## C11. Hand-written help is at least as good as LLM help, and LLM output must be checked

- **Rule.** Treat authored hints as the reference. Check LLM output against the case's tests before it reaches the player.
- **Sources.** [pardos2024] abstract; [santos2024] abstract; [leinonen2023] abstract; [denny2020] abstract.
- **Effect.** Pardos: N = 274; ChatGPT help had significant gains over control; no significant difference from human tutor help; "failed quality checks on 32% of problems", reduced to near 0% for algebra and 13% for statistics after self-consistency. Santos: n = 106, within-subjects, C, GPT-4 beat the stock message on 1 of 6 tasks; "Handwritten explanations still outperform". Leinonen: LLM messages "sometimes surpass" originals, rated by experts in artificial conditions per Santos.
- **Rating.** Moderate. Santos is C with GCC, not Python. Model versions are older than current ones. Students preferred LLM messages in Santos (secondary).
- **What it changes.** The offline hint set is not a downgrade. Author it first, then let the tutor draw on it.

## C12. What a tutor should refuse: expert practice, not tested policy

- **Rule.** Refuse the complete solution to the current task and code that fills the player's blanks, enforced outside the model. Allow concept explanations, syntax facts, and reading of the player's own error. *Inference* from the sources below; no trial compares refusal lists.
- **Sources.** [bastani2025] full; [liffiton2023] abstract; [codeaid2024] abstract; [pisan2026] abstract; [kazemitabaar2023b] abstract.
- **Design.** CodeHelp: 52 students, 12 weeks, **developer-run**, perceptions and usage, no learning measure. CodeAid: 700 students, 8,000 uses, thematic, no learning trial, **developer-run**, gives pseudo-code and annotates errors. Pisan: preprint, deployed system tuned with scripted personas, **no learners measured**.
- **Effect.** Pisan's claim: "a capable model pressed by a frustrated student does not withhold reliably on a prompt alone", so it uses a policy layer, a code stripper and a judge. Kazemitabaar 2023b: children, four coding approaches, "AI Single Prompt" among them.
- **Rating.** Weak.
- **What it changes.** An in-character prompt with "don't give the answer" will be broken by asking in-story ("Partner, just show me how you'd crack it"). Enforce in code. In-character pressure as a jailbreak path is *inference*, unmeasured.

## C13. Measuring whether the learner can now do it unaided

- **Rule.** Use tutor-off tasks isomorphic to practice, with changed surface, and at least once with delay. Include reading and debugging items. Don't let the same test double as practice.
- **Sources.** [bastani2025] full; [shen2026] full; [kazemitabaar2023] abstract; [kulik2016] abstract; [parker2016] abstract; [lee2015] full.
- **Effect.** Templates: Bastani's practice then unassisted exam; Shen's debugging, reading, conceptual and code items; Kazemitabaar's one-week retention post-test. Kulik: effects depend on who wrote the test. Parker: SCS1 is a validated, language-independent CS1 test, with "care must be taken to avoid undermining the validity argument". Lee: validated 24 items from 1,494 crowd respondents.
- **Rating.** Moderate as method. No validated Python-specific unaided test for adult self-learners found.
- **What it changes.** Ten cases, each ending in a tutor-off check on changed evidence, plus a return check on an earlier case. For the project's own playtest, SCS1 before and after gives an outside measure (not Python-syntax, licensed access not checked).

---

# A. Programming education

## A1. Tracing and reading relate to writing; sequencing them first is under-tested

- **Rule.** Before any writing task, have the player predict output of similar code. Testable: predict accuracy on each case's concept should precede and predict writing success.
- **Sources.** [lister2004] abstract; [lopez2008] abstract; [xie2019] abstract.
- **Design.** Lister: multinational, seven countries, students. Lopez: exam correlations after one semester. Xie: exploratory mixed-methods comparison of skill-sequenced material.
- **Effect.** Lister: many students "weak at these tasks". Lopez: correlations and a path diagram suggesting a hierarchy (a secondary source gives 46% of variance; not read by me in the paper). Xie: improved completion and error rate.
- **Rating.** Moderate for correlation; weak for "reading first causes better writing". I found no RCT of reading-first order. Secondary note: some weak students could write more than they could read, per a source I did not verify.
- **What it changes.** The motion comic can pause on a suspect's script and ask "what does this print?" before asking for code. Cheap.

## A2. PRIMM improved attainment in school, not yet tested on self-learners

- **Rule.** Use the sequence predict, run, investigate, modify, make within a case.
- **Sources.** [sentance2019] abstract.
- **Design.** 13 schools, 493 students aged 11 to 14, control group, 8 to 12 weeks, teacher-led, built on sociocultural theory. Randomisation not stated in the abstract.
- **Effect.** "Learners performed better in the post test than the control group"; no effect size in the abstract.
- **Rating.** Moderate for schools, weak for this learner. The rationale rests on language and mediation; whether a tutor can stand in for classroom talk is untested.
- **What it changes.** A case template that fits a detective flow: predict what the file says, run, investigate, alter, then write own tool. Fit is *inference*.

## A3. Parsons problems save time with equal learning, for novices

- **Rule.** Use them for first contact with a new construct to save time, with distractors built from known errors. Fade them. Never let them stand as proof of writing ability.
- **Sources.** [ericson2022] full; [ericson2017] abstract; [ericson2023] abstract.
- **Effect.** Ericson 2017: significantly less time than fix or write; "no statistically significant difference in the learning performance, or in student retention" a week later. Ericson 2022: "Only two randomized controlled studies" compare gains with writing, both undergraduates in Python; there is "evidence that some students strongly dislike them"; one study found them better for novices and fix/write better for more advanced students.
- **Rating.** Moderate. Mostly single-institution. The 2023 multi-institution work comes from the same working group, and its abstract reports no results I could use.
- **What it changes.** A scripter may be the "more advanced" case, so offer skip or go straight to writing. Mechanically, assembling a torn-up script suits the theme (*inference*).

## A4. Subgoal labels: helpful short-term and for those at risk, not always on exams

- **Rule.** Label steps in worked examples by purpose. Reuse those labels in tutor speech and hint text.
- **Sources.** [margulieux2012] abstract; [morrison2015] abstract; [margulieux2020] full.
- **Effect.** Margulieux 2020: quasi-experiment, five sections, 265 university students, one semester; quizzes improved, "not on exams"; students averaging 70% or lower: control 44% vs subgoal 25%; authors read this as half as likely to fail or withdraw (mechanism partly post hoc). Morrison 2015: "did not replicate as expected".
- **Rating.** Moderate, contested. University students; no study found in a game.
- **What it changes.** Consistent labelling across ten cases. Low cost.

## A5. Novices lack a working model of the machine; Python aliasing is a documented trap

- **Rule.** Treat "how Python runs this" as a learning goal. Show state changing line by line. Build a specific case around list references and mutation.
- **Sources.** [sorva2013], [fincher2020], [qian2017], [veerasamy2016], [lu2024], all abstract.
- **Effect.** Fincher: defines notional machines, with a literature review and teacher examples. Sorva: review arguing for the notional machine as an "explicit learning objective". Veerasamy: Python exam, misconceptions "spotted in list referencing and inbuilt functions". Lu: mutable-variable misconceptions "widespread", the tutor "appears to improve understanding"; no effect size in the abstract.
- **Rating.** Moderate that the misconceptions exist. Weak that any given visual fixes them. I did not establish a ranked Python misconception list.
- **What it changes.** A case where two suspects' files are the same object. Detective's evidence board as a visual of names pointing to objects is *inference*, untested.

## A6. Error messages: readable and hand-written help; the wider effect is contested

- **Rule.** Hand-write short, plain, positive messages with a fix hint for the errors each case will produce. Keep Python's real message visible, since reading it is the skill.
- **Sources.** [denny2014], [becker2016], [denny2020], [denny2021], [santos2024], all abstract; [lee2011] abstract.
- **Effect.** Denny 2014: "no significant effect". Becker 2016: Java, reduced errors and repeat errors. Denny 2020: RCT n > 700, shorter debugging, "very early stages". Denny 2021: length, jargon, sentence structure and vocabulary affect readability. Lee 2011: 116 MTurk novices, fallible character that blames itself; more levels completed in similar time.
- **Rating.** Contested on overall effect; moderate for readability and speed. Evidence for later learning (transfer) missing.
- **What it changes.** In-character error framing where the partner takes blame has one small supporting study ([lee2011], **developer-run**). Showing the original traceback alongside is my *inference*, to avoid dependence.

## A7. Debugging needs teaching, and knowing a strategy doesn't mean using it

- **Rule.** Teach a named debugging procedure, and make the player use it, not just see it. Testable: rate of systematic moves vs random edits by case.
- **Sources.** [mccauley2008] abstract; [ko2019] abstract; [lee2015] full; [shen2026] full.
- **Effect.** Ko: 17 students aged 15 to 18, five weeks: "defaulting to ineffective trial and error, even when they knew systematic strategies would be more effective". Shen: debugging among the most hurt skills under AI (exploratory subarea).
- **Rating.** Weak to moderate. Michaeli and Romeike's classroom study on a systematic debugging process exists (DOI 10.1145/3361721.3361724) but no text could be obtained, so its result is unknown.
- **What it changes.** Debugging fits the detective premise: hypothesis, evidence, test. That fit is *inference*; do not claim it is a proven effect.

## A8. Autograders: feedback is usually pass/fail, and learners can over-rely on tests

- **Rule.** Tell the player what the output differed in, not just fail. Prevent running tests as a guess-and-check loop: use hidden changed inputs for the case's final check.
- **Sources.** [keuning2018], [messer2023], [baniassad2021], all abstract.
- **Effect.** Keuning: 101 tools; feedback "mostly focuses on identifying mistakes and less on fixing problems". Messer (preprint): feedback "often limited to whether the unit tests have passed or failed". Baniassad: regression penalties introduced; the abstract states aim, **results unread**.
- **Rating.** Weak. Descriptive reviews; no strong learning trial found.
- **What it changes.** Case checks reply with story-consistent specifics, such as what the script returned vs what the evidence shows. Don't penalise repeats on no evidence.

## A9. Plan composition is a known difficulty; evidence read is thin

- **Rule.** Teach named patterns (filter, accumulate, count) and how to merge them, as separate goals from syntax.
- **Sources.** [soloway1986] abstract; [fisler2014] abstract.
- **Effect.** Fisler: students in functional-language CS1 courses made "fewer low-level errors" on the Rainfall problem and chose different structures. No effect size in abstract.
- **Rating.** Weak (from what I read). Older studies and de Raadt's work on strategies were not retrieved.
- **What it changes.** Recurring investigator techniques named across cases as plans. *Inference*.

## A10. Prior languages help on true carryovers and mislead on false friends

- **Rule.** Ask which language the player scripts in. Show contrasts only for constructs that look the same but behave differently. Testable: use the player's prior language as a covariate on each case's first attempt.
- **Sources.** [shrestha2020] full; [tshukudu2020] abstract.
- **Design.** Shrestha: 450 Stack Overflow posts, 18 languages; interviews with 16 professionals (5 to 31 years), mostly self-taught when switching. Tshukudu: near-novices, Python to Java and Java to Python.
- **Effect.** Shrestha: "276 (61%)" posts had incorrect assumptions from prior languages; e.g. R to Python Pandas assignment on copies. Correct prior-language assumptions in 30 sampled posts per pair: Perl to Python 13, Ruby to Python 14, R to Python 12, so more than half were incorrect in each (small samples). Tshukudu: most difficulty on false carryover "due to negative semantic transfer", little on true carryover.
- **Rating.** Moderate. SO posts over-sample confusion. Only professionals or students. No bash, PowerShell or VBA to Python study found, so **what an adult scripter gets wrong is unknown**. Don't write that list from memory; collect it from playtests.
- **What it changes.** A setup question, plus a per-language table of false friends built from observed errors. Interview finding: they learned opportunistically by mapping, so they'll do this anyway.

## A11. Topic order: no strong evidence

- **Rule.** Order by prerequisite and don't claim it's evidence-based. Make early concepts secure, since later ones build on them.
- **Sources.** [robins2010] abstract.
- **Effect.** Learning edge momentum: proposed mechanism with a simulated grade model; "success in acquiring one concept makes learning other closely linked concepts easier".
- **Rating.** Weak: it's a hypothesis. I found no randomised comparison of Python topic orders.
- **What it changes.** Ten cases, one topic each: fix the order by dependency and don't spend design time optimising it.

## A12. Self-paced programming courses lose most learners early, and light nudges don't fix it

- **Rule.** Assume early loss. Case 1 must be finishable in one sitting and give a real result. Testable: survival curve by case, with the steepest loss expected in cases 1 and 2.
- **Sources.** [ihantola2020] abstract; [feklistova2021] abstract; [kizilcec2020] abstract.
- **Effect.** Ihantola: over 8,000 students, fixed-schedule retention 45%, self-paced 13%, "mostly because of different starts"; some earn near-full points one week and stop. Kizilcec: 247 courses, one-quarter million; hypothesised medium-to-large effects "not supported"; self-regulation prompts raised early engagement "but not final completion rates". Feklistova: 1,065 participants; non-completers made more resubmissions per programming task and lower quiz scores.
- **Rating.** Moderate to strong for early loss. Ihantola is two course versions, not randomised, and the counterfactual for a game isn't known. MOOC learners may have different goals.
- **Limits.** The Reich and Ruipérez-Valiente Science article had no abstract to read, so its completion figures aren't reported here.
- **What it changes.** Self-paced is a stated requirement, so the schedule fix isn't available as-is. A soft structure such as "new case each week, optional" is worth testing (*inference*). Story cliffhangers as retention tools are unmeasured here.

---

# B. Games and story

## B1. Gamification averages a small positive effect; points-and-badges can backfire

- **Rule.** Skip points, badges and leaderboards unless a test shows benefit. Don't add them to a story game to raise engagement.
- **Sources.** [sailer2020] full; [zhan2022] abstract; [hanus2015] secondary; [kwon2021] abstract; [abramovich2013] abstract.
- **Effect.** Sailer: cognitive g = .49 (k = 19, N = 1,686), motivational g = .36, behavioural g = .25; called "small". Game fiction moderator: cognitive .47 with vs .51 without; motivational .34 vs .32; behavioural .41 (k = 3) vs .10 (k = 7, n.s.). Studies with game fiction less often randomised (r = -.41). Zhan: 21 programming studies, positive, largest on motivation, pedagogical agents "limited effect" (no effect sizes read). Hanus (secondary): 71 students, leaderboard and badges, lower motivation and final exam over 16 weeks. Kwon: gamified assessment gave lower content knowledge.
- **Rating.** Moderate, heterogeneous. Sailer judged publication bias not severe, but subgroups have few studies.
- **What it changes.** The fiction moderator suggests fiction helps behaviour (engagement) and not cognition. That matches keeping story for persistence and not expecting it to teach.

## B2. Rewards can undermine intrinsic motivation; informational feedback doesn't

- **Rule.** Treat praise and feedback as information about competence. Avoid scoring hint-free runs or completion rewards as the main driver.
- **Sources.** [deci1999] abstract; [cerasoli2014] abstract; [abramovich2013] abstract.
- **Effect.** Deci: completion-contingent d = -0.36 on free-choice, performance-contingent d = -0.28, positive feedback d = 0.33. Cerasoli: intrinsic motivation predicts performance, ρ = .21 to .45, and incentives crowd it out when directly performance-tied. Tangible rewards more harmful to children than college students.
- **Rating.** Contested historically (critiques exist, covered by the other agent). Moderate as design caution.
- **What it changes.** Whether a story reveal counts as a tangible reward is **unknown**. Don't assume it either way.

## B3. Narrative did not improve learning on average; it may help engagement

- **Rule.** Don't justify story as a learning method. Keep it short relative to practice, and test a story-off or story-thin variant on unaided score. Testable: story seconds per coding minute; learning difference between variants.
- **Sources.** [adams2012] abstract; [clark2016] full; [sykora2020] abstract; [wouters2013] abstract; [sailer2020] full; [mayer2019] abstract; contrary [jemmali2018] abstract, [cordova1996] abstract, [rowe2011] abstract, [naul2020] abstract.
- **Design.** Adams: college students, under 2 hours, Crystal Island and a detective game, Cache 17. Clark: 69 samples, 6,868 K-16 participants. Sýkora: 95 children aged about 8, home, two weeks. Jemmali: rich vs light narrative in a programming game, **developer-run**, N not read. Cordova: elementary children. Rowe: 153 middle schoolers, correlational.
- **Effect.**
  - Adams: game worse than slides on retention (d = 1.37), transfer (d = 0.57); removing the detective theme: post-test d = -0.16, learning time d = -0.22, not significant; "no evidence that computer-based narrative games offer a superior venue".
  - Clark: no story g = 0.44; thin g = 0.47; medium g = -0.03; thick g = 0.36 (CI -0.43 to 1.15, 5 studies); relevant story g = 0.17 vs irrelevant g = 0.63 (not significant after controls); contextualisation b = -0.07, p = .01. Multiple sessions g = 0.44 vs single g = 0.08.
  - Sýkora: "no between-group difference", all |d| < 0.29, for gains, engagement, enjoyment, time.
  - Wouters: games d = 0.29 on learning; "not more motivating" (d = 0.26, n.s.); more effective with multiple sessions and supplementary instruction.
  - Jemmali: rich narrative "fewer programming errors and increased engagement".
  - Naul: narrative review naming four effective features, no effect size in the abstract.
  - Cordova: "dramatic increases" in motivation and learning from contextualisation, with personalisation and choice.
- **Rating.** Moderate that story adds nothing on average. Contested on engagement and for long play.
- **Limits.** Adams warns: "no evidence concerning longer periods". Clark's moderators are confounded and thick stories rarely studied. Most evidence is children or short lab sessions. No adult 10-case story study found. The one programming study favours rich narrative, from the game's own developers, on errors not post-test.
- **What it changes.** The voiced comic is a cost to justify, by persistence, not learning. Its place in this project may still be right: an adult who stays may learn more than one who quits. That is a hypothesis to test. Ten sessions fit the multi-session finding.

## B4. Wrapping programming tasks in a story neither helps nor hurts performance

- **Rule.** Case dressing is safe for task performance, so write the wrapper freely. Keep the task specification clear, and test any wrap against a plain version when a case has unexplained failure.
- **Sources.** [lovellette2024] abstract; [bouvier2016] abstract; [leinonen2021] abstract.
- **Effect.** Lovellette: three years, three contextualised tasks and generic versions: "no effect on the performance of novice programmers". Authors think context might support interest. Bouvier: the abstract gives background, that context can affect cognitive load; Leinonen 2021's abstract summarises the working group as finding "no such benefits for novice programmers"; its own result was not in the text I got.
- **Rating.** Moderate. University novices on performance, not learning over time.
- **What it changes.** Good news for the design: the story wrapper doesn't look harmful on task scores. It doesn't justify the wrapper as teaching either.

## B5. Interesting but irrelevant detail can hurt; tutor speech may be better as text during work

- **Rule.** During coding, hide anything not needed for the task. Separate story beats from work. Make the coding partner's help text. Testable: A/B voiced vs text tutor while coding.
- **Sources.** [rey2012] abstract; [sundararajan2020] abstract; [schroeder2013] abstract; [mayer2019] abstract.
- **Effect.** Rey: 39 effects, small to medium on retention, medium on transfer. Sundararajan: "can hinder learning", moderated by pacing and others; numbers not in the abstract. Schroeder: 43 studies, 3,088 participants, "small but significant" for agents, better for K-12 than post-secondary; "on-screen text facilitated learning more effectively" than narration.
- **Rating.** Moderate for seductive details in text and multimedia (other agent covers the general case). Weak for applying this to a game with pauses. Schroeder's text-vs-narration result conflicts with modality findings (other agent's area) and Mayer 2019 lists modality as promising. **Contested.**
- **What it changes.** Voiced story during pauses, text from the tutor when typing. Motion comic visuals never run during a coding task. No study specifically tested voiced motion comics; this is *inference*.

## B6. Put learning in the core mechanic (children's evidence)

- **Rule.** The program must be the investigation. Its output moves the plot. If story and code can be swapped out independently, integration has failed. Testable: remove the story; does the code task still produce what the plot needs?
- **Sources.** [habgood2011] abstract; [ke2016] abstract; [andersen2011] abstract; [lee2015] full.
- **Effect.** Habgood: 58 children aged 7 to 11, 2 hours: "learned more from the intrinsic version"; 16 children in free choice "spent 7 times longer" playing it. Ke: 69 articles, themes only. Andersen 2011: optional objectives that reinforce the primary goal were useful; others harmed retention (see B10).
- **Rating.** Moderate from one strong design and a qualitative review. Weak for adults. I found no independent replication.
- **What it changes.** "The story pauses and the player writes Python to crack evidence" reads like alternating cutscene and exercise, which is close to Habgood's extrinsic design. Better: players read real files, run real parsers, and the case resolves by what their program actually finds, with wrong output leading somewhere plausible. This is the largest cheap design change suggested here. *Inference* from children's data.

## B7. Engagement and learning can move in opposite directions

- **Rule.** Never tune difficulty or pacing on engagement alone. A/B on tutor-off score, with retention as a guard.
- **Sources.** [lomas2013] abstract; [rowe2011] abstract; [wilson2019] abstract; [barth2026] secondary; [bastani2025] full.
- **Effect.** Lomas: online maths game, 10K and 70K subjects; "more engaged and played longer when the game was easier", and "the most engaging design conditions produced the slowest rates of learning". Rowe: a "strong positive relationship" between engagement and learning (correlational). Wilson: optimal error about 15.87% for gradient-descent binary classifiers.
- **Rating.** Moderate. Contrary correlational data exists (Rowe), and engaged learners may simply learn more. Wilson's 85% is a mathematical result about machine learners on binary tasks; **don't use it as a difficulty target for programming**.
- **What it changes.** Playtest goals name both quantities. A design that is easy and well liked may be the failure.

## B8. Programming games can match tutorials, in less time, but absolute learning is modest

- **Rule.** Guided debugging missions, not an open sandbox. Personify the tool as fallible.
- **Sources.** [lee2015] full; [lee2011] abstract; [lee2014] abstract; [kroustalli2021] abstract; [zhan2022] abstract.
- **Design.** Lee 2015: **developer-run**, randomised, 60 US adults from MTurk, 18 to 41, mostly college graduates; Codecademy Python vs Gidget vs puzzle designer; up to 7 days; pseudo-code test.
- **Effect.** Lee 2015: median post-test 12, 10, 5 of 24; increases 140%, 100%, -9.1%; game took about half the time; "best median post-test score was 50% correct". Lee 2014: 44 teens. Kroustalli: 59 lower-secondary students, CodeCombat better, "not found to be statistically significant".
- **Rating.** Moderate to weak. Small, same lab, no independent replication, short.
- **What it changes.** Strongest direct evidence that an adult can learn programming concepts from a game. Note the free-build tool taught nothing measurable, so the "make" step needs structure. And after estimated 5 to 10 hours, half correct at best: ten cases may not reach "Python from zero". Set expectations and measure.

## B9. Mastery gates: positive on learning, but self-paced gating costs completion; story gating is untested

- **Rule.** Separate story progress from certified mastery. Let a stuck player continue with a consequence and a marked gap, then return. Testable: A/B hard gate vs soft gate on both completion and tutor-off score.
- **Sources.** [kulik1990] abstract; [pane2014] abstract; [hicks2016] abstract; [ihantola2020] abstract.
- **Effect.** Kulik: 108 evaluations, positive on exams, stronger for weaker students; "self-paced mastery programs often reduce the completion rates in college classes". Hicks: students at a "roadblock" in a science game, "dropping out when they cannot (or do not want to) progress further". Pane: no first-year effect.
- **Rating.** Moderate for the trade-off, old college data. **Unknown for story gated on mastery**: I found no study. The soft-gate rule is *inference*.
- **What it changes.** A hard gate combined with unlimited tutor help gives the worst pairing: players reach the gate with the tutor's work and stop at it, or the gate certifies nothing. So gate on a tutor-off check, and give it an escape route.

## B10. Extras that don't support the main goal cost retention; tutorials matter only for complex games

- **Rule.** No collectibles or side objectives unless they reinforce the case. Test tutorials only where mechanics can't be discovered.
- **Sources.** [andersen2011] abstract; [andersen2012] abstract.
- **Effect.** Andersen 2011: over 27,000 players, A/B; secondary objectives "can easily harm the retention"; ones that reinforce the primary goal are consistently useful. Andersen 2012: over 45,000 players; tutorials increased play time up to 29% in the most complex game, no significant gain in the two simpler ones.
- **Rating.** Moderate; commercial casual games, engagement only, no learning measure.
- **What it changes.** Cut anything like side-quests for points. A web Python game is probably at the complex end (*inference*), so onboarding is worth building and measuring.

---

# What I looked for and couldn't establish

- **Voiced motion comics.** No study tested them. Closest is comic cutscenes in a child maths game [sykora2020]. Interruption cost of story during problem solving: unknown.
- **In-character AI tutors.** No controlled test of a persona LLM tutor on learning. Searches found opinion pieces and general chatbot trust studies only (not cited). Whether a persona raises over-reliance or eases refusal is unknown.
- **Adult self-learners with an LLM tutor.** No RCT in a self-paced setting with unaided delayed measures. [nie2024] and [lehmann2024] are nearest.
- **Long-term effects.** No generative-AI tutor trial I read measured retention over months.
- **Hint escalation.** No randomised programming study comparing the number or order of hint levels. A preprint chapter [not cited; arXiv 2603.07311 abstract read] is descriptive.
- **Story gated on mastery.** No experiment found, in games or otherwise. Optional vs required mastery also: not found in online courses.
- **Adult scripters moving to Python.** No study of bash, PowerShell or similar to Python. Stack Overflow data covers R, Perl, Ruby, Matlab, C++.
- **Ranked Python misconception list for adults.** Not established. Do not generate one from memory.
- **PRIMM outside schools** and with a tutor replacing discussion: not found.
- **Replication of intrinsic integration** beyond children: not found.
- **Reading-first order:** no RCT found.
- **Topic order in Python:** no RCT found.
- **Unread papers, existence checked only or not cited.** [hanus2015] and [barth2026] and [shih2010] are secondary-read. Michaeli and Romeike 2019 existence seen in Crossref; no text, not counted. Razzaq and Heffernan 2010, Reich and Ruipérez-Valiente 2019, Bai 2020, Hamari 2016, Baker 2010: abstract unavailable, not relied on. Results in the search summary from Sankaranarayanan 2026 and a "JATES" study were not checked and are not used. O'Neill's audit of AI meta-analyses (EdArXiv) was seen only in a news report and is not relied on.
- **Model staleness.** The newest models tested are GPT-4o. No trial of 2026 frontier models with a learning outcome was read. All AI results are provisional.

# Verification

A script checked every source below against Crossref or arXiv on title, year and first author. Negative controls: a fabricated citation (reported NOT-FOUND, which I read in the output), a real DOI with a wrong title, a real DOI with a wrong first author, and a nonexistent arXiv id; none verified. Note: the repository listing for [ihantola2020] named Noponen first; Crossref names Ihantola, used here.

# Sources


| ID | First author, year | Title | Venue | DOI or arXiv | Read |
|---|---|---|---|---|---|
| bastani2025 | Bastani 2025 | Generative AI without guardrails can harm learning: Evidence from high school mathematics | Proceedings of the National Academy of Sciences | 10.1073/pnas.2422633122 | full |
| kestin2025 | Kestin 2025 | AI tutoring outperforms in-class active learning: an RCT introducing a novel research-based design in an authentic educational setting | Scientific Reports | 10.1038/s41598-025-97652-6 | full |
| nie2024 | Nie 2024 | The GPT Surprise: Offering Large Language Model Chat in a Massive Coding Class Reduced Engagement but Increased Adopters Exam Performances | PREPRINT: arXiv | arXiv:2407.09975 | full |
| shen2026 | Shen 2026 | How AI Impacts Skill Formation | PREPRINT: arXiv | arXiv:2601.20245 | full |
| lehmann2024 | Lehmann 2024 | AI Meets the Classroom: When Do Large Language Models Harm Learning? | PREPRINT: arXiv | arXiv:2409.09047 | full |
| bassner2026 | Bassner 2026 | Less stress, better scores, same learning: The dissociation of performance and learning in AI-supported programming education | Computers and Education: Artificial Intelligence | 10.1016/j.caeai.2025.100537 | abstract |
| barth2026 | Barth 2026 | Steering AI Tutors Through System Prompts: A Crossover Study on Self-Regulated Learning and Cognitive Engagement Scaffolds in CS1 | Proceedings of the 2026 ACM Conference on International Computing Education Research Vol. 1 | 10.1145/3765964.3811656 | secondary |
| eastwood2026 | Eastwood 2026 | Guardrails or Roadblocks? Effects of Pedagogical Style and Context Awareness in AI Teaching Assistants for Programming | PREPRINT: arXiv | arXiv:2609.29995 | full |
| pisan2026 | Pisan 2026 | Teaching a Large Language Model Tutor to Withhold the Answer: A Supervisor Architecture and an Evidence-Driven Method for Tuning Socratic Behavior | PREPRINT: arXiv | arXiv:2608.12292 | abstract |
| kazemitabaar2025 | Kazemitabaar 2025 | Exploring the Design Space of Cognitive Engagement Techniques with AI-Generated Code for Enhanced Learning | Proceedings of the 30th International Conference on Intelligent User Interfaces | 10.1145/3708359.3712104 | full |
| kazemitabaar2023 | Kazemitabaar 2023 | Studying the effect of AI Code Generators on Supporting Novice Learners in Introductory Programming | Proceedings of the 2023 CHI Conference on Human Factors in Computing Systems | 10.1145/3544548.3580919 | abstract |
| kazemitabaar2023b | Kazemitabaar 2023 | How Novices Use LLM-based Code Generators to Solve CS1 Coding Tasks in a Self-Paced Learning Environment | Proceedings of the 23rd Koli Calling International Conference on Computing Education Research | 10.1145/3631802.3631806 | abstract |
| codeaid2024 | Kazemitabaar 2024 | CodeAid: Evaluating a Classroom Deployment of an LLM-based Programming Assistant that Balances Student and Educator Needs | Proceedings of the CHI Conference on Human Factors in Computing Systems | 10.1145/3613904.3642773 | abstract |
| liffiton2023 | Liffiton 2023 | CodeHelp: Using Large Language Models with Guardrails for Scalable Support in Programming Classes | Proceedings of the 23rd Koli Calling International Conference on Computing Education Research | 10.1145/3631802.3631830 | abstract |
| prather2024 | Prather 2024 | The Widening Gap: The Benefits and Harms of Generative AI for Novice Programmers | Proceedings of the 2024 ACM Conference on International Computing Education Research - Volume 1 | 10.1145/3632620.3671116 | abstract |
| chen2025 | Chen 2025 | Examining the Usage of Generative AI Models in Student Learning Activities for Software Programming | PREPRINT: arXiv | arXiv:2511.13271 | abstract |
| lyu2024 | Lyu 2024 | Evaluating the Effectiveness of LLMs in Introductory Computer Science Education: A Semester-Long Field Study | Proceedings of the Eleventh ACM Conference on Learning @ Scale | 10.1145/3657604.3662036 | abstract |
| fan2024 | Fan 2024 | Beware of metacognitive laziness: Effects of generative artificial intelligence on learning motivation, processes, and performance | British Journal of Educational Technology | 10.1111/bjet.13544 | abstract |
| darvishi2024 | Darvishi 2024 | Impact of AI assistance on student agency | Computers & Education | 10.1016/j.compedu.2023.104967 | abstract |
| pardos2024 | Pardos 2024 | ChatGPT-generated help produces learning gains equivalent to human tutor-authored help on mathematics skills | PLOS ONE | 10.1371/journal.pone.0304013 | abstract |
| deng2025 | Deng 2025 | Does ChatGPT enhance student learning? A systematic review and meta-analysis of experimental studies | Computers & Education | 10.1016/j.compedu.2024.105224 | abstract |
| weidlich2025 | Weidlich 2025 | ChatGPT in education: An effect in search of a cause | PREPRINT: PsyArXiv/EdArXiv (Center for Open Science) | 10.31234/osf.io/t6uzy_v2 | abstract |
| bartos2026 | Bartoš 2026 | Effect of Artificial Intelligence on Learning: A Meta-Meta-Analysis | PREPRINT: PsyArXiv/EdArXiv (Center for Open Science) | 10.31234/osf.io/h529e_v1 | abstract |
| wangfan2026retract | Wang 2026 | Retraction Note: The effect of ChatGPT on students' learning performance, learning perception, and higher-order thinking: insights from a meta-analysis | Humanities and Social Sciences Communications | 10.1057/s41599-026-07310-z | abstract |
| huang2025 | Huang 2025 | A Meta-Analysis of LLM Effects on Students across Qualification, Socialisation, and Subjectification | PREPRINT: arXiv | arXiv:2509.22725 | abstract |
| ma2014 | Ma 2014 | Intelligent tutoring systems and learning outcomes: A meta-analysis. | Journal of Educational Psychology | 10.1037/a0037123 | abstract |
| kulik2016 | Kulik 2016 | Effectiveness of Intelligent Tutoring Systems: A Meta-Analytic Review | Review of Educational Research | 10.3102/0034654315581420 | abstract |
| steenbergen2014 | Steenbergen-Hu 2014 | A meta-analysis of the effectiveness of intelligent tutoring systems on college students' academic learning | Journal of Educational Psychology | 10.1037/a0034752 | abstract |
| vanlehn2011 | VanLehn 2011 | The Relative Effectiveness of Human Tutoring, Intelligent Tutoring Systems, and Other Tutoring Systems | Educational Psychologist | 10.1080/00461520.2011.611369 | abstract |
| nesbit2014 | Nesbit 2014 | How Effective are Intelligent Tutoring Systems in Computer Science Education? | 2014 IEEE 14th International Conference on Advanced Learning Technologies | 10.1109/icalt.2014.38 | abstract |
| crow2018 | Crow 2018 | Intelligent tutoring systems for programming education: a systematic review | Proceedings of the 20th Australasian Computing Education Conference | 10.1145/3160489.3160492 | abstract |
| aleven2016 | Aleven 2016 | Help Helps, But Only So Much: Research on Help Seeking with Intelligent Tutoring Systems | International Journal of Artificial Intelligence in Education | 10.1007/s40593-015-0089-1 | abstract |
| marwan2019 | Marwan 2019 | An Evaluation of the Impact of Automated Programming Hints on Performance and Learning | Proceedings of the 2019 ACM Conference on International Computing Education Research | 10.1145/3291279.3339420 | abstract |
| price2017 | Price 2017 | Factors Influencing Students' Help-Seeking Behavior while Programming with Human and Computer Tutors | Proceedings of the 2017 ACM Conference on International Computing Education Research | 10.1145/3105726.3106179 | abstract |
| baker2004 | Baker 2004 | Off-task behavior in the cognitive tutor classroom: when students game the system | Proceedings of the SIGCHI Conference on Human Factors in Computing Systems | 10.1145/985692.985741 | abstract |
| shih2010 | Shih 2010 | A Response-Time Model for Bottom-Out Hints as Worked Examples | Chapman & Hall/CRC Data Mining and Knowledge Discovery Series | 10.1201/b10274-17 | secondary |
| xiao2024 | Xiao 2024 | Exploring How Multiple Levels of GPT-Generated Programming Hints Support or Disappoint Novices | Extended Abstracts of the CHI Conference on Human Factors in Computing Systems | 10.1145/3613905.3650937 | abstract |
| orourke2014 | O'Rourke 2014 | Hint systems may negatively impact performance in educational games | Proceedings of the first ACM conference on Learning @ scale conference | 10.1145/2556325.2566248 | full |
| santos2024 | Santos 2024 | Not the Silver Bullet: LLM-enhanced Programming Error Messages are Ineffective in Practice | Proceedings of the 2024 Conference on United Kingdom & Ireland Computing Education Research | 10.1145/3689535.3689554 | abstract |
| leinonen2023 | Leinonen 2023 | Using Large Language Models to Enhance Programming Error Messages | Proceedings of the 54th ACM Technical Symposium on Computer Science Education V. 1 | 10.1145/3545945.3569770 | abstract |
| denny2014 | Denny 2014 | Enhancing syntax error messages appears ineffectual | Proceedings of the 2014 conference on Innovation & technology in computer science education - ITiCSE '14 | 10.1145/2591708.2591748 | abstract |
| becker2016 | Becker 2016 | Effective compiler error message enhancement for novice programming students | Computer Science Education | 10.1080/08993408.2016.1225464 | abstract |
| denny2020 | Denny 2020 | Error Message Readability and Novice Debugging Performance | Proceedings of the 2020 ACM Conference on Innovation and Technology in Computer Science Education | 10.1145/3341525.3387384 | abstract |
| denny2021 | Denny 2021 | On Designing Programming Error Messages for Novices: Readability and its Constituent Factors | Proceedings of the 2021 CHI Conference on Human Factors in Computing Systems | 10.1145/3411764.3445696 | abstract |
| ericson2022 | Ericson 2022 | Parsons Problems and Beyond: Systematic Literature Review and Empirical Study Designs | Proceedings of the 2022 Working Group Reports on Innovation and Technology in Computer Science Education | 10.1145/3571785.3574127 | full |
| ericson2017 | Ericson 2017 | Solving parsons problems versus fixing and writing code | Proceedings of the 17th Koli Calling International Conference on Computing Education Research | 10.1145/3141880.3141895 | abstract |
| ericson2023 | Ericson 2023 | Multi-Institutional Multi-National Studies of Parsons Problems | Proceedings of the 2023 Working Group Reports on Innovation and Technology in Computer Science Education | 10.1145/3623762.3633498 | abstract |
| sentance2019 | Sentance 2019 | Teaching computer programming with PRIMM: a sociocultural perspective | Computer Science Education | 10.1080/08993408.2019.1608781 | abstract |
| margulieux2012 | Margulieux 2012 | Subgoal-labeled instructional material improves performance and transfer in learning to develop mobile applications | Proceedings of the ninth annual international conference on International computing education research | 10.1145/2361276.2361291 | abstract |
| morrison2015 | Morrison 2015 | Subgoals, Context, and Worked Examples in Learning Computing Problem Solving | Proceedings of the eleventh annual International Conference on International Computing Education Research | 10.1145/2787622.2787733 | abstract |
| margulieux2020 | Margulieux 2020 | Reducing withdrawal and failure rates in introductory programming with subgoal labeled worked examples | International Journal of STEM Education | 10.1186/s40594-020-00222-7 | full |
| lister2004 | Lister 2004 | A multi-national study of reading and tracing skills in novice programmers | ACM SIGCSE Bulletin | 10.1145/1041624.1041673 | abstract |
| lopez2008 | Lopez 2008 | Relationships between reading, tracing and writing skills in introductory programming | Proceedings of the Fourth international Workshop on Computing Education Research | 10.1145/1404520.1404531 | abstract |
| xie2019 | Xie 2019 | A theory of instruction for introductory programming skills | Computer Science Education | 10.1080/08993408.2019.1565235 | abstract |
| sorva2013 | Sorva 2013 | Notional machines and introductory programming education | ACM Transactions on Computing Education | 10.1145/2483710.2483713 | abstract |
| fincher2020 | Fincher 2020 | Notional Machines in Computing Education: The Education of Attention | Proceedings of the Working Group Reports on Innovation and Technology in Computer Science Education | 10.1145/3437800.3439202 | abstract |
| qian2017 | Qian 2017 | Students' Misconceptions and Other Difficulties in Introductory Programming: A Literature Review | ACM Transactions on Computing Education | 10.1145/3077618 | abstract |
| veerasamy2016 | Veerasamy 2016 | Identifying Novice Student Programming Misconceptions and Errors From Summative Assessments | Journal of Educational Technology Systems | 10.1177/0047239515627263 | abstract |
| lu2024 | Lu 2024 | Identifying and Correcting Programming Language Behavior Misconceptions | Proceedings of the ACM on Programming Languages | 10.1145/3649823 | abstract |
| parker2016 | Parker 2016 | Replication, Validation, and Use of a Language Independent CS1 Knowledge Assessment | Proceedings of the 2016 ACM Conference on International Computing Education Research | 10.1145/2960310.2960316 | abstract |
| mccauley2008 | McCauley 2008 | Debugging: a review of the literature from an educational perspective | Computer Science Education | 10.1080/08993400802114581 | abstract |
| ko2019 | Ko 2019 | Teaching Explicit Programming Strategies to Adolescents | Proceedings of the 50th ACM Technical Symposium on Computer Science Education | 10.1145/3287324.3287371 | abstract |
| keuning2018 | Keuning 2018 | A Systematic Literature Review of Automated Feedback Generation for Programming Exercises | ACM Transactions on Computing Education | 10.1145/3231711 | abstract |
| messer2023 | Messer 2023 | Automated Grading and Feedback Tools for Programming Education: A Systematic Review | PREPRINT: PsyArXiv/EdArXiv (Center for Open Science) | 10.35542/osf.io/wpsgk | abstract |
| baniassad2021 | Baniassad 2021 | STOP THE (AUTOGRADER) INSANITY: Regression Penalties to Deter Autograder Overreliance | Proceedings of the 52nd ACM Technical Symposium on Computer Science Education | 10.1145/3408877.3432430 | abstract |
| soloway1986 | Soloway 1986 | Learning to program = learning to construct mechanisms and explanations | Communications of the ACM | 10.1145/6592.6594 | abstract |
| fisler2014 | Fisler 2014 | The recurring rainfall problem | Proceedings of the tenth annual conference on International computing education research | 10.1145/2632320.2632346 | abstract |
| shrestha2020 | Shrestha 2020 | Here We Go Again: Why Is It Difficult for Developers to Learn Another Programming Language? | Proceedings of the ACM/IEEE 42nd International Conference on Software Engineering | 10.1145/3377811.3380352 | full |
| tshukudu2020 | Tshukudu 2020 | Understanding Conceptual Transfer for Students Learning New Programming Languages | Proceedings of the 2020 ACM Conference on International Computing Education Research | 10.1145/3372782.3406270 | abstract |
| robins2010 | Robins 2010 | Learning edge momentum: a new account of outcomes in CS1 | Computer Science Education | 10.1080/08993401003612167 | abstract |
| ihantola2020 | Ihantola 2020 | Deadlines and MOOCs: How Do Students Behave in MOOCs with and without Deadlines | 2020 IEEE Frontiers in Education Conference (FIE) | 10.1109/fie44824.2020.9274023 | abstract |
| feklistova2021 | Feklistova 2021 | Learners' Performance in a MOOC on Programming | Education Sciences | 10.3390/educsci11090521 | abstract |
| kizilcec2020 | Kizilcec 2020 | Scaling up behavioral science interventions in online education | Proceedings of the National Academy of Sciences | 10.1073/pnas.1921417117 | abstract |
| lovellette2024 | Lovellette 2024 | Contextualization, Authenticity, and the Problem Description Effect | ACM Transactions on Computing Education | 10.1145/3643864 | abstract |
| bouvier2016 | Bouvier 2016 | Novice Programmers and the Problem Description Effect | Proceedings of the 2016 ITiCSE Working Group Reports | 10.1145/3024906.3024912 | abstract |
| leinonen2021 | Leinonen 2021 | Exploring the Effects of Contextualized Problem Descriptions on Problem Solving | Proceedings of the 23rd Australasian Computing Education Conference | 10.1145/3441636.3442302 | abstract |
| sailer2020 | Sailer 2020 | The Gamification of Learning: a Meta-analysis | Educational Psychology Review | 10.1007/s10648-019-09498-w | full |
| zhan2022 | Zhan 2022 | The effectiveness of gamification in programming education: Evidence from a meta-analysis | Computers and Education: Artificial Intelligence | 10.1016/j.caeai.2022.100096 | abstract |
| deci1999 | Deci 1999 | A meta-analytic review of experiments examining the effects of extrinsic rewards on intrinsic motivation | Psychological Bulletin | 10.1037/0033-2909.125.6.627 | abstract |
| cerasoli2014 | Cerasoli 2014 | Intrinsic motivation and extrinsic incentives jointly predict performance: A 40-year meta-analysis. | Psychological Bulletin | 10.1037/a0035661 | abstract |
| adams2012 | Adams 2012 | Narrative games for learning: Testing the discovery and narrative hypotheses. | Journal of Educational Psychology | 10.1037/a0025595 | abstract |
| clark2016 | Clark 2016 | Digital Games, Design, and Learning: A Systematic Review and Meta-Analysis | Review of Educational Research | 10.3102/0034654315582065 | full |
| wouters2013 | Wouters 2013 | A meta-analysis of the cognitive and motivational effects of serious games. | Journal of Educational Psychology | 10.1037/a0031311 | abstract |
| mayer2019 | Mayer 2019 | Computer Games in Education | Annual Review of Psychology | 10.1146/annurev-psych-010418-102744 | abstract |
| naul2020 | Naul 2020 | Why Story Matters: A Review of Narrative in Serious Games | Journal of Educational Computing Research | 10.1177/0735633119859904 | abstract |
| rowe2011 | Rowe 2011 | Integrating Learning, Problem Solving, and Engagement in Narrative-Centered Learning Environments | International Journal of Artificial Intelligence in Education | 10.3233/jai-2011-019 | abstract |
| cordova1996 | Cordova 1996 | Intrinsic motivation and the process of learning: Beneficial effects of contextualization, personalization, and choice. | Journal of Educational Psychology | 10.1037/0022-0663.88.4.715 | abstract |
| jemmali2018 | Jemmali 2018 | Educational Game Design: An Empirical Study of the Effects of Narrative | Proceedings of the 13th International Conference on the Foundations of Digital Games | 10.1145/3235765.3235783 | abstract |
| sykora2020 | Sýkora 2020 | Can narrative cutscenes improve home learning from a math game? An experimental study with children | British Journal of Educational Technology | 10.1111/bjet.12939 | abstract |
| schroeder2013 | Schroeder 2013 | How Effective are Pedagogical Agents for Learning? A Meta-Analytic Review | Journal of Educational Computing Research | 10.2190/ec.49.1.a | abstract |
| habgood2011 | Habgood 2011 | Motivating Children to Learn Effectively: Exploring the Value of Intrinsic Integration in Educational Games | Journal of the Learning Sciences | 10.1080/10508406.2010.508029 | abstract |
| lomas2013 | Lomas 2013 | Optimizing challenge in an educational game using large-scale design experiments | Proceedings of the SIGCHI Conference on Human Factors in Computing Systems | 10.1145/2470654.2470668 | abstract |
| wilson2019 | Wilson 2019 | The Eighty Five Percent Rule for optimal learning | Nature Communications | 10.1038/s41467-019-12552-4 | abstract |
| lee2011 | Lee 2011 | Personifying programming tool feedback improves novice programmers' learning | Proceedings of the seventh international workshop on Computing education research | 10.1145/2016911.2016934 | abstract |
| lee2015 | Lee 2015 | Comparing the Effectiveness of Online Learning Approaches on CS1 Learning Outcomes | Proceedings of the eleventh annual International Conference on International Computing Education Research | 10.1145/2787622.2787709 | full |
| lee2014 | Lee 2014 | Principles of a debugging-first puzzle game for computing education | 2014 IEEE Symposium on Visual Languages and Human-Centric Computing (VL/HCC) | 10.1109/vlhcc.2014.6883023 | abstract |
| kulik1990 | Kulik 1990 | Effectiveness of Mastery Learning Programs: A Meta-Analysis | Review of Educational Research | 10.2307/1170612 | abstract |
| pane2014 | Pane 2014 | Effectiveness of Cognitive Tutor Algebra I at Scale | Educational Evaluation and Policy Analysis | 10.3102/0162373713507480 | abstract |
| andersen2011 | Andersen 2011 | On the harmfulness of secondary game objectives | Proceedings of the 6th International Conference on Foundations of Digital Games | 10.1145/2159365.2159370 | abstract |
| andersen2012 | Andersen 2012 | The impact of tutorials on games of varying complexity | Proceedings of the SIGCHI Conference on Human Factors in Computing Systems | 10.1145/2207676.2207687 | abstract |
| hicks2016 | Hicks 2016 | Using game analytics to evaluate puzzle design and level progression in a serious game | Proceedings of the Sixth International Conference on Learning Analytics & Knowledge | 10.1145/2883851.2883953 | abstract |
| sundararajan2020 | Sundararajan 2020 | Keep it Coherent: A Meta-Analysis of the Seductive Details Effect | Educational Psychology Review | 10.1007/s10648-020-09522-4 | abstract |
| rey2012 | Rey 2012 | A review of research and a meta-analysis of the seductive detail effect | Educational Research Review | 10.1016/j.edurev.2012.05.003 | abstract |
| ke2016 | Ke 2016 | Designing and integrating purposeful learning in game play: a systematic review | Educational Technology Research and Development | 10.1007/s11423-015-9418-1 | abstract |
| abramovich2013 | Abramovich 2013 | Are badges useful in education?: it depends upon the type of badge and expertise of learner | Educational Technology Research and Development | 10.1007/s11423-013-9289-2 | abstract |
| roll2011 | Roll 2011 | Improving students' help-seeking skills using metacognitive feedback in an intelligent tutoring system | Learning and Instruction | 10.1016/j.learninstruc.2010.07.004 | abstract |
| hanus2015 | Hanus 2015 | Assessing the effects of gamification in the classroom: A longitudinal study on intrinsic motivation, social comparison, satisfaction, effort, and academic performance | Computers & Education | 10.1016/j.compedu.2014.08.019 | secondary |
| kroustalli2021 | Kroustalli 2021 | Studying the effects of teaching programming to lower secondary school students with a serious game: a case study with Python and CodeCombat | Education and Information Technologies | 10.1007/s10639-021-10596-y | abstract |
| kwon2021 | Kwon 2021 | The Dark Side of Narrow Gamification: Negative Impact of Assessment Gamification on Student Perceptions and Content Knowledge | INFORMS Transactions on Education | 10.1287/ited.2019.0227 | abstract |
| tranle2026 | Tran-Le 2026 | How Does LLM-powered Coding Assistance Shape Incidental Learning? Exploring Cognitive Forcing Strategies in Programming Education | Proceedings of the AAAI Conference on Artificial Intelligence | 10.1609/aaai.v40i48.42121 | secondary |

Counts: 110 sources verified; read level full 14, abstract 92, secondary 4.
