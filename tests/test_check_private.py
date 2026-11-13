"""tools/check_private.py fails on each kind of personal detail and passes a clean tree."""
import pathlib
import subprocess
import sys
import tempfile
import unittest

TOOL = pathlib.Path(__file__).resolve().parent.parent / "tools" / "check_private.py"


def run(files, terms=None):
    with tempfile.TemporaryDirectory() as d:
        root = pathlib.Path(d)
        subprocess.run(["git", "init", "-q", str(root)], check=True)
        for name, text in files.items():
            (root / name).write_text(text, encoding="utf-8")
        if terms is not None:
            (root / ".private-terms").write_text(terms, encoding="utf-8")
        subprocess.run(["git", "-C", str(root), "add", *files], check=True)
        return subprocess.run([sys.executable, str(TOOL), str(root)], capture_output=True, text=True)


class CheckPrivate(unittest.TestCase):
    def test_clean_tree_passes(self):
        r = run({"a.md": "Mail t@example.invalid, path /path/to/repo, 127.0.0.1, ~/.claude.\n"})
        self.assertEqual(r.returncode, 0, r.stdout)

    def test_each_generic_kind_fails_and_hides_the_match(self):
        # Assembled at runtime, so this file matches no pattern and needs no exemption.
        at, ip, home, users = "@", "192." + "168.1.20", "/" + "home/jo/dev", "C:" + r"\Users\Jo\repo"
        for kind, text in (("email", "ask jo" + at + "mail.example.net"), ("private IP", "ssh " + ip),
                           ("home path", "cd " + home), ("home path", users)):
            r = run({"a.md": text + "\n"})
            self.assertEqual(r.returncode, 1, kind)
            self.assertIn(f"a.md:1: {kind}", r.stdout)
            self.assertNotIn(text.split()[-1], r.stdout)

    def test_local_terms_fail_and_lookaheads_allow_exceptions(self):
        self.assertEqual(run({"a.md": "Secret Project X\n"}, "secret project\n").returncode, 1)
        self.assertEqual(run({"a.md": "Ada Lovelace\n"}, "ada(?! lovelace)\n").returncode, 0)

    def test_report_says_whether_local_terms_loaded(self):
        self.assertIn("no .private-terms here", run({"a.md": "plain\n"}).stdout)
        self.assertIn("with local .private-terms", run({"a.md": "plain\n"}, "nothing\n").stdout)


if __name__ == "__main__":
    unittest.main()
