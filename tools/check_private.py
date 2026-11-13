#!/usr/bin/env python3
"""Fails if a tracked file matches a configured pattern: an email address, a private IP, a home-folder path, or a
line of the git-ignored `.private-terms` (one regex per line: your names, projects, employer, hostnames). A pass means
only that no pattern matched; a personal workflow or a recognisable incident can match none, so admission still
needs a reader (durable-knowledge, "Feeding the library").

Usage: python3 tools/check_private.py [repo]   (exit 1 and one line per hit, or exit 0)
"""
import pathlib
import re
import subprocess
import sys

GENERIC = {
    "email": r"\b[\w.+-]+@(?!example\.(?:com|org)\b)(?!users\.noreply\.github\.com\b)(?!forge\.local\b)[\w-]+(?:\.[\w-]+)*\.(?!invalid\b|test\b|example\b|local\b)[a-z]{2,}\b",
    "private IP": r"\b(?:10|192\.168|172\.(?:1[6-9]|2\d|3[01]))(?:\.\d{1,3}){2,3}\b",
    "home path": r"(?<![\w/])(?:/home/|/Users/|[A-Za-z]:[\\/]Users[\\/])(?!<|\$|you\b|me\b|USER\b|name\b)[A-Za-z][\w.-]+",
}


def patterns(root):
    pats = dict(GENERIC)
    extra = root / ".private-terms"
    if extra.exists():
        for i, line in enumerate(extra.read_text(encoding="utf-8").splitlines(), 1):
            if line.strip() and not line.startswith("#"):
                pats[f".private-terms:{i}"] = line.strip()
    return {k: re.compile(v, 0 if k in GENERIC else re.I) for k, v in pats.items()}


def hits(root):
    files = subprocess.run(["git", "-C", str(root), "ls-files"], capture_output=True, text=True,
                           check=True).stdout.splitlines()
    pats = patterns(root)
    for f in files:
        try:
            text = (root / f).read_text(encoding="utf-8")
        except (UnicodeDecodeError, FileNotFoundError, IsADirectoryError):
            continue
        for n, line in enumerate(text.splitlines(), 1):
            for name, rx in pats.items():
                if rx.search(line):
                    yield f"{f}:{n}: {name}"


def main():
    root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    local = (root / ".private-terms").exists()
    found = list(hits(root))
    for h in found:
        print(h)  # names the pattern, never the matched text
    terms = "with local .private-terms" if local else "generic patterns only; no .private-terms here"
    print(f"private: {len(found)} pattern match(es), {terms}" if found else f"private: no configured pattern matches ({terms})")
    return 1 if found else 0


if __name__ == "__main__":
    sys.exit(main())
