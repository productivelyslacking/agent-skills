---
name: teaching-programming
description: Teaching people to program: exercises, autograders, error help, debugging and tracing tasks, moving between languages. Use when designing a coding lesson, exercise or checker, or hints for learners' code. Also load teaching-design.
---

# Teaching programming

Assumes **teaching-design**, which has the general rules and how far to trust them. Thesis: **programming skill is a working
model of the machine, used to read, predict, debug and compose code; code that passes with help shows none of it.** From a
literature review, not from use (D22). Tags like `[G-A1]` are entries in `../teaching-design/EVIDENCE-CODE-GAMES-AI.md`. Most
evidence is students or children, none an adult scripter moving to Python. Samples and numbers: `NOTES.md` beside this file,
read on demand.

## Reading before writing

- **Have the learner predict the output before writing similar code.** Reading and tracing correlate with writing. Moderate for
  the correlation, weak that reading first causes better writing: no randomised test of the order was found [G-A1].
- **Predict, run, investigate, modify, make** is a usable lesson shape, tested teacher-led in schools; untested on self-learners,
  and whether a tutor can replace its talk is unknown [G-A2].
- **Parsons problems save time at first contact, with equal learning a week later.** Build distractors from known errors, fade
  them, and never treat one as proof of writing ability. Let a learner who scripts already skip them, since they may suit novices
  more and some dislike them (inference). Moderate [G-A3].
- **Label worked-example steps by purpose, and reuse those labels in hints.** It helped quizzes more than exams, at-risk students
  most; reuse in hints is inference. Moderate, contested [G-A4].

## The machine

- **Make "how the language runs this" a goal, and show state changing line by line;** novices often lack that model. Give Python's
  list references and mutation their own lesson. Moderate that the misconceptions exist, weak that any given visual
  fixes them [G-A5].
- **Don't write a ranked misconception list from memory;** none is established for Python adults. Collect one from your learners [G-A5].

## Errors and debugging

- **Keep the real error message visible, and add short, plain, hand-written help for the errors each lesson will produce,** since
  reading real messages is the skill. Contested overall; moderate for readability and speed, no evidence on transfer; keeping the
  original alongside is inference [G-A6].
- **Teach a named debugging procedure and make the learner use it:** learners default to trial and error even knowing better.
  That enforcing a procedure fixes this is untested. Weak to
  moderate [G-A7].
- **A fallible, self-blaming character for error framing has one small developer-run study behind it.** Weak [G-A6].

## Checkers

- **Say what the output differed in, not just fail.** Weak: descriptive reviews, no strong trial [G-A8].
- **Consider hidden, changed inputs for the final check,** so tests don't become a guess-and-check loop: the evidence author's rule,
  not a tested result. Whether to penalise repeat runs is unknown. Weak [G-A8].
- **Unaided checks include reading and debugging items, not only writing,** on changed surfaces, and don't double as practice.
  Moderate as method [G-C13]. SCS1 could give an outside measure; its access is unchecked and it skips Python syntax.

## Plans, order and prior languages

- **Teach named patterns (filter, accumulate, count) and how to merge them, as goals separate from syntax;** plan composition is a
  known difficulty. Weak from what was read [G-A9].
- **Order topics by dependency, and don't claim the order is evidence-based:** no randomised comparison was found. Secure early
  concepts, since later ones build on them; that part is a hypothesis [G-A11].
- **Ask which language the learner already uses, and show contrasts only where constructs look alike but behave differently,** since
  false carryovers cause the most trouble. Moderate. What Bash or PowerShell scripters get wrong in Python is unknown: collect it from
  their errors, not memory [G-A10].

## Programming games

- **Prefer guided debugging missions to an open sandbox:** in the nearest adult evidence a debugging game matched a course in about
  half the time and a free-build tool taught nothing measurable. Moderate to weak, no independent replication [G-B8].
- **Set expectations:** a game of a few hours may not take someone from zero to real programs. Measure, don't promise [G-B8].
- **Plan for loss in the first units.** The evidence author predicts the steepest loss there and suggests a first unit finishable in
  one sitting; neither is tested for a game [G-A12].

## Not established

Bash or PowerShell to Python; a ranked Python misconception list; reading-first order; PRIMM outside schools; adult self-learners with
an LLM tutor; a validated Python-specific unaided test for adults. Mark them unknown, and don't fill them in.
