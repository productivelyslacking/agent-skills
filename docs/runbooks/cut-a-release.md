# Cut a release

**Just do this:** with `main` green in CI, tag it and push the tag. People who pin (`tools/sync-claude --pin vX.Y.Z`)
stay on a tag until they choose the next one; people who track `main` get every change at their next session.

```bash
git switch main && git pull --ff-only
tools/check.sh                                  # in WSL on Windows
git tag -a vX.Y.Z -m "vX.Y.Z: <one line on what changed>"
git push origin vX.Y.Z
"gh" release create vX.Y.Z --verify-tag --generate-notes   # optional: a release page with notes
```

**Which number:** MAJOR when a rule, skill or role is removed or renamed, or a role may now do something it couldn't
(approve, merge, publish); MINOR for a new skill, rule or role, or a rule that now applies more widely; PATCH for
wording, fixes and checks.

**Verify:** `git ls-remote --tags origin` lists the tag, and `tools/sync-claude --pin vX.Y.Z` on a scratch clone
leaves it on that commit. Never move or delete a pushed tag: someone may be pinned to it.
