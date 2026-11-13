# Decisions

What was decided about this library and why: D1, D2, ... Each: context, options, decision, when to revisit.

## Index

- D1 - One repo layout for every repo, the standard's text in durable-knowledge (2026-10-08)
- D2 - `AGENTS.md` is the rule sheet; `CLAUDE.md` is the import line and keeps its path (2026-10-08)
- D3 - `CANDIDATES.md` moves to `docs/` (2026-10-08)
- D4 - The machine-readable layout is JSON, not YAML (2026-10-08)
- D5 - layout-check built; Forgejo's template feature adopted (2026-10-08)
- D6 - Rules state the requirement and a source tag; quotes and the requirement inventory live in `docs/REQUIREMENTS.tsv` (2026-10-08)
- D7 - Studio operations never reduces quality (2026-10-05)
- D8 - Code does what logic can (2026-10-06)
- D9 - Merge approval delegated to the merge-reviewer (2026-10-05)
- D10 - Look for an established open-source tool before building one (2026-10-07)
- D11 - If you can't finish honestly, stop and report; that is an acceptable result (2026-10-08)
- D12 - Per-file decisions and status entries are the layout's second allowed form (2026-10-21)
- D13 - Keep the studio on the goal: critical path, minor findings don't block, CI as evidence (2026-11-03)
- D14 - Each session pulls the library and repairs its links (2026-11-05)
- D15 - Four review rules taken from Google's Elephant-Goldfish Model; its pipeline left out (2026-11-06)
- D16 - Pin merges to the tested head; rebase before the first push, merge after (2026-11-06)
- D17 - Vet third-party skills as dependencies; three failed fixes stop the fixing; first baseline test (2026-11-06)
- D18 - Adopt the rest of the outside research; the diagnosis rule changes process, not outcome, on an easy bug (2026-11-07)
- D19 - "Do one thing well" becomes two boundary tests, not a rule (2026-11-07)
- D20 - Merging rules move from agent-team into a landing skill (2026-11-07)
- D21 - First candidate review: promote what recurred, move domain facts to NOTES.md (2026-11-07)
- D22 - Two teaching skills from a literature review, ahead of real use (2026-11-06)
- D23 - Two story skills from research, ahead of real use (2026-11-06)
- D24 - Two art skills from research, ahead of real use (2026-11-06)
- D25 - Production-stages and directing skills and a director role, from research, ahead of real use (2026-11-06)
- D26 - A psychologist reviewer role and skill from research, ahead of real use (2026-11-06)

## D1 - One repo layout for every repo, the standard's text in durable-knowledge (2026-10-08)

**Context.** Repos put status, decisions, runbooks and scripts in different places under different names
(survey: `studio-scratch/2026-10-08/repo-layout/details.md`). The owner approved the proposal "as recommended":
one `DECISIONS.md` per repo, `AGENTS.md` as the one source with `CLAUDE.md` containing just `@AGENTS.md`, the
code folder whatever the language expects, scratch and logs never in repos.
**Decision.** The standard's text is durable-knowledge, "Repo layout" (rule 10 points there);
`tools/repo-layout.json` is the copy `tools/layout-check` reads; `tools/check.py` keeps the two in step.
**Revisit** if a repo kind keeps needing the same `.layout-check` exception: that exception belongs in the
standard.

## D2 - `AGENTS.md` is the rule sheet; `CLAUDE.md` is the import line and keeps its path (2026-10-08)

**Context.** The library's `CLAUDE.md` was the product: every machine's `~/.claude/CLAUDE.md` imports it by
absolute path. The survey suggested keeping it as a named exception to the layout.
**Options.** (a) Keep `CLAUDE.md` as the rule sheet and allow it in `.layout-check`. (b) Move the rule sheet to
`AGENTS.md` and make `CLAUDE.md` the line `@AGENTS.md`, so every machine's existing import line keeps working
and reaches the rules one hop further.
**Decision.** (b): the library follows its own standard with no exception, and no machine's `~/.claude/CLAUDE.md`
changes. Tested on a scratch checkout with `claude -p --setting-sources project` (2026-10-08; evidence in
`studio-scratch/2026-10-08/layout-apply/details.md`): a scratch `CLAUDE.md` copied from this machine's
`~/.claude/CLAUDE.md`, importing the checkout's `CLAUDE.md`, gave a fresh session rule 10's title and the
dependency-policy row; with the `@AGENTS.md` line broken, or `AGENTS.md` absent, it could not. Not run before
merging: the same chain from the real user-scope `~/.claude/CLAUDE.md` (it imports the main checkout); the
runbook's first check runs it after the merge.
**Cost.** A machine that *copied* `CLAUDE.md` instead of importing it would now get only the import line; README
says to copy `AGENTS.md`. Tools that read the file as plain text (opencode, Qwen Code: work/local-agents) must
point at `AGENTS.md`.
**Revisit** if Claude Code stops following relative imports inside an imported file.

## D3 - `CANDIDATES.md` moves to `docs/` (2026-10-08)

**Context.** The layout allows eight visible root entries plus what README's table names; `CANDIDATES.md` sat at
the root. It is the library's inbox of lessons seen once in some project, waiting to recur.
**Options.** (a) Keep it at the root, listed in README's table. (b) Rename it `docs/LESSONS.md`. (c) Move it to
`docs/CANDIDATES.md`, a project-specific CAPITALS doc, beside an empty `docs/LESSONS.md`.
**Decision.** (c). It is a doc, so it goes in `docs/`; and it is not the library's lessons log: `LESSONS.md` holds
traps about *this repo* (its checks, its import chain), while candidates are other projects' lessons on their way
into skills. One file for both would mix two differently-governed things (rule 7). Every reference (`AGENTS.md`,
durable-knowledge, `tools/check.py`) changed in the same commit.
**Revisit** if `LESSONS.md` stays empty for months: then the library has no traps of its own and (b) costs nothing.

## D4 - The machine-readable layout is JSON, not YAML (2026-10-08)

**Context.** The brief suggested `tools/repo-layout.yaml`. layout-check is standard-library Python, which has a
JSON parser and no YAML parser.
**Decision.** `tools/repo-layout.json`: no dependency (dependency-policy, "Actually needed"), and the file is read
by a tool more than by people; the people read durable-knowledge.
**Revisit** if a second tool needs the spec and already depends on a YAML library.

## D5 - layout-check built; Forgejo's template feature adopted (2026-10-08)

**Context.** dependency-policy, "Before building a tool". Candidates and licences:
`studio-scratch/2026-10-08/repo-layout/details.md`, section 2.
**Decision.** Template: adopt Forgejo's template repositories (already running; Copier, MIT, does updates too but
adds a Python tool to every new-repo step). Checker: build, standard library only: repolinter (Apache-2.0) is
archived; ls-lint (MIT) checks names only, not that files exist or what `CLAUDE.md` contains.
**Revisit** Copier if template changes need pushing into existing repos; ls-lint if the naming rules grow.

## D6 - Rules state the requirement and a source tag; quotes and the requirement inventory live in `docs/REQUIREMENTS.tsv` (2026-10-08)

**Context.** The owner asked to condense the agent instructions "while still keeping all of the requirements
intact", then (2026-10-08): "are the quotes necessary or are thwy adding bulk?" `AGENTS.md` loads in every session
and each role file in every run of that role, so a quote there is paid for on every call.
**Decision.** A rule line in `AGENTS.md` or `agents/*.md` states the requirement and a short source tag, such as
"(owner, 2026-10-07)" or "(D2)". `docs/REQUIREMENTS.tsv` holds one row per requirement in those files (rule, where it
was, the phrases that must stay in its file) and, for a tagged rule, the full quote, its date and where it came
from; a quote that records a decision is also verbatim in its entry here. `tools/check_requirements.py` (run by
`tools/check.sh`) fails on a missing phrase, a tag with no quote, a quote no rule cites, a quote still inline, or
a decision entry without its quote. A reworded rule updates its row in the same commit; a dropped rule deletes its
row, visibly. Tie-breaker for a quote: the file named in its `quote_source`.
**Cost.** Editing a role now means editing its rows too, and a new rule added without a row goes unchecked (the
inventory covers what existed on 2026-10-08). Evidence: `studio-scratch/2026-10-08/condense/details.md`.
**Revisit** if row upkeep becomes the larger cost, or the phrase match turns out to block harmless rewording often.

## D7 - Studio operations never reduces quality (2026-10-05)

**Context.** The team-ops role measures and cuts the studio's cost. The owner, 2026-10-05, verbatim: "just make
sure the ops agent knows we never reduce quality".
**Decision.** Its first rule (`agents/team-ops.md`; agent-team, "Running the factory lean"): savings in tokens,
time, waits and rework, never in the quality of the game, assets, code, tests or reviews; a proposal that can't
show quality holds is dropped.
**Revisit** only if the owner says so.

## D8 - Code does what logic can (2026-10-06)

**Context.** The owner, 2026-10-06: "look for any items that can be done in code (like the router) to save tokens
any time something logic can handle it instead".
**Decision.** Every team-ops run ranks repeated work a script could do (`tools/team_repeats.py`) and briefs the
uncovered items; a script replaces reasoning only where its result is as trustworthy and it can fail
(`agents/team-ops.md`; agent-team, "Code does what logic can").
**Revisit** only if the owner says so.

## D9 - Merge approval delegated to the merge-reviewer (2026-10-05)

**Context.** The owner, 2026-10-05, asked for "a merge reviewer that can approve merges for me too for now"
(recorded in the producer's auto-memory, `merge-delegation.md`).
**Decision.** The producer merges only on the merge-reviewer's APPROVE or APPROVE-IF (`agents/merge-reviewer.md`);
look and feel, save formats, history rewrites, anything published and exports are held for the owner. Until the
user revokes it. The producer's memory (`merge-delegation.md`, "How to apply") records what stays the owner's: "Still the owner's, always: look and feel calls (concept picks, style), save-format changes, destructive or history-rewriting steps, anything public, and exports."
**Revisit** when the owner revokes or narrows it.

## D10 - Look for an established open-source tool before building one (2026-10-07)

**Context.** The owner, 2026-10-07: "In the future, i want to make sure we research whether a well known open source
tool exists that fits our need instea dof building our own tool as a reflex every time."
**Decision.** dependency-policy, "Before building a tool" holds the method; the developer records adopt, wrap or
build before building, and the tech lead's designs start from that call and its reviews flag a tool without one.
**Revisit** only if the owner says so.

## D11 - If you can't finish honestly, stop and report; that is an acceptable result (2026-10-08)

**Context.** The owner, 2026-10-08, verbatim: "yes, add the stop and report rule". The rule as proposed: "If you can't
finish honestly, stop and say what's blocking you; that is an acceptable result." Evidence: ImpossibleBench (Zhong,
Raghunathan, Carlini, arXiv 2510.20270): giving the agent an explicit abort option cut GPT-5's cheating from 54% to 9%
(a strict "STOP and report" prompt cut it from 92% to 1% on Conflicting-LiveCodeBench; METR found a plain "don't
cheat" weak); `studio-scratch/2026-10-07/agent-honesty/details.md`. Local runs: in the 2026-10-07 opencode rerun both
final reports claimed full success with fabricated evidence (`studio-scratch/2026-10-07/opencode-rerun/details.md`).
**Decision.** Working rule 4 in `AGENTS.md` and `skills/ground-truth/SKILL.md` carries the sentence, so it is in
the core sheet for local agents too. Untested on gpt-oss; the numbers are from other models.
**Revisit** if a measured run shows agents stopping on work they could have finished.

## D12 - Per-file decisions and status entries are the layout's second allowed form (2026-10-21)

**Context.** a web app keeps one file per decision (`docs/decisions/Dnnn.md`, its D85) and one status entry per branch
(`docs/status.d/<slug>.md`, folded into STATUS.md at landing), because parallel branches that each appended to
DECISIONS.md and STATUS.md conflicted at most landings. Until now it passed layout-check through `allow` lines,
which admit the folders without checking anything in them. The 2026-10-21 a web app audit
(`studio-scratch/2026-10-21/a web app-audit/audit.md`, decision D-1) asked: keep that, or converge on one DECISIONS.md
with a merge resolver as a Linux service project did?
**Options.** (a) Converge: rewrite 114 decision files into one, for no gain in safety. (b) Keep a web app's as an
`allow` exception: unchecked, and every repo that wants it reinvents it. (c) Make it a named second form of the
standard, selected per repo, and checked.
**Decision.** (c), approved by the owner on 2026-10-21. durable-knowledge, "Repo layout", "Per-file decisions and
status" is the text; `tools/repo-layout.json` "forms" is its copy, with the two `.layout-check` lines
(`form decision-files: ...`, `form status-entries: ...`); `tools/check.py` fails if the prose doesn't give each
line; `tools/layout-check` admits a form's folder only with its line, and checks file names, the folder, the
status README, DECISIONS.md's link and task lists in entries (tests/test_layout_check.py, class Forms). The single
DECISIONS.md stays the default. This is D1's revisit condition met: a repo kept needing the same exception.
**Revisit** if a third repo needs another variant, or if a per-file repo's tooling stops printing the index.

## D13 - Keep the studio on the goal: critical path, minor findings don't block, CI as evidence (2026-11-03)

**Context.** The owner, 2026-11-03: "I feel like development work never gets anywhere because the agent workflow
tends to spin it's wheels indefinitely on the most mundane tasks and I want to optimize it to deliver actual
code/results." Measured the same day on two projects run with this discipline from a second copy of the library:
on one, merge reviews outnumbered builds 92 to 58, 86 of 210 issues were raised by reviews, follow-ups or checkers
(32 of the last 44), and the milestones leading to the deliverable closed none; on the other, every cutover issue
stayed open while tooling and review follow-ups closed. A review of another project's agent setup found the same
cycle and the same fixes (scoped documentation, a 1-2 minute PR check, a drift checker that decayed into a no-op,
quarantined flaky tests). The owner then asked to port the fixes here "where applicable".
**Decision.** Ported: agent-team "Work the critical path" (promotes the 2026-10-21 "keeps agents busy" candidate,
bounded to the path); only breaking and major issues block, beside the merge-reviewer's bar (promotes the
2026-10-16 candidate; player-facing minor bugs are still filed, as the owner asked on a web app); two review rounds;
"fix the class" kept for gate, security and data findings only; the CI run as the build-and-test evidence for QA
and the tech lead; a fast PR check; a rationalizations table; ground-truth's progress rule, default tie-breakers,
flaky gates and decayed checks; durable-knowledge's lesson homes, invariant headlines, evidence in the pull request
and read-what-the-brief-cites. Core rules for local agents gain "say what you need and stop" (all) and "only what
Acceptance asks" (developer).
**Not ported, deliberately.** The other copy's risk tiers, where light changes merge on green CI without the
merge-reviewer: here D9 has the producer merge only on the merge-reviewer's verdict, until the owner says
otherwise. The producer making small changes itself: the owner asked on 2026-10-05 that it delegate hands-on work.
Batching library updates per milestone: here the owner's standing permission is to commit and push them as they
happen.
**Revisit** after the next studio run: compare merged changes per day and issues raised by reviews against the
numbers above, and ask the owner about tiers if merge reviews still outnumber builds.

## D14 - Each session pulls the library and repairs its links (2026-11-05)

The owner, 2026-11-05: "make sure any claude session we open on this computer use the most up to date agent-skills repo".
A clone linked into `~/.claude` only moves when someone pulls, and a new skill also needs its link re-run (README).

**Decision:** a `SessionStart` hook runs `tools/sync-claude`, which pulls `main` fast-forward only, links skills and roles,
and removes links to anything deleted. It never blocks a session or touches local work: on any failure it warns and
carries on. Only `main` is followed, so a checked-out branch is left alone.

**Trust:** the hook runs whatever `main` holds in this private repo at every session start, the same trust the rule sheet
already has. Don't make this repo public or give others push access without revisiting this.

**Not done:** `additionalContext` tells a session to re-read changed rules instead of restarting it, because the order of
memory loading and hooks isn't documented in anything read here. **Revisit** if sessions start slowly on a bad network: the
pull is capped at 10 seconds.

## D15 - Four review rules taken from Google's Elephant-Goldfish Model; its pipeline left out (2026-11-06)

**Context.** The owner asked whether the library could learn from `google/elephant-goldfish-model` (Apache-2.0, read at
`dea7761`), a plugin where a full-context agent drafts a design doc and reviewers without the conversation history check
it. Told the choice was skills or candidates, the owner said: "yes, add them to the skills directly". These are outside
ideas, in our own wording. They had not been tried here, and the repo's docs that were searched give no measurement; D17 records the first test.

**Decision.** Added: the fresh reader's paraphrase (ground-truth); a settled list across review rounds, with churn
stopping them, and evidence the reviewer can read for any dispute (agent-team, merge-reviewer); a reviewer that returned
nothing counts as not run (agent-team). Unlike the source, the author can't settle its own finding by contesting it: a
reviewer withdraws it or the owner accepts the risk, because D9 makes the reviewer's verdict the gate.

**Not taken.** The five-stage review (10 reviewer runs per pass) and the loop of up to five rounds needing two clean ones:
D13 caps reviews at two rounds after measuring them outrunning builds. Its `test_scenarios.yaml` files: nothing found in
the repo runs them. Its zero-decision plan standard, tone rules and LLM drift report. Its `omitClaudeMd` reviewer setting
is untested here and would not suit the merge-reviewer, which must enforce project rules.

**Revisit** at D13's next studio run: if settled findings still come back, or a closed one hid a real defect, change or
drop these rules.

## D16 - Pin merges to the tested head; rebase before the first push, merge after (2026-11-06)

**Context.** A comparison with a second copy of this library found two landing rules this one lacked. Asked whether ideas
may cross between the copies and what to do first, the owner answered: "1. yes 2. your recommendation". Ideas only, in our
own wording, naming no employer, client or project.

**Decision.** The producer merges a pull request with `gh pr merge --match-head-commit` (agent-team), and a pushed branch
takes main by merging, never by a rewrite (agent-team, developer). D9 is unchanged: the merge-reviewer still never merges
here. This repo has no branch protection: GitHub answers that a private repo needs a paid plan or going public. So the flag
catches a moved head but not a red one, and reading the CI run stays the producer's job.

**Not taken.** The other copy's merge-reviewer merging by itself, which relies on branch protection. Its light, standard and
full tiers stay out as in D13.

**Revisit** if this repo gets branch protection, or on D13's next studio run if merge reviews still outnumber builds.

## D17 - Vet third-party skills as dependencies; three failed fixes stop the fixing; first baseline test (2026-11-06)

**Context.** A comparison with listed community skills found three gaps, and the owner said "yes, go ahead with those three":
no test of whether a rule changes behaviour, no bar for third-party skills, and no limit on repeated fixes.

**Decision.** dependency-policy now covers skills, plugins and MCP servers. Three failed fixes stop the fixing (ground-truth,
developer). The two are ideas from `obra/superpowers` and community warnings, in our own wording, and are not yet tested.

**The test.** D15's re-check rule, on one written fixture, with scoring fixed first: 5 fresh agents without the rule text, 5
with it, both given the same round 1 outcomes. Control and rule both left settled findings closed (5 of 5) and both reopened
a failed fix and a settled finding whose evidence the diff removed (5 of 5), so the rule did not over-suppress. **The one
difference was churn: put to the owner in 0 of 5 without the rule, 5 of 5 with it.** So the churn clause changes behaviour;
the settled-list wording showed no effect once outcomes are written down, which leaves recording them as the part that
matters. It does not show that a HOLD is the better outcome, and one fixture scored by its author is weak evidence.

**Not taken.** Installing REA or any listed pack. REA's own disclaimer limits it to lawful analysis of software you own or
may examine, and the owner wants nothing suggested that breaks such rules, so it is only an option for our own builds, open
source and our own network, vetted first and run in a throwaway VM. Its pitch of rebuilding features from other people's
apps is out.

**Revisit** when D13's next studio run gives real re-checks to compare, and test the two new rules if either misfires.

## D18 - Adopt the rest of the outside research; the diagnosis rule changes process, not outcome, on an easy bug (2026-11-07)

**Context.** The owner: "yes, add all recommended from you research so far and then test the baseline". Sources: `mattpocock/skills`,
`obra/superpowers`, `blader/humanizer` and a second copy of this library. Ideas in our own wording. Apart from where noted, these
come from reading, not from a failure seen here.

**Decision.** ground-truth: no theory until one command reproduces it; interview in rounds. durable-knowledge: dated claims in
STATUS, merge danger in pull requests, the observed-failure bar, not restating the environment, matching a rule's form to the
failure, and how to run a baseline. ops-scripting: walkthrough scripts for steps only a person can do. prose-editing: what marks
text as generated. developer: test first, with expected values from an independent source. agent-team and three roles now cover
other software with a smaller cast, instead of a second team skill that would half-cover the same ground. CI gets read-only
permissions, and four candidates join `docs/CANDIDATES.md`.

**Not taken.** Claiming work through branches: only needed when several tools or people share a repo at once. Kept for when the
problem appears: wayfinder, software-factory's questions, to-questionnaire, codebase-design. Skipped: git-guardrails (its own repo
records a bypass and that it fails open), the packs as installs.

**The test.** A real copy of a small repo with a planted truncation bug, a decoy TODO, and a trap (`round()` still fails customer
1043, by the spec), 5 fresh agents per arm, scoring fixed first.

| Scored | Without rule | With rule |
|---|---|---|
| Reproduced 1042 before the first edit to `billing/` | 5/5 | 5/5 |
| Report lists 3 or more candidate causes | 0/5 | 4/5 |
| Right fix, including the trap | 5/5 | 5/5 |
| Regression test fails on the old code | 5/5 | 5/5 |
| No debug output left, root cause named | 5/5 | 5/5 |
| Touched the decoy | 0/5 | 0/5 |

By the criterion written first, **this gives no evidence that the rule improves how a bug gets fixed on a bug this size.** Seen
after the fact, so weaker: with the rule all 5 saw the failure before writing the fix and tested labelled hypotheses, against 2 of 5
and 0 of 5 without it. It cost about 30% more time (mean 60 s against 46 s) and 2% more tokens. The bug could be solved by reading,
so the fixture can't show what the rule is for: the bug that resists a first look, like the one that took six landings. My scoring
script also misjudged two points (it missed reports, and scripts that test and fix in one command), so those were scored by hand
from the commands. **Kept for now,** because it answers a failure seen here and did no harm.

**Revisit** with a harder fixture, one whose cause can't be found by reading. If the rule still changes nothing, cut the hypothesis
list and keep only "reproduce first".

## D19 - "Do one thing well" becomes two boundary tests, not a rule (2026-11-07)

**Context.** The owner asked whether the Unix philosophy could join these rules or is outdated. The library already follows it
(rule 10, one thesis per skill, small branches). Taken literally it backfires: more pieces to choose between and keep in step,
shallow modules, and no agreement on what "one thing" is.

**Decision.** Asked whether to add them, the owner said "yes, add them": two tests, describe it without "and" and imagine deleting it
(durable-knowledge), and in ops-scripting, a job as what the person wants done, plus structured output for tools and agents. No new
rule on the sheet, so nothing here gives agents a reason to split for its own sake. The deletion test comes from
`mattpocock/skills`. No failure seen here prompted this, and it has no baseline test.

**Revisit** at D13's next studio run, and if `agent-team` keeps growing: it is over 340 lines, and its merging rules are the first
candidate to split.

## D20 - Merging rules move from agent-team into a landing skill (2026-11-07)

**Context.** `agent-team` had reached 381 lines and failed D19's "describe it without and" test. The owner asked to "split agent-team
as recommended". **Decision.** Its review and merging rules move, text unchanged, into **landing**, which holds on any project and
fires when reviewing or merging without the studio. They change for different reasons from the studio's roles and briefs.
**Cost:** one more description in every session. **Revisit** if agents reviewing a branch stop finding these rules.

## D21 - First candidate review: promote what recurred, move domain facts to NOTES.md (2026-11-07)

**Context.** `docs/CANDIDATES.md` held 120 entries against a review threshold of about twenty. The owner asked for the review to be done
rather than walked through together. Options for a domain fact: promote it unproven, delete a lesson that cost real time, or leave the list
unreadable. **Decision.** 52 facts true only of one skill's domain move unchanged to that skill's `NOTES.md`, read on demand. 24 entries with a recorded recurrence, a user decision or an observed cost here become rules. 3 are dropped as already covered. 41 stay.

**Judgement calls worth a second look.** Re-addressing (one network, three sightings) and "look for open pull requests" (once, here) were
promoted without a second project. Nothing was checked against those projects' own lessons files. **Revisit** if `NOTES.md` files get
long, or if nobody reads them.

## D22 - Two teaching skills from a literature review, ahead of real use (2026-11-06)

**Context.** Building a game that teaches Python, the owner asked: "I also want to make sure we are creating well researched teaching
skills in our skills repo." The usual bar for a skill is an observed failure (durable-knowledge), and this has none yet; the owner's
request is what clears it ("the owner says it definitely belongs"). **Options.** One skill; two skills; notes in the game's repo only.
**Decision.** Two skills. **teaching-design** holds for teaching anything, and **teaching-programming** holds what's specific to code;
they change for different reasons, and the second is useless on a course that isn't about programming. Each rule carries its rating
and a tag into one of two evidence files beside teaching-design, read on demand. Two research agents wrote those files on 2026-11-06,
and each citation was confirmed to exist by script, with fabricated citations as controls that the script rejected. About 300 sources;
most were read only as abstracts, and almost none studied an adult learning alone, which both skills say. **Deliberately left out:** the
citation script (its results are in the files; a kept checker would be tooling no current goal needs), a baseline test (nothing real to
test it on yet), and hard numbers from the evidence as gates. **Cost:** two more descriptions in every session and about 150 KB of evidence
in the repo. **Revisit** after the game's first playtest: cut any rule that changed nothing or that the playtest contradicts, and run the
baseline from "Test it two ways" if a rule still looks doubtful.

## D23 - Two story skills from research, ahead of real use (2026-11-06)

**Context.** The owner asked: "Let's do some well researched story rules and skills too." Relayed later by the producer: the owner may
offer each game's first chapter free and wants every chapter to make players want the next. The usual bar for a skill is an observed failure
(durable-knowledge), and this has none yet; as in D22, the owner's request is what clears it. **Options.** One skill; two skills; notes in a
game's repo only. **Decision.** Two skills. **story-design** holds for any story meant to hold an audience, and **interactive-story** for a
story where the player's actions are part of it. They change for different reasons, and the second is useless on a linear story. Two research
passes on 2026-11-06 produced the evidence files beside story-design, which both skills cite. Every rule leads with its claim and names its
kind, so craft advice isn't read as measured, and the checks a writer runs are marked as derived (story-design's are in `CHECKS.md` beside it, so the skill stays near its size limit). The measured file's 102 DOIs resolved at Crossref,
with fabricated citations as controls that the script rejected; the craft file had no such check, and its read marks are the check. **Boundary tests.** Delete either skill and its rules reappear across
every story or every game script, so both earn their place. The voice and stills section is the one part that fails "describe it without
and": none of its evidence depends on player action. It stays in interactive-story because story-design was over its size limit and game writers
load both; split it if voice work recurs. Story in a learning product stays with **teaching-design**. Plot reveals from the works cited sit in a skippable last section of the craft file, under the writer role's spoiler rule. **Limits.** Openings and first chapters have no
entry in either research file, and the skills say so instead of filling the gap. Almost nothing measures adults returning to a story. No limit on content is set here; each project's owner
decides. The exclusion of sexual content involving anyone not clearly an adult is this library's fixed limit, not a research finding, and is the one rule with no
citation. **Deliberately left out:** the citation check and editing scripts (a kept checker would be tooling no current goal needs), a baseline test
(nothing real to test on yet), and the owner's game details. **Cost:** two more descriptions in every session and about 180 KB of evidence in the
repo. An independent review on 2026-11-06 opened the sources and found no raised rating; it corrected what two rules said their studies measured, and the evidence files' headers list the entries it changed. **Revisit** after a story game's first playtest: cut any rule that changed nothing or that the playtest contradicts, and research openings directly if first chapters
become a real decision.
## D24 - Two art skills from research, ahead of real use (2026-11-06)

**Context.** The owner, of the studio's art agents: "They will likely need rules skills for crafting the prompts and judging output and etc."
The usual bar for a skill is an observed failure (durable-knowledge), and this has none yet; as with D22, the owner's request clears it. Agents
had a role sheet with general prompt advice and game-assets for licences, and nothing that named models, gave a check's error rate, or kept taste
with the owner. **Options.** Extend game-assets; one art skill; two; notes in a game's repo only. **Decision.** Two skills. **art-direction**
holds for any image, whatever made it; **generated-art** holds for images from a model. They change for different reasons: model facts decay in
months, and craft doesn't. Boundary tests: each can be described without "and" (judging what an image must do, against terms set before it was made; using a model's
output safely). Deleting either brings its rules back into every brief and every prompt run. Licences, the manifest and credits stay in game-assets. **What the evidence moved.** Model recipes, check cards, LoRA settings
and the To-test list went to `generated-art/NOTES.md` so that SKILL.md stays general. The adult-appearance exclusion is stated in art-direction,
because it holds however an image was made, and enforced in generated-art, because that's where the failed checks are. Flash limits stay in
art-direction, not gamedev-team-practices, because they belong in the brief. **Binding, not findings:** a person who looks young, paired with any
sexual or suggestive content, is excluded outright; no automatic check gates adult appearance or sexualised drift, whatever the numbers show, so a human or independent look covers every image that could break the rule, a model's look can only send an image to discard or to a person, and doubtful images are discarded; the agent that prompted an
image doesn't score it; the owner judges look and feel; no living artist is named as a style to imitate. **The owner's rules, with their source.** On production order (owner, 2026-11-06): "We should also only do the final post production like movement, touchup, finalization and everything when we are happy with the story... We don't want to invest too early in something particular when it could change after testing/focus group feedback." "Use the cheapest images that answer the question" is the producer's statement of that rule; a production skill is planned. "The owner judges look and feel" is the producer's brief, not a quote from the owner. **Ratings.** Two research agents wrote
the evidence on 2026-11-06, giving kind and access but no strength grades, so the skills say only "one study", "several" or "disputed", and nothing
is rated strong. **Deliberately left out:** the citation check (throwaway; its result went with the hand-back), a baseline test and T1 to T20 (the
GPU was in use, and there is nothing real to test on yet), and the project's name, story and look: entries on periods and genres stay as evidence about them, not as a target. `agents/presentation.md` now
gives the token budget by pipeline rather than "keep the prompt short", which held only for CLIP-era models. An independent review on 2026-11-06 (4 blocks, 30 should-fix, 22 minor) changed "verified" to "read", settled WCAG's area at the normative 21,824 px, and made the owner-note rule do what the owner asks.
**Cost:** two more descriptions in every session, about 150 KB of evidence and a 25 KB notes file. **Revisit** after the next run on real models:
re-date or correct NOTES.md, record each T result, and cut any rule that changed nothing or that the run contradicts. When the planned production
skill lands, move the production-order lines there. Other automatic checks become gates only on our own measured error rates, never on a card's. Adult appearance and sexualised drift are never gated by an automatic check.

## D25 - Production-stages and directing skills and a director role, from research, ahead of real use (2026-11-06)

**Context.** The owner, on a story-led game: "We should also only do the final post production like movement, touchup, finalization and
everything when we are happy with the story. We should probably have our producer agents have skills and rules forged in heavy game and
movie production research. We don't want to invest too early in something particular when it could change after testing/focus group
feedback." Then: "There should be a director agent too though (heavily researched for rules/skills)." And: "I want be
entertained/surprised/motivated when I do my first play through." As with D22, the owner's request is what clears the skill bar of an
observed failure. Three research passes on 2026-11-06 (games, 48 claims; film and animation, 52; directing, 70) also found agent-team's
final-quality vertical slice and milestone-only human playtest unsupported as defaults.

**Options.** Rules added to agent-team alone; one new skill; a producer deciding story with no director; two skills and a role.

**Decision.** Two skills and a role. **production-stages** says when to commit to what. **directing** says how creative calls get made and
what a director can't judge. `agents/director.md` holds the authority: its veto, and what comes to the owner in a form with no plot.
Boundary tests: production-stages survives "without and" (when to commit); directing doesn't quite, but its parts change together, since all
follow from one holder deciding on another's behalf; deleting either makes its rules reappear across agent-team's roles and briefs. Keeping
both apart also lets a project use stages without a director, which the critical-path rule requires. **Moved on the evidence:** the
decides, delegates and escalates list went to the role, not the skill, so there's one copy; spoilers went to directing, because they follow
from who may read what; tester budget stays in production-stages and single-use reactions in directing, with a pointer. agent-team changes:
the slice stops being the default, human tests attach to commitments, the owner keeps feel and look. Each rule carries its kind and a tag into
`EVIDENCE-PRODUCTION.md` or `EVIDENCE-DIRECTING.md`, with disagreements and unanswered questions kept.

**What it can't claim.** Most sources were reached second-hand: no director's book was opened, and Pixar's numbers are press and an editor's
interview. Nothing compares production orders. Executives say tests diagnose better than they forecast; one researcher disagrees; nothing
measures it. Whether a strong vision predicts quality isn't known. Frequent mid-production change to core design (-0.44; the category's 0.57
is a different question, 'final game resembled the initial vision'; 273 usable responses) is volunteer self-report, and the software
late-change study (171 projects) points the other way, so both are kept. **Biggest open risk:** no evidence shows AI cold readers predict human surprise, and a
director can't judge its own.

**Deliberately left out.** The citation script (run once, with planted bad numbers it caught; a kept checker is tooling no current goal needs);
the seal's check script (proved in scratch on four plants, specified in directing; a project writes its own, for its own forge. Its issue and PR
channels ran only against a stubbed `gh`, and a real forge is untried. A stub whose list calls failed first gave a false exit 0; fixed, so a failed
query reads "not checked", and the skill says so); a baseline test
(nothing real to test on yet); pass numbers for story tests (no source gives any). An independent review on 2026-11-06 (7 blocks, 24 should-fix,
11 minor) corrected the 0.57, added the gate for final production, wired the seal into the roles and the project's CLAUDE.md, moved all story
content into the sealed folder, and ended the seal where the owner has played. The seal is still unproven inference, written for one human
owner. The owner reports agents' file reads don't show in their terminal (2026-11-06); prompts and hand-backs still do. That's one setup and not a test, so directing still tells a project to test its own. **Cost:** two more descriptions in every session, a tenth role, and about
225 KB of evidence read on demand. At two people the seal's standing cost is one folder, neutral IDs, a short CLAUDE.md block and a check script.
Cold reads, the per-chapter review and any human test cost a run or a person each time, and nobody has measured them.

**Revisit** after a story-led game's first owner playthrough and first human tests: compare what cold readers said with what people did,
drop AI readers for surprise if they don't track, and cut any rule that changed nothing or that the play contradicts.

## D26 - A psychologist reviewer role and skill from research, ahead of real use (2026-11-06)

**Context.** The owner asked whether a psychologist could say that a more attractive, assertive, kind or aggressive character or line
would make a surprise, misdirection or learning moment more potent, and accepted the role on the honest answer: partly (relayed by the
producer, so these aren't verbatim). The owner's limits: traits can't track gender or race; misdirection stays in authored story, and the live tutor
never tricks the player or uses persuasion tricks to keep them playing; advice about plot goes to the director, not the owner. The usual bar for a skill is an
observed failure (durable-knowledge), and this has none yet; as in D22, the owner's request is what clears it. **Options.** Questions added to
teaching-design and story-design; a skill with no role; a role and a skill. **Decision.** A `psychologist` role and a **psychology-review** skill.
The review cuts across teaching and story, and is a separate read of someone else's work, so neither skill can hold it. It advises the director
on story and the designer on lessons, and argues for learning where the two pull apart; it doesn't decide. The director role is D25's. It never says a change "will" work: a
small search found no study that varies a character's trait and measures a story moment's force, so a finding is a sourced guess plus a proposed test.
**Boundary tests.** Described without "and": it reviews likely effect on a reader or learner. Deleted, its limits and its evidence on misdirection and
perception reappear in every story note. **Evidence.** `EVIDENCE.md` holds 44 claims from one research pass on 2026-11-06, citing the teaching and
story evidence by number rather than copying it. Mostly abstract-level, with two papers read in full, and its 222 DOIs resolved at Crossref by script. The fixed limits have no research behind them. teaching-design
gained two short rules and a clause: its gap on self-efficacy has evidence on direction, and the self-determination theory results it would add are already
[L-C21] or correlational, so no rule on the theory was written. **Incomplete areas, written as unknown:** narrative betrayal, attachment after a twist,
race in fiction, adult-beginner tone and AI tutor warmth, dark patterns in learning apps. **Deliberately left out:** 9 of the research's 31 draft questions, as uncheckable, tied to no decision or over the
skill's size limit (one more moved to teaching-design), the citation check script, a baseline test (nothing real to test on yet), and project details. **Review.** An independent review on 2026-11-06 opened 12 sources; of seven it read in full, four changed a rule. It corrected a misreported study behind the misdirection rule, a rule on attractiveness its own citations contradicted, a bias note that read as permission, and a hand-back that would have leaked plot; it cut a need-satisfaction rule from both skills as earning no current place. Its corrections are listed in `EVIDENCE.md`'s header. **Cost:** one more description
in every session, one more role, and about 100 KB of evidence in the repo. **Revisit** after its first real review of a story game that teaches programming: cut any
rule that changed nothing, and re-research the incomplete areas if a real decision turns on one. Revisit sooner if a fixed limit blocks a note the owner wanted.

## D27 - A general, publishable library: agent-skills (2026-11-13)

**Context.** The owner wants the library public and useful to anyone. A scan found the personal email on 158 of 216
commits, two commits with a private IP, about 130 private project names, dated quotes of the owner, machine notes in
`AGENTS.md`, no licence, and six candidates from a project done for the owner's employer. **Decision.** The owner's
calls: name `agent-skills` (the skills already meet the open Agent Skills format); MIT; employer-project material
removed, not renamed; `docs/` kept with details removed. The tree is cleaned on a branch and pushed to a new private
repo with fresh history, so the old history never goes public. Project names became descriptions ("an action RPG",
"a web app"), quotes are tagged "owner", and the employer rule, push permission and machine notes moved to the
owner's `~/.claude/CLAUDE.md`. The team was generalized: game-studio became **agent-team** and studio-ops
**team-ops**; the core cast fits any software project, games and story work add six roles. No roles merged: qa,
tech-lead, merge-reviewer and psychologist stay apart so their verdicts stay independent (D9, D26). The hand-back lines
repeated in each role stay repeated: each role loads only its own file, so moving them to a shared file would cost
every role a skill load. `tools/check_private.py` fails on emails, private IPs, home paths and the patterns in a
git-ignored `.private-terms`. **Revisit** if another tool than Claude Code is tested against the skills.


## D28 - Budgets for the text every session loads (2026-11-13)

**Context.** The owner wants instruction text cheap for users without losing quality. Every session loaded about
6,600 tokens (estimated at 3.6 characters per token): `AGENTS.md` about 2,000 (half a skill table repeating the
descriptions), 24 skill descriptions about 3,700, role descriptions about 900. **Decision.** Skill descriptions under
300 characters, role descriptions under 420, `AGENTS.md` under 5,500, enforced by `tools/check.py`; the index in
`AGENTS.md` keeps a few words per skill, since each description already says when to load it. prose-editing gains
"Instructions a model loads": the rule alone where it loads every session, a clause of reason where it loads on use,
incidents and numbers in `NOTES.md` or evidence files. **Evidence.** A fresh agent given only the descriptions picked
the right skill for 48 of 48 tasks before the cut and 48 of 48 after; the descriptions went from 13,793 to 6,208
characters. The tasks were written by the editor, so the test catches lost triggers, not subtle ones. **Revisit** if a
skill stops being picked in real use.

## D29 - Self-improvement with limits: privacy at entry, caps on growth (2026-11-13)

**Context.** The library improves by feeding lessons from every project into it (durable-knowledge, "Feeding the
library"). That path is how project names, an employer's work and one owner's workflow got in (D27), and it had no
limit: `docs/CANDIDATES.md` reached 61 entries against a "review past about twenty" note nobody enforced, and three
skill bodies passed 18,000 characters. **Decision.** Entries name the kind of project, never the project; no people,
hosts, paths, accounts, customer data, employer or client work, or personal workflow; `tools/check_private.py` plus
each owner's git-ignored `.private-terms` enforce the common cases. `tools/check.py` fails past 30 candidates, on a
candidate older than 90 days, and on skill bodies over 18,000 characters or role bodies over 7,000. A promotion
replaces or merges before it adds; incidents move to the skill's `NOTES.md`, read on demand. Roles learn the same way
(agent-team), and team-ops's library changes carry no session data. **First review, 2026-11-13:** 3 candidates already
in skills deleted; 4 recurrences promoted (one writer per copy, jobs that outlive their session: ops-scripting;
model licence below the headline: dependency-policy; a passing check covers only what it checks: ground-truth notes);
single-domain facts moved to generated-art, directing, ops-scripting and agent-team notes. The owner, 2026-11-13:
"Bloat and fluff is the enemy... make sure we don't accumulate more over time"; rule 10 in `AGENTS.md` says so. **Revisit** if the caps
force out a lesson that later recurs.

## D30 - Model tier by task, gates on the strongest (2026-11-13)

**Context.** The owner asked whether roles should run on different models, the strongest for thinking and a simple
one for simple work. Tools allow it per agent (Claude Code's `model:`; Codex, Gemini CLI, OpenCode and Cursor have
their own settings), and mechanical work runs well on cheaper models. **Decision.** agent-team picks a tier per task:
strongest for judgment and every gate, fast for mechanical work, balanced otherwise, with effort split the same way.
Gates never move down a tier, since a weaker gate misses defects without a sign. Other work moves down only after one
task has run on both tiers and been compared. Roles keep `model: inherit`: no comparison exists yet, and a fixed
default would decide for every task in a role. Tiers, not model names, because names change and the library serves
several tools. **Revisit** once a comparison shows a role's work holds on a lower tier.

## D31 - An outside review: principles over one owner's profile, one admission test (2026-11-13)

**Context.** An outside review of `a671b2d` (no edits, check passing) found: personal conventions stated as universal;
several promotion thresholds, with role lessons added the same day; no follow-up after promotion; a candidate parser
that let headings escape it (28 entries read as 22, one undated, so never expiring); a privacy check claiming more
than it checks; size limits that could relocate bloat. **Decision.** All six taken, two in part.
(1) Layout, scratch folder, backlog and the interview rule are a default profile under stated principles; a
project's own conventions win. (2) One admission test for rules, skills and roles (failure, scope, independent
evidence, overlap, a limit); the owner's say-so admits an experiment, not proof. Taken in part: the owner may still
admit an experiment, since it is their library, but it is marked as one. (3) A substantial or doubtful addition
records in its `NOTES.md` what should improve, what might regress and what triggers a revisit. (4) Each candidate is
parsed alone with a real date and a Target; tests fail on the old parser. (5) The privacy check reports "no
configured pattern matches", says whether local terms loaded, and exempts no file. (6) Taken in part: `AGENTS.md`
plus ground-truth get a joint limit of 20,000 characters, and every check prints the loaded totals; `NOTES.md` gets
no limit, because it loads only when cited and a cap would push evidence out rather than cut rules. Moving text there
no longer counts as a cut. The review asked for no new governance framework; these are edits to existing rules.
**Revisit** if a fork finds the default profile still binds where its own conventions should win.

## D32 - Licence: compatibility for the use first, permissive as a tie-breaker (2026-11-13)

**Context.** A second outside review found dependency-policy's licence order (permissive, then weak copyleft, GPL,
AGPL) too rigid for a general policy: it didn't separate running a tool from incorporating code, grouped licences
with different obligations, let one owner's preference for commercial flexibility override a project's own goals, and
its admission bar listed only permissive licences, so it read as an allowlist. Sources it cited: Linux Foundation
licence best practices, the GNU GPL FAQ and licence list, the OSI FAQ. **Decision.** Taken. The bar asks for an open
source licence compatible with the intended use (running, modifying, linking, embedding, distributing, network
service), read at its exact version and exceptions; source-available terms are a project policy call. Permissive
licences break ties among technically similar candidates where broad reuse matters, which is what the owner's
2026-10-07 quote asked for ("if the intended purpose of each tool is similar"); a project's licensing goals override
it, copyleft is weighed by its actual obligations, and a weaker tool doesn't win on licence alone. **Revisit** if a
review shows agents rejecting a better copyleft tool by category again.

## D33 - Pre-publication review: installer ownership, the tested tree, delegation as a condition (2026-11-13)

**Context.** A third outside review of `d8b0b68` held publication on three defects it reproduced and two
overstatements. **Decision.** All taken. (1) `tools/sync-claude` replaced same-named links it didn't own and an existing
`~/.local/bin/layout-check`: it now creates or updates only links that are absent or already point into its clone, and
reports anything else with how to resolve it; two regression tests failed on the old script and pass now. (2)
APPROVE-IF reported `HEAD^{tree}`, the tree before the reviewer's fix, and `git diff` left out new files: the reviewer
now stages the fix and reports `git write-tree` with a staged binary patch, and the producer compares
`HEAD^{tree}` after applying and committing it (reproduced in a scratch repo: the old hash equals the unpatched tree,
the new one equals the producer's). (3) merge-reviewer asserted a past delegation; it is now a gate only where the
current project or task delegates merge approval in writing, otherwise its verdict is a recommendation. (4)
`AGENTS.md` and `DESIGN.md` restated a looser promotion rule; both now point to the admission test. (5) The README
claimed trustworthiness and buried that only Claude Code is tested; it now states intent, says so under the intro,
and gives the core loading cost with ground-truth. **Later, not blocking:** a pinned install distinct from tracking
`main`, and the team workflow as an explicitly optional profile. **Revisit** if a fork reports either as a problem.

## D34 - Latest or a release; the team workflow as core plus scale-up (2026-11-13)

**Context.** D33's two follow-ups. Tracking `main` delivers every change at the next session, which the owner wants for
their own machines, but a stranger also receives untested rules that way. agent-team read as one required process
although most of it only pays off with several parallel agents. **Decision.** (1) `tools/sync-claude --pin vX.Y.Z`
keeps a clone on a release tag until the person changes it; `--main` switches back; no option keeps tracking `main`,
the default and the owner's choice. A missing tag or local changes leave the clone where it was, with a warning
(five tests). Releases follow `docs/runbooks/cut-a-release.md`; pushed tags are never moved. (2) agent-team names its
core (the cast for any project, the brief, handoffs, roles learn, the critical path) and marks the board and parallel
running *(scale-up)*, with the GPU lock, job router, delegated merge gate and team-ops named as part of that profile;
a project's own process wins. **Revisit** if pinned users report needing a channel between releases and `main`.
