# ops-scripting: notes

Read on demand. Single sightings from real projects, kept out of `SKILL.md` until one recurs; each names the kind of
project and its date.

## Single sightings

Moved from the library's candidate list on 2026-11-13: true of this skill's domain, not yet seen twice.

- **2026-10-06, action-rpg - Intel I219 (e1000e) NICs can hang under bridged VM traffic, and a link-state check still passes.** Fifteen minutes into the first jobs on new Proxmox VMs (rsync and SSH from one PC, NIC capped at 80 MB/s), two of three ThinkCentre nodes logged "Detected Hardware Unit Hang" every 2 s with no reset; their LAN went dark while `ip link` said UP. Just before each hang an SSH session failed with "message authentication code incorrect": corrupted frames that TCP's offloaded checksum let through. Before putting load through an onboard I219 bridge, check `journalctl -k` during the first heavy run, and make health checks look for the hang, not just link state. (Likely the known TSO bug; the fix, offloads off, wasn't applied: a network change for the owner.) Target: ops-scripting or ground-truth (rule 6).
- **2026-11-05, firewall-box - Installing a package that touches boot can silently swap the initrd builder.** On Ubuntu 26.04, `clevis-initramfs` removed dracut for initramfs-tools with `-y`, leaving an initrd that could not open the LUKS root, one reboot from an unbootable box. Nothing failed; the install looked routine. Read the `Remv` lines of `apt-get -s install` first, and inspect the new initrd (`lsinitrd`) before rebooting. Target: ops-scripting.
- **2026-11-05, ci-runners - Moving CI to single-use runners exposes failures a persistent build cache was hiding.** Persistent runners may skip a Dockerfile's package step for days. Cold ones run it every job, and a pinned snapshot mirror took 3 to 36 s per uncached file against 0.05 s cached, with apt retrying. Re-running a commit that passed earlier also isn't a clean comparison: the first cold runs failed at that step, then at an audit whose advisories were published after the pass. Reproduce a failure from another network before blaming the new runner, and use a real install, since a package manager's `--dry-run` never fetches the slow file. Target: ops-scripting, or "unsure".
- **2026-11-05, ci-runners - When baking a Docker build cache into a CI image, stop before any security audit step.** A cached layer replays a past audit result, so later jobs on identical source skip the check, and a new advisory also breaks the image build itself. Cut the stage before the source copy: dependency layers are shared, because cache keys depend on the instruction and its inputs, not on the Dockerfile that contains them (not yet proved on a real build). Then rebuild to confirm every `RUN` reports `CACHED`, rather than trusting the exit code. Target: ops-scripting, or "unsure".
- **2026-11-07, firewall-box - A rollback that relies on what an earlier run left behind dies with a reinstall.** A runbook's "one symlink back to the previous build" depended on an older setup script having installed that build; the current script no longer did, so on a clean install the rollback would have pointed the service at nothing, and no check failed. Have the current setup script install anything a runbook relies on, and have the verify step check that it's there. Target: ops-scripting.

## The unattended contract

- **One writer per copy, the sightings behind it.** A two-way `rsync --delete` reverted whichever side copied back;
  `git checkout -- FILE` dropped the file's other edits; editing a bash script mid-run broke the run.
- **A job survives its session, the sightings behind it.** A watcher started over ssh died with the session's processes,
  and a closed terminal ended an agent session with its background jobs.

## Inputs and outputs

- **A secret in argv, the incident.** A key passed as `sudo grep -rlF "$key" ...` landed in `auth.log` on two machines and
  needed rotating; `curl -H "Authorization: token $(cat token)"` exposes it in `ps` the same way.

## Protect by permission, not by recognition

- Review after review found one more alias a path check missed: a symlink swapped in at run time, a second mount of the
  same volume, a caller-set environment variable that steered which target counted as "protected". Each fix recognised
  one more shape of the same thing, until the privileges were separated.

## Containers

- A plain `rm -f` on one check script's containers left 20 anonymous volumes a day.
- Persisting HOME in a GPU container took one job from 705 s to 436 s.

## Environment assumptions

- **Present is not working, the incident.** On an atomic distro image, `docker` was installed but its socket failed at
  boot (no `docker` group), and every script calling it failed. The distro's helper copied the group from a list that
  didn't contain it, skipped it silently and exited 0.
