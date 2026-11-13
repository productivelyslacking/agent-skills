<!-- Research notes from 2026-11-06, kept as written apart from this note and removed references to the session's scratch files.
Rules and how to use them are in SKILL.md. "The game" throughout means the project that prompted the review: a self-paced web
game teaching Python to an adult who knows some scripting, told as a voiced detective story with an AI tutor. "The other agent"
means the author of the sibling evidence file. The citation-check script was not kept; its results are stated here (D22). -->

# How adults learn a skill: evidence base for a teaching-design skill

Scope: general learning science only. Programming education, games, narrative and AI tutors are covered by another agent. Target game for the "changes" lines: a self-paced web game teaching Python from zero to an adult who knows some scripting, detective story, one case per topic, ten cases.

## How to read this

**Read levels.** FT = full text obtained and the cited sections read (not always every page). ABS = abstract only. SEC = only described by another source, no number from it counted as read directly. A number from a SEC source is always labelled with the paper that reported it.

**Ratings.** Strong = several consistent meta-analyses or large trials. Moderate, weak, contested as the words say.

**Verification.** A script matched title, year and first author against Crossref, then OpenAlex; Source lines below were generated from that output, so a year or DOI here is the database record, which can differ by one year from the citation year (online-first). The two negative controls come back NOT FOUND in the output: an invented paper, and a real title with a wrong author and year.

**What verification caught.** I had a first author wrong: the biopsychology relearning paper is Janes et al. 2020, not "Higham 2022". The Sana and Yan interleaving paper was also filed under the wrong first author. Both failed the check and were corrected.

**Search budget.** 30 of 30 web searches used. Crossref, OpenAlex, ERIC, Europe PMC and Semantic Scholar API lookups are extra, used to retrieve records and abstracts for works already named by a search or found in a database.

**Numbers quoted from preprints.** Noetel 2022 sections were read in the PsyArXiv preprint, Koedinger 2023's "about 7 opportunities" in the preprint, Brunmair 2019 in the accepted manuscript. The published versions were not compared.

**Population warning that applies throughout.** Nearly all of this is undergraduates or school pupils, on short tasks, often with a test they were told about. Almost none is an adult choosing to learn alone with no grade at stake. Treat effect sizes as direction and rough order, not as what the game will get.

---

## C1. Producing an answer from memory beats re-reading for delayed tests

**Rule.** Every new concept gets at least one attempt to produce it from memory, not a re-read, before the case ends. Test: on a delayed test (at least 1 week), the retrieval version scores higher than a same-time re-read version. On an immediate test expect no gain or a loss, so never evaluate this with an immediate test.

**Sources.**
- Yang, Luo, Vadillo et al. (2021). Psychological Bulletin. doi:10.1037/bul0000309. read=ABS. Classroom meta-analysis, 222 studies, 48,478 students. "g = 0.499"; modulated by control strategy, format match, feedback, repetitions and more.
- Sotola, Crede (2020). Educational Psychology Review. doi:10.1007/s10648-020-09563-9. read=ABS. 52 samples from real classes, N = 7,864. "d = .42"; "d = .51" when quiz performance counted toward grades. Reported as an association.
- Schwieren, Barenberg, Dutke (2017). Psychology Learning & Teaching. doi:10.1177/1475725717695149. read=ABS. Psychology classes, 19 publications, 72 effects. "d = 0.56".
- Agarwal, Nunes, Blunt (2021). Educational Psychology Review. doi:10.1007/s10648-021-09595-9. read=ABS. Coded 50 classroom experiments, 49 effects, n = 5,374; "57%" showed medium or large benefits; only 6% non-WEIRD.
- Larsen, Butler, Roediger III (2009). Medical Education. doi:10.1111/j.1365-2923.2009.03518.x. read=ABS. RCT, adult medical residents, about 40. With feedback, 39% vs 26% at over 6 months, "d = 0.91".
- Larsen, Butler, Roediger III (2013). Medical Education. doi:10.1111/medu.12141. read=ABS. 47 Year 1 medical students; testing vs studying over 6 months, "η2 = 0.33".
- Green, Moeller, Spak (2018). Medical Teacher. doi:10.1080/0142159x.2018.1430354. read=ABS. Health professions, 19 studies; 21 of 23 retention outcomes favoured testing, "SMD 0.12-2.5".
- Roediger, Karpicke (2006). Psychological Science. doi:10.1111/j.1467-9280.2006.01693.x. read=ABS. Students, prose. Restudy wins at 5 min; testing wins at 2 days and 1 week; restudy raises confidence.
- Rowland (2014). Psychological Bulletin. doi:10.1037/a0037559. read=ABS, Adesope, Trevisan, Sundararajan (2017). Review of Educational Research. doi:10.3102/0034654316689306. read=ABS. Both favour testing; the abstracts give no overall number, and I did not read one in the papers, so none is reported.
- Donoghue, Hattie (2021). Frontiers in Education. doi:10.3389/feduc.2021.581216. read=ABS. 242 studies; practice testing and distributed practice most effective; effects "much greater for lower than higher ability students"; mostly surface outcomes.

**Rating.** Strong for delayed retention of taught material. Moderate for complex material.

**Limits and contrary evidence.**
- Complexity dispute. van Gog, Sweller (2015). Educational Psychology Review. doi:10.1007/s10648-015-9310-x. read=ABS argue the effect shrinks or disappears as element interactivity rises. Karpicke, Aue (2015). Educational Psychology Review. doi:10.1007/s10648-015-9309-3. read=ABS reply that element interactivity is not measurably defined and find a small positive effect with worked examples. Rawson (2015). Educational Psychology Review. doi:10.1007/s10648-015-9308-4. read=ABS says the conclusion is not warranted. Rummer, Ende, Glim et al. (2025). preprint, no venue in record. doi:10.31234/osf.io/d7pcx_v1. read=ABS, a preprint with n = 111 and 117, replicated a key negative study with more power and found the effect independent of text complexity. It is not peer reviewed as far as I read.
- I found no multi-lab pre-registered replication.
- Sotola's larger effect when quizzes count for grades suggests a no-stakes game may get less. That is my inference; no study I read tests it for voluntary adult learners.
- Pan, Rickard (2018). Psychological Bulletin. doi:10.1037/bul0000151. read=FT: transfer from testing is weakest for problems involving worked examples (see C17).

**Changes in the game.** A case cannot be advanced by reading the notebook again. The player types or predicts code from memory. A later case's clue requires the earlier construct with the notebook closed, then opens it as feedback.

---

## C2. When first attempts would mostly fail, fade the support rather than dropping the test

**Rule.** If first-attempt success will be low, give cues or incremental hints that shrink over attempts, ending with self-generation or the answer. Test on a delay, since immediate tests hide the difference.

**Sources.**
- Finn, Metcalfe (2010). Memory & Cognition. doi:10.3758/mc.38.7.951. read=ABS. Incremental hints until self-generated. Equal to standard feedback immediately, best at 30 min and 1 day.
- Fiechter, Benjamin (2017). Psychonomic Bulletin & Review. doi:10.3758/s13423-017-1366-9. read=ABS. Where standard retrieval did not help, diminishing cues "enhanced memory performance substantially". No number in the abstract.
- Finley, Benjamin, Hays et al. (2011). Journal of Memory and Language. doi:10.1016/j.jml.2011.01.006. read=ABS. English-Iñupiaq word pairs; diminishing cues best on the final cued recall.
- Belland, Walker, Kim et al. (2016). Review of Educational Research. doi:10.3102/0034654316670999. read=ABS. Computer-based scaffolding in STEM, 144 studies, primary to adult. "ḡ = 0.46"; largest among adult learners. Whether scaffolding faded or not made no difference.

**Rating.** Moderate that scaffolding complex problems helps. Weak for any specific hint ladder: lab recall tasks, few studies.

**Limits and contrary evidence.**
- Sitzmann, Ely (2011). Psychological Bulletin. doi:10.1037/a0022777. read=ABS: in adult work-related training, help seeking did not show a significant relationship with learning.
- Aleven, Roll, McLaren et al. (2016). International Journal of Artificial Intelligence in Education. doi:10.1007/s40593-015-0089-1. read=ABS: as the title says, help helps but only so much; feedback on help seeking changed use of help, not learning. Tutoring systems, classroom.
- Koedinger, Aleven (2007). Educational Psychology Review. doi:10.1007/s10648-007-9049-0. read=ABS call the balance of giving and withholding an open problem.
- Most hint research I saw is inside intelligent tutors, which the other agent covers. I found none for a self-learner outside them.

**Changes in the game.** A stuck puzzle gives a hint chain from hint to partial code to full answer, and the same construct returns later with a shorter chain. Do not make the chain a toll on progress.

---

## C3. Spacing practice across days beats massing it, and the best gap grows with how long it must last

**Rule.** Revisit each topic after a real time gap. Set the gap from the target retention: for 1 week, about 20-40% of it; for 1 year, about 5-10% of it, which by my arithmetic is about 1.4-2.8 days and about 18-36 days. The curve "at first increased, and then gradually reduced", which I read as a too-long gap costing less than a too-short one; the abstract does not state that comparison. Test: delayed test at 4 weeks, not 1 week.

**Sources.**
- Latimier, Peyre, Ramus (2020). Educational Psychology Review. doi:10.1007/s10648-020-09572-8. read=ABS. 29 studies, spaced vs massed retrieval. "g = 0.74".
- Cepeda, Pashler, Vul et al. (2006). Psychological Bulletin. doi:10.1037/0033-2909.132.3.354. read=FT. 839 assessments, 317 experiments, verbal recall. Optimal gap rises with retention interval.
- Cepeda, Vul, Rohrer et al. (2008). Psychological Science. doi:10.1111/j.1467-9280.2008.02209.x. read=ABS. More than 1,350 people, facts, gaps up to 3.5 months, tests up to 1 year. Proportions above are from this abstract.
- Donovan, Radosevich (1999). Journal of Applied Psychology. doi:10.1037/0021-9010.84.5.795. read=ABS. 63 studies, 112 effects, task performance. "0.46"; moderated by task type and gap; higher in studies with low rigour.
- Karpicke, Bauernschmidt (2011). Journal of Experimental Psychology: Learning, Memory, and Cognition. doi:10.1037/a0023436. read=ABS. Long intervals gave "a 200% improvement" over no spacing between tests.
- Rohrer, Taylor (2006). Applied Cognitive Psychology. doi:10.1002/acp.1266. read=ABS. 216 college students, maths. Benefit "nil" at 1 week, "extremely large" at 4 weeks. No number given.
- Kerfoot, DeWolf, Masser et al. (2006). Medical Education. doi:10.1111/j.1365-2929.2006.02644.x. read=ABS. RCT, medical students, weekly emailed questions; 95 of 133 finished. Cohen's "1.01 and 0.73" for those 6-8 and 9-11 months out.

**Rating.** Strong that spacing helps. Moderate on the numeric gap rule, which rests largely on one large facts study.

**Limits and contrary evidence.** Mostly verbal and factual material. Donovan's moderators mean a complex-task effect may be smaller. A self-paced learner can binge, and nothing makes a player come back; I found no trial of spaced review in an unpaid self-paced game.

**Changes in the game.** Ten cases played in one weekend get almost no spacing. Schedule review by wall-clock time, not by case number: on return, the first thing is a short cold-recall from earlier cases, sized to time away. Decide the retention target first, because it sets the gap.

---

## C4. Expanding review intervals are not reliably better than equal ones

**Rule.** Do not build an expanding schedule on the claim that expanding itself helps. Total spacing matters. Adapt to item performance only if there are enough items to adapt on.

**Sources.**
- Latimier, Peyre, Ramus (2020). Educational Psychology Review. doi:10.1007/s10648-020-09572-8. read=ABS. Expanding vs uniform, 54 effects: "g = 0.034", not significant; more exposures favour expanding.
- Karpicke, Bauernschmidt (2011). Journal of Experimental Psychology: Learning, Memory, and Cognition. doi:10.1037/a0023436. read=ABS. No schedule "inherently superior".
- Karpicke, Roediger (2009). Memory & Cognition. doi:10.3758/mc.38.1.116. read=ABS. Text; "no differences" a week later.
- Kang, Lindsey, Mozer et al. (2014). Psychonomic Bulletin & Review. doi:10.3758/s13423-014-0636-z. read=ABS. Vocabulary over 4 weeks: equal at 8 weeks after training, but expanding gave much higher average recall during training.
- Mettler, Massey, Kellman (2016). Journal of Experimental Psychology: General. doi:10.1037/xge0000170. read=ABS. Adaptive beat fixed schedules; no expanding-equal difference.
- Lindsey, Shroyer, Pashler et al. (2014). Psychological Science. doi:10.1177/0956797613504302. read=ABS. Middle school language course: personalised review "16.5%" over massed, "10.0%" over one-size spacing.
- Tabibian, Upadhyay, De et al. (2019). Proceedings of the National Academy of Sciences. doi:10.1073/pnas.1815156116. read=ABS. Algorithm plus natural experiment on Duolingo data. Observational.
- Cepeda, Pashler, Vul et al. (2006). Psychological Bulletin. doi:10.1037/0033-2909.132.3.354. read=FT. Across 18 studies expanding did better overall, with variability that makes conclusions "necessarily tentative".

**Rating.** Moderate. **Conflicts with common belief** behind flashcard apps.

**Limits.** Kang shows a real benefit if average recall during learning is the goal. Adaptive evidence comes from many small items, and a ten-topic game may have too few. That last point is my inference.

**Changes in the game.** No Leitner or SM-2 machinery in the first build. A simple "review what you got wrong plus a sample, after a real gap" is defensible.

---

## C5. Practise to a modest criterion in one sitting, then relearn later; more in a single sitting buys little

**Rule.** In a first session, stop at about 3 correct recalls of a concept. Return later for short relearning rounds. Plan for about 7 practice opportunities per skill across the game, not 7 in a row.

**Sources.**
- Rawson, Dunlosky (2011). Journal of Experimental Psychology: General. doi:10.1037/a0023956. read=ABS. 533 students, conceptual material, retention 1-4 months. Prescription "an initial criterion of 3 correct recalls and then to relearn them 3 times at widely spaced intervals".
- Rawson, Dunlosky, Sciartelli (2013). Educational Psychology Review. doi:10.1007/s10648-013-9240-4. read=ABS. Course exams, real class.
- Janes, Dunlosky, Rawson et al. (2020). Applied Cognitive Psychology. doi:10.1002/acp.3699. read=ABS. Biopsychology course; "ds ranging from 0.54 to 1.10".
- Rohrer, Taylor (2006). Applied Cognitive Psychology. doi:10.1002/acp.1266. read=ABS. 3 vs 9 maths problems in one session: no difference at 1 or 4 weeks.
- Kim, Wang, Thompson et al. (2015). Educational Data Mining. no DOI, educationaldatamining.org/EDM2015/proceedings/poster630-631.pdf. read=FT. ASSISTments. 3 consecutive correct is adequate on next-problem correctness; higher thresholds predict transfer better.
- Matayoshi, Cosyn, Uzun, Kurd-Misto (2025). Journal of Educational Data Mining. doi:10.5281/zenodo.15698758, from the journal page. NOT in Crossref or OpenAlex. read=ABS. A/B test in an adaptive maths system. Higher threshold, less forgetting, "over time this difference decreases". Not in Crossref or OpenAlex; I read the abstract on the journal's own page.
- Koedinger, Carvalho, Liu et al. (2023). Proceedings of the National Academy of Sciences. doi:10.1073/pnas.2221311120. read=FT. Models of 1.3 million observations, 27 datasets. Preprint: "about 7 opportunities per component of knowledge".

**Rating.** Moderate.

**Limits and contrary evidence.** Driskell, Willis, Copper (1992). Journal of Applied Psychology. doi:10.1037/0021-9010.77.5.615. read=ABS find overlearning has a moderate effect on retention, moderated by degree, task and retention period, in tension with Rohrer. Rawson's material is concept definitions, not procedures. Kelly's and Matayoshi's populations are school and college maths in adaptive tools.

**Changes in the game.** No drill wall of ten near-identical puzzles in a case. Three correct, move on, reuse the skill in later cases, and count opportunities per skill in content review.

---

## C6. Mastery gating raises scores in some settings but costs time and, when self-paced, completion

**Rule.** Gate only on true prerequisites, with fresh retry items and corrective help. Track drop-off at every gate and make a gate that loses players a design bug.

**Sources.**
- Kulik, Kulik, Bangert-Drowns (1990). Review of Educational Research. doi:10.2307/1170612. read=ABS. 108 controlled evaluations, college to upper elementary. Positive effects, stronger for weaker students, more time on task. "Self-paced mastery programs often reduce the completion rates in college classes." The mean effect is not in the abstract and I did not read one.
- Slavin (1987). Review of Educational Research. doi:10.2307/1170235. read=FT. Group-based, school, at least 4 weeks. "Essentially no evidence" on standardised measures; on experimenter-made measures, positive but moderate, and little evidence that effects last.
- Bloom (1984). Educational Researcher. doi:10.2307/1175554. read=ABS. The 2-sigma claim comes from two doctoral dissertations.
- Koedinger, Carvalho, Liu et al. (2023). Proceedings of the National Academy of Sciences. doi:10.1073/pnas.2221311120. read=FT. Pre-practice accuracy about 65%, 55% vs 75% for lower vs upper half, learning rate similar at "about 0.1 log odds or 2.5% in accuracy per opportunity". Elementary to college.
- Lee, Lichand, Barnard et al. (2026). Proceedings of the Thirteenth ACM Conference on Learning @ Scale. doi:10.1145/3774398.3811619. read=ABS. Refit: the learning-rate variation estimate "inflates by a median of 118%" under one specification. arXiv preprint; I read the abstract.

**Rating.** Contested on size. Moderate that it helps on matched tests. **Conflicts with common belief:** the "2 sigma" figure is not a safe planning number, and the completion cost is rarely mentioned.

**Limits.** The two main reviews disagree over which studies count and over test type. All old and classroom-based.

**Changes in the game.** Hard-gating every case is the risk, and the completion finding is the closest evidence to a self-paced adult. Differences in starting knowledge are large, so a scripter should be able to test out of a topic (see C8).

---

## C7. Interleaving helps when things are confusable; it is not a general rule

**Rule.** Mix practice among constructs that a learner must choose between. Do not mix unrelated topics. Test: does the player pick the right construct on an unlabelled problem a month on?

**Sources.**
- Brunmair, Richter (2019). Psychological Bulletin. doi:10.1037/bul0000209. read=FT. 59 studies, 238 effects. "g = 0.42" overall; paintings 0.67, photographs 0.35, maths 0.34; expository text and tastes not significant; words "g = -0.39", favouring blocking.
- Firth, Rivers, Boyle (2021). Review of Education. doi:10.1002/rev3.3266. read=ABS. 26 studies, mostly lab undergraduates. Hedges' g "up to 0.65" for memory and "up to 0.66" for transfer; best when differences are subtle.
- Rohrer, Dedrick, Hartwig et al. (2020). Journal of Educational Psychology. doi:10.1037/edu0000367. read=ABS. Pre-registered cluster RCT, 54 Grade 7 classes, 4 months. 61% vs 38%, "d = 0.83".
- Sana, Yan (2022). Psychological Science. doi:10.1177/09567976211057507. read=ABS. Grades 9-12, N = 155, science quizzes. Interleaved vs blocked "d = 0.35".
- Hausman, Kornell (2014). Journal of Applied Research in Memory and Cognition. doi:10.1016/j.jarmac.2014.03.003. read=ABS. Four experiments, mixing anatomy and Indonesian flashcards. No reliable effect.
- Carvalho, Goldstone (2013). Memory & Cognition. doi:10.3758/s13421-013-0371-0. read=ABS. Blocking better for low-similarity categories.
- Suzuki, Sunada (2019). Studies in Second Language Acquisition. doi:10.1017/s0272263119000470. read=ABS. 129 intermediate second-language learners. Hybrid blocked-then-interleaved beat each alone.
- Rau, Aleven, Rummel (2013). Learning and Instruction. doi:10.1016/j.learninstruc.2012.07.003. read=ABS. 158 Grade 5-6 pupils in a tutor. Which dimension you interleave matters.
- Kornell, Bjork (2008). Psychological Science. doi:10.1111/j.1467-9280.2008.02127.x. read=ABS, Yan, Bjork, Bjork (2016). Journal of Experimental Psychology: General. doi:10.1037/xge0000177. read=ABS. Learners rate blocking as better even after doing better with interleaving.

**Rating.** Moderate, higher for visual categories and maths. Contested for text and words.

**Limits.** The largest trial is school children. I found no transition rule for when to switch from blocked to interleaved: the hybrid support is one published trial plus a student-journal study I did not count. None tests code.

**Changes in the game.** A topic per case is blocked by construction, which is fine at first exposure. Later cases must then require choosing among earlier constructs without saying which, for example a clue solvable only by telling apart two similar tools.

---

## C8. Novices learn more with heavy guidance, and that advantage fades or reverses with knowledge

**Rule.** Default to a worked example then a similar problem for someone new to a topic. Check per topic, not per player, and drop examples for those who show they already know it. When unsure, give the help, since withholding costs a novice more than giving costs an expert.

**Sources.**
- Tetzlaff, Simonsmeier, Peters et al. (2025). Learning and Instruction. doi:10.1016/j.learninstruc.2025.102142. read=ABS. 60 experimental studies, 176 effects, 5,924 participants. Low prior knowledge learn better with high assistance "d = 0.505"; high prior knowledge with low assistance "d = −0.428". Not symmetrical.
- Barbieri, Miller-Cotto, Clerjuste et al. (2023). Educational Psychology Review. doi:10.1007/s10648-023-09745-1. read=ABS. Maths, elementary to postsecondary, 55 studies, 181 effects. "g = 0.48"; correct examples alone beat incorrect ones or a mix.
- Alfieri, Brooks, Aldrich et al. (2011). Journal of Educational Psychology. doi:10.1037/a0021017. read=ABS. 580 comparisons: explicit beats unassisted discovery, "d –0.38". 360 comparisons: enhanced discovery beats other instruction, "d 0.30".
- Kalyuga (2007). Educational Psychology Review. doi:10.1007/s10648-007-9054-3. read=ABS, Kirschner, Sweller, Clark (2006). Educational Psychologist. doi:10.1207/s15326985ep4102_1. read=ABS, Mayer (2004). American Psychologist. doi:10.1037/0003-066x.59.1.14. read=ABS. Narrative reviews that agree on direction.
- Simonsmeier, Flaig, Deiglmayr et al. (2021). Educational Psychologist. doi:10.1080/00461520.2021.1939700. read=ABS. Pretest knowledge vs normalised gain "rNG+ = −.059" with a prediction interval of [–.688, .621]. Prior knowledge does not uniformly help.

**Rating.** Strong.

**Limits.** Evidence is weighted to maths and science. Tetzlaff say the evidence is less clear for younger students and for humanities and language learning. Moderated by how prior knowledge is measured.

**Changes in the game.** This player is a novice in Python syntax but not in the idea of a loop, so a global "skip tutorial" is the wrong grain. Each case opens with a short check that can skip its worked example.

---

## C9. Fading from example to solo work may help, but evidence is mixed

**Rule.** Move from complete example, to examples with the last step blank, then earlier steps, then a solo problem. Compare against plain example-problem pairs if this costs extra to build.

**Sources.**
- Renkl, Atkinson, Maier et al. (2002). The Journal of Experimental Education. doi:10.1080/00220970209599510. read=ABS. Field plus 2 lab experiments. Fading helps near transfer; fading backward beats forward.
- Salden, Aleven, Schwonke et al. (2009). Instructional Science. doi:10.1007/s11251-009-9107-8. read=ABS. Adaptive beat fixed fading, which beat problem solving, in a tutor.
- Belland, Walker, Kim et al. (2016). Review of Educational Research. doi:10.3102/0034654316670999. read=ABS. 144 studies: scaffolding's effect "did not vary" with scaffolding change or its logic.
- Wittwer, Renkl (2010). Educational Psychology Review. doi:10.1007/s10648-010-9136-5. read=ABS. 21 studies: instructional explanations added to examples give minimal benefit overall, and help concept more than procedure.

**Rating.** Contested.

**Limits.** Renkl's result is near transfer only. Belland concerns general scaffolding, not example fading specifically, so it is not a direct refutation.

**Changes in the game.** Use last-step-blank variants within a case because they are cheap to write. Do not build adaptive fading on this evidence.

---

## C10. Self-explanation prompts help on average but do not reliably improve worked examples or long retention

**Rule.** Prefer a retrieval attempt to an "explain why" prompt where only one fits. Use explain prompts sparingly, structured rather than open, and measure on a delayed test.

**Sources.**
- Bisra, Liu, Nesbit et al. (2018). Educational Psychology Review. doi:10.1007/s10648-018-9434-x. read=ABS. 69 effects from 64 reports. "g = .55".
- Rittle-Johnson, Loehr, Durkin (2017). ZDM. doi:10.1007/s11858-017-0834-z. read=ABS. Maths: small to moderate immediately; evidence for classrooms and retention "much more limited"; scaffolding helps.
- Barbieri, Miller-Cotto, Clerjuste et al. (2023). Educational Psychology Review. doi:10.1007/s10648-023-09745-1. read=ABS. Adding prompts to worked examples gave "a negative effect" vs examples without.
- Larsen, Butler, Roediger III (2013). Medical Education. doi:10.1111/medu.12141. read=ABS. 47 medical students, 6 months. Testing with explanation beat self-explanation alone ("TE = 40% > SE = 29%", "d = 0.70"), testing alone also did ("T = 36% > SE = 29%", "d = 0.48"); self-explanation beat plain study ("d = 0.68").

**Rating.** Contested. **Conflicts with common belief** that prompts always add value to examples.

**Changes in the game.** Do not put "explain why this works" after every example. Asking for free-text explanation is also hard to grade without AI, so a choice among explanations is the cheap version. Whether that keeps the effect is unknown.

---

## C11. Cognitive load theory is a useful way of thinking but a poor measuring instrument

**Rule.** Use it to ask "what on screen is not needed for this step?" Do not treat a load rating as a success metric. Decide between designs on delayed tests.

**Sources.**
- Sweller, van Merriënboer, Paas (2019). Educational Psychology Review. doi:10.1007/s10648-019-09465-5. read=ABS. Statement of the theory.
- de Jong (2009). Instructional Science. doi:10.1007/s11251-009-9110-0. read=ABS. Conceptual, methodological and application problems.
- Schnotz, Kürschner (2007). Educational Psychology Review. doi:10.1007/s10648-007-9053-4. read=ABS. Theory allows contradictory explanations; reducing load can impair learning.
- Kalyuga (2011). Educational Psychology Review. doi:10.1007/s10648-010-9150-7. read=ABS. Germane load "essentially indistinguishable" from intrinsic load, added on theory not data.
- Krieglstein, Beege, Rey et al. (2022). Educational Psychology Review. doi:10.1007/s10648-022-09683-4. read=ABS. Four questionnaires: internal consistency satisfactory; correlations "partially contradict" theory, yet seem to support three factors.
- Naismith, Cavalcanti (2015). Academic Medicine. doi:10.1097/acm.0000000000000893. read=ABS. 48 simulation studies; validity evidence "mean score 1.55/5"; correlations between load and learning ran positive to negative; 71% used self-report.
- Karpicke, Aue (2015). Educational Psychology Review. doi:10.1007/s10648-015-9309-3. read=ABS. Element interactivity not quantitatively defined and applied inconsistently.

**Rating.** Contested as theory. Its practical advice is rated separately in C8 and C23.

**Changes in the game.** No in-game "how hard was that?" survey as the measure of a design. Report time and delayed score.

---

## C12. Explanatory feedback beats correct-answer feedback, which beats right/wrong; feedback can backfire

**Rule.** After an attempt give why, not just whether. Never only "wrong". Keep it about the task, not the person. Test: right/wrong-only vs elaborated on new problems.

**Sources.**
- Van der Kleij, Feskens, Eggen (2015). Review of Educational Research. doi:10.3102/0034654314564881. read=ABS. Computer-based, 40 studies, 70 effects. Elaborated "0.49", correct answer "0.32", right/wrong "0.05".
- Mertens, Finn, Lindner (2022). Journal of Educational Psychology. doi:10.1037/edu0000764. read=ABS. Network meta-analysis, 77 studies, 163 effects. Elaborated most likely most effective for recall and transfer; right/wrong less effective.
- Swart, Nielen, Sikkema - de Jong (2019). Educational Research Review. doi:10.1016/j.edurev.2019.100296. read=ABS. Learning from text, 104 contrasts, 6,124 participants, primary to university. "g+ = 0.35"; after reading, elaborated and correct-answer feedback beat right/wrong.
- Wisniewski, Zierer, Hattie (2020). Frontiers in Psychology. doi:10.3389/fpsyg.2019.03087. read=ABS. 435 studies, N > 61,000. "d = 0.48", heterogeneous, so not one treatment.
- Kluger, DeNisi (1996). Psychological Bulletin. doi:10.1037/0033-2909.119.2.254. read=ABS. 607 effects, 23,663 observations. "d =.41" but over a third of interventions decreased performance; effectiveness falls as attention moves toward the self.
- Butler, Roediger (2008). Memory & Cognition. doi:10.3758/mc.36.3.604. read=ABS. Feedback reduces false learning from multiple-choice lures.
- Metcalfe (2017). Annual Review of Psychology. doi:10.1146/annurev-psych-010416-044022. read=ABS. Corrective feedback after errors is what makes errors useful.

**Rating.** Strong.

**Limits.** Kluger covers performance broadly, not only education. How much explanation is enough is unresolved, and longer feedback may go unread by a self-learner. I found no number on that.

**Changes in the game.** Each wrong answer needs a written explanation, ideally specific to the wrong answer, which is a real writing cost per puzzle. In-story praise such as "you are a natural detective" moves attention to the self, and is the kind of thing Kluger would predict weakens feedback. That application is my inference.

---

## C13. Immediate or delayed feedback: no general winner

**Rule.** Give feedback right after an attempt is finished. Do not build artificial delay. Get the delay benefit from revisiting in later cases.

**Sources.**
- Kulik, Kulik (1988). Review of Educational Research. doi:10.2307/1170349. read=ABS. 53 studies. Applied classroom: immediate usually better. Experimental acquisition of test content: delayed usually better.
- Van der Kleij, Feskens, Eggen (2015). Review of Educational Research. doi:10.3102/0034654314564881. read=ABS. Delay lowered effects; the interaction with learning level was not significant.
- Butler, Karpicke, Roediger (2007). Journal of Experimental Psychology: Applied. doi:10.1037/1076-898x.13.4.273. read=ABS. Lab, delayed better; the authors attribute this to spacing.
- Metcalfe, Kornell, Finn (2009). Memory & Cognition. doi:10.3758/mc.37.8.1077. read=ABS. Grade 6, delayed better. College students, no difference once lag to test was controlled.
- Mullet, Butler, Verdin et al. (2014). Journal of Applied Research in Memory and Cognition. doi:10.1016/j.jarmac.2014.05.001. read=ABS. College engineering homework, 1 week delay improved transfer on exams; students preferred immediate.
- Swart, Nielen, Sikkema - de Jong (2019). Educational Research Review. doi:10.1016/j.edurev.2019.100296. read=ABS. Feedback directly after reading beats feedback during reading.

**Rating.** Contested.

**Limits.** A delay also spaces the material, so the two are confounded, and Metcalfe's adult result suggests that matters. Delay costs little in a course with a deadline, but a self-learner may simply leave. That is my inference.

**Changes in the game.** Do not interrupt mid-attempt with correction where a complete attempt fits. Respond when the code is run. A week-later feedback mechanic is not supported for this player.

---

## C14. Attempting a problem before teaching can beat teaching first, under specific conditions, and is contested

**Rule.** Use it for concepts, not for bare syntax. Keep the attempt short and support it with contrasting cases, then teach directly from the attempts. Never leave the discovery unassisted. Test on transfer problems.

**Sources.**
- Sinha, Kapur (2021). Review of Educational Research. doi:10.3102/00346543211019105. read=ABS. 53 studies, 166 comparisons. "g 0.36 [95% confidence interval 0.20; 0.51]"; stronger with fidelity; favouring instruction first for Grades 2-5 and domain-general skills; bias-corrected "g 0.87".
- Loibl, Roll, Rummel (2016). Educational Psychology Review. doi:10.1007/s10648-016-9379-x. read=ABS. Review: works "only if" contrasting cases or instruction built on student solutions are used.
- Ashman, Kalyuga, Sweller (2019). Educational Psychology Review. doi:10.1007/s10648-019-09500-5. read=ABS. Two randomised experiments, Year 5, N = 64 and 71. Instruction first better; on transfer too when element interactivity was higher.
- Newman, DeCaro (2019). Learning and Instruction. doi:10.1016/j.learninstruc.2019.05.005. read=ABS. Undergraduates, statistics, N = 123, 190, 147. Exploring beat instruct-then-practise overall; worked examples during exploration gave mixed results; helped when preceded by a pretest.
- Alfieri, Brooks, Aldrich et al. (2011). Journal of Educational Psychology. doi:10.1037/a0021017. read=ABS. Unassisted discovery loses to explicit instruction.
- Stockard, Wood, Coughlin et al. (2018). Review of Educational Research. doi:10.3102/0034654317751919. read=ABS. Direct Instruction curricula, 328 studies, all estimated effects positive except metaregressions on affect. A specific curriculum, and the abstract does not state ages.

**Rating.** Contested.

**Limits and contrary evidence.** In my judgement a bias correction that raises an effect to 0.87 is unusual. I found no independent re-analysis in the search, so I would plan around 0.36 and not 0.87. Ashman is young children, and Sinha's age moderator may partly explain the gap. Sinha's finding for domain-general skills favours teaching first, which could matter for generic programming skill. How that maps to Python is unknown.

**Changes in the game.** A detective setup invites "work it out first". That is defensible only as a short supported attempt that the following teaching uses. A puzzle a player cannot possibly solve without new syntax is unassisted discovery and is the failing form.

---

## C15. A wrong guess before study is not wasted

**Rule.** Start a case with 2-3 quick guesses about the target concept, then teach it, then show why each guess was right or wrong. Test: guessed items and related items on a 48-hour test.

**Sources.**
- Pan, Sana (2021). Journal of Experimental Psychology: Applied. doi:10.1037/xap0000345. read=ABS. 5 experiments, n = 1,573, expository text. Pretests beat post-tests at 5 min and 48 hr, with or without feedback.
- Kornell, Hays, Bjork (2009). Journal of Experimental Psychology: Learning, Memory, and Cognition. doi:10.1037/a0015729. read=ABS. Failed retrieval attempts enhanced learning, with questions designed to be unanswerable.
- Little, Bjork (2016). Memory & Cognition. doi:10.3758/s13421-016-0621-z. read=ABS. Multiple-choice pretests helped related, untested information too, over 48 hours.
- Chan, Meissner, Davis (2018). Psychological Bulletin. doi:10.1037/bul0000166. read=ABS. Meta-analysis: testing potentiates new learning; several factors can make it impair instead.
- Metcalfe (2017). Annual Review of Psychology. doi:10.1146/annurev-psych-010416-044022. read=ABS. Errors followed by correction help, high-confidence errors most.

**Rating.** Moderate.

**Limits.** Mostly text facts and short delays. No evidence I found on whether repeated failure in the first minutes discourages a voluntary novice. Treat that as a risk to measure, not as settled.

**Changes in the game.** Fits the story: a hunch before the evidence. Frame guesses as hunches, with no score or penalty.

---

## C16. Performance during learning is a poor signal of learning; difficulty helps only when it is the right difficulty

**Rule.** Never judge a design by in-session accuracy, speed or smoothness. Add a difficulty only if it makes the learner do the thing being learned. Do not add it where the material is already overwhelming.

**Sources.**
- Soderstrom, Bjork (2015). Perspectives on Psychological Science. doi:10.1177/1745691615569000. read=ABS. Integrative review: performance during instruction is unreliable as an index of learning.
- Schmidt, Bjork (1992). Psychological Science. doi:10.1111/j.1467-9280.1992.tb00029.x. read=ABS. Motor and verbal: conditions that speed acquisition can hurt long-term performance.
- Bertsch, Pesta, Wiscott et al. (2007). Memory & Cognition. doi:10.3758/bf03193441. read=ABS. 86 studies, generation effect ".40".
- Schindler, Richter (2023). Educational Psychology Review. doi:10.1007/s10648-023-09758-w. read=ABS. Text generation "g = .41", not explained by time on task, strongest when complementing what the text already prompts.
- Chen, Kalyuga, Sweller (2015). Journal of Educational Psychology. doi:10.1037/edu0000018. read=ABS. Worked examples win on high-interactivity material for novices, generation on low-interactivity.
- Chen, Castro-Alonso, Paas et al. (2018). Frontiers in Psychology. doi:10.3389/fpsyg.2018.01483. read=ABS. Many failures to get desirable difficulties occur when working memory is already stressed.

**Rating.** Moderate. The direction is well supported. "Which difficulty for whom" is mostly explained after the fact.

**Limits.** Chen and colleagues come from the cognitive-load side and argue a position; see C11 on how hard "element interactivity" is to pin down.

**Changes in the game.** Playtest reports must include a delayed check. A case that testers find smooth has not thereby shown it teaches. Do not add obscure wording or hidden information as "desirable difficulty": it is difficulty without the skill.

---

## C17. Near transfer can be taught; far transfer mostly does not happen

**Rule.** Practise the skill in several forms, have learners compare cases, and test on new problems. Do not claim the game teaches general reasoning. Test with a new problem type in a different story context.

**Sources.**
- Pan, Rickard (2018). Psychological Bulletin. doi:10.1037/bul0000151. read=FT. 192 effects, N = 10,382. "d = 0.40"; stronger with elaborated retrieval and response congruency, and affected by initial test performance; with those absent, bias-corrected estimates often show no positive transfer.
- Butler (2010). Journal of Experimental Psychology: Learning, Memory, and Cognition. doi:10.1037/a0019902. read=ABS. Repeated testing beat repeated study on new inferential questions, even from other knowledge domains.
- Alfieri, Nokes-Malach, Schunn (2013). Educational Psychologist. doi:10.1080/00461520.2013.775712. read=ABS. 57 experiments. Case comparison "d = .50"; better with similarity-finding and principles after the comparison.
- Barnett, Ceci (2002). Psychological Bulletin. doi:10.1037/0033-2909.128.4.612. read=ABS. Nine dimensions; a single far-transfer effect size is "misguided".
- Sala, Gobet (2017). Current Directions in Psychological Science. doi:10.1177/0963721417712760. read=ABS. Chess, music, working memory with children. Small to moderate effects shrink with better design. "Far transfer of learning rarely occurs".
- Simons, Boot, Charness et al. (2016). Psychological Science in the Public Interest. doi:10.1177/1529100616661983. read=ABS. Brain training improves trained tasks, little beyond them.
- Fyfe, McNeil, Son et al. (2014). Educational Psychology Review. doi:10.1007/s10648-014-9249-3. read=ABS. Concrete then fade to abstract, argued in a review. No pooled effect read.
- Blume, Ford, Baldwin et al. (2009). Journal of Management. doi:10.1177/0149206309352880. read=ABS. Workplace, 89 studies. Predictors of transfer such as motivation and work environment, stronger for open skills.

**Rating.** Moderate for near transfer through varied practice and comparison. Moderate that far transfer is rare: Barnett, Ceci (2002). Psychological Bulletin. doi:10.1037/0033-2909.128.4.612. read=ABS warn against a single verdict.

**Limits.** Most studies are not skill-acquisition settings for adults. Blume is correlational.

**Changes in the game.** Do not teach loops only through suspect lists. Vary data and story, and put side-by-side cases where two solutions share a principle. Final case: an unfamiliar task. Do not advertise "detective thinking" as a general benefit.

---

## C18. Learners misjudge what they have learned, and the misjudgement is hard to fix

**Rule.** Never use self-rating, satisfaction or a sense of ease as evidence of learning, whether in the game or in playtests. Show players their own delayed results. Tell them effort is expected, and do not rely on telling alone.

**Sources.**
- Deslauriers, McCarty, Miller et al. (2019). Proceedings of the National Academy of Sciences. doi:10.1073/pnas.1821936116. read=FT. Randomised crossover, 149 students in introductory physics at Harvard. Active class: "0.56" SD lower feeling of learning, "0.46" SD higher test score.
- Roediger, Karpicke (2006). Psychological Science. doi:10.1111/j.1467-9280.2006.01693.x. read=ABS. Restudy raises confidence and lowers delayed recall.
- Sitzmann, Ely, Brown et al. (2010). Academy of Management Learning & Education. doi:10.5465/amle.9.2.zqr169. read=ABS. Meta-analysis, education and workplace: self-assessment relates most to motivation and satisfaction, only moderately to learning.
- Kornell, Bjork (2009). Journal of Experimental Psychology: General. doi:10.1037/a0017350. read=ABS. 12 experiments: people predict little learning from more study, and overrate stability.
- Koriat, Bjork (2005). Journal of Experimental Psychology: Learning, Memory, and Cognition. doi:10.1037/0278-7393.31.2.187. read=ABS. Judgments made with the answer in view create an illusion of competence.
- Carpenter, Wilford, Kornell et al. (2013). Psychonomic Bulletin & Review. doi:10.3758/s13423-013-0442-z. read=ABS, Toftness, Carpenter, Geller et al. (2017). Metacognition and Learning. doi:10.1007/s11409-017-9175-0. read=ABS. Fluent instructor: higher perceived learning, no more actual learning. Video lecture, students.
- Kirk-Johnson, Galla, Fraundorf (2019). Cognitive Psychology. doi:10.1016/j.cogpsych.2019.101237. read=ABS. Effort read as poor learning, so effective strategies get avoided.
- Yan, Bjork, Bjork (2016). Journal of Experimental Psychology: General. doi:10.1037/xge0000177. read=ABS. Debiasing about interleaving had "only modest effects" until tests were separated by schedule.
- Yue, Bjork, Bjork (2013). Journal of Educational Psychology. doi:10.1037/a0031971. read=ABS. Learners preferred identical on-screen text though it taught less.
- Mullet, Butler, Verdin et al. (2014). Journal of Applied Research in Memory and Cognition. doi:10.1016/j.jarmac.2014.05.001. read=ABS. Preferred immediate feedback, learned better with delayed.
- Karpicke, Butler, Roediger III (2009). Memory. doi:10.1080/09658210802647009. read=ABS. 177 college students, most re-read and few self-test.
- Bjork, Dunlosky, Kornell (2013). Annual Review of Psychology. doi:10.1146/annurev-psych-113011-143823. read=ABS. Review of faulty mental models of learning.

**Rating.** Moderate by the definition used here: consistent, replicated across labs, one meta-analysis and one strong trial, but no pooled estimate of the illusion found.

**Limits and contrary evidence.**
- Rea, Wang, Muenks et al. (2022). Journal of Intelligence. doi:10.3390/jintelligence10040127. read=ABS: students can mostly recognise effective strategies and still do not use them. The problem may be doing, not knowing.
- Biwer, Egbrink, Aalten et al. (2020). Journal of Applied Research in Memory and Cognition. doi:10.1016/j.jarmac.2020.03.004. read=ABS: a pilot, N = 47, raised use of practice testing.
- Dunning-Kruger is disputed. Kruger, Dunning (1999). Journal of Personality and Social Psychology. doi:10.1037/0022-3514.77.6.1121. read=ABS is the original; Gignac, Zajenkowski (2020). Intelligence. doi:10.1016/j.intell.2020.101449. read=ABS, N = 929, argue a statistical artefact; Jansen, Rafferty, Griffiths (2021). Nature Human Behaviour. doi:10.1038/s41562-021-01057-0. read=ABS, about 4,000 per study, find support for low performers being less able to judge correctness. Do not build design on it either way.

**Changes in the game.** "Ready to move on?" with self-report should not unlock progress. A skip must be a test. Explain early that struggling on recall is the method working, and show a before-and-after on their own results.

---

## C19. One-off nudges to plan or set goals do not raise completion at scale

**Rule.** Do not rely on a plan-making prompt to keep people going. Build the return into the game. If you add a prompt, test it against completion, not early activity.

**Sources.**
- Kizilcec, Reich, Yeomans et al. (2020). Proceedings of the National Academy of Sciences. doi:10.1073/pnas.1921417117. read=FT. About 250,000 students, 247 online courses, pre-registered waves. Long-term planning prompts for committed English-fluent students: "β = 0.19 percentage points" in year 1 and "β = −0.23 pp" in year 2, both non-significant. Self-regulation prompts raised early engagement, not completion. Value-relevance raised completion only for developing-country students in courses with a global gap.
- Andor, Fels, Renz et al. (2018). RePEc: Research Papers in Economics. doi:10.4419/86788918. read=FT. Four RCTs, 15,574 participants. No significant overall effect; one course up 19%. Working paper.
- Gollwitzer, Sheeran (2006). Advances in Experimental Social Psychology. doi:10.1016/s0065-2601(06)38002-1. read=ABS. 94 tests, not education-specific. Implementation intentions "d = .65". The contrast is the point.
- Theobald (2021). Contemporary Educational Psychology. doi:10.1016/j.cedpsych.2021.101976. read=ABS. University students, extended training, 49 studies, 5,786 people. "g = .38"; feedback helped. Extended programmes differ from a single prompt.
- Sitzmann, Ely (2011). Psychological Bulletin. doi:10.1037/a0022777. read=ABS. Adults, work training, k = 430, N = 90,380. Goal level, persistence, effort and self-efficacy accounted for 17% of variance; planning, monitoring, help seeking and emotion control were not significant.

**Rating.** Strong for one-off prompts at scale in MOOCs. Moderate for sustained training.

**Limits.** MOOC learners are not game players, and the effect could differ. Sitzmann is correlational.

**Changes in the game.** A "when will you play next?" dialog is not a retention plan. Effort there goes further on what pulls people back. How to do that is outside my scope, since game hooks belong to the other agent.

---

## C20. Giving the learner control of what and when does not by itself help learning; control of pace does

**Rule.** Offer a good default path. Give the player stop, replay and step-through controls. Do not hand sequencing to the learner as a learning feature.

**Sources.**
- Karich, Burns, Maki (2014). Review of Educational Research. doi:10.3102/0034654314526064. read=ABS. 18 articles, 29 effects. "g = 0.05".
- Niemiec, Sikorski, Walberg (1996). Journal of Educational Computing Research. doi:10.2190/jv1u-eq5p-x2pb-pdba. read=ABS. 24 studies. Small and negative.
- Merkt, Weigand, Heier et al. (2011). Learning and Instruction. doi:10.1016/j.learninstruc.2011.03.004. read=ABS. German secondary pupils. Micro features such as stopping and browsing helped more than macro features such as tables of contents.
- Hasler, Kersten, Sweller (2007). Applied Cognitive Psychology. doi:10.1002/acp.1345. read=ABS. Primary pupils. Learner-paced gave better scores and lower load, though stop and play were rarely used.
- Noetel, Griffith, Delaney et al. (2021). Review of Educational Research. doi:10.3102/00346543211052329. read=FT. Design principles mattered more when system-paced ("g = 0.41") than learner-paced ("g = 0.27").

**Rating.** Moderate. **Conflicts with common belief** that self-direction is what makes adult learning work, though I found few adult-only tests.

**Limits.** The two control meta-analyses mix age groups and are old in part. Choice may still help motivation (C21).

**Changes in the game.** An open case map is fine for story reasons, not as a learning feature, and prerequisites should still constrain it. Keep replay and stepping everywhere.

---

## C21. Autonomy and interest track persistence and quality; rewards are contested

**Rule.** Explain why each skill matters. Give small choices. Prefer informational praise on the work. Do not expect rewards to cost nothing or to buy quality, and test them.

**Sources.**
- Howard, Bureau, Guay et al. (2021). Perspectives on Psychological Science. doi:10.1177/1745691620966789. read=ABS. 344 samples, 223,209 students. Intrinsic motivation tied to success and well-being, identified regulation to persistence; external regulation not tied to performance or persistence and tied to lower well-being. Correlational.
- Cerasoli, Nicklin, Ford (2014). Psychological Bulletin. doi:10.1037/a0035661. read=ABS. k = 183, N = 212,468. Intrinsic motivation predicts performance "ρ = .21-45"; incentives better predict quantity, intrinsic motivation quality.
- Deci, Koestner, Ryan (1999). Psychological Bulletin. doi:10.1037/0033-2909.125.6.627. read=ABS. 128 studies. Engagement, completion and performance rewards "d = -0.40, -0.36, and -0.28" on free-choice motivation; positive feedback "d = 0.33". Worse for children than college students.
- Cameron, Banko, Pierce (2001). The Behavior Analyst. doi:10.1007/bf03392017. read=ABS. Rewards "in general" not harmful; harm when tangible, expected and loosely tied to performance.
- Patall, Cooper, Robinson (2008). Psychological Bulletin. doi:10.1037/0033-2909.134.2.270. read=ABS. 41 studies. Choice helps, more so with 2-4 successive choices, instructionally irrelevant ones, and for children than adults.
- Lazowski, Hulleman (2016). Review of Educational Research. doi:10.3102/0034654315617832. read=ABS. 92 effects, 38,377 people. Interventions "d = 0.49", randomised designs smaller.
- Wong, Adesope (2020). Educational Psychology Review. doi:10.1007/s10648-020-09545-x. read=ABS. Emotional design: retention "g+ = 0.35", transfer "0.27", motivation "0.15".

**Rating.** Moderate for the association. Contested for rewards. **Causal evidence for design is thinner than the theory's standing suggests.**

**Limits.** Howard is correlational and mostly school and college. Patall found choice works less strongly for adults, and instructionally irrelevant choice does the most.

**Changes in the game.** Tie each case's lesson to something a scripter would want to do. Cosmetic or story choices are the kind Patall found work. Avoid rewards merely for showing up. XP design belongs with the other agent.

---

## C22. Growth-mindset messaging is not worth budget

**Rule.** Do not spend effort on lessons about mindset to raise learning. Test only if cheap.

**Sources.**
- Macnamara, Burgoyne (2023). Psychological Bulletin. doi:10.1037/bul0000352. read=ABS. 63 studies, N = 97,672. "d̅ = 0.05"; not significant after bias correction; highest-quality studies "d̅ = 0.02". Financial-incentive authors report larger effects.
- Burnette, Billingsley, Banks et al. (2023). Psychological Bulletin. doi:10.1037/bul0000368. read=ABS. 53 samples. Focal subgroups with high fidelity "d = 0.14, 95% CI [.06, .22]".
- Sisk, Burgoyne, Sun et al. (2018). Psychological Science. doi:10.1177/0956797617739704. read=ABS. Interventions k = 43, N = 57,155. "Overall effects were weak"
- Yeager, Hanselman, Walton et al. (2019). Nature. doi:10.1038/s41586-019-1466-y. read=ABS. Large pre-registered US trial of adolescents, grades up among lower-achieving students, context-dependent.

**Rating.** Weak for any general effect. The two most recent meta-analyses disagree on subgroup benefit. All are school or student populations.

**Changes in the game.** No growth-mindset lesson. Telling people struggling is normal is justified by C18, not by this literature.

---

## C23. Multimedia: signal, keep related things together, segment, cut irrelevance

Numbers marked (via Noetel) were read in Noetel, Griffith, Delaney et al. (2021). Review of Educational Research. doi:10.3102/00346543211052329. read=FT, an overview of 29 reviews, 1,189 studies and 78,177 participants, average "g = 0.38". It found only one of 29 reviews did a formal quality assessment, so the evidence is many small experiments.

| Principle | Rule | Evidence as stated | Rating |
|---|---|---|---|
| Signalling | Highlight what the current step is about | "g = 0.43", k = 209, Schneider, Beege, Nebel et al. (2018). Educational Research Review. doi:10.1016/j.edurev.2017.11.001. read=SEC (via Noetel) | Strong |
| Contiguity | Put explanation beside the code and sync it in time | "g = 0.74", k = 46; temporal "g = 0.78", k = 13 (via Noetel); Ginns (2006). Learning and Instruction. doi:10.1016/j.learninstruc.2006.10.001. read=ABS, abstract says substantial for complex material | Strong |
| Segmenting | Break into meaningful learner-paced chunks | Rey, Beege, Nebel et al. (2019). Educational Psychology Review. doi:10.1007/s10648-018-9456-4. read=ABS, 56 investigations, "small to medium", more learning time; high prior knowledge benefitted more on retention. "g = 0.34", k = 123; instructor-segmented "0.41" vs learner-segmented "0.20" (via Noetel) | Moderate |
| Coherence | Cut interesting but irrelevant details, especially persistent ones | Rey (2012). Educational Research Review. doi:10.1016/j.edurev.2012.05.003. read=ABS, 39 effects, small to medium. Sundararajan, Adesope (2020). Educational Psychology Review. doi:10.1007/s10648-020-09522-4. read=ABS "g = 0.33", k = 68; persistent "0.43", transient "0.12", CI crossing zero (via Noetel) | Moderate |
| Modality | Speech plus picture can beat text plus picture, mainly when system-paced | Ginns (2005). Learning and Instruction. doi:10.1016/j.learninstruc.2005.07.001. read=ABS "d = 0.72" as cited in Reinwein (2011). Journal of Psycholinguistic Research. doi:10.1007/s10936-011-9180-4. read=ABS, which got "d = 0.38" with 86 effects and "d = 0.20" after trim and fill. Tabbers, Martens, Van Merriënboer (2004). British Journal of Educational Psychology. doi:10.1348/000709904322848824. read=ABS, 111 students, web lesson about an hour, learner-paced: **reversed**, spoken text worse | Contested |
| Conversational style | Write to "you" | Ginns, Martin, Marsh (2013). Educational Psychology Review. doi:10.1007/s10648-013-9228-0. read=ABS: retention "d = 0.30", transfer "d = 0.54"; small and not significant in studies longer than 35 min | Moderate |
| Pre-training | Teach parts and names first | Mayer, Mathias, Wetzell (2002). Journal of Experimental Psychology: Applied. doi:10.1037/1076-898x.8.3.147. read=ABS: better transfer in 3 experiments, short lessons | Weak |

**Limits.** Most of these are short science explanations with college students. A rule's size could be different for code. Noetel, Griffith, Delaney et al. (2021). Review of Educational Research. doi:10.3102/00346543211052329. read=FT: effects are smaller when self-paced, which this game is. Rey, Beege, Nebel et al. (2019). Educational Psychology Review. doi:10.1007/s10648-018-9456-4. read=ABS's high-prior-knowledge result seems to me to run against what cognitive load theory would predict.

**Conflicts with common belief.** The modality effect is often taught as settled, but here it halves in replication, drops to 0.20 after bias correction, and reversed in a learner-paced web lesson.

**Changes in the game.** Clue text beside the code it refers to, not on another page. Highlight the current line. Short chunks with a do-step between them. Story colour that competes visually with code while the player is working is the persistent-distractor case, with the larger harm. Coordinate with the narrative agent: the rule concerns irrelevant detail shown during learning, not story as such.

---

## C24. Narration with on-screen text: the answer depends on which case you mean

The one-line "don't narrate on-screen text" is wrong as stated, because it merges cases with different evidence.

| Case | Evidence as stated | Direction |
|---|---|---|
| **A. Text is primary; add voice** | "g = -0.04", k = 23 (Adesope, Nesbit (2012). Journal of Educational Psychology. doi:10.1037/a0026147. read=ABS via Noetel). Thesis version, redundant vs text only: "−.130", k = 16, CI −.259 to −.001. Adesope, Nesbit (2012). Journal of Educational Psychology. doi:10.1037/a0026147. read=ABS abstract: "did not differ" | No gain |
| **B. Voice is primary; add text** | "g = 0.29", k = 34 (via Noetel). Thesis: ".335", k = 16 | Helps, on average |
| **C. A picture or animation is also on screen** | Thesis: with images "-.006", k = 30, vs no images ".380", k = 15. Abstract: advantage for "picture-free materials". Mayer, Heiser, Lonn (2001). Journal of Educational Psychology. doi:10.1037/0022-0663.93.1.187. read=ABS: worse with animation. Moreno, Mayer (2002). Journal of Educational Psychology. doi:10.1037/0022-0663.94.1.156. read=ABS: helps "provided there was no other concurrent visual material" | Benefit disappears |
| **D. Learner-paced** | Thesis: ".068", k = 14, not significant, vs system-paced ".220", k = 30. Abstract concurs | Benefit disappears |
| **E. Key terms, not verbatim** | Thesis: low redundancy ".526", k = 7, vs high ".158", k = 37. Abstract: key terms "associated with better learning outcomes". Mayer, Johnson (2008). Journal of Educational Psychology. doi:10.1037/0022-0663.100.2.380. read=ABS: 2-3 word labels, retention "d = 0.47 and 0.70", no transfer gain. Yue, Bjork, Bjork (2013). Journal of Educational Psychology. doi:10.1037/a0031971. read=ABS: identical text impaired; slight rewording helped; too much difference as bad; learners preferred identical. Contrary: Mayer, Heiser, Lonn (2001). Journal of Educational Psychology. doi:10.1037/0022-0663.93.1.187. read=ABS found summaries worse | Key terms usually better |
| **F. Timing** | Kalyuga, Chandler, Sweller (2004). Human Factors: The Journal of the Human Factors and Ergonomics Society. doi:10.1518/hfes.46.3.567.50405. read=ABS, technical apprentices, 25: separate-in-time beat concurrent when time was limited | Sequence helps |
| **G. Low prior knowledge** | Thesis: ".187", k = 35; high ".088", k = 3, not significant. Very few high-knowledge studies | Possibly novices only |
| **H. Non-native listeners, content learning** | Thesis L2: ".378", k = 4, N = 334, I² 82.7%. Lee, Mayer (2018). Applied Cognitive Psychology. doi:10.1002/acp.3436. read=ABS, Korean students, 16-min video in English: text only beat narration plus text, and both beat narration alone. Mayer, Lee, Peebles (2014). Applied Cognitive Psychology. doi:10.1002/acp.3050. read=ABS, fast 9-min chemistry video: captions did not help. Chan, Kruger, Doherty (2022). The Journal of Specialised Translation. doi:10.26034/cm.jostrans.2022.087. read=FT, 70 native Chinese speakers, lecture videos in an English-medium context: L1 subtitles helped; L2 subtitles were read differently and looked more demanding | Text support helps or is neutral; narration may be the weaker channel |
| **I. Non-native, reading in the foreign language** | Diao, Sweller (2007). Learning and Instruction. doi:10.1016/j.learninstruc.2006.11.007. read=ABS: tertiary EFL, written plus spoken was worse than written only, on comprehension and mental load. Thesis lists this study at "−.493" | Harm |
| **J. Non-native, learning to listen** | Diao, Chandler, Sweller (2007). The American Journal of Psychology. doi:10.2307/20445397. read=ABS: script or subtitles better on that passage, worse on a later audio-only one | Short-term gain, listening cost |
| **K. Subtitled video, language-learning outcomes** | "g = 0.99", k = 15 for comprehension; "g = 0.87", k = 10 for vocabulary (Montero Perez, Van Den Noortgate, Desmet (2013). System. doi:10.1016/j.system.2013.07.013. read=SEC via Noetel). Alotaibi, Mahdi, Alwathnani (2023). Education Sciences. doi:10.3390/educsci13030274. read=ABS: "d = 0.69", 26 studies. These outcomes are language, not content | Large benefit, but a different question |
| **L. Same-language subtitles, native speakers, content** | Gernsbacher (2015). Policy Insights from the Behavioral and Brain Sciences. doi:10.1177/2372732215602130. read=ABS: narrative, over 100 studies, "benefit everyone". A narrative policy piece, not a meta-analysis. Kruger, Steyn (2013). Reading Research Quarterly. doi:10.1002/rrq.59. read=ABS: English lectures, reading subtitles correlated with comprehension; correlational. Kruger, Hefer, Matthew (2014). Journal of Eye Movement Research. doi:10.16910/jemr.7.5.4. read=ABS: "promising" for L1 and L2 | Thin. Two searches found no meta-analysis |
| **M. Audio vs print** | Singh, Alexander (2022). Educational Psychology Review. doi:10.1007/s10648-021-09653-2. read=ABS: co-presenting audio with print beat print for struggling readers and EFL, "g = .32 to g = 1.67"; "a paucity" for older students with no identified needs. Brysbaert (2019). Journal of Memory and Language. doi:10.1016/j.jml.2019.104047. read=ABS: adults read silently at "238 words per minute (wpm)" for non-fiction; oral reading "183 wpm"; slower with English as a second language | Fluent readers are slowed by forced narration (my inference from rates) |

Thesis means Adesope (2010). Summit (Simon Fraser University). no DOI, summit.sfu.ca etd5852. read=FT, Chapter 3: an earlier version of the journal meta-analysis, 48 effects from 32 reports and N = 3,192, whereas the journal has 57 studies. I could not get the journal's full text, so its tables are known only via its abstract and Noetel. Thesis results were heterogeneous in most categories, with an overall I² of 82.8%, and postsecondary was 35 of 48 effects. Cases C, D, E and G are moderator analyses, which are not experiments. The thesis also says of the low-redundancy category that it was highly heterogeneous, with mixed results inside it.

**Reconciling redundancy with subtitles.** Chan, Kruger, Doherty (2022). The Journal of Specialised Translation. doi:10.26034/cm.jostrans.2022.087. read=FT point out that classic redundancy studies were not on subtitled video, and cite Kruger's work as showing no redundancy effect there. That matches cases C to E only partly. No study I read compares them head-on, so why they differ is unknown.

**Rules.**
1. In a self-paced, text-led game, do not add voice-over of the text for learning reasons. Expected gain is about zero. Add it for accessibility or atmosphere and only if it can be turned off and the text is not locked to its pace.
2. If a passage is voice-led, add short key terms placed next to the code or diagram rather than the whole transcript.
3. If code or a diagram needs attention, do not make the player read a transcript and listen at the same moment. Note that all image evidence concerns diagrams and animations. Applying it to code is my inference.
4. Always provide a captions toggle, for access and because non-native players mostly benefit. Do not turn captions off on the strength of the redundancy principle: the evidence of harm is from short system-paced lessons and is not specific to subtitles. Default on or off is untested for this case; if voice is used at all, I would default to on for non-native locales and leave it as a user setting elsewhere.
5. For a non-native player, the safest route to content is written text they can pace. This is supported by Lee, Mayer (2018). Applied Cognitive Psychology. doi:10.1002/acp.3436. read=ABS but the evidence is thin, with one study at that design and Diao, Sweller (2007). Learning and Instruction. doi:10.1016/j.learninstruc.2006.11.007. read=ABS pointing the other way when reading is itself hard.
6. A/B test: full narration plus text vs text alone vs voice plus key terms; measure 1-week delayed score and time on task, split by native and non-native players.

**Rating.** Moderate for A, B, D and E as averages. Contested for H, I and J. Weak for L. **Conflicts with common belief** in both directions: the pure redundancy principle (redundancy always harms) and the claim that captions benefit everyone.

**Changes in the game.** The default build is text-first with no voice-over. That saves large audio cost at no expected learning loss, judged from these averages. If voice is used for story scenes, its text can be a transcript when no code is on screen, and only key terms when it is.

---

## C25. Ideas not to design around

| Idea | Finding | Sources | Rating |
|---|---|---|---|
| Learning styles (matching to visual or auditory) | "Virtually no evidence" for the needed interaction, though many versions untested. Tests meeting the criteria: very low, non-significant effects. College adults, audiobook vs e-text: no interaction | Pashler, McDaniel, Rohrer et al. (2008). Psychological Science in the Public Interest. doi:10.1111/j.1539-6053.2009.01038.x. read=ABS, Aslaksen, Lorås (2018). Frontiers in Psychology. doi:10.3389/fpsyg.2018.01538. read=ABS, Rogowsky, Calhoun, Tallal (2015). Journal of Educational Psychology. doi:10.1037/a0037478. read=ABS, Rogowsky, Calhoun, Tallal (2020). Frontiers in Psychology. doi:10.3389/fpsyg.2020.00164. read=ABS, Cuevas (2015). Theory and Research in Education. doi:10.1177/1477878515606621. read=ABS | Moderate that it fails: few direct tests, all null; no credible positive evidence found |
| Learning pyramid ("90% of what you teach") | Not from empirical research; versions predate it by over 160 years; "The Pyramid is rubbish" | Letrud, Hernes (2018). Cogent Education. doi:10.1080/2331186x.2018.1518638. read=ABS, Masters (2019). Medical Education. doi:10.1111/medu.13813. read=ABS | Strong as a debunking of the numbers. The general point that doing beats passive reception has its own evidence, C1 |
| Digital natives and multitasking | No such skilled native; designing for multitasking hurts | Kirschner, De Bruyckere (2017). Teaching and Teacher Education. doi:10.1016/j.tate.2017.06.001. read=ABS | Moderate. Review |
| 10-15 minute attention limit | Primary data do not support it; variation is mostly between teachers | Bradbury (2016). Advances in Physiology Education. doi:10.1152/advan.00109.2016. read=ABS, Wilson, Korn (2007). Teaching of Psychology. doi:10.1177/009862830703400202. read=ABS. Observational contrast: Guo, Kim, Rubin (2014). Proceedings of the first ACM conference on Learning @ scale conference. doi:10.1145/2556325.2566239. read=ABS, 6.9 million sessions, shorter videos more engaging | Moderate against the number. Engagement data say keep things short, but that is engagement, not learning |
| Brain training, "learning to think" | Trained task improves; little beyond | Simons, Boot, Charness et al. (2016). Psychological Science in the Public Interest. doi:10.1177/1529100616661983. read=ABS, Sala, Gobet (2017). Current Directions in Psychological Science. doi:10.1177/0963721417712760. read=ABS | Strong |
| Deliberate practice as the whole story | "4% for education" of performance variance, under 1% for professions | Macnamara, Hambrick, Oswald (2014). Psychological Science. doi:10.1177/0956797614535810. read=ABS | Moderate |
| 85% correct is the optimal difficulty | Derived for gradient-descent learners on binary classification; shown in neural networks. I saw no human instructional trial in the sections read | Wilson, Shenhav, Straccia et al. (2019). Nature Communications. doi:10.1038/s41467-019-12552-4. read=FT | Weak for teaching. Do not use as a tuning target without testing |
| Bloom's 2 sigma | See C6 | Bloom (1984). Educational Researcher. doi:10.2307/1175554. read=ABS, Slavin (1987). Review of Educational Research. doi:10.2307/1170235. read=FT | Contested |
| Andragogy (adults need a distinct theory) | Empirical literature "inconclusive", "a fragmented article of faith at best" | Rachal (2002). Adult Education Quarterly. doi:10.1177/0741713602052003004. read=ABS | Weak as a basis. I found no direct test of whether adults learn by different mechanisms |
| Neuromyths generally | Teachers interested in neuroscience believed 49% of those tested | Dekker, Lee, Howard-Jones et al. (2012). Frontiers in Psychology. doi:10.3389/fpsyg.2012.00429. read=ABS | Survey; shows prevalence, not effect |
| Re-reading and highlighting | Karpicke, Butler, Roediger III (2009). Memory. doi:10.1080/09658210802647009. read=ABS calls re-reading of "limited benefit" yet most students do it. Donoghue, Hattie (2021). Frontiers in Education. doi:10.3389/feduc.2021.581216. read=ABS: underlining and summarization least effective "but still with relatively high effects", so not useless. Dunlosky, Rawson, Marsh et al. (2013). Psychological Science in the Public Interest. doi:10.1177/1529100612453266. read=ABS is the usual source, but I read an abstract without its ratings | as listed | Moderate |

---

## C26. Video is fine, and adding it helps, in college trials

**Rule.** Use video or animation if it shows something text cannot, and do not treat it as a teaching method in itself.

**Sources.**
- Noetel, Griffith, Delaney et al. (2021). Review of Educational Research. doi:10.3102/0034654321990713. read=ABS. 105 randomised trials, 7,776 college students. Swapping in video "g = 0.28"; adding video "g = 0.80"; possible publication bias.
- Noetel, Griffith, Delaney et al. (2021). Review of Educational Research. doi:10.3102/00346543211052329. read=FT. Meaningful animation "g = 0.40"; decorative "g = -0.05" (from Höffler and Leutner as reported there).
- Koedinger, Kim, Jia et al. (2015). Proceedings of the Second (2015) ACM Conference on Learning @ Scale. doi:10.1145/2724660.2724681. read=SEC. Doer effect, doing beat watching in a MOOC. Abstract not retrieved; title and secondary description only. Another search result reported failing to find this effect in one course, which I did not verify.

**Rating.** Moderate for video in college. Weak for "doing beats watching" as read here, though C1 supports the direction.

**Changes in the game.** No requirement for video. A short animation of execution order could qualify. Decorative motion does not.

---

## What I looked for and could not establish

- **Any study of narration, subtitles or redundancy with code as the visual.** None found. Everything applied to code in C24 is inference.
- **A meta-analysis of same-language subtitles for native speakers learning content.** Two searches found none. Case L is thin.
- **The full tables of Adesope, Nesbit (2012). Journal of Educational Psychology. doi:10.1037/a0026147. read=ABS.** I used the thesis version and Noetel's report of the journal's numbers.
- **Numbers in Rowland (2014). Psychological Bulletin. doi:10.1037/a0037559. read=ABS, Adesope, Trevisan, Sundararajan (2017). Review of Educational Research. doi:10.3102/0034654316689306. read=ABS, Kulik, Kulik, Bangert-Drowns (1990). Review of Educational Research. doi:10.2307/1170612. read=ABS, Rey (2012). Educational Research Review. doi:10.1016/j.edurev.2012.05.003. read=ABS, and Ginns (2005). Learning and Instruction. doi:10.1016/j.learninstruc.2005.07.001. read=ABS directly.** Search snippets gave figures from secondary sources, which I did not report as read.
- **Effects for adults learning alone, voluntarily, without grades.** Closest: MOOC trials (C19), medical residents (C1), work-training correlational data (C2, C19). So all transfer to this player is unknown in size.
- **A switch-over rule from blocked to interleaved practice.** Thin hybrid support only (C7).
- **Hint design outside intelligent tutors.** Almost nothing found. The other agent's scope may have more.
- **Whether pretests or failing first discourage voluntary novices.** Learning effects are known; dropout effects were not found.
- **An independent check of the 0.87 bias-adjusted estimate in Sinha, Kapur (2021). Review of Educational Research. doi:10.3102/00346543211019105. read=ABS.** One search found no critique or replication, which does not show none exists.
- **A multi-lab, pre-registered replication of the testing effect.** One search found none. Rummer, Ende, Glim et al. (2025). preprint, no venue in record. doi:10.31234/osf.io/d7pcx_v1. read=ABS is a single-lab preprint.
- **Whether the learning-rate regularity holds.** Koedinger, Carvalho, Liu et al. (2023). Proceedings of the National Academy of Sciences. doi:10.1073/pnas.2221311120. read=FT vs Lee, Lichand, Barnard et al. (2026). Proceedings of the Thirteenth ACM Conference on Learning @ Scale. doi:10.1145/3774398.3811619. read=ABS is live. I read only the critique's abstract, and I found no reply.
- **Sources dropped because no abstract or text could be retrieved, so no claim uses them:** Kapler 2015 on spacing, Broadbent and Poon 2015 on online self-regulation, Tarchi 2021 on subtitles, Uttl 2017 on student evaluations, Gick and Holyoak 1983, Moreno 2010.
- **Source quality.** Web search summaries contained errors and hedges, so they were used to find works, not as evidence. No figure here comes from a blog or a search snippet.
