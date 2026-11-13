"""tools/sync-claude against a throwaway home, remote and clone."""
import json
import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "tools" / "sync-claude"


def git(cwd, *args):
    identity = ["-c", "user.name=t", "-c", "user.email=t@example.invalid"]
    subprocess.run(["git", *identity, *args], cwd=cwd, check=True, capture_output=True)


class SyncClaude(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp)
        self.home = self.tmp / "home"
        self.home.mkdir()
        self.remote = self.tmp / "remote.git"
        subprocess.run(["git", "init", "-q", "--bare", "-b", "main", str(self.remote)], check=True)
        self.author = self.tmp / "author"
        subprocess.run(["git", "clone", "-q", str(self.remote), str(self.author)], check=True, capture_output=True)
        git(self.author, "checkout", "-q", "-b", "main")
        for path in ["AGENTS.md", "CLAUDE.md", "skills/one/SKILL.md", "agents/qa.md", "tools/layout-check"]:
            file = self.author / path
            file.parent.mkdir(parents=True, exist_ok=True)
            file.write_text("v1\n")
        shutil.copy(SCRIPT, self.author / "tools" / "sync-claude")
        self.push("first")
        self.clone = (self.tmp / "clone").resolve()
        subprocess.run(["git", "clone", "-q", str(self.remote), str(self.clone)], check=True, capture_output=True)

    def push(self, message):
        git(self.author, "add", "-A")
        git(self.author, "commit", "-qm", message)
        git(self.author, "push", "-q", "origin", "main")

    def sync(self, *args):
        env = dict(os.environ, HOME=str(self.home))
        done = subprocess.run([str(self.clone / "tools/sync-claude"), *args], env=env, capture_output=True, text=True)
        self.assertEqual(done.returncode, 0, done.stderr)
        return json.loads(done.stdout) if done.stdout.strip() else {}

    def tag(self, name):
        git(self.author, "tag", "-a", name, "-m", name)
        git(self.author, "push", "-q", "origin", name)

    def rules(self):
        return (self.clone / "AGENTS.md").read_text()

    def test_pin_stays_on_its_tag_while_main_moves(self):
        self.tag("v1.0.0")
        (self.author / "AGENTS.md").write_text("v2\n")
        self.push("rules v2")
        self.assertEqual(self.sync("--pin", "v1.0.0"), {})
        self.assertEqual(self.rules(), "v1\n")
        self.sync("--pin", "v1.0.0")
        self.assertEqual(self.rules(), "v1\n")
        self.assertTrue((self.home / ".claude/skills/one").is_symlink())

    def test_pin_moves_to_a_newer_tag_and_says_the_rules_changed(self):
        self.tag("v1.0.0")
        self.sync("--pin", "v1.0.0")
        (self.author / "AGENTS.md").write_text("v2\n")
        self.push("rules v2")
        self.tag("v1.1.0")
        out = self.sync("--pin", "v1.1.0")
        self.assertEqual(self.rules(), "v2\n")
        self.assertIn("AGENTS.md", out["hookSpecificOutput"]["additionalContext"])

    def test_missing_tag_warns_and_leaves_the_clone_alone(self):
        out = self.sync("--pin", "v9.9.9")
        self.assertIn("v9.9.9", out["systemMessage"])
        self.assertEqual(self.rules(), "v1\n")

    def test_pin_with_local_changes_warns_and_leaves_them(self):
        self.tag("v1.0.0")
        (self.author / "AGENTS.md").write_text("v2\n")
        self.push("rules v2")
        self.sync()
        (self.clone / "AGENTS.md").write_text("my edit\n")
        out = self.sync("--pin", "v1.0.0")
        self.assertIn("local changes", out["systemMessage"])
        self.assertEqual(self.rules(), "my edit\n")

    def test_back_to_main_after_a_pin(self):
        self.tag("v1.0.0")
        (self.author / "AGENTS.md").write_text("v2\n")
        self.push("rules v2")
        self.sync("--pin", "v1.0.0")
        self.sync("--main")
        self.assertEqual(self.rules(), "v2\n")

    def test_first_run_links_and_imports_silently(self):
        self.assertEqual(self.sync(), {})
        self.assertEqual((self.home / ".claude/skills/one").resolve(), self.clone / "skills/one")
        self.assertEqual((self.home / ".claude/agents/qa.md").resolve(), self.clone / "agents/qa.md")
        self.assertEqual((self.home / ".local/bin/layout-check").resolve(), self.clone / "tools/layout-check")
        self.assertEqual((self.home / ".claude/CLAUDE.md").read_text(), f"@{self.clone}/CLAUDE.md\n")

    def test_keeps_machine_notes_and_import_appears_once(self):
        (self.home / ".claude").mkdir()
        (self.home / ".claude/CLAUDE.md").write_text("my notes\n")
        self.sync()
        self.sync()
        self.assertEqual((self.home / ".claude/CLAUDE.md").read_text(), f"@{self.clone}/CLAUDE.md\nmy notes\n")

    def test_pulls_new_skill_and_prunes_removed_one(self):
        self.sync()
        shutil.rmtree(self.author / "skills/one")
        (self.author / "skills/two").mkdir()
        (self.author / "skills/two/SKILL.md").write_text("v1\n")
        self.push("swap")
        self.assertEqual(self.sync(), {})
        self.assertTrue((self.home / ".claude/skills/two/SKILL.md").exists())
        self.assertFalse((self.home / ".claude/skills/one").is_symlink())

    def test_rule_change_tells_the_session(self):
        self.sync()
        (self.author / "AGENTS.md").write_text("v2\n")
        self.push("rules")
        context = self.sync()["hookSpecificOutput"]["additionalContext"]
        self.assertIn(str(self.clone / "AGENTS.md"), context)

    def test_failed_pull_warns_and_still_links(self):
        (self.author / "AGENTS.md").write_text("v2\n")
        self.push("rules")
        (self.clone / "AGENTS.md").write_text("local edit\n")
        out = self.sync()
        self.assertIn("git pull failed", out["systemMessage"])
        self.assertTrue((self.home / ".claude/skills/one").is_symlink())
        self.assertEqual((self.clone / "AGENTS.md").read_text(), "local edit\n")

    def test_other_branch_is_left_alone(self):
        git(self.clone, "checkout", "-q", "-b", "work/x")
        self.assertIn("work/x", self.sync()["systemMessage"])

    def test_leaves_foreign_entries_alone(self):
        (self.home / ".claude/skills/one").mkdir(parents=True)
        (self.home / ".claude/skills/synced").mkdir()
        out = self.sync()
        self.assertIn("left alone", out["systemMessage"])
        self.assertTrue((self.home / ".claude/skills/one").is_dir())
        self.assertTrue((self.home / ".claude/skills/synced").is_dir())

    def test_leaves_a_foreign_link_alone_and_says_so(self):
        elsewhere = self.tmp / "someone-elses-skill"
        elsewhere.mkdir()
        (self.home / ".claude/skills").mkdir(parents=True)
        (self.home / ".claude/skills/one").symlink_to(elsewhere)
        out = self.sync()
        self.assertEqual((self.home / ".claude/skills/one").resolve(), elsewhere)
        self.assertIn("skills/one", out["systemMessage"])
        self.assertIn("not this library", out["systemMessage"])

    def test_leaves_an_existing_command_alone_and_says_so(self):
        bin_dir = self.home / ".local/bin"
        bin_dir.mkdir(parents=True)
        (bin_dir / "layout-check").write_text("#!/bin/sh\necho mine\n")
        out = self.sync()
        self.assertFalse((bin_dir / "layout-check").is_symlink())
        self.assertEqual((bin_dir / "layout-check").read_text(), "#!/bin/sh\necho mine\n")
        self.assertIn("layout-check", out["systemMessage"])


if __name__ == "__main__":
    unittest.main()
