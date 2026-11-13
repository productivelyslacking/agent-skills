# Working rules

These hold on any project. Their full text is the **ground-truth** skill: load it for any work beyond the
trivial and follow its pointers.

1. **Write it down, in the same session, in a named home.** Lessons, declines,
   deliberate omissions, and reasons that collapsed. If it would change a future
   session, it is not recorded until it is in a file. Only what cost real time or would change a decision,
   written as part of the change, not as a docs pass.
2. **Verify against the real thing, not the description of it.** Measure rather
   than reason. Docs describe the general case; the running system is the one to
   describe.
3. **The plausible generic answer is the default failure mode.** Generated
   content fills gaps with the statistically normal version, which is fluent,
   canonical-looking, and about a different system. Mark unknowns rather than
   letting them be filled in.
4. **Never assert what you cannot demonstrate.** A claim ahead of its artifact
   reads as done, so nobody goes looking. If you can't finish honestly, stop and say what's blocking
   you; that is an acceptable result (owner, 2026-10-08; D11).
5. **One source of truth.** Copies are generated or referenced, never
   maintained. Name the tie-breaker when two can drift.
6. **Check with something that can fail.** Silent success is the dangerous mode;
   a green gate is evidence only about what it checks; a test that has never
   failed proves nothing.
7. **Name the distinct cases.** One rule covering two differently-governed
   things is wrong and survives review because it reads clean.
8. **Secrets never in the repo, an example, a log, or a screenshot.** Confirm
   destructive or outward-facing actions. Never route around a permission denial.
9. **Calibrate to blast radius.** Customer data, published claims, and signed
   policy earn the full weight. A personal project earns rules 1 and 2. Work toward the goal: hardening,
   tooling and docs no current goal needs are not progress, and when only the user can unblock the goal, say
   what's needed and stop.
10. **Design for a human with little time and attention.** One command per job, the answer first, predictable
   places in every repo, fewer choices. Bloat and fluff are the enemy (owner, 2026-11-13): every line loaded must earn its
   tokens, and growth replaces or merges before it adds.
11. **Build so someone else could take it over tomorrow** (owner, 2026-10-21). Even while we keep running it, every
   change leaves the docs, decisions, tests and one-command setup current enough for a stranger to carry on.

## Skill library

The index: the source of truth for what exists. Each skill's description says when to load it.

| Skill | Use when |
|---|---|
| **ground-truth** | Always. The full text of the rules above |
| **durable-knowledge** | Recording lessons and decisions; repo layout; writing skills |
| **claim-integrity** | Documents with checkable claims: policy, compliance, marketing |
| **prose-editing** | Cutting and shaping prose and instructions |
| **migrations** | Any migration or cutover |
| **ops-scripting** | Scripts that run unattended |
| **data-pipelines** | Reports, warehouses, metrics from several sources |
| **dependency-policy** | Adding third-party code; adopt before you build |
| **teaching-design** | Anything that teaches a skill |
| **teaching-programming** | Teaching people to program |
| **production-stages** | When to commit to what in a game or story production |
| **directing** | Holding a story-led project's vision |
| **story-design** | Any story meant to hold an audience |
| **interactive-story** | Stories shaped by the player's actions |
| **psychology-review** | How an audience or learner will read a choice |
| **godot-dotnet** | Godot 4 C# builds, exports, CI |
| **game-simulation-testing** | Game rules, AI and balance tested without a human |
| **game-saves** | Game save files |
| **game-assets** | Game art, audio, licences, credits |
| **art-direction** | What an image should show and whether it works |
| **generated-art** | Making images with a model |
| **gamedev-team-practices** | Readying a game project for collaborators |
| **agent-team** | Splitting work across role agents |
| **landing** | Getting a branch onto main |

Adding a skill is governed by "Writing a new skill" in **durable-knowledge**;
add its row here.

**Feeding the library, on every project:** when a lesson or decision you record
would hold beyond the current project, route it to this library by **durable-knowledge**,
"Feeding the library": a candidate first, admitted to a skill only under its admission test.
Library updates are committed and pushed as they happen only where the owner's own
`~/.claude/CLAUDE.md` grants that standing permission; other repos wait to be asked.

## Working on this library

When the work is in this library itself: read its `docs/STATUS.md` first, and run `tools/check.sh` before
committing. This file is loaded on every machine through `~/.claude/CLAUDE.md`, which imports the library's
`CLAUDE.md` (the line `@AGENTS.md`); keep it short.
