---
name: prose-editing
description: Cutting and shaping written work: docs, runbooks, READMEs, reports, prompts and instructions for models. Use when editing or reviewing prose, when a draft is padded or hedged, or before shipping written work.
---

# Prose editing

Assumes **ground-truth**. This is about the words and the shape, not the facts. `NOTES.md` beside this file holds
worked examples.

## The test

Every sentence tells the reader **what to do**, **what to expect**, or **what happens if they get it wrong**; cut one
that does none. Concision is not brevity: never cut substance to hit a length, cut the scaffolding around it.

## Cut

- **Throat-clearing.** Put the substance in the first sentence.
- **Restatement.** Say it once, in the best place.
- **Filler transitions** ("it's worth noting that", "as mentioned above", "in order to").
- **Editorializing that changes no behavior** ("unglamorous but important").
- **Vague quantification** ("a surprising share"). Give the real reason it works, or cut the claim.
- **Hedging** that avoids committing. State real uncertainty plainly, with the decision criteria.
- **Blockquotes for emphasis.** Keep them for warnings that change what someone does.

## Cut what marks text as generated

A model picks what fits the widest range of readers; a writer picks for one reader and one subject. Look for the structure
first, because word habits change with each model. A sentence stays only if it gives this reader something they don't have.

- **Staging instead of stating.** "Not X but Y" when nobody said X, a one-line closer that repeats the point, a run-up
  before the point, a saying that sounds deep and claims nothing. State the fact.
- **Rhythm by rule.** Triads and dashes everywhere, repeated sentence openings, stacked qualifiers. Use three items when
  there are three.
- **Inflation.** Ordinary facts called pivotal or robust, sales language, unnamed authorities, "-ing" riders implying
  meaning. Say what it does, or cut it.
- **Formatting by rule.** Bold on every item and a heading on every thought, where the emphasis or structure means nothing.
- **Draft leftovers.** Chat wrappers, knowledge-limit disclaimers, a heading repeated as the first sentence, text about
  the document rather than its subject.
- **The wrong reader.** Re-explaining what they already know, so the decision arrives last.

Keep what the writer meant, and add nothing to replace what you cut. A real contrast, a true list of three or a quoted
source stays; a tell counts only when it adds nothing.

## Protected: the *why* is never fluff

Keep a sentence explaining **why** (this order, this tool, this check first, this step can't be skipped) though it
issues no instruction: the reason lets the reader handle the case the document didn't anticipate and see when the
procedure no longer applies. Give the reason wherever it isn't obvious, above all for security and compliance rules,
where intent is what lets someone apply the rule where none covers. When a sentence carries a flourish and a reason,
rewrite it to keep the reason. The test is **"would the reader be worse at this without it."**

## Cut unearned structure

Add tiers, tables, matrices, nested headings or branches only where the work needs them, not because they look
rigorous. Ask: does the work actually branch here (if every reader takes the same path, it's a list)? Is this step
needed, or does it only look thorough? If the procedure is four steps, write four: a four-step procedure followed on
first read beats a correct nine-step one that gets skimmed. Gotchas, sequencing traps and the why stay.

## Instructions a model loads

Rule sheets, skills, role files and prompts are paid for in tokens every time they load, and the reader is a model
that needs the rule, not the story of it. Price them by when they load (D28):

- **Every session** (rule sheets, skill and role descriptions): the rule alone. A description says what the skill
  covers and when to load it, in under 300 characters; `tools/check.py` enforces the budgets.
- **On use** (a skill or role body): the rule plus one clause of reason. One concrete failure only where the rule
  reads as optional without it, without dates, counts or project names.
- **On demand** (`NOTES.md`, `EVIDENCE*.md`): the incidents, numbers, dates and sources. The body points there.

Write imperatives. Don't restate a rule another loaded file holds; point to it by name. A pinned requirement in
`docs/REQUIREMENTS.tsv` moves with its rewrite, never silently.

## Shape of a procedure

Purpose → When to use → Before you start → Steps → **Verify** → If it doesn't work → Escalate

- **Never omit Verify**: it is the most often skipped and most valuable part.
- One action per step. Name UI elements exactly. Give the full path.
- **Flag irreversible steps before the step**, not after.
- Write for a competent stranger: knows the domain, has never seen this environment.
- Titles name what someone would search for. No dates, versions, or "v2".

## Tone

- Plain language, short sentences.
- **Don't soften constraints with teeth** (forfeiture, termination, data loss, personal liability): say so plainly.
- Link vendor documentation rather than copying it, and document only what's specific to how you work: a reprint is
  stale on arrival.
