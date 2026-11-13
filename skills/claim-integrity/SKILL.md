---
name: claim-integrity
description: Documents whose claims someone will rely on: security plans, compliance statements, policies, handbooks, marketing copy, status pages. Use before writing or editing one, or whenever a sentence asserts a capability, certification, threshold or practice.
---

# Claim integrity

For documents whose sentences *are* the deliverable, relied on by someone. Assumes **ground-truth**. The
question for every sentence: **what makes this true, and what would make it false?** Incidents behind these rules are in
`NOTES.md` beside this file.

## Decide first: are you describing or prescribing?

The two have opposite failure modes, and mixing them makes a document both wrong and unactionable. Say which it is, in
the document.

- **Descriptive** (a security plan, handbook, status report, README of current behaviour) must match reality: stating a
  better practice than the one in place is a false claim, and a costly one where the document creates an obligation.
- **Prescriptive** (a standard, runbook, spec, target state) must state the correct practice: documenting today's weaker
  habit makes it permanent. State the standard, then flag the shortfall.

## The claim register

Where claims accumulate, keep one file: **one row per checkable claim, with its basis and what would falsify it.**

| Claim | Where it appears | Basis | Falsified by |
|---|---|---|---|

- **A claim without a Basis isn't ready:** that turns "sounds defensible" into "is sourced", and nothing automated can
  check whether a sentence is true.
- **Narrow the wording when the falsifier is easy to test,** rather than dropping the claim.
- **Record the date, who confirmed it, and whether the basis is a business statement, a primary source or an
  inference:** they decay differently.
- **Keep retired claims, struck through, with the reason and the reasoning that collapsed:** a claim removed without
  trace gets reintroduced in good faith.
- **Couple a claim to its mechanism:** when the mechanism goes, the claim goes in the same change, and the register
  records the coupling so it isn't reinstated without it.

## Mark unknowns with the right marker

- **`[CONFIRM: x]`**: a local fact unknowable from outside (a contact, an SLA target, a contract term, a headcount).
  Someone fills a blank.
- **`[GAP: x]`**: the correct answer *is stated in the document*; reality may not meet it. Produces remediation work.

Never use `[CONFIRM]` where the answer is a known standard and only the local implementation is in question: it files a
gap as an unknown, and it never gets fixed. Search for placeholders with a pattern that catches every form used
(`\[[A-Z]` misses `[30/40]` and `[SPECIFY: ...]`): widen, then filter.

## Separate what is required from what was chosen

Say which each provision is: a mandate can't be changed, a choice can, and people rely on knowing which. Never describe
a decision as a requirement, or a requirement as a preference.

## Write to the requirement, not around it

When prose must satisfy a spec, control or acceptance criterion, every sentence states what meets *that* item. Cut
rationale borrowed from other frameworks, hedging and posture philosophy, lead-ins that restate the requirement, and
anything hypothetical, future-tense or outside the actual system. **State what is in place, affirmatively;** for an
exclusion, lead with its concrete basis, not the absence.

## Precision is the differentiator, not a constraint

For a claim with a real-world referent (a certification, attestation, regulatory status) the exact wording is the
product: "our enclave was in scope for a client's assessment" is not "we are certified", and the audience that cares
will check. Shortening a precise claim into a familiar one is the commonest way a true statement becomes false. **Never
name a capability, platform or framework you don't deliver:** it creates demand you can't serve, and losing on a
technical call is worse than never being considered.

## Verify, then keep verifying

- **Check claims against primary sources:** record the source, its date and what you checked; note sources gone dead.
- **Sweep the whole surface for the retired thing,** including what is actually published, not just the repo: a false
  claim fixed on the one page a reviewer opened survives elsewhere, the commonest recurrence. Keep a list of retired
  claims and names.
- **Quote a count only from the final run:** a number from an intermediate run reads as current and nobody re-checks it.
- **When the platform removes your enforcement point, rebuild it:** if a build step failed on a retired claim and the
  new platform has no build, crawl what is live.
