# data-pipelines: notes

Read on demand. Holds the examples behind `SKILL.md`'s rules.

## Connectors

- Quirks of the kind a per-source file holds: an API that drops the cursor on an empty page; a tenant that stamps local
  time, not UTC; a field that is null before the 2023 migration; an endpoint that times out unless pulled filtered.
- A delimiter inside an unquoted CSV field shifts that row's columns and corrupts data with no error.
