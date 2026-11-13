"""tools/check.py's candidate rules: each entry is checked alone, needs a real date and a Target, and expires."""
import pathlib
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
GOOD = "- **{d}, web-app - A headline.** The fact. Target: ground-truth."


def run_with(candidates_body):
    with tempfile.TemporaryDirectory() as d:
        dest = pathlib.Path(d) / "lib"
        files = subprocess.run(["git", "-C", str(ROOT), "ls-files"], capture_output=True, text=True,
                               check=True).stdout.splitlines()
        for f in files:
            (dest / f).parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(ROOT / f, dest / f)
        head = (ROOT / "docs/CANDIDATES.md").read_text().split("\nFormat:", 1)[0]
        fmt = "\nFormat: `- **YYYY-MM-DD, <project kind> - Headline.** The fact. Target: <skill>.`\n\n"
        (dest / "docs/CANDIDATES.md").write_text(head + fmt + candidates_body + "\n")
        r = subprocess.run([sys.executable, str(dest / "tools/check.py")], capture_output=True, text=True)
        return [l for l in r.stdout.splitlines() if l.startswith("docs/CANDIDATES.md")]


class Candidates(unittest.TestCase):
    def test_valid_entries_pass(self):
        self.assertEqual(run_with(GOOD.format(d="2099-01-01") + "\n" + GOOD.format(d="2099-01-02")), [])

    def test_undated_heading_fails(self):
        out = run_with(GOOD.format(d="2099-01-01") + "\n## An old-style heading\nIts text. Target: ground-truth.")
        self.assertEqual(len(out), 1, out)
        self.assertIn("doesn't match the format", out[0])

    def test_malformed_entry_between_valid_ones_fails(self):
        body = "\n".join([GOOD.format(d="2099-01-01"), "- a loose note with no date or target",
                          GOOD.format(d="2099-01-02")])
        out = run_with(body)
        self.assertEqual(len(out), 1, out)
        self.assertIn("a loose note", out[0])

    def test_impossible_date_fails(self):
        self.assertEqual(len(run_with(GOOD.format(d="2099-13-40"))), 1)

    def test_expired_candidate_fails(self):
        out = run_with(GOOD.format(d="2000-01-01"))
        self.assertEqual(len(out), 1, out)
        self.assertIn("older than", out[0])

    def test_over_the_cap_fails(self):
        out = run_with("\n".join(GOOD.format(d=f"2099-01-{i:02d}") for i in range(1, 32)))
        self.assertTrue(any("31 entries" in l for l in out), out)


if __name__ == "__main__":
    unittest.main()
