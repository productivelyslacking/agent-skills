---
name: story-design
description: Any story meant to hold an audience: structure, openings, chapter endings, twists and fair clues, casts, content rating, reviewing generated drafts. Use when outlining, writing or reviewing a story. Player-driven stories: also interactive-story.
---

# Story design

Assumes **ground-truth**. Thesis: **know which story decisions rest on a measurement, which on craft opinion and which
on nothing, and write each so a reviewer can check it**, not a fluent, formula-shaped story defended with folklore.

**How far to trust this.** Research-based and unproven: written from a review, not from use (D23 in
`docs/DECISIONS.md`); its first real test is a story game's first playtest. Most measured studies were read only as
abstracts, and most used students, one sitting, short stimuli and self-report. `NOTES.md` beside this file holds the
numbers, examples and dates.

**Reading a rule.** Claim, reason, sources, kind. `[M8]` is entry 8 in `EVIDENCE-MEASURED.md`; `[C19]`, `[CD3]`, `[CW2]`
are a claim, disagreement and weak-support item in `EVIDENCE-CRAFT.md` (spoiler warning at its top). Kinds: *measured*,
rated per case; *practitioner*, *critic*, *official*, *vendor* report what someone says, rated for standing, not truth;
*demonstrated* means a work does it, not that it worked; *inference* is untested reasoning. Read the entry before a hard
decision; add no sources from memory. For a story in a learning product, also load **teaching-design**.

## What isn't known

- **Treat "the story will bring them back" as a hypothesis.** No study found shows a story bringing adults back,
  measured by return; the nearest results are about children in paid visits [M9] and a pull that comes from pairing, not
  plot [M12]. [M9, M12, M13] Measured: weak for children, weak as evidence about story, no evidence for adults.
- **Count returns; don't report an absorption score as return.** Absorption goes with enjoyment and attitudes, none
  found predicting return, and in a game it correlated nearly perfectly with flow, so it can't credit the writing. [M4,
  M5, M9] Measured: strong for attitudes, no evidence for return, weak for the rest. Inference.
- **A high stop rate alone doesn't indict the story.** Low completion is common on Steam, unsplit by amount of story;
  compare with earlier or story-thin builds. [M13, M15] Measured: moderate as description, no evidence for story games.
  The comparison is inference.
- **Don't lean on popular claims.** Unfinished things aren't better remembered, though people do resume lab tasks;
  neither tested in stories [M11], measured, moderate. Spoilers neither ruin nor improve stories: small, inconsistent
  effects [M22], measured, contested on direction, moderate that it's small. No formula was tested (not proof none
  exists) and named arcs are correlational [M40, C5], measured, no evidence and weak. Shifting emotional direction
  raised engagement in one paper on film ratings and article reading, stronger for thrillers, untested in chapters or
  games [M40], measured, moderate.

## Openings and chapter endings

**The research has almost nothing on openings or first chapters**: these rules borrow from nearby evidence, which is
inference. Chapter endings have a little direct evidence, none on adult behaviour.

- **State no number for how soon the question must come.** The one figure is weak, and the act and teaser templates come
  from film and TV guides; none links timing to quality or covers chapters. Record where the question first appears;
  don't grade it. [C1, C4, C11] Critic; measured weakly; low standing.
- **Raise a question the audience can half-answer.** Curiosity peaks at moderate confidence (lower when the answer feels
  important): give enough for a suspicion; a stake may stand in for knowledge. [M1] Measured: moderate for trivia, weak
  for stories; inference.
- **Let them start something of their own**, such as an unsolved case: people tend to resume what they began. [M11]
  Measured: moderate for lab tasks, no evidence in stories; inference.
- **Deliver or deliberately subvert what the opening promises.** Feints promising another story are blamed for one
  game's trouble; deliberate misleading drew critics. A mystery's culprit is met early, undefined. [C13, C40, C49]
  Critic; demonstrated; practitioner, period.
- **Don't judge a first chapter by what it drew**: violent descriptions raise choosing, not average enjoyment. Count who
  starts the next chapter. [M34] Measured, moderate; the count is inference.
- **End a chapter on an unanswered question; don't count on a peak moment.** A cliffhanger beat a resolved ending on
  desire for more at no cost to enjoyment, but not a merely open one; children kept playing serial parts. [M8, M9]
  Measured: contested on intention, moderate on enjoyment, weak for children, no evidence on adult return. That openness
  does the work is inference.
- **Pay something in each chapter, and don't test this by asking what people prefer**: people ask for everything yet
  enjoy teasing more (resolution is half of what was measured), and unanswered boxes are blamed for eroding trust. [M2, C12, C53] Measured: moderate for trivia
  and ads, weak for stories, no evidence for long-form; critic, second-hand. Doing both in a chapter is inference.
- **Test chapter endings instead of borrowing act-outs**, which fit commercial breaks; a peak may matter more for continuing at once than across a gap.
  Recap on return: testers playing scenarios apart forgot context (inference that it holds across real gaps). [C11, C24,
  M8] Critic, low standing; practitioner; measured, no evidence on real gaps.

## Structure

- **Use a named structure as questions on a finished outline, never as page targets or proof.** None is shown to cause
  better stories; whether templates or only mechanical use cause sameness is argued by anecdote, with no condition for
  choosing. An LLM likely fills a beat sheet literally. [C2, C3, C5, C7, C80, CD8, CW1] Critic and practitioner,
  contested; inference on LLMs.
- **Plan a long middle by goal changes, not as one act.** One study, read second-hand, has parts turning on goals and
  new information; nothing supports an interval. [C3, C25] Critic and practitioner, descriptive; inference.

## Surprise and fair clues

- **Test a reveal with five questions, not Knox's or Van Dine's lists** (several of their rules are racist or class
  artefacts): Indicated beforehand? Explains everything before it? Surprises? No authorial lie? Only real-world rules or
  ones already given? [C13, C14, C15, C50, M21, CW9] Practitioner, period, for the lists; critic, low standing, for the
  reduction; the sorting is inference; measured, no evidence on fair foreshadowing.
- **A narrator may conceal if no sentence lies on re-reading.** The best-known case was judged fair, yet stays
  controversial and a one-off; whether unreliable narration raises engagement isn't known. [C17, M23] Demonstrated and
  critic; the test is inference; measured, no evidence.
- **Don't solve anything with coincidence, intuition or a power introduced for the purpose.** [C16, C50] Critic
  reporting practitioners, low standing; practitioner on magic; applying that to reveals is inference.
- **Keep more than one suspect plausible as long as you can.** Enjoyment rose with uncertainty in one study; no pool
  size was found. [M20, C18] Measured, weak; critic, single.
- **Don't let the story depend on a twist staying hidden.** Spoilers do little harm, but people underpredict harm from
  spoiling how a plot unfolds, so protect that; it doesn't cover a spoiled thing the audience must solve. Not permission
  to spoil: an owner keeping their own first play unspoiled decides that (**directing**). [M22] Measured, contested on
  direction; inference.

## Character

- **Show what the lead does for others before asking anyone to hope.** Moral behaviour built disposition, which
  predicted hope (and wanting liked characters to act immorally if it improved their odds); it explained liking of the
  ending better than overall enjoyment. [M7] Measured, moderate, written text, one sitting. Acts for others, a grey act
  costing less, and this saying little about continuing are inference.
- **Give every named character a goal that isn't about the protagonist.** [C33, C58e, C63] Practitioner, untested; the
  grouping is inference.
- **Ask of each archetype: what are we saying about this character that we aren't intending?** [C52] Practitioner, about
  companions; widening it is inference.

## Cast and tropes

- **Check who holds power, who's guilty and who dies, not headcount**: a generated cast can look balanced with no
  interior life. [C58e] Practitioner, plus measured LLM defaults; inference.
- **For each harm, ask whose story it serves and whether the victim has one to lose.** A pattern and a purpose make the
  trope, not one death; sources differ on gender or role, with no condition for choosing. [C58a, CD13] Practitioner,
  contested; inference.
- **Check named stereotypes against the role**, such as the femme fatale and the Dragon Lady (harm argued, not measured;
  `NOTES.md`); mentors who exist to die: nothing reached. These are what the research reached, not a list: absence here
  clears nothing. [C28, C52, C58b, C58c] Critic and practitioner; inference.
- **Decide cast balance and sexualised casting on what the story needs and who it's for**: box-office links are
  associations, attitude effects small and disputed, and who a cast drives away is measured in one hostile community.
  [M32, M33] Measured: weak for association, no evidence for cause, moderate on small attitude effects, contested on
  their meaning.

## Violence, sex and language

Darkness and graphic content are separate decisions: remembered loss is valued [M36]; violence isn't shown to raise
average enjoyment [M34], moderate, contested at the margin; "sex sells" fails for ads, and sex in stories is unmeasured
[M35].

- **Sexual content involving anyone not clearly an adult is excluded, in every project**: a fixed limit of this library.
  [no research: D23]
- **Name what each violent or profane beat does in the plot or a relationship, or cut it.** Makers and a critic report
  it cheapening as filler or when claimed meaningful without consequence; sources split on meaning against silly, so
  pick a tone; horror audiences differ. [C68, C70, C72, CD11, M34] Inference from four sources, no outcome data;
  measured, moderate, contested at the margin.
- **Do a profanity pass after drafting, and check recorded takes.** [C69] Practitioner, the only statement found;
  checking takes is inference.
- **After a bleak scene, count who stops**: those who quit aren't in the samples. [M36] Measured: moderate when
  remembered, no evidence on continuation; inference.
- **Write the project's limit down, axis by axis, before drafting.** The owner decides; apart from the exclusion above,
  this skill sets none. Recorded voice is costly to change; leaving out nudity alone won't lower a rating. [C62a]
  Inference.
- **Read the ESRB and MPA guides before arguing a rating** (summary in `NOTES.md`). No rating body assessed any of this;
  both hedge, neither covers works told in stills, MPA's rules PDF wasn't opened and MPA rates films (an analogy).
  Whether a self-published web game needs an ESRB rating wasn't researched. [C59, C60, C61, C62] Official.

## Generated fiction

Vendors wrote some sources and a contrary paper went unread [C83]: sameness isn't settled.

- **Plan twists, foreshadowing and payoffs outside the model.** LLM stories were read as accelerating without resolving
  the plot, from a model-judged uniqueness score after peaks. [C74] Measured proxy, short stories, 2023-24 models;
  reading it as pacing is the authors'; the plan is inference.
- **Expect the first idea to be everyone's; instruction wording won't change that, and temperature is reported not to.**
  Plots repeat across runs and models; a better or stranger premise lifted scores for humans and models alike. [C73,
  C74, CW15] Measured, corroboration some; temperature second-hand.
- **Supply names, jobs and settings rather than only banning names**: defaults differ by model family and shift by
  version, so a banned list goes stale. [C75, C76, C82] Measured, preprints; supplying them is untested inference.
- **Plan in stages a human reviews, with shared memory across scenes, and expect mostly deletion.** [C80] Measured,
  qualitative, 15 users of the authors' own 2022 tool; most, not all, tended to cut.
- **Don't accept general-reader preference as a gate.** Experts preferred humans to prompted AI, general readers didn't,
  and fine-tuning on an author reversed it. Use only text you have rights to. [C79, CD14] Measured, blind, short
  literary excerpts. That experts should gate is inference: where general readers are the audience, their preference is
  still data, but not a stand-in for quality.
- **Rank tell-lists below structural checks**: they go stale and don't fix plot. [C81, CW13] Critic, not opened;
  inference.

## Checks

Run `CHECKS.md` (draft audit, first-chapter check) on any draft of a scene or larger before handing it back, and keep
the results with it. Derived rules, not measured.

## Not established

Write as unknown: first chapters; free samples; adult return; suspense against surprise over long play; fair
foreshadowing; unreliable narrators; cast balance as a cause; sexual content and enjoyment; antagonists, betrayal and
long-serial tension. The evidence files end with full lists.
