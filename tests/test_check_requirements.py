"""Tests for tools/check_requirements.py (standard library only).

The real library must pass; each deliberately broken copy must fail naming the requirement, tag or core line it
broke (a local-agent rule dropped from tools/gen_local_agents.py, an overlong core line).
Run: python3 -m unittest discover -s tests
"""
import pathlib, shutil, subprocess, sys, tempfile, unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
TOOL = ROOT / "tools" / "check_requirements.py"


def run(root):
    r = subprocess.run([sys.executable, str(TOOL), str(root)], capture_output=True, text=True)
    return r.returncode, r.stdout


class Copy:
    """The files the checker reads, copied to a scratch folder so a test can break one."""

    def __enter__(self):
        self.dir = pathlib.Path(tempfile.mkdtemp(prefix="requirements-test-"))
        shutil.copy(ROOT / "AGENTS.md", self.dir)
        shutil.copytree(ROOT / "agents", self.dir / "agents")
        shutil.copytree(ROOT / "skills", self.dir / "skills")
        (self.dir / "tools").mkdir()
        shutil.copy(ROOT / "tools" / "gen_local_agents.py", self.dir / "tools")
        (self.dir / "docs").mkdir()
        for name in ("REQUIREMENTS.tsv", "DECISIONS.md"):
            shutil.copy(ROOT / "docs" / name, self.dir / "docs")
        return self

    def __exit__(self, *exc):
        shutil.rmtree(self.dir)

    def edit(self, rel, old, new):
        path = self.dir / rel
        text = path.read_text()
        assert old in text, (rel, old)
        path.write_text(text.replace(old, new, 1))


class CheckRequirements(unittest.TestCase):
    def test_library_passes(self):
        code, out = run(ROOT)
        self.assertEqual(code, 0, out)

    def test_deleted_requirement_fails_naming_it(self):
        with Copy() as c:
            c.edit("agents/qa.md", "- Don't write files in the repo: your report is your final message.\n", "")
            code, out = run(c.dir)
        self.assertEqual(code, 1)
        self.assertIn("Q12 (agents/qa.md): requirement missing", out)

    def test_rewrapped_line_still_passes(self):
        with Copy() as c:
            c.edit("agents/qa.md", "your report is your final message.", "your report is\n  your final message.")
            self.assertEqual(run(c.dir)[0], 0)

    def test_dropped_quote_fails_naming_the_rule(self):
        with Copy() as c:
            c.edit("docs/REQUIREMENTS.tsv", "just make sure the ops agent knows we never reduce quality\t", "\t")
            code, out = run(c.dir)
        self.assertEqual(code, 1)
        self.assertIn("S02 (agents/team-ops.md): tag (owner, 2026-10-05) has no quote", out)

    def test_tag_without_a_row_fails(self):
        with Copy() as c:
            c.edit("agents/writer.md", "  conflict.", "  conflict (owner, 2026-10-01).")
            code, out = run(c.dir)
        self.assertEqual(code, 1)
        self.assertRegex(out, r"agents/writer\.md:\d+: source tag \(owner, 2026-10-01\) has no row with its quote")

    def test_decision_tag_without_a_row_fails(self):
        with Copy() as c:
            c.edit("agents/writer.md", "  conflict.", "  conflict (D3).")
            code, out = run(c.dir)
        self.assertEqual(code, 1)
        self.assertRegex(out, r"agents/writer\.md:\d+: source tag \(D3\) has no row")

    def test_quote_left_inline_fails(self):
        with Copy() as c:
            c.edit("agents/team-ops.md", "(owner, 2026-10-05).",
                   "(owner, 2026-10-05: \"just make sure the ops agent knows we never reduce quality\").")
            code, out = run(c.dir)
        self.assertEqual(code, 1)
        self.assertIn("S02: its quote is still inline in agents/team-ops.md", out)

    def test_decision_without_its_quote_fails(self):
        with Copy() as c:
            c.edit("docs/DECISIONS.md", "yes, add the stop and report rule", "(cut)")
            code, out = run(c.dir)
        self.assertEqual(code, 1)
        self.assertIn("A26: D11 in docs/DECISIONS.md lacks the quote verbatim", out)

    def test_local_agent_rule_dropped_from_the_generator_fails(self):
        with Copy() as c:
            c.edit("tools/gen_local_agents.py", '"local-agent", "local-agent@forge.local"', '"agent", "a@b"')
            code, out = run(c.dir)
        self.assertEqual(code, 1)
        self.assertIn("L01 (tools/gen_local_agents.py): requirement missing", out)

    def test_overlong_core_line_fails(self):
        with Copy() as c:
            c.edit("docs/REQUIREMENTS.tsv", "\tNever merge, push or touch another branch.\tdeveloper\n",
                   "\tNever merge, push or touch another branch." + " Really." * 30 + "\tdeveloper\n")
            code, out = run(c.dir)
        self.assertEqual(code, 1)
        self.assertIn("V24: core line has stray whitespace or is over 200 characters", out)

    def test_role_rule_scoped_to_all_or_another_role_fails(self):
        for scope, says in (("all", "V24: scoped to all, but it comes from agents/developer.md"),
                            ("qa", "V24: scoped to qa (agents/qa.md), but it comes from agents/developer.md"),
                            ("", "V24: a core line needs a scope")):
            with Copy() as c:
                c.edit("docs/REQUIREMENTS.tsv", "\tNever merge, push or touch another branch.\tdeveloper\n",
                       f"\tNever merge, push or touch another branch.\t{scope}\n")
                code, out = run(c.dir)
            self.assertEqual(code, 1, scope)
            self.assertIn(says, out)

    def test_shared_rule_from_a_skill_is_checked(self):
        with Copy() as c:
            c.edit("skills/agent-team/SKILL.md", "everything else is read-only.", "the rest too.")
            code, out = run(c.dir)
        self.assertEqual(code, 1)
        self.assertIn("G01 (skills/agent-team/SKILL.md): requirement missing", out)


if __name__ == "__main__":
    unittest.main()
