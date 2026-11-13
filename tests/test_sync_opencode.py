"""tools/sync-opencode against a throwaway home, with a stand-in `opencode` on PATH that reports what it loads.

- it links every skill and generated role and adds the rule files to opencode.json, keeping the user's keys;
- a rerun changes nothing; a file it didn't make is left alone and reported; a JSONC opencode.json is left alone;
- --check fails until the install is in place, and fails when OpenCode doesn't list a role or lists one without
  its permissions (what OpenCode does with a file it can't parse, or a field it drops);
- --uninstall leaves opencode.json as it was and no links behind.
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "tools" / "sync-opencode"
ROLES = sorted(p.stem for p in (ROOT / "local-agents" / "opencode" / "agents").glob("*.md"))
SKILLS = sorted(p.parent.name for p in (ROOT / "skills").glob("*/SKILL.md"))

# Stands in for `opencode`: `debug agents` lists every role linked in the config folder as OpenCode would, except
# those named in $DROP (skipped) or $BARE (listed without permissions); `api skill.list` lists the linked skills.
FAKE = """#!/usr/bin/env python3
import json, os, pathlib, sys
cfg = pathlib.Path(os.environ["XDG_CONFIG_HOME"]) / "opencode"
drop, bare = os.environ.get("DROP", "").split(), os.environ.get("BARE", "").split()
if sys.argv[1:] == ["debug", "agents"]:
    ids = [p.stem for p in sorted((cfg / "agents").glob("*.md")) if p.stem not in drop]
    full = [{"action": "*", "resource": "*", "effect": "deny"}]
    print(json.dumps([{"id": i, "color": "#000000", "permissions": [] if i in bare else full} for i in ids]))
elif sys.argv[1:] == ["api", "skill.list"]:
    print(json.dumps({"data": [{"id": p.name} for p in sorted((cfg / "skills").iterdir())]}))
"""


class SyncOpenCode(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp)
        self.home = self.tmp / "home"
        self.cfg = self.home / ".config" / "opencode"
        self.cfg.mkdir(parents=True)
        (self.home / ".claude").mkdir()
        (self.home / ".claude" / "CLAUDE.md").write_text("Machine facts.\n")
        self.bin = self.tmp / "bin"
        self.bin.mkdir()
        self.prior = {"$schema": "https://opencode.ai/config.json", "model": "local/x", "instructions": ["mine.md"]}
        (self.cfg / "opencode.json").write_text(json.dumps(self.prior, indent=4) + "\n")

    def run_it(self, *args, fake=True, **env):
        if fake:
            (self.bin / "opencode").write_text(FAKE)
            (self.bin / "opencode").chmod(0o755)
        else:
            (self.bin / "opencode").unlink(missing_ok=True)
        path = f"{self.bin}{os.pathsep}{Path(sys.executable).parent}{os.pathsep}/usr/bin:/bin"
        env = dict(os.environ, HOME=str(self.home), XDG_CONFIG_HOME=str(self.home / ".config"), PATH=path, **env)
        return subprocess.run([sys.executable, str(SCRIPT), *args], env=env, capture_output=True, text=True)

    def config(self):
        return json.loads((self.cfg / "opencode.json").read_text())

    def test_sync_links_everything_and_keeps_the_users_keys(self):
        self.assertEqual(self.run_it().returncode, 0)
        self.assertEqual(sorted(p.name for p in (self.cfg / "skills").iterdir()), SKILLS)
        self.assertEqual(sorted(p.stem for p in (self.cfg / "agents").iterdir()), ROLES)
        self.assertEqual((self.cfg / "agents" / "qa.md").resolve(), ROOT / "local-agents/opencode/agents/qa.md")
        rules = (ROOT / "local-agents/opencode/AGENTS.md").as_posix()
        self.assertEqual(self.config(), dict(self.prior, instructions=["mine.md", rules,
                                                                      (self.home / ".claude/CLAUDE.md").as_posix()]))
        again = self.run_it()
        self.assertEqual((again.returncode, again.stdout), (0, ""))

    def test_check_fails_until_installed(self):
        before = self.run_it("--check")
        self.assertEqual(before.returncode, 1)
        self.assertIn("instructions don't include", before.stdout)
        self.run_it()
        after = self.run_it("--check")
        self.assertEqual(after.returncode, 0, after.stdout)
        self.assertIn(f"OpenCode lists all {len(ROLES)} roles and {len(SKILLS)} skills", after.stdout)

    def test_check_fails_when_opencode_skips_or_strips_a_role(self):
        self.run_it()
        skipped = self.run_it("--check", DROP="qa")
        self.assertEqual(skipped.returncode, 1)
        self.assertIn("OpenCode doesn't list role qa", skipped.stdout)
        stripped = self.run_it("--check", BARE="developer")
        self.assertEqual(stripped.returncode, 1)
        self.assertIn("lists role developer without its permissions", stripped.stdout)

    def test_check_without_opencode_says_it_checked_files_only(self):
        self.run_it()
        done = self.run_it("--check", fake=False)
        self.assertEqual(done.returncode, 0, done.stdout)
        self.assertIn("checked the files only", done.stdout)

    def test_a_file_it_did_not_make_is_left_alone(self):
        (self.cfg / "agents").mkdir()
        (self.cfg / "agents" / "qa.md").write_text("mine\n")
        done = self.run_it()
        self.assertEqual(done.returncode, 1)
        self.assertIn("isn't this library's link", done.stdout)
        self.assertEqual((self.cfg / "agents" / "qa.md").read_text(), "mine\n")

    def test_jsonc_config_is_left_alone(self):
        text = '{\n  // my comment\n  "model": "local/x"\n}\n'
        (self.cfg / "opencode.json").write_text(text)
        done = self.run_it()
        self.assertEqual(done.returncode, 1)
        self.assertIn("isn't plain JSON", done.stdout)
        self.assertEqual((self.cfg / "opencode.json").read_text(), text)

    def test_uninstall_restores_the_config_and_removes_the_links(self):
        self.run_it()
        self.assertEqual(self.run_it("--uninstall").returncode, 0)
        self.assertEqual(self.config(), self.prior)
        self.assertEqual([p for d in ("skills", "agents") for p in (self.cfg / d).iterdir()], [])


if __name__ == "__main__":
    unittest.main()
