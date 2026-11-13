# migrations: notes

Read on demand. Holds the evidence behind `SKILL.md`'s rules.

## Re-addressing hosts and clients

- Seen three times on one network. A grep of config files and a socket check both came back clean, and the apps broke:
  their stored links still named the old address, visible only through each app's API.
