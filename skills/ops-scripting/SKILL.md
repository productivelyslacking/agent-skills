---
name: ops-scripting
description: Scripts that run unattended: endpoint automation, scheduled jobs, remediation, provisioning, CI steps. Use when writing or debugging a script that runs without a human watching (as SYSTEM, from cron, across a fleet).
---

# Ops scripting

Assumes **ground-truth**. The distinguishing constraint: **nobody is watching.** No one answers a prompt, reads a
warning, or notices that it half-worked, and in fleet automation the blast radius is every endpoint at once. The
incidents and numbers behind these rules are in `NOTES.md` beside this file.

## One command per job

For anything a person runs by hand (ground-truth rule 10): one command per job (`forge import <repo>`, `forge status`)
that does every step, checks each with something that can fail, and stops at the first failure with one plain line:
what went wrong and the exact next thing to do. Print steps that need the person's own login verbatim (what to paste,
where). A runbook's step list is the reference behind the command, not a substitute. A job is what the person wants
done, not the steps inside it; where to draw the line is in **durable-knowledge**, "One thesis per skill". A tool that
another tool or an agent reads prints JSON on request, with a plain summary for people.

**Several steps only a person can do get a walkthrough script** (a new account, secrets in a dashboard, a one-off
cutover): one stage per screen with progress shown; open the page before asking for what's on it; say exactly what to
click and copy; hide secret input and write each value where it belongs (stdin or a 0600 file, never argv); confirm
before anything irreversible. Check a dashboard's steps or ask; don't guess them. An agent doesn't run it, since it
blocks on a person: it traces each value statically and gives the person the one command.

## The unattended contract

- **Nothing interactive, ever:** a prompt unattended is a hang, and a hang is a timeout with no diagnostic. In
  PowerShell: no `Read-Host`, `Get-Credential`, `Out-GridView` or `pause`, and `-Confirm:$false` on anything that asks.
- **Make every action idempotent:** it will be re-run, scheduled, retried, or run by someone who doesn't know it ran.
  Check state, act only if needed, make acting twice harmless.
- **Leave no half-state a re-run can't recover from:** it will be interrupted. Write the marker after the work.
- **Lock, or make the work order-independent:** a misfiring scheduler runs it concurrently with itself.
- **One writer per copy.** Two writers that read, modify and write the same file, mirror or checkout lose each other's
  work: a two-way sync with delete reverts one side, a path checkout drops the file's other edits, and editing a bash
  script mid-run breaks the run, because bash reads it as it goes. Lock or merge on write, sync one way, and run long
  scripts from a fixed copy.
- **A job survives its session only if something else owns it:** jobs started from ssh or a terminal die with it. Run
  long jobs under a service, `systemd-run --user` or tmux, and write each result line to a file a resumed run reads
  before starting again.

## Running as SYSTEM

SYSTEM or a service account is a different world from your session; test as the account it will run under.

- **No user profile:** `$env:USERPROFILE`, `~`, `AppData` and the desktop point elsewhere or nowhere; `HKCU:` is the
  wrong hive. To inspect user state, enumerate profiles.
- **No mapped drives or user network context** (UNC paths may not resolve), and a different temp directory and PATH.

## Inputs and outputs

- **Accept parameters as named arguments and as environment variables:** most RMM platforms pass env vars. Document
  which names the platform sets.
- **Exit codes are the contract:** 0 for success, distinct non-zero codes per failure, because the platform alerts on
  them. A script that exits 0 after failing is worse than one that crashes.
- **Separate detection from remediation:** detect answers "does this machine need work?" by exit code alone, so the
  platform reports the fleet's real state rather than a count of runs.
- **Write output for someone reading a log at 2am:** timestamped lines, what is about to happen, then the outcome.
  Suppress a linter rule against transcript-style output rather than the output.
- **Never print secrets:** the platform captures all output.
- **Never put a secret on a command line:** `sudo` and auditd log the full argv and `ps` shows it to every user. Hand it
  over on stdin or in a 0600 file the command reads (`grep -F -f /dev/stdin`, `curl -H @file`, `--password-file`),
  privileged commands most of all.
- **A Windows path inside a script's string literal is not text:** `C:\repo` in a Python string, `$'...'` or `printf`
  becomes `C:`, a carriage return and `epo` (`\a` a bell), and the file looks right in most viewers. Pass paths as
  arguments or build them from a backslash variable, then check the written bytes (`repr`, `od -c`) for control
  characters.

## Protect by permission, not by recognition

When a script or service acts for a less-trusted caller, protect what it must not touch by **who may open it**, not by
recognising its path or name: every path check misses another alias (a symlink swapped in at run time, a second
mount, a caller-set environment variable). Run the untrusted part under an account the OS denies access to everything
protected, hand secrets in per call, act only on an explicitly named target in a scrubbed environment, and keep path
checks as a second layer. **When a review finds a second alias of the same protected object, stop listing aliases and
separate the privileges.**

## Containers

- **Clean up what the run made:** `docker rm -fv` or `--rm`; a plain `rm -f` keeps the anonymous volume. Give test stacks
  no restart policy, since a cancelled CI step gets no clean-up, and sweep by label at the next job's start.
- **`timeout docker run` stops the client, not the container:** name it and `docker rm -f` it on timeout.
- **Headless Chromium or Electron:** `--init` (`xvfb-run` as PID 1 hangs silently) and `--shm-size=512m` (the renderer
  dies on the default 64 MB).
- **Write single-file bind mounts in place** (`cat new > file`): `sed -i` and rename-saving editors make a new inode the
  container never sees. Diff the file as the container sees it before reloading.
- **Persist HOME for GPU containers:** with `--rm` and a throwaway HOME they recompile and re-tune every run.

## Provenance

- **Stamp the script with a version and its commit, and print both at run start:** it is how a field symptom traces to a
  revision, and a stale deployment otherwise presents as bugs you already fixed.
- **Bump the version with every change that ships:** a lagging version is worse than none, and where deployment is
  manual it is the only way to tell what is out there.

## Environment assumptions

Verify rather than assume, and fail with a clear message, not a stack trace:

- **Runtime version** on the target, usually older than yours (Windows PowerShell 5.1 and PowerShell 7 differ enough to
  break scripts); **module and tool availability** beyond the OS baseline; **OS build and edition**; **network and
  proxy** before any download.
- **Present is not working:** check a tool with its own health command (`docker info`), not `command -v`. Before
  prescribing a platform's fix, check its precondition, since helpers skip silently and exit 0; re-run the health check
  after any fix, because a process started before a group change still lacks it.
- **Prefer the platform's built-ins:** installing a module on every endpoint to save twenty lines is a fleet-wide change
  for a convenience.

## Before it reaches the fleet

- **One machine, then a pilot ring, then the fleet:** a bad script everywhere is the fastest outage available.
- **Run the static analyzer in CI:** fail on errors, report warnings without blocking so a deliberate pattern isn't
  forced into a worse rewrite, and tighten once the backlog is clear.
- **Test the failure paths:** missing module, no network, insufficient rights, the thing already done.
- **Know how to stop and reverse it:** how to pull the script, and what undoing its change requires.
- **Comment for a stranger:** comment-based help on every function, and why on any non-obvious step.
