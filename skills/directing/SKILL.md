---
name: directing
description: Holding a story-led project's vision across story, look, voice and pacing: recorded calls, notes, sequence review, who decides, keeping the plot from an owner. Use when acting as director, when creatives disagree, or before claiming a scene will surprise anyone.
---

# Directing

Assumes **ground-truth**. Thesis: **a director makes the creative calls, writes them down so they bind, and knows which
ones it can't judge**, so meetings end in verdicts and nobody rates a surprise it knows.

**How far to trust this.** Research-based and unproven: written from a review, not use (D25); first test, a story-led
game's first owner playthrough. No director's book was opened, every measured study was read as an
abstract only, none studied an AI director; `NOTES.md` says how each source was reached.

**Never claim strong direction improves work:** whether a single strong vision predicts quality isn't known [DR-70];
shared team vision is stronger on self-report than on objective measures [DR-66]; game revenue varied more with middle
managers than innovative roles, in a role mapping recalled from memory [DR-67]. These rules aim at fewer open questions
and contradictions, checkable but unmeasured.

**Reading a rule:** claim, reason, kind, tag. `[DR-54]` is a claim with its limits and examples in
`EVIDENCE-DIRECTING.md`, `[DR-DRAFT]` its draft of the role; `[F-C5]`, `[G-C20]` are in
`../production-stages/EVIDENCE-PRODUCTION.md`. Kinds: *measured*; *practitioner*; *demonstrated* (on one production;
says nothing about cause); *reported* (journalism or encyclopedia); *inference*, the research author's, or *inference
(editor)*.

## When a project needs one

**Have a director when story is the product; otherwise keep the functions and skip the title.** Half-Life kept a story
keeper, a written document and tests that overruled opinion, with no director: the main counterexample. Practitioner,
one winner's retelling [DR-39]. Role: `agents/director.md`.

## Deciding and recording

- **Make the call and write it down with its reason and date;** fundamentals left open cost months. Reported, anonymous,
  with rival causes; practitioner [DR-14, DR-9].
- **Log open creative questions with their age; report count and oldest:** latency is the measurable, plot-free symptom.
  Inference [DR-14].
- **Write decisions with examples already made, not only principles:** agents share no hallway; unwritten means absent.
  Inference, untested [DR-17].
- **Write a scene's done condition before work starts, and let the producer stop it:** agents loop cheaply. The director
  can't waive the producer's budget and round count. Reported; the ownership is inference [DR-40].

## Statements that reject options

- **A statement is usable only if it rejects a real option:** ask two agents what it rules out; if they differ, redo it.
  Practitioner; the test is inference [DR-11, DR-15].
- **Before briefing anyone, write four things:** what it's about, what that rejects, one named person as audience proxy,
  what changes between first and last scene. Practitioner, stated after the event; the set is inference [DR-5, DR-11,
  DR-12].
- **Rank what gets given up first, and name what can't be.** Borrow Murch's order for a cut: emotion, story, rhythm,
  then the rest (his percentages are priority, not measurement). Planted facts can't go. Practitioner,
  second-hand; the exception is inference [DR-30, DR-18].

## Giving notes

- **From the owner and non-experts take the problem, not the fix** ("she seems too meek", not "make her outfit red").
  Practitioner, no outcome evidence, cited from an earlier pass not re-read here [DR-23, DR-29].
- **Say what you saw, ask what was meant, propose, and log refusals with reasons.** One podcast anecdote, practitioner
  [F-C50].
- **Keep a plain "this fails":** plussing is unverified and could blunt a note, so a reviewer's output format must be
  able to return a fail. Inference [DR-22, F-C51, DR-69].
- **A voice note gives at least who's speaking, to whom, and how.** Verbs and objectives versus adjectives is disputed,
  for human actors: test both on the chosen voice engine. Practitioner, untested here [DR-27, DR-24].
- **Give a performer beat and objective, not the plot;** take many, choose in the edit against picture and neighbours.
  Practitioner, disputed on count; cost differs for synthetic voices. Inference [DR-25].
- **Don't rewrite someone's work to your taste.** Practitioner, a passing remark [DR-2].

## Reviewing a sequence

- **Judge the assembled reel, not script or runtime,** whose length isn't the felt length. Reported, anecdotes
  pointing opposite ways [DR-35].
- **Log pacing per scene, then watch anyway:** words, seconds, longest stretch without player action, branch reach.
  Demonstrated on a shooter; the fields are inference [DR-34].
- **Ask per scene:** whose objective changes, what we know now that we didn't, what breaks if it's cut. Inference,
  assembled from practitioners; no director's systematic scene criteria were reached [DR-33].
- **Keep every cut; someone other than the scene's writer owns reel review, which the writer sees.** No account of the
  editor's role was reached, so the split is untested. Reported, inference [DR-42, DR-37, DR-6].

## Who decides what

- **Reviewers advise; whoever is responsible decides and records why,** keeping each decision in one place. Told by the
  studio's head, no denominators or failures [DR-19, F-C5]; for agents, inference.
- **Name the veto, and who's above it, before the fight;** advice-only forums sit in studios that still replace
  directors [DR-20, F-C24]. Here only the owner, who hasn't read the plot, ranks above the director, so before they play
  each chapter the producer starts a fresh reviewer with `sealed/` and their written limits. It returns PASS or FAIL,
  plot-free and not via the director, on premise, cast balance, content limits, art style, consistent facts. A FAIL goes
  to the owner as below; they can always break the seal. Inference [DR-DRAFT].
- **The seal limits a report's form, never whether it's made.** A blocker, broken promise, or drift from premise, cast
  balance or content limits reaches the owner via the producer, plot-free; if it can't, say "s014: a problem I can't
  describe without plot. Break the seal for it, or leave it to me?" Board the count and oldest age of held findings. Ask
  about content by general category; specifics spoil. Inference (editor).
- **Fix one way to settle a dispute:** a test if one can decide; otherwise the named tie-breaker decides and records it.
  Inference [DR-45].
- **Split logistics (producer) from content (director);** a company blog [DR-8]. Someone must own cutting: the producer
  sizes a cut, the director, who can read the plot, picks what goes. Reported; the split is inference [DR-38]. Don't let
  a director crowd out the producer: inference; revenue, not quality, roles mapped from memory [DR-67].

## Keeping story from the owner

A project may keep its story from its owner so their first play stays real; what they've read is no clean test of
surprise. All inference (editor), from [DR-DRAFT] and [DR-58], with no precedent as a method [DR-62]; record what leaks
on the first run. It assumes the owner is the only human; a second who reads ahead (ask) removes most of the cost as
stand-in, moderator and independent look.

**The rule: anything the owner or producer routinely sees carries IDs, counts and states, never what happens, to whom or
why.**

- **All story lives in `sealed/`** at the repo root, listed in README's table: "contains the plot; don't open it if you
  want your first play". It holds every plot-bearing document, note, result and log and the story content (text, stills,
  voice, prompts); the build reads it there. Only neutral IDs (`s014`) cross out.
- **The project's CLAUDE.md, which every agent loads, says in these words:** "Story is kept from the owner until their
  first play (directing). Outside `sealed/`, everything you write and every hand-back carries IDs, counts and states,
  never what happens, to whom or why. Put findings with plot in `sealed/notes/<issue>.md` (if you can't write to the
  repo, `scratchpad/<task>/sealed/`) and hand back a verdict per criterion and that path. The producer and owner don't
  open `sealed/`. A problem you can't state without plot: say 's014, blocking, can't be described without plot'." The
  producer is included since the owner reads its writing; its briefs give ID and file.
- **It's a convention, not access control:** the owner can break it any time (README says how); a stranger can take
  over by reading it (rule 11).
- **The seal ends where the owner has played;** dissolve it after the last chapter. Offer play chapter by chapter early:
  it spends the surprise in small amounts and gets a human reaction sooner.
- **Sealed work needs delegated merge approval for story PRs; ask before the first.** The owner doesn't open their
  diffs; a merge-reviewer HOLD on look shows a plot-free frame only.
- **Keep a plot-free test scene for device checks,** or game-studio's device tryouts spend the first play.
- **Test what your tool shows of agents' file reads before trusting the seal;** one setup's report isn't a test. Decide
  at the start on channels nothing here closes: a watched session showing reads or prompts, PR image thumbnails, CI logs
  that print lines, merge-conflict text, preview builds, session logs read by team-ops.

| Where it leaks | Instead |
|---|---|
| Issues, PRs, commits (bodies too), branches, filenames | `s014: retelling fails`, `story/s014-r2`, `s014_bg_a.png`; detail in `sealed/notes/<issue>.md`. Still one issue per item |
| Stills, clips, contact sheets, prompts, credits, manifests | Under `sealed/`, or plot-free |
| Board, status, decisions log, hand-backs, reports | `s014: reel v3, 2 of 3 cold readers retold it as intended`; counts; a plot-free pointer to a sealed entry |

**Where this meets other rules:**
- *The board and issues* stay the state and only list of open work, in IDs and counts; *reports* open with counts.
- *Read the evidence, not the report* has a named exception: on a plot-bearing criterion the producer takes QA's
  verdict, the merge-reviewer re-opens the evidence; the producer still reads all plot-free evidence and checks each
  sealed path exists. The director copies what must last from scratch into `sealed/`.
- *The user keeps feel and look,* before first play on plot-free frames and the test scene.
- *art-direction and generated-art (D24)* bind here; the exclusion isn't sealed away. An image that could break it gets
  the independent look, which can only discard it or send it to a person; on a sealed story image doubt means discard,
  counted on the board. The owner can sign off plain, plot-free portraits labelled by letter, giving adult appearance
  its person. The director picks only among frames in the owner-approved style, provisional until played; a clean model
  look clears nothing, and the owner's play is the person's look at the latest. Rejected frames stay in `sealed/`,
  offered after play with the count; exclusion discards aren't.

**Check the seal with something that can fail.** Keep plot words, not cast names the owner knows, in `sealed/TERMS.txt`.
Before each report a script runs `grep -c -i -F -f` over every tracked file outside `sealed/`, full commit messages,
branch and file names, and issue and PR titles, bodies and comments; read names with `git ls-files -z` or quoted
non-ASCII names are skipped. It prints channel and count, **never the matching line**, and hides a file name that itself
hits. Strip blank lines from the terms (one matches everything); an unreachable forge or failed query is "not checked",
never a pass. Plant a term to see it fail; it catches only listed words, so a clean run isn't proof. Report a leak by
where, not what, and stop: it cost one surprise.

## What the director can't judge

- **Don't judge your own surprise:** knowing an outcome worsens reasoning about what others believe even when warned, so
  "imagine you don't know" fails, at least for people; untested for models. Measured, not on stories or models; abstract
  and encyclopedia [DR-54, DR-55].
- **The owner's first play and each tester's happen once:** plan what spends them, not as routine checks. Don't argue a
  spoiler wouldn't matter: studies disagree, one found unspoiled stories more enjoyable; **story-design**'s "harm is
  small" is about writing a story that holds, and an unspoiled first play is the owner's choice. Inference, measured and
  contested [DR-62, DR-58, G-C20].
- **AI cold readers aren't validated: this skill's biggest open risk.** Nothing shows they predict human surprise; a
  model can report surprise it didn't "feel" and share the writer's blind spots. The producer starts each outside the
  repo with one file of what the player sees and a `sealed/` path for its answer; it hands back only "done". Ask for a
  retelling, its theory, what it expects next, where it lost interest; the contradictions and misreadings it finds are
  also untested against people. All guessing the same at one panel is a finding, none guessing weak evidence; compare
  them with the first humans. Inference [DR-61].
- **Ask the owner early, without plot: may a human stand-in read ahead, and in what state should your first play
  happen?** Their call; no precedent found. Inference [DR-62].
- **Time a first reader, ask when they guessed, check clues on a second reading:** newcomers take far longer than makers
  think. Reported; the rest is from low-standing advice sites [DR-56, DR-60].
- **Have someone else judge your ideas:** creators forecast others' new ideas better than managers, not their own.
  Measured on circus acts, abstract only [DR-52].
- **Weigh a test by who, when and what they were told, never by "they ignored it and were right",** which has no
  denominator. Reported [DR-49, DR-50]. How to run one: **production-stages**.

**Don't claim** "this twist will surprise you" (report what readers said) or "the owner will love this" (unmeasured
until play).

## Not established

Write as unknown every gap marked above (AI readers predicting humans, strong vision predicting quality, verbs versus
adjectives on a voice model, scene criteria, the editor's role, directing with the plot hidden), and how directors judge
a twist they know.
