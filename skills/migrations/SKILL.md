---
name: migrations
description: Moving content, data or a system between platforms: inventory, dry runs, resumable runs, validation against the source, the cutover. Use when planning, running or debugging any migration or cutover.
---

# Migrations

Assumes **ground-truth**. In a migration both systems are real, partly authoritative and disagreeing, and what fails to
survive the move rarely says so. The characteristic failure isn't a crash but a run that reports success while leaving
something behind, found months later by whoever needed it. Sightings behind these rules are in `NOTES.md` beside this
file.

## Sequence

1. **Enumerate before you touch anything:** a read-only inventory of counts, sizes, types and edge cases. You can't size,
   schedule or validate what you haven't counted, and its output is the baseline every later validation compares
   against, so keep it.
2. **Preflight both sides:** access, permissions, quota and API limits on source *and* destination. A rejected file type
   found at item 4,000 is a re-run; found in preflight it's a config change.
3. **Dry-run every unit, then real-run every unit; don't interleave:** a whole-set dry run surfaces the systemic
   problems at once instead of one a day.
4. **Persist per-item state** so an interrupted run resumes rather than restarts, and "what moved" is a query, not a
   guess.
5. **Move the delta after the first pass, don't re-copy:** re-copying is slow and silently overwrites destination edits.
6. **Validate against the source, not "the job succeeded":** counts, sizes and checksums per unit against step 1's
   enumeration. Exit zero is not evidence.

## Fidelity: name what does not survive

**Every migration loses something:** write down what before you start and get it acknowledged, since a loss is
acceptable only if someone chose it. Common casualties, none of which error:

- **Version history**, reduced to the current version.
- **Permissions and sharing**, remapped approximately.
- **Timestamps and authorship**, reset to the migration date and account, destroying "who touched this and when".
- **Metadata, tags and custom fields** with no destination equivalent.
- **Comments, annotations and rationale**, the most often missed: rules written *beside* what they govern (config
  comments, CMS editorial notes, review threads) don't travel. Extract them to a durable file **before** the move.
- **Links between items**, left dead or pointing at the old system.
- **Automations, integrations and webhooks** aimed at the old system.

## The two-system window

Between first copy and cutover, both systems are live and diverging.

- **Name in writing which side is authoritative** for the whole window: it is a decision, not an assumption.
- **Freeze the source or plan the delta,** explicitly.
- **Never delete from the source** until the destination is validated *and* has been used long enough for gaps to
  surface. Read-only beats deleted.
- **Name the cutover moment and who announces it:** without one you get two half-used systems and a year of "which one
  is real?".
- **Have a rollback, and know its expiry:** the point past which new work on the destination makes going back
  impossible.

## Migration is the moment to drop what should not survive

- **Treat legacy content as a coverage checklist, not a content source:** much of it describes dead tooling, retired
  processes and former clients. Mine it for scope; re-author rather than copy.
- **Decide per category: migrate, archive or drop, and record the drops,** or someone re-imports them.
- **Know what's in a source export before anything derived from it ships:** exports routinely hold credentials, tokens,
  internal hostnames and client-identifying data.

## Rollout across many units

- **Batch, checkpoint per batch, re-run only failures.**
- **One writer per destination unit:** parallel across units, serial within one.
- **Keep a per-unit status table:** "where are we?" becomes a lookup.
- **Make every step idempotent:** it will be re-run, including by someone who doesn't know it ran.

## Afterward

- **Archive the source visibly, pointing at the replacement:** a dead system that looks alive gets edited.
- **Record the fidelity losses and decisions where the next person looks,** not in the script's comments.
- **Rebuild the verification you lost:** if the old platform checked at build time and the new one has no build, check
  the deployed artifact.

## Re-addressing hosts and clients

Old addresses hide outside the thing you changed, and nothing reports them. Before moving a host or subnet, list what
names the old address: firewall rules on literal IPs (they stop matching while the rule list looks complete; prefer
zone or network objects), every source-address allowlist in front of the services (reverse proxy, host firewall, app
trusted-proxy lists), and each app's stored links, by asking its API, since config greps and socket checks miss them.
Link co-located services by `localhost` or container name, and update them all in the same change.
