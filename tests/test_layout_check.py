"""Tests for tools/layout-check and the spec/section agreement in tools/check.py (standard library only).

Each check is run against a deliberately broken copy and must fail with its own message; the template the
checker writes (--stub) must pass. Run: python3 -m unittest discover -s tests
"""
import importlib.machinery, importlib.util, json, pathlib, shutil, subprocess, sys, tempfile, unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
TOOL = ROOT / "tools" / "layout-check"


def run(*args, cwd=None):
    r = subprocess.run([sys.executable, str(TOOL), *map(str, args)], capture_output=True, text=True, cwd=cwd)
    return r.returncode, r.stdout


class Template:
    """A fresh git repo holding exactly what --stub writes (the template's content)."""

    def __init__(self, git=True):
        self.dir = pathlib.Path(tempfile.mkdtemp(prefix="layout-test-"))
        code, out = run("--stub", self.dir)
        assert code == 0, out
        if git:
            subprocess.run(["git", "init", "-q", str(self.dir)], check=True)
            subprocess.run(["git", "-C", str(self.dir), "add", "-A"], check=True)

    def __enter__(self):
        return self.dir

    def __exit__(self, *exc):
        shutil.rmtree(self.dir)


class LayoutCheck(unittest.TestCase):
    def test_template_passes(self):
        for git in (True, False):
            with Template(git) as d:
                code, out = run(d)
                self.assertEqual(code, 0, out)
                self.assertIn("follows the standard layout", out)

    def test_missing_readme_exact_message(self):
        with Template() as d:
            (d / "README.md").unlink()
            code, out = run(d)
            self.assertEqual(code, 1)
            self.assertIn("missing README.md: the start page; create it from the template\n", out)

    def test_each_required_file_fails_on_its_own(self):
        expected = {
            "README.md": "missing README.md: the start page; create it from the template",
            "AGENTS.md": "missing AGENTS.md: rules for AI agents; create it from the template",
            "CLAUDE.md": "missing CLAUDE.md: one line, @AGENTS.md; create it from the template",
            "docs/STATUS.md": "missing docs/STATUS.md: where things stand; create it from the template",
            "docs/DESIGN.md": "missing docs/DESIGN.md: how it works; create it from the template",
            "docs/DECISIONS.md": "missing docs/DECISIONS.md: what was decided and why; create it from the template",
            "docs/LESSONS.md": "missing docs/LESSONS.md: traps and corrected facts; create it from the template",
            "tools/check.sh": "missing tools/check.sh: runs every check CI runs; create it from the template",
            "tests/": "missing tests/: the tests; create it from the template",
        }
        for rel, message in expected.items():
            with self.subTest(rel), Template(git=False) as d:
                target = d / rel
                shutil.rmtree(target) if target.is_dir() else target.unlink()
                code, out = run(d)
                self.assertEqual(code, 1, out)
                self.assertIn(message + "\n", out)

    def test_fix_hint_fixes_missing_files(self):
        with Template(git=False) as d:
            (d / "docs" / "STATUS.md").unlink()
            code, out = run("--fix-hint", d)
            self.assertEqual(code, 1)
            fix = [l for l in out.splitlines() if l.startswith("  fix: ")][0][len("  fix: "):]
            self.assertTrue(fix.startswith("layout-check --stub "), fix)
            code, out = run(*fix.split()[1:])
            self.assertEqual(code, 0, out)
            self.assertEqual(run(d)[0], 0)

    def test_claude_md_must_be_the_import_line(self):
        with Template() as d:
            (d / "CLAUDE.md").write_text("# Rules\n\nDo things.\n")
            code, out = run(d)
            self.assertEqual(code, 1)
            self.assertIn("CLAUDE.md is not the one line @AGENTS.md", out)

    def test_folder_claude_md_needs_agents_md_beside_it(self):
        with Template() as d:
            (d / "tools" / "CLAUDE.md").write_text("@AGENTS.md\n")
            subprocess.run(["git", "-C", str(d), "add", "-A"], check=True)
            code, out = run(d)
            self.assertEqual(code, 1)
            self.assertIn("missing tools/AGENTS.md: the rules tools/CLAUDE.md imports", out)

    def test_agents_md_must_point_to_status(self):
        with Template() as d:
            (d / "AGENTS.md").write_text("# Agent rules\n\nBe good.\n")
            self.assertIn("AGENTS.md doesn't send agents to docs/STATUS.md", run(d)[1])

    def test_unlisted_top_level_folder(self):
        with Template() as d:
            (d / "game").mkdir()
            (d / "game" / "main.gd").write_text("extends Node\n")
            subprocess.run(["git", "-C", str(d), "add", "-A"], check=True)
            code, out = run(d)
            self.assertEqual(code, 1)
            self.assertIn("game/ is not in README.md's layout table", out)
            readme = d / "README.md"
            readme.write_text(readme.read_text().replace("|---|---|\n", "|---|---|\n| `game/` | The game |\n"))
            self.assertEqual(run(d)[0], 0, run(d)[1])

    def test_readme_sections(self):
        with Template() as d:
            readme = d / "README.md"
            readme.write_text(readme.read_text().replace("## When it breaks", "## Trouble"))
            self.assertIn('README.md has no "When it breaks" section', run(d)[1])

    def test_misplaced_status(self):
        with Template() as d:
            (d / "docs" / "STATUS.md").rename(d / "CURRENT_STATE.md")
            code, out = run("--fix-hint", d)
            self.assertEqual(code, 1)
            self.assertIn("misplaced CURRENT_STATE.md: it goes in docs/STATUS.md", out)
            self.assertIn("mv CURRENT_STATE.md docs/STATUS.md", out)
            self.assertNotIn("missing docs/STATUS.md", out)

    def test_logs_and_scratch_even_when_ignored(self):
        for name in ("build.log", "scratchpad"):
            with self.subTest(name), Template() as d:
                (d / ".gitignore").write_text((d / ".gitignore").read_text() + name + "\n")
                p = d / name
                p.mkdir() if name == "scratchpad" else p.write_text("x\n")
                code, out = run(d)
                self.assertEqual(code, 1)
                self.assertIn(f"{name} doesn't belong in a repo", out)

    def test_env_only_when_tracked(self):
        with Template() as d:
            (d / ".env").write_text("TOKEN=x\n")
            self.assertEqual(run(d)[0], 0)  # ignored by the template's .gitignore: allowed
            subprocess.run(["git", "-C", str(d), "add", "-f", ".env"], check=True)
            self.assertIn(".env doesn't belong in a repo: secrets", run(d)[1])

    def test_names(self):
        cases = {
            "docs/lore.md": "docs/lore.md should be CAPITALS",
            "docs/runbooks/Restore_Backup.md": "docs/runbooks/Restore_Backup.md should be lowercase-with-dashes",
            "docs/notes/a.md": "docs/notes/ is not a docs folder the layout knows",
            "docs/evidence/oct-8/a.txt": "docs/evidence/oct-8/ should be named YYYY-MM-DD",
        }
        for rel, message in cases.items():
            with self.subTest(rel), Template(git=False) as d:
                (d / rel).parent.mkdir(parents=True, exist_ok=True)
                (d / rel).write_text("x\n")
                code, out = run(d)
                self.assertEqual(code, 1, out)
                self.assertIn(message, out)
        with Template(git=False) as d:
            (d / "docs" / "evidence" / "2026-10-08").mkdir(parents=True)
            (d / "docs" / "runbooks" / "restore-backup.md").write_text("x\n")
            (d / "docs" / "LORE.md").write_text("x\n")
            self.assertEqual(run(d)[0], 0, run(d)[1])

    def test_exceptions_file(self):
        with Template() as d:
            (d / "build.log").write_text("x\n")
            (d / ".layout-check").write_text("allow build.log: test fixture\n")
            self.assertEqual(run(d)[0], 0, run(d)[1])
            (d / ".layout-check").write_text("allow build.log\n")
            self.assertIn(".layout-check line 1 is not 'allow <path>: <reason>'", run(d)[1])

    def test_todo_must_cite_an_issue(self):
        tag = "TO" + "DO"  # spelled apart so this file doesn't trip the check it tests
        with Template() as d:
            (d / "tools" / "a.py").write_text(f"x = 1\n# {tag}: page the logs\n")
            subprocess.run(["git", "-C", str(d), "add", "-A"], check=True)
            code, out = run(d)
            self.assertEqual(code, 1)
            self.assertIn("tools/a.py:2 has a TODO or FIXME that cites no issue", out)
            (d / "tools" / "a.py").write_text(f"x = 1\n# {tag}(#12): page the logs\n# a {tag} in prose\n")
            self.assertEqual(run(d)[0], 0, run(d)[1])

    def test_only_tracked_files_are_checked_in_a_checkout(self):
        with Template() as d:
            (d / "tools" / "b.py").write_text("# FIX" + "ME later\n")
            self.assertEqual(run(d)[0], 0, run(d)[1])  # not committed yet: CI sees what is tracked
            subprocess.run(["git", "-C", str(d), "add", "-A"], check=True)
            self.assertIn("tools/b.py:1 has a TODO or FIXME that cites no issue", run(d)[1])

    def test_status_keeps_no_task_list(self):
        with Template() as d:
            (d / "docs" / "STATUS.md").write_text("# Status\n\nNext: milestone M2 (#4).\n- [ ] add passkeys\n")
            subprocess.run(["git", "-C", str(d), "add", "-A"], check=True)
            code, out = run(d)
            self.assertEqual(code, 1)
            self.assertIn("docs/STATUS.md:4 is a task list item", out)
            (d / "docs" / "STATUS.md").write_text("# Status\n\nNext: milestone M2 (#4).\n- [x] done item\n")
            self.assertEqual(run(d)[0], 0, run(d)[1])

    def test_bad_usage_exits_2(self):
        self.assertEqual(run("/nonexistent/path")[0], 2)
        self.assertEqual(run("--no-such-flag")[0], 2)

    def test_the_library_follows_the_layout(self):
        code, out = run(ROOT)
        self.assertEqual(code, 0, out)


class Forms(unittest.TestCase):
    """The second allowed forms (docs/decisions/, docs/status.d/): rejected unless .layout-check selects them, and
    then checked their own way. Each case fails if the form is wrongly accepted or wrongly rejected."""

    DECISIONS = "form decision-files: one file per decision\n"
    STATUS = "form status-entries: one entry per branch\n"

    def per_file(self, d, layout_check):
        """d shaped like a repo using both forms, with the given .layout-check."""
        (d / "docs" / "decisions").mkdir()
        (d / "docs" / "decisions" / "D001.md").write_text("# D1 - x (2026-10-21)\n")
        (d / "docs" / "decisions" / "D114.md").write_text("# D114 - y (2026-10-21)\n")
        (d / "docs" / "DECISIONS.md").write_text("# Decisions\n\nOne file each in [decisions/](decisions/).\n")
        (d / "docs" / "status.d").mkdir()
        (d / "docs" / "status.d" / "README.md").write_text("# Branch entries\n\n- [ ] the format, as an example\n")
        (d / "docs" / "status.d" / "work-x.md").write_text("**2026-10-21: branch `work/work-x`:** did x.\n")
        (d / ".layout-check").write_text(layout_check)

    def test_both_forms_selected_pass(self):
        with Template(git=False) as d:
            self.per_file(d, self.DECISIONS + self.STATUS)
            self.assertEqual(run(d), (0, f"layout-check: {d.resolve()} follows the standard layout\n"))

    def test_folder_without_its_form_line_fails(self):
        for line, folder in ((self.STATUS, "decisions"), (self.DECISIONS, "status.d")):
            with self.subTest(folder), Template(git=False) as d:
                self.per_file(d, line)  # selects only the other form
                code, out = run(d)
                self.assertEqual(code, 1, out)
                self.assertIn(f"docs/{folder}/ is not a docs folder the layout knows", out)

    def test_selected_form_without_its_folder_fails(self):
        for line, folder in ((self.DECISIONS, "docs/decisions/"), (self.STATUS, "docs/status.d/")):
            with self.subTest(folder), Template(git=False) as d:
                (d / ".layout-check").write_text(line)
                code, out = run(d)
                self.assertEqual(code, 1, out)
                self.assertIn(f"missing {folder}: .layout-check selects form", out)

    def test_misnamed_files_fail(self):
        cases = {"docs/decisions/D7.md": "form decision-files's files: Dnnn.md",
                 "docs/decisions/notes.md": "form decision-files's files",
                 "docs/decisions/old/D002.md": "docs/decisions/old is not named like",
                 "docs/status.d/Work_X.md": "form status-entries's files: <slug>.md",
                 "docs/status.d/x.txt": "form status-entries's files"}
        for rel, message in cases.items():
            with self.subTest(rel), Template(git=False) as d:
                self.per_file(d, self.DECISIONS + self.STATUS)
                (d / rel).parent.mkdir(parents=True, exist_ok=True)
                (d / rel).write_text("x\n")
                code, out = run(d)
                self.assertEqual(code, 1, out)
                self.assertIn(message, out)

    def test_decisions_page_must_point_to_the_folder(self):
        with Template(git=False) as d:
            self.per_file(d, self.DECISIONS + self.STATUS)
            (d / "docs" / "DECISIONS.md").write_text("# Decisions\n\n## D1 - x\n")
            code, out = run(d)
            self.assertEqual(code, 1, out)
            self.assertIn("docs/DECISIONS.md doesn't point to docs/decisions/", out)

    def test_status_entries_need_their_readme(self):
        with Template(git=False) as d:
            self.per_file(d, self.DECISIONS + self.STATUS)
            (d / "docs" / "status.d" / "README.md").unlink()
            code, out = run(d)
            self.assertEqual(code, 1, out)
            self.assertIn("missing docs/status.d/README.md", out)

    def test_status_entry_keeps_no_task_list(self):
        with Template(git=False) as d:
            self.per_file(d, self.DECISIONS + self.STATUS)
            (d / "docs" / "status.d" / "work-x.md").write_text("**2026-10-21: branch `work/work-x`:** x.\n- [ ] y\n")
            code, out = run(d)
            self.assertEqual(code, 1, out)
            self.assertIn("docs/status.d/work-x.md:2 is a task list item", out)

    def test_unknown_form_fails(self):
        with Template(git=False) as d:
            self.per_file(d, self.DECISIONS + self.STATUS + "form decision-folder: a typo\n")
            code, out = run(d)
            self.assertEqual(code, 1, out)
            self.assertIn(".layout-check line 3: no form named decision-folder", out)

    def test_each_form_line_in_the_spec_selects_its_form(self):
        spec = json.loads((ROOT / "tools" / "repo-layout.json").read_text())
        with Template(git=False) as d:
            self.per_file(d, spec["forms"]["decision-files"]["line"] + "\n" + spec["forms"]["status-entries"]["line"])
            self.assertEqual(run(d)[0], 0, run(d)[1])


class SpecAgreesWithSection(unittest.TestCase):
    """tools/check.py fails when durable-knowledge's "Repo layout" and tools/repo-layout.json disagree."""

    def check_copy(self, edit):
        with tempfile.TemporaryDirectory() as tmp:
            copy = pathlib.Path(tmp) / "lib"
            shutil.copytree(ROOT, copy, ignore=shutil.ignore_patterns(".git", "__pycache__"))
            edit(copy)
            r = subprocess.run([sys.executable, str(copy / "tools" / "check.py")], capture_output=True, text=True)
            return r.returncode, r.stdout

    def test_clean_copy_passes(self):
        self.assertEqual(self.check_copy(lambda c: None)[0], 0)

    def test_tree_line_changed_in_section(self):
        def edit(c):
            p = c / "skills" / "durable-knowledge" / "SKILL.md"
            p.write_text(p.read_text().replace("  LESSONS.md     Traps and corrected facts", "  LESSONS.md     Gotchas"))
        code, out = self.check_copy(edit)
        self.assertEqual(code, 1)
        self.assertIn("its tree differs from tools/repo-layout.json", out)

    def test_entry_changed_in_spec(self):
        def edit(c):
            p = c / "tools" / "repo-layout.json"
            p.write_text(p.read_text().replace('"tests/"', '"test/"', 1))
        code, out = self.check_copy(edit)
        self.assertEqual(code, 1)
        self.assertIn("its tree differs from tools/repo-layout.json", out)

    def test_question_changed(self):
        def edit(c):
            p = c / "tools" / "repo-layout.json"
            p.write_text(p.read_text().replace('"How does it work?"', '"How is it built?"'))
        code, out = self.check_copy(edit)
        self.assertEqual(code, 1)
        self.assertIn("four-questions table differs", out)

    def test_form_line_changed_in_spec(self):
        def edit(c):
            p = c / "tools" / "repo-layout.json"
            p.write_text(p.read_text().replace('"line": "form status-entries: one entry per branch',
                                               '"line": "form status-entries: an entry per branch'))
        code, out = self.check_copy(edit)
        self.assertEqual(code, 1)
        self.assertIn("doesn't give form status-entries's .layout-check line", out)

    def test_forbidden_name_missing_from_section(self):
        def edit(c):
            p = c / "tools" / "repo-layout.json"
            p.write_text(p.read_text().replace('"pattern": "scratch*"', '"pattern": "tmp*"'))
        code, out = self.check_copy(edit)
        self.assertEqual(code, 1)
        self.assertIn("doesn't name `tmp*`", out)


if __name__ == "__main__":
    unittest.main()
