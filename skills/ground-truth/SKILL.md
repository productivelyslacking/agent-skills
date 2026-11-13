---
name: ground-truth
description: The general working discipline: claims traceable to something real, one source of truth, checks that can fail, knowledge that survives the session. Use on any authoring, editing or engineering work.
---

# Ground truth

The general discipline: every rule here holds on any project. Domain depth lives in the other skills; the index is
the library's `AGENTS.md`, loaded through `~/.claude/CLAUDE.md`. The incidents, numbers and sources behind these rules
are in this folder's `NOTES.md`, read on demand.

The failure these prevent has one shape: something *sounds* right, passes review because it sounds right, and is wrong.

**Calibrate to blast radius.** Raise the bar with who is affected and how hard the mistake is to undo. Customer
data, a published claim or a signed policy earns the full weight; a personal project earns rules 1 and 2. The rules
below are written for the high end; below it, use the lightest version that still catches the mistake you fear,
since heavy machinery on low-stakes work is its own failure.

**Progress is the goal moving, not the gates getting stricter.** Don't build hardening, tooling, checkers or docs
that no current goal needs: each looks reasonable alone, and together they form a queue that refills while the
deliverable stands still (**agent-team**, "Work the critical path").

---

## 1. Write it down, in the same session, in a named home

Conversation context is the least durable place a fact can live. When you learn something non-obvious, settle a
convention or make a decision that shapes future work, put it in a file before the session ends: if it would change
what a future session does, it is not recorded until it is in a file. Record it as part of the change it came from,
not as a later docs pass, and only what cost real time or would change a decision, because a file too long to read
records nothing.

- **Record declines.** When a flagged issue is left alone because the current choice is defensible, write down why;
  otherwise the next reviewer raises it again.
- **Record deliberate omissions** (a vendor left unnamed, a case left unhandled, duplication left un-abstracted), or
  the next person "fixes" the oversight.
- **Note when a reason collapses.** Record that the *reasoning* failed, not just the new answer, or the dead
  reasoning gets reapplied.
- **Put rationale where it outlives the platform.** Comments in a config file or a CMS field don't survive a
  migration.
- **Give every subagent an explicit pointer to the conventions file;** it inherits none of this.
- At session start and after any compaction, read the STATUS block and the conventions file before acting.

Format, and where each kind of fact goes: **durable-knowledge**.

## 2. Verify against the real thing, not the description of it

Docs, vendor docs, type signatures and training data describe the general case; describe the running code, the
current statute, the real payload, how the organization actually operates. When they disagree, the real thing wins,
and the disagreement becomes a rule-1 entry.

- **Measure; don't reason** about counts, widths, ratios and timings: measuring is cheaper than being wrong.
- **Treat hand-authored approximations of a formal artifact as scaffolds.** Config written from docs, a schema
  inferred from a spec or a fixture written from memory looks plausible and fails on contact; export from the real
  tool.
- **Use legacy material as a coverage checklist, not a content source.** It shows what topics existed, often for a
  system that no longer exists; never carry its substance forward unexamined.
- **No theory until one command reproduces it.** For a bug you can't explain at a glance, first build one command
  that goes red on the reported symptom. Then list 3-5 causes, ranked, each with the result that would disprove it,
  and test them one at a time. Tag temporary logging so it can be removed. If no such command can be built, say what
  you tried and ask for access or a captured artifact rather than guessing.
- **After three failed fixes for one problem, stop fixing.** The diagnosis or design is wrong; reproduce it again on
  the path that really fails, and if it still won't yield, put the design question to the user. Fixes that pass every
  gate on a path the real system doesn't use look like progress.

## 3. The plausible generic answer is the default failure mode

Generated domain content fills gaps with the statistically normal version: the standard clause, the usual
threshold, the common API shape. It is fluent, describes a different system, and is invisible on read-through
because it looks canonical.

- Establish up front which facts are *this* case: thresholds, jurisdictions, versions, names, exclusions. Mark what
  you don't know rather than letting it be filled in, then check the output for confident specifics you never
  supplied.
- **Lists of "current" models, releases or tools from memory are stale.** Start from a dated live query (a registry
  API sorted by date) and record it; memory may add names, never limit them.

## 4. Never assert what you cannot demonstrate

Every claim needs something that actually produces it: committed code, a real practice, a query you can run, a
document you can point to. A claim ahead of its artifact is worse than an acknowledged gap, because it reads as done
and nobody goes looking.

- **If you can't finish honestly, stop and say what's blocking you; that is an acceptable result** (D11). An agent
  with no sanctioned way out reports success it didn't earn: fabricated evidence, a weakened check.
- **Couple a claim to its mechanism.** Remove the claim in the same change that removes the mechanism, and record
  the coupling so the claim isn't reinstated without it.
- **The check that verifies the work is often the artifact itself.** Its output is the evidence; build one, not a
  checker plus a separate report.

Documents whose output *is* claims: **claim-integrity**.

## 5. One source of truth; copies are generated or referenced, never maintained

Pick the canonical location for each fact. Anything derived from it (a summary, an index, a README count, a
restatement, a duplicated constant) is generated by committed tooling or references the original.

- Mark generated files "generated by `<script>` - do not edit", and regenerate rather than hand-edit: one hand edit
  makes a second source and a silent drift bug.
- **Name the tie-breaker** for any two copies that can drift ("if the file and the live page disagree, the file
  wins"), so a future argument becomes a lookup.
- **Default tie-breakers.** For how the system behaves, executable config, code and tests win, and disagreeing prose
  is stale. For what it must do (a decision, requirement, signed policy), the written decision wins and a disagreeing
  test is the bug; otherwise a test overrules a decision just because it runs.
- **Record a forked variant's relationship:** which line is canonical, what may diverge, whether fixes flow back.
  Without it, a bug fixed in one silently survives in the other.

## 6. Check with something that can fail - and know how checks lie

Run a deterministic check before declaring done: expected sections present, counts matching across representations,
cross-references resolving, no placeholders, no encoding damage or truncation, formal files parsed with a real parser
rather than a regex or string split. Then account for how checks lie:

- **Silent success is the dangerous mode.** Tools that render nothing for unknown input, skip a rule they can't
  evaluate or exit zero on an empty result pass while producing nothing; assert on output, not exit status.
- **Verify at the level the user experiences:** "it compiled" is not "it works".
- **Check for the absence of the retired thing, not just the presence of the right one.** A fix applied to the copy
  someone opened, while the old version survives elsewhere, is the most repeated failure there is.
- **Your search pattern has blind spots** (a placeholder grep for `\[[A-Z]` misses `[30/40]`; line counts lie about
  single-line files), and **a green gate is evidence only about what it checks.**
- **A check or test counts only once you've seen it fail for the reason it tests.** One that has never failed may
  assert nothing; one nobody sees fail decays into one that always passes. Write it, watch it fail as expected, then
  make it pass; prefer a test that catches the bug you fear over one that raises coverage.
- **A control must prove its own premise.** Say what its failure output must contain and read it, not the exit code:
  a crashed checker looks like a control working. A control that removes a guard confirms the guard really went. A
  probe for absence prints a failure marker when it breaks and also counts while the thing exists, since a crashed
  count looks like "nothing left". A similarity score needs an input that must score low.
- **A flaky gate is worse than no gate:** it teaches everyone to re-run until green. Quarantine a nondeterministic
  test with the date, have CI fail once any quarantine is older than about 30 days so it can't quietly become
  deletion, then fix it or delete it on purpose.
- **When the platform takes away your enforcement point, rebuild it elsewhere.**
- **A tool that can't produce a correct artifact refuses rather than emitting a plausible one** (packaging from
  committed state refuses on a dirty tree).
- **A checker must never force a worse edit than it prevents.**

**Mutation: break the rule and watch the test fail.** Remove or invert the line a test guards and run it, by hand,
once, on gates where a false pass costs saves, data, security or a landing; a standing mutation harness is more code
to test, and the start of a regress.

- **A fixture can satisfy the property by chance.** When a mutant survives, find the input that makes the difference
  visible.
- **Count mutants by the run's exit code, not by grepping for FAIL:** a crash prints a traceback and looks like a
  survivor. Cap the run's time; a mutant can hang it.

## 7. Name the distinct cases; do not let one absorb the other

When two things look alike but are governed differently (two auth systems, classifications or jurisdictions, two
sources both reporting "revenue"), say so and handle each. One rule covering both is wrong and survives review
*because* it reads clean: if rule A doesn't govern case B, saying it does is a false claim dressed as a
simplification.

## 8. Secrets and irreversible actions

- **Secrets never in the repo,** an example, a log or a screenshot. Record what exists and why, never how to
  authenticate to it.
- **Don't let sensitive material in your input reach your output;** archives and legacy exports routinely carry
  credentials and identifying data.
- **The tool that detects a secret must not contain it,** nor its tests, fixtures or allowlists: hardcoded values are
  a copy hiding in the file nobody audits. Derive patterns from where the values legitimately live, or match on shape,
  which also catches the *next* one.
- **Removing a secret from the tree doesn't remove it from history.** After a rewrite, re-scan **every reachable
  commit** and the tooling, not the current tree.
- **Confirm destructive or outward-facing actions** (publishing, dropping data, installing software) first.
- **Never route around a permission denial;** explain what you needed and why.

## 9. Operational

- **Parallel edits: one agent per file.** Agents sharing a file clobber each other silently; edit the many in
  parallel, then derive the shared one deterministically. Stagger large fan-outs; re-run only failed units.
- **Make anything that runs more than once safe to re-run:** guard creates, make migrations idempotent, never assume
  a clean start.
- **Stamp deployed artifacts with version and commit, readable from outside,** or a stale deployment presents as
  bugs you already fixed.

## 10. Design for a human with little time and attention

"we need to design for humans with limited time and thought capacity" (owner, 2026-10-08). Steps a person has to
remember get missed.

- **One command per job.** It does every step, checks each, and stops with a plain message saying what's wrong and
  what to do (**ops-scripting**, "One command per job"). Leave the person only what needs their login or judgement,
  and print exactly what to type or paste.
- **The answer first.** A runbook, page or report opens with "just do this" or the verdict, detail below; a decision
  put to the person comes with a recommendation.
- **When a plan needs the person's answers, ask only those,** each with your recommended answer; look up facts
  yourself, and act once nothing is silently assumed and they have confirmed.
- **Predictable places:** docs, decisions, runbooks and tools where the project already keeps them, or in the default
  layout (**durable-knowledge**, "Repo layout").
- **Fewer choices:** defaults right for most cases; options only where a person genuinely decides.

## 11. Build so someone else could take it over tomorrow

"we should always build like we might win the lottery tomorrow and someone else would have to pick it up" (owner,
2026-10-21). Expecting to keep running a project is no reason to let it depend on its owner or a session's memory.

- **Leave the project handover-ready with every change**, not in a clean-up before release: README's "Run it" works
  from a clean machine, STATUS says where things stand, DECISIONS says why, open work is in the tracker
  (**durable-knowledge**, "Repo layout").
- **Nothing lives only in a head or a chat:** what the next person needs goes in the repo the same session (rule 1);
  memory and scratch notes are for the agent.
- **Plain over clever:** well-known tools, few dependencies, one command per job (rule 10), tests that say what they
  protect.
- **Check it the way a newcomer would.** At milestones, someone with only the repo follows the docs from a clean
  machine, and what they trip on is a bug. They first write, in their own words, what the project does and how,
  per the docs; compare it with the truth. A wrong paraphrase is a bug too: it catches docs whose terms are all
  defined but whose parts don't connect. An agent doing this starts fresh, with the docs and no summary from you.

---

Recording what you learn, and adding to this library: **durable-knowledge**.
