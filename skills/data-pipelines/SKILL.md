---
name: data-pipelines
description: Combining sources into reports, warehouses, dashboards or metrics: connectors, transforms, reconciliation. Use when building or debugging a pipeline, defining a metric, or when two sources disagree about a number.
---

# Data pipelines

Assumes **ground-truth**; for work where numbers move between systems and someone decides from the result. The hazard: a pipeline that fails loudly gets fixed, but one that silently drops a tenth of its rows produces a
report that looks fine and is wrong until a number is challenged in a meeting. Examples behind these rules are in
`NOTES.md` beside this file.

## Land raw, immutably; derive everything else

Land the source payload exactly as received and never mutate it; every table, metric and report downstream comes from
committed transform code.

- **Never `UPDATE` one wrong number in the warehouse; fix the transform:** the patch is a second source of truth that
  the next refresh reverts or that drifts invisibly.
- **Land API responses in staging, then normalize,** never straight into reporting tables: you re-run from staging when
  the transform proves wrong, as it will.
- **No spreadsheet maintained beside the report:** two answers and no way to say which is right.

## Point-in-time correctness

Re-running last month's report must reproduce last month's numbers, or late data and retroactive source edits silently
rewrite history. Immutable raw plus effective-dating buys this. Decide whether each metric is as-of-run or
as-of-period, and say which on the report.

## Reconcile: counts, not "the job succeeded"

Assert at every hop, as part of the run, not on a dashboard someone might check: a pipeline that doesn't count rows
drops them.

- **Row counts** source → landed → transformed: the silent drop is the commonest real failure and the easiest to catch.
- **Control totals** on money and quantity columns.
- **Distinct-key cardinality** and **null rates** per column.
- **Freshness:** the newest record is as new as expected.

**Add business assertions, since schema tests check shape, never meaning:** `not_null` and `unique` pass on wrong
numbers. Assert this total equals that total, this ratio sits in this range, a closed month doesn't move.

## Conformed metrics: two sources rarely mean the same thing

Two sources that seem to measure the same thing almost never do (CRM and billing revenue differ on recognition timing,
conversion date and cancellations), and unioning them or picking one gives a confidently wrong number that survives
review *because* it looks clean.

- **Define each plane separately, in writing, with its source field.**
- **Make the delta an explicit, monitored output,** not something resolved by picking a winner.
- **Ship a tile only if you can walk metric → query → source field.**

## Connectors

- **Keep a per-source quirks file:** non-obvious facts found while debugging (a cursor dropped on an empty page, local
  time instead of UTC) are lost by morning otherwise.
- **Distrust the API docs:** commit real responses as fixtures, pin contract tests to them, and generate the schema
  from real payloads.
- **Parse with a real parser and assert the field count per record:** splitting CSV on commas or regex-matching JSON
  shifts columns with no error.
- **Pin types explicitly:** lost leading zeros, IDs turned to floats and locale-ambiguous dates corrupt silently.

## Orchestration

- **One writer per table or partition:** parallelize extraction per source, serialize the merge, since concurrent
  upserts into a shared dimension clobber silently.
- **Checkpoint per source:** a failure re-runs that source alone.
- **Make every step idempotent:** guarded creates, `CREATE OR ALTER` views, merges not blind inserts; never assume a
  clean database.
- **Match poll intervals** to how fast the upstream changes.

## Reports

- **Every chart answers a stated question;** cut tiles that exist only because the data did.
- **State each metric's definition beside it,** including its as-of semantics.
- **Make the reconciliation query your data-quality page,** not a checker plus a separate dashboard.
