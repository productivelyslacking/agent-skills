---
name: durable-knowledge
description: Making knowledge outlive the session: lessons, decisions, memory, where a fact belongs, writing a skill, the standard repo layout. Use when recording something learned, setting up a repo's docs, creating or editing a skill, or deciding whether something is worth keeping.
---

# Durable knowledge

**ground-truth** rule 1 says write it down; this says how, where, and when it graduates. Anything that lives only in a
conversation is already lost: compaction, session end or a new window erases it. The incidents, dates and approvals
behind these rules are in `NOTES.md` beside this file, read on demand.

# Writing a memory or lessons entry

## What qualifies

Record a fact that is non-obvious, cost real time to establish (about half an hour, or a failed landing), and would
change what a future session does: a corrected mistake, a convention, an environment quirk, a decline, a deliberate
omission, a reason that collapsed.

Don't record what code, git history or a doc already holds, what is true only in this conversation, or general
practice (a skill or nowhere). If the repo states it, record the non-obvious thing that made you look.

## Where it goes

- **Project-specific facts go in the project repo, never user-level memory:** they are wrong in the next project, and a
  confidently wrong memory gets trusted.
- **Cross-project facts** (tooling, environment, preferences) go in `~/.claude/CLAUDE.md`.
- **A lesson's first home is the thing that prevents it:** the code, test, config, runbook or skill the change already
  touches, stated as the rule. `docs/LESSONS.md` keeps only traps with no better home; delete an entry once it is
  encoded elsewhere, since a fact in a test and a lessons file is a maintained copy (**ground-truth** rule 5). Never
  build a test or tool only to hold a lesson.

Each kind's home in the standard layout (below); `AGENTS.md` names any extra:

| Kind | Home |
|---|---|
| Lessons, traps, gotchas | Where they're prevented (above); otherwise `docs/LESSONS.md` |
| Behavioral / decision rules | `AGENTS.md` |
| Rationale for a choice | `docs/DECISIONS.md` |
| Declined suggestions and why | `docs/DECISIONS.md`, or the review doc it came from |
| Current state, pick-up-here | `docs/STATUS.md` |
| Open work: bugs, roadmap items, review findings not fixed | The repo's issue tracker, one issue each ("Repo layout") |

**In a repo that will see repeated sessions, set up the homes first**, even empty (below).

## Repo layout

The principle: the four things a person looks for (what it is, where it stands, why it is so, what's left) are in
predictable places (ground-truth rule 10). **A project's existing conventions win;** this section is the default
profile for a repo that has none. `tools/repo-layout.json` is its machine-readable copy for `tools/layout-check`, and
`tools/check.py` fails if they disagree. Start a new repo with `layout-check --stub` in an empty `git init`.

```
README.md        START HERE. What this is, how to run it, and a table of every top-level entry
AGENTS.md        Rules for AI agents. The only copy
CLAUDE.md        One line: @AGENTS.md   (so Claude Code loads the same file)
docs/            The four files below, runbooks/, and any project-specific CAPITALS files
  STATUS.md      Where things stand today and the next step (pick up here)
  DESIGN.md      How it works and what it is meant to be
  DECISIONS.md   What was decided and why: D1, D2, ... with an index at the top
  LESSONS.md     Traps and corrected facts
  runbooks/      What to do when something breaks, or how to do a job: one file each, verb-noun.md
src/             The code (or the folder the language or engine expects; README's table names it)
tests/           The tests
tools/           Scripts people and CI run. tools/check.sh runs every check CI runs
.forgejo/workflows/   CI (.github/workflows/ while a repo still lives on GitHub)
```

Allowed at the root without a README row: `LICENSE`, dotfiles, and files a language's tooling demands (`package.json`,
`*.csproj`, `requirements.*`, `project.godot`). Any other top-level entry (the code folder an engine expects,
`vendor/`) is fine once README's table names it.

| Question | Where |
|---|---|
| How do I run it? | `README.md`, section "Run it" (the first section after one paragraph saying what it is) |
| How does it work? | `docs/DESIGN.md` |
| What was decided, and why? | `docs/DECISIONS.md` |
| What do I do when it breaks? | `docs/runbooks/` (linked from README, section "When it breaks") |

**Naming.**

1. **Fixed files are CAPITALS** (`STATUS.md`): recognised, and they sort first.
2. **Files and folders you make many of are lowercase-with-dashes** (`docs/runbooks/restore-backup.md`).
3. **A runbook is named for the job, verb first:** `restore-backup.md`, `add-a-node.md`.
4. **Dates in names are `YYYY-MM-DD`.**
5. **Project-specific docs are extra CAPITALS files in `docs/`** (a game's `LORE.md`), each with a line in README's
   docs table. Folders in `docs/` are `runbooks/` and `evidence/` only, plus the second form's `decisions/` and
   `status.d/` where `.layout-check` selects it (below).

**Where things do not go.**

- **Scratch, logs and run output never go in a repo**, tracked or ignored (`*.log`, `scratch*`): use the scratch
  folder the session or machine provides. Build output goes in a git-ignored `build/` or `out/`.
- **Evidence goes in the pull request** (description or CI log, pinned to a commit). `docs/evidence/YYYY-MM-DD/`
  holds only what a published claim rests on: committed evidence is more to review and conflict on.
- **A pull request states its merge danger:** one-way or two-way door (can a revert undo it?) and blast radius, so the
  reviewer knows how hard to look.
- **Secrets never.** Commit a `.env.example`; `.env` is ignored, never tracked.
- **Config** stays where its tool expects it; a `config/` folder only for several files.
- **Decisions are one `docs/DECISIONS.md`** (D1, D2, ...; each with MADR's headings: context, options, decision, when
  to revisit), not a folder, so numbered references stay valid. The one exception is the second form.

**The second form: per-file decisions and status.** Where many branches land in parallel, decisions and status
paragraphs conflict in the same two files. Such a repo may keep one file per decision and one status entry per
branch, each selected by its own line in `.layout-check`:

```
form decision-files: one file per decision, docs/decisions/Dnnn.md; docs/DECISIONS.md says where they are and how to add one
form status-entries: one entry per branch, docs/status.d/<slug>.md, folded into docs/STATUS.md at landing
```

- **`decision-files`**: each decision is `docs/decisions/Dnnn.md` (D7 is `D007.md`); `docs/DECISIONS.md` holds no
  decisions, links `decisions/` and says how to add one. The repo's tooling prints the index.
- **`status-entries`**: a branch writes `docs/status.d/<slug>.md` and never edits STATUS.md; the entry is folded in at
  landing. `docs/status.d/README.md` gives the format. An entry keeps no task list.

`layout-check` admits each folder only with its form's line and checks its contents. Choose one form per repo and
keep it; the single file is the default.

**Open work lives in one list,** the project's own (default: its issue tracker): every bug, roadmap item and review
finding not fixed in the change that found it is one entry there, filed before the merge. STATUS.md says where things stand and links the current
milestone or issue, with no task list (`- [ ]`). **It dates what it claims:** each claim carries the date or commit it
was true at, never a bare "currently" or "now", because status falls behind the code. DESIGN.md says what it is meant
to be, not what is left. A TODO or FIXME cites its issue, `TODO(#12)`; `layout-check` fails both. Labels are scoped,
one of each set: `type/` bug, security, feature, docs, test, chore; `priority/` high, medium, low; `area/` the repo's
modules; `status/` in-progress, blocked, needs-decision (waiting on the user), idea (deferred). Milestones are the
roadmap's steps in order. A repo without a tracker yet says so with an `allow` line.

**Agent files: one source.** `AGENTS.md` holds the rules; `CLAUDE.md` beside it is the one line `@AGENTS.md`, in any
folder that needs its own notes. Claude Code reads `AGENTS.md` only where no `CLAUDE.md` exists and not every
session; an importing `CLAUDE.md` loads it every session, once. A symlink works, but a
Windows checkout can turn it into a text file. **README is for people, AGENTS.md for agents:** AGENTS.md says "read
`docs/STATUS.md` first" and links the docs rather than repeating them. Never tell agents to read DECISIONS, LESSONS or
a requirements file whole; an agent reads the entries its brief cites, since a read-first list is paid by every agent
on every task.

**Checking a repo.** `layout-check [path]` prints one line per finding and exits 1 on any (`--fix-hint`, `--stub`).
A repo names exceptions in `.layout-check`, `allow <path>: <reason>`, one per line, and selects the second form with
`form <name>: <reason>`. Move existing repos to the layout one at a time, each with the user's OK (**migrations**).

## Format

```
- **Headline stating the rule.** The corrected fact, why the wrong version was
  tempting, and what to do differently. Verified YYYY-MM-DD (external facts only).
```

- **The headline is the invariant, not the incident** ("In image X, `/opt` is a real directory", not "`/opt` broke the
  build"): it alone should change behavior, since the body gets skimmed.
- **Record the reusable fact:** "X is not Y, and Y looks right because Z", not "I got file A wrong".
- **Date only what decays.** A fact about an external system (vendor support, a version, a price, a tool's behaviour)
  carries "verified YYYY-MM-DD"; skills and docs carry no dated incident logs. Don't rewrite existing entries to this
  format. `docs/CANDIDATES.md` keeps its dates: they count second sightings.
- Make relative dates absolute, and link related entries so a reader lands on the whole cluster.

## Maintenance

- **Update an existing entry rather than adding a near-duplicate:** two entries on one fact will drift.
- **Delete entries that prove wrong:** a stale memory is trusted.
- **Verify an entry before relying on it:** confirm any file, function, flag or path it names still exists.
- **Consolidate append-only logs:** replace entries circling one fact with one, and consolidate a lessons file too long
  to read in one sitting before adding to it.

# Writing a new skill

## Admitting a rule, skill or role

One test for every addition: a library rule, a promoted candidate, a role lesson, a new skill. Answer each in a line,
in the commit or decision that adds it:

1. **Failure:** what went wrong in real work. An idea from elsewhere has none yet, and says so.
2. **Scope:** which projects and agents it fits. Would it hold for a different person, organization, layout and tool?
   If only for one owner, it goes in their own config.
3. **Evidence:** independent sightings (two projects that each hit the failure, not one piece of advice copied
   twice) or a paired test (below).
4. **Overlap:** the rule it replaces or merges into; add only when none fits.
5. **Limit:** one case where it should not apply.

Without independent evidence it waits as a candidate. The owner's say-so admits it as an experiment, marked so, not as
proof. Where it lands: true of one repo, that repo's conventions; of one domain, a skill; of everything,
**ground-truth**.

**Close the loop on a substantial or doubtful addition.** Its skill's `NOTES.md` records what should improve, what
might regress, and the event that triggers a revisit. After real use, keep, narrow, merge or remove it. Success is a
better outcome at acceptable cost, not an agent following the rule.

## Feeding the library

When a lesson or decision you record in any project would hold in another project of its kind:

1. **`docs/CANDIDATES.md` already has it from an independent project, or the owner admits it as an experiment** →
   admit it (above) and delete the candidate. Replace or merge an existing rule before adding one.
2. **Otherwise** → append a candidate: `- **YYYY-MM-DD, <project kind> - Headline.** The fact. Target: <skill>, or "new: <name>".`

What enters the library is general:

- **Name the kind of project, never the project** ("a web app"), and no people, hosts, paths, accounts or customer data. Keep the concrete failure that made it a lesson. `tools/check_private.py` catches common leaks; add your own names and terms to the clone's git-ignored `.private-terms`.
- **Nothing from work done for an employer or client** unless its owner allows it.
- **No personal workflow.** How one owner works (machines, permissions, schedules) goes in their own `~/.claude/CLAUDE.md`.

What keeps it from bloating, enforced by `tools/check.py`:

- **`docs/CANDIDATES.md` holds at most 30 entries, none older than 90 days.** At either limit, review with the owner: promote, merge or drop. A fact true of one skill's domain only goes to that skill's `NOTES.md`.
- **Skill bodies stay under 18,000 characters and role bodies under 7,000;** `AGENTS.md` and **ground-truth**, which
  load for nearly every task, stay under 20,000 together. Cut rules that no longer change behaviour and repeated
  anecdotes. Moving text to `NOTES.md` preserves evidence; it is not a cut. A substantive change states its net change
  in loaded characters (`tools/check.py` prints the totals).

Edit the library in its clone, never in `~/.claude/skills`; run `tools/check.sh` before committing; commit and push only where the owner's `~/.claude/CLAUDE.md` grants standing permission.

## One thesis per skill

State the thesis in a sentence; if you cannot, split it. Content off the thesis goes elsewhere **even when it is good
advice**, the part most often broken. Split a skill that grows uneven, half its rules idle on half the work it fires
on, and let the universal part fall back to ground-truth.

**Two boundary tests, for a skill, tool or module.** Aim for a clear boundary, not the smallest pieces: every split is
one more thing to choose between and keep in step.

1. **Describe it without "and".** If you can't, it may be two things; split only if the parts change for different
   reasons.
2. **Imagine deleting it.** If the complexity vanishes, it was a pass-through: remove it. If it reappears across its
   callers, it earns its place.

## The description is the trigger

Nothing else loads until the skill fires, so the description alone decides whether it does. Write when to use it, not
what it is about, which fires unpredictably: the artifacts, file types and moments ("Use when writing X, when Y
changes, before Z"), in the words people use, informal ones too.

## Write the body for one pass

- Length is a cost: skimmed rules don't apply. Cut generic good practice; what could be guessed takes space from what
  couldn't.
- Lead each rule with the claim, then the reason; never cut the reason: it covers the unanticipated case.
- Prefer a concrete failure to an abstraction: "a grep for `\[[A-Z]` misses `[30/40]`" lands; "be careful with
  patterns" does not.
- **Don't restate what the environment says** (`--help`, a config, the layout): the copy goes stale. Keep what no
  lookup reveals.
- **Match the form to the failure.** A known step skipped: a plain prohibition with its reason. Wrong output shape: say
  what the output is, parts in order. A required item omitted: a slot in the template. Conditional behaviour: a
  condition the agent can observe, not a rule plus exemptions.

## Test it two ways

1. **Does it fire correctly?** On work where it should, and quiet elsewhere.
2. **Does it change what you would otherwise do?** A skill that restates default behavior is overhead: delete it.

**For the second, run a baseline when the rule is costly or doubtful.** Write the scoring first; give fresh agents the
same real task, at least 5 with the rule and 5 without, and score what they did from the diff and their commands, not
their reports. If the control already behaves, cut the rule. Include a trap the rule must not make worse. One fixture
is weak evidence: record its limits with the result.

## Keep the library tight, not small

No target count; a recurring pattern earns its file. Before adding, ask whether an existing skill covers it
or should absorb it, whether two skills now overlap enough to merge, and whether it is a pattern or a lesson in a
skill's clothes. Guard against overlap, not count: two skills half-covering a topic both fire unreliably. Prune and
merge as readily as you add.

**Adding a skill means adding its row to the index in the library's `AGENTS.md`** (loaded everywhere through
`~/.claude/CLAUDE.md`), the single source of truth for what exists; a skill missing from it gets no routing.
