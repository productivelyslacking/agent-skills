#!/usr/bin/env python3
"""Tests for tools/gen_local_agents.py (standard library only). Run: python3 -m unittest discover -s tests

- the rule sheet is found in both library layouts, and a dangling or empty one stops the generator;
- every generated role and the rule-sheet wrapper start with the Claude-features preamble, word for word;
- a Claude-specific term in the library is printed by --check (one plant per kind), not failed; stale output fails;
- --install then --uninstall leaves a HOME byte-identical (empty, with the user's own settings, and with a CRLF +
  BOM settings file), a conflicting user value or a JSONC file stops the install with nothing changed, and an
  install from before the manifest is refused until --uninstall removes it;
- a rerun (--sync, what the hooks run) never overwrites what the user changed after the install (a settings key,
  an item removed from a list, a link, SKILLS.md) and never touches keys it doesn't own; --uninstall leaves them;
- a run killed at each point (journal, each change, mid-write, manifest) of --install, --sync and --uninstall:
  settings.json is never empty or partial, the next run finishes it, and --uninstall then restores HOME exactly;
- two runs at once take turns on the lock;
- with the hooks installed, a pull that adds a skill updates ~/.qwen/SKILLS.md; without them it goes stale; the
  clone's own hooks still run, and --uninstall-hooks restores .git/hooks and .git/config byte for byte;
- the core sheet is the `core` cells of docs/REQUIREMENTS.tsv scoped to `all`, each tagged with its row, and only
  rules from a source every role reads (AGENTS.md, a skill, the generator); each core-mode role carries the core
  lines scoped to it and none scoped to another; every core-mode file carries the L01 identity line, so a role's
  "the project's identity" is overridden, and its sources' git blob hashes; editing a cell makes it
  stale and marking rows past the budget fails --check; it is within 450 tokens by the endpoint's tokenizer when
  that answers (else by the estimate, said in the output), and the estimate never counts lower than the endpoint;
- --rules core installs the core sheet and roles, is recorded and kept by --sync, and switching back and
  uninstalling leaves HOME byte-identical; a real Qwen Code run against a scripted model sends the core sheet in
  its prompt under core and the full sheet under full (skipped where `qwen` isn't installed);
- the OpenCode roles carry only v2 frontmatter (a subagent, a hex colour, permissions that deny all first), allow
  exactly what their tools map to and nothing disallowed, and an unmapped colour stops the generator.
"""
import base64, hashlib, http.server, json, os, pathlib, shutil, stat, subprocess, sys, tempfile, threading, unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import gen_local_agents as g

RULES = "# Working rules\n\n1. **Write it down.** In a named home.\n"


def library(tmp, files):
    """A minimal library: one skill, the real qa role, and the given top-level files."""
    root = pathlib.Path(tmp)
    (root / "skills" / "ground-truth").mkdir(parents=True)
    (root / "skills" / "ground-truth" / "SKILL.md").write_text(
        "---\nname: ground-truth\ndescription: The general working discipline, for any project at all.\n---\nBody.\n")
    (root / "agents").mkdir()
    shutil.copy(ROOT / "agents" / "qa.md", root / "agents" / "qa.md")
    (root / "docs").mkdir()
    (root / "docs" / "REQUIREMENTS.tsv").write_text(
        "id\tfile\tcore\tscope\nA01\tAGENTS.md\tWrite it down.\tall\n"
        "L01\ttools/gen_local_agents.py\tCommit as local-agent <local-agent@forge.local>; never as the user.\tall\n")
    for name, text in files.items():
        (root / name).write_text(text)
    return root


def copy_library(dest):
    """The real library's working tree (what git tracks plus local changes), without .git."""
    dest.mkdir(parents=True, exist_ok=True)
    for name in ("AGENTS.md", "CLAUDE.md", "skills", "agents", "tools", "local-agents"):
        src = ROOT / name
        (shutil.copytree if src.is_dir() else shutil.copy)(src, dest / name)
    (dest / "docs").mkdir()
    shutil.copy(ROOT / "docs" / "REQUIREMENTS.tsv", dest / "docs")
    shutil.rmtree(dest / "tools" / "__pycache__", ignore_errors=True)
    return dest


def snapshot(home):
    """Every entry under home: type, link target or mode and content hash."""
    out = []
    for dirpath, dirs, files in os.walk(home):
        for name in sorted(dirs + files):
            p = pathlib.Path(dirpath) / name
            rel = str(p.relative_to(home))
            if p.is_symlink():
                out.append((rel, "l", os.readlink(p)))
            elif p.is_dir():
                out.append((rel, "d", oct(p.stat().st_mode)))
            else:
                out.append((rel, "f", oct(p.stat().st_mode), hashlib.sha256(p.read_bytes()).hexdigest()))
    return sorted(out)


def gen(root, home, *args):
    env = dict(os.environ, HOME=str(home))
    return subprocess.run([sys.executable, str(root / "tools" / "gen_local_agents.py"), *args],
                          capture_output=True, text=True, env=env, cwd=root)


def make_home(tmp):
    home = pathlib.Path(tmp) / "home"
    (home / ".claude").mkdir(parents=True)
    (home / ".claude" / "CLAUDE.md").write_text("@/somewhere/CLAUDE.md\n\nMachine facts.\n")
    return home


class RulesFile(unittest.TestCase):
    def rules(self, files):
        with tempfile.TemporaryDirectory() as tmp:
            root = library(tmp, files)
            path = g.rules_file(root)
            return path.name, path.read_text()

    def test_rules_in_claude_md(self):
        self.assertEqual(self.rules({"CLAUDE.md": RULES}), ("CLAUDE.md", RULES))

    def test_claude_md_imports_agents_md(self):
        self.assertEqual(self.rules({"CLAUDE.md": "@AGENTS.md\n", "AGENTS.md": RULES}), ("AGENTS.md", RULES))

    def test_both_layouts_same_rules_text(self):
        self.assertEqual(self.rules({"CLAUDE.md": RULES})[1],
                         self.rules({"CLAUDE.md": "@AGENTS.md\n", "AGENTS.md": RULES})[1])

    def test_import_of_missing_agents_md_stops(self):
        with self.assertRaises(SystemExit) as e:
            self.rules({"CLAUDE.md": "@AGENTS.md\n"})
        self.assertIn("imports AGENTS.md, which doesn't exist", str(e.exception.code))

    def test_empty_rule_sheet_stops(self):
        with self.assertRaises(SystemExit) as e:
            self.rules({"CLAUDE.md": "@AGENTS.md\n", "AGENTS.md": "\n"})
        self.assertIn("the rule sheet is empty", str(e.exception.code))


class Terms(unittest.TestCase):
    """The term scan is a report printed by --check, not a gate (producer, 2026-10-08): PREAMBLE covers the class."""

    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.root = copy_library(pathlib.Path(self.tmp))

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def report_line(self, out, rel):
        return next((l for l in out.splitlines() if l.startswith(f"terms: {rel}: ")), "")

    def test_real_library_check_is_ok_and_reports(self):
        r = gen(ROOT, self.tmp, "--check")
        self.assertEqual(r.returncode, 0, r.stdout)
        self.assertIn("claude-md", self.report_line(r.stdout, "AGENTS.md"))

    # One plant per kind of Claude-only text, each in a skill, then the generator rerun (LOCAL-TOOLS.md lists where
    # each term appears, so it changes): --check prints the hit with its term id and passes.
    PLANTS = {
        "claude-tool": "Hand the result back with SendMessage.",
        "scratchpad": "Keep notes in the session scratchpad.",
        "claude-env": "Set CLAUDE_CODE_MAX_TURNS=5 first.",
        "claude-other": "If unsure, ask Claude.",
        "plan-mode": "Start in plan mode.",
        "slash-command": "Run /compact when it gets long.",
        "model-name": "Use model: opus for this.",
        "mcp": "The servers are in .mcp.json.",
    }

    def test_planted_term_is_printed_not_failed(self):
        skill = self.root / "skills" / "ground-truth" / "SKILL.md"
        clean = skill.read_text()
        before = self.report_line(gen(self.root, self.tmp, "--check").stdout, "skills/ground-truth/SKILL.md")
        for tid, line in self.PLANTS.items():
            with self.subTest(tid):
                self.assertNotIn(f"{tid} ", before + ",")
                skill.write_text(clean + "\n" + line + "\n")
                self.assertEqual(gen(self.root, self.tmp).returncode, 0)
                r = gen(self.root, self.tmp, "--check")
                self.assertEqual(r.returncode, 0, r.stdout)
                self.assertIn(f"{tid} 1", self.report_line(r.stdout, "skills/ground-truth/SKILL.md"), r.stdout)
        skill.write_text(clean)

    def test_plant_in_a_role_description_is_reported(self):
        role = self.root / "agents" / "qa.md"
        role.write_text(role.read_text().replace("description: ", "description: Ask Claude first. ", 1))
        self.assertTrue(any(l.startswith("terms: agents/qa.md: ") and "claude-other 1" in l
                            for l in g.term_report(self.root)))

    def test_stale_output_still_fails(self):
        role = self.root / "agents" / "qa.md"
        role.write_text(role.read_text() + "\nA new line.\n")
        r = gen(self.root, self.tmp, "--check")
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("local-agents/qwen/agents/qa.md: stale", r.stdout)

    def test_every_mention_of_claude_is_counted(self):
        """Each case-insensitive 'claude' or 'anthropic' in the scanned text is inside some term's match or counted
        as claude-other, so the report misses none."""
        import re
        found = g.scan(ROOT)
        for path in g.scanned(ROOT):
            rel = str(path.relative_to(ROOT))
            text = g.agent_text(path) if rel.startswith("agents/") else path.read_text()
            spans = [m.span() for _, pat, _ in g.TERMS if pat for m in re.finditer(pat, text)]
            uncovered = [m for m in re.finditer(g.CATCH_ALL, text) if not any(a <= m.start() < b for a, b in spans)]
            self.assertEqual(len(uncovered), found["claude-other"].get(rel, 0), rel)


# The preamble, word for word as the producer wrote it (2026-10-08); a change to it fails here on purpose.
PREAMBLE = ("Some instructions below mention Claude Code features (its tools such as Agent, Skill, SendMessage, plan "
            "mode, slash commands, scratchpad, permission prompts or settings) that don't exist here. Ignore those "
            "parts and use your own tools; when an instruction depends on one, say so in your hand-back.")


def first_paragraph(text):
    """The first text a model reads in a generated file: after the frontmatter and the provenance comment."""
    import re
    text = re.sub(r"\A---\n.*?\n---\n", "", text, flags=re.S)
    text = re.sub(r"\A<!--.*?-->\n", "", text, flags=re.S)
    return text.split("\n\n", 1)[0]


class Preamble(unittest.TestCase):
    def test_every_generated_role_and_the_rules_wrapper_start_with_it(self):
        out = g.generate(ROOT)
        for tool in ("qwen", "opencode"):
            roles = [rel for rel in out if rel.startswith(f"local-agents/{tool}/agents/")]
            self.assertEqual(len(roles), len(list((ROOT / "agents").glob("*.md"))))
        roles = [rel for rel in out if "/agents/" in rel]
        for rel in roles + ["local-agents/qwen/AGENTS.md", "local-agents/opencode/AGENTS.md"]:
            with self.subTest(rel):
                self.assertEqual(first_paragraph(out[rel]), PREAMBLE)
                self.assertEqual(first_paragraph((ROOT / rel).read_text()), PREAMBLE)  # the committed copy

    def test_wrapper_carries_the_whole_rule_sheet(self):
        self.assertTrue(g.generate(ROOT)["local-agents/qwen/AGENTS.md"].endswith(g.rules_file(ROOT).read_text()))

    def test_installed_rule_sheet_starts_with_it(self):
        with tempfile.TemporaryDirectory() as tmp:
            root, home = copy_library(pathlib.Path(tmp) / "lib"), make_home(tmp)
            self.assertEqual(gen(root, home, "--install").returncode, 0)
            self.assertEqual(first_paragraph((home / ".qwen" / "AGENTS.md").read_text()), PREAMBLE)


def opencode_front(text):
    """An OpenCode role's frontmatter: {key: value} for top-level keys, and its permissions as (action, resource,
    effect) triples in order."""
    import re
    block = re.match(r"---\n(.*?)\n---\n", text, re.S).group(1)
    top = {l.split(":", 1)[0]: l.split(":", 1)[1].strip() for l in block.splitlines() if not l.startswith(" ")}
    vals = [json.loads(v) if v.startswith('"') else v
            for v in re.findall(r"^ +-? *(?:action|resource|effect): (.*)$", block, re.M)]
    return top, [tuple(vals[i:i + 3]) for i in range(0, len(vals), 3)]


class OpenCodeRoles(unittest.TestCase):
    """The roles in OpenCode's v2 format (D35). tools/sync-opencode --check asks a real OpenCode whether it loads
    them; these hold the shape it accepted on 2.2.7."""

    def test_v2_frontmatter_only(self):
        for rel, text in g.generate(ROOT).items():
            if not rel.startswith("local-agents/opencode/agents/"):
                continue
            with self.subTest(rel):
                top, perms = opencode_front(text)
                self.assertEqual(set(top) - {"color"}, {"description", "mode", "permissions"})  # no v1 name/tools/model
                self.assertEqual(top["mode"], "subagent")
                self.assertRegex(json.loads(top["color"]), r"^#[0-9a-f]{6}$")
                self.assertEqual(perms[0], ("*", "*", "deny"))

    def test_permissions_follow_the_roles_tools(self):
        out = g.generate(ROOT)
        allowed = lambda role: {a for a, r, e in opencode_front(out[f"local-agents/opencode/agents/{role}.md"])[1]
                                if e == "allow" and r == "*"}
        self.assertEqual(allowed("qa"), {"read", "grep", "glob", "shell", "skill", "external_directory"})
        self.assertTrue({"edit", "webfetch", "websearch"} <= allowed("developer"))

    def test_disallowed_edit_is_not_allowed(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = library(tmp, {"AGENTS.md": RULES})
            text = (root / "agents" / "qa.md").read_text().replace("tools: ", "tools: Edit, ", 1)
            (root / "agents" / "qa.md").write_text(text.replace("model:", "disallowedTools: Edit, Write\nmodel:", 1))
            perms = opencode_front(g.opencode_agent(root, root / "agents" / "qa.md"))[1]
            self.assertNotIn(("edit", "*", "allow"), perms)

    def test_unmapped_colour_stops_the_generator(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = library(tmp, {"AGENTS.md": RULES})
            path = root / "agents" / "qa.md"
            path.write_text(path.read_text().replace("color: red", "color: mauve"))
            with self.assertRaises(SystemExit) as e:
                g.opencode_agent(root, path)
            self.assertIn("color 'mauve'", str(e.exception.code))


class InstallRoundTrip(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.root = copy_library(pathlib.Path(self.tmp) / "lib")
        self.home = make_home(self.tmp)

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def round_trip(self):
        before = snapshot(self.home)
        r = gen(self.root, self.home, "--install")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertEqual(gen(self.root, self.home, "--check-install").returncode, 0)
        self.assertNotEqual(snapshot(self.home), before)
        r = gen(self.root, self.home, "--uninstall")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertEqual(snapshot(self.home), before)

    def test_empty_home(self):
        self.round_trip()

    def test_prior_settings_come_back_byte_identical(self):
        qwen = self.home / ".qwen"
        qwen.mkdir()
        # The user's own values, in the user's own formatting: one equal to ours, two lists to add to.
        (qwen / "settings.json").write_text('{"model": {"name": "x"},\n "general": {"enableAutoUpdate": false},'
                                            ' "context": {"fileName": ["QWEN.md"]},'
                                            ' "skills": {"directories": ["/mine/skills"]}}')
        before = (qwen / "settings.json").read_bytes()
        gen(self.root, self.home, "--install")
        data = json.loads((qwen / "settings.json").read_text())
        self.assertEqual(data["skills"]["directories"][0], "/mine/skills")
        self.assertEqual(data["context"]["fileName"][0], "QWEN.md")
        gen(self.root, self.home, "--uninstall")
        self.assertEqual((qwen / "settings.json").read_bytes(), before)
        self.round_trip()

    def test_second_uninstall_leaves_the_users_equal_values(self):
        """With no manifest, --uninstall looks for an install from before the manifest; finding none, it must not
        take a key that merely equals one of ours (here the user's own enableAutoUpdate: false)."""
        qwen = self.home / ".qwen"
        qwen.mkdir()
        (qwen / "settings.json").write_text('{"general": {"enableAutoUpdate": false}}\n')
        before = snapshot(self.home)
        for args in ("--install", "--uninstall", "--uninstall"):
            self.assertEqual(gen(self.root, self.home, args).returncode, 0)
        self.assertEqual(snapshot(self.home), before)

    def test_conflicting_user_value_stops_with_nothing_changed(self):
        qwen = self.home / ".qwen"
        qwen.mkdir()
        (qwen / "settings.json").write_text('{"general": {"gitCoAuthor": {"commit": true, "pr": true}}}\n')
        before = snapshot(self.home)
        r = gen(self.root, self.home, "--install")
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("general.gitCoAuthor is already", r.stderr)
        self.assertEqual(snapshot(self.home), before)

    def test_user_edit_after_install_is_kept(self):
        gen(self.root, self.home, "--install")
        s = self.home / ".qwen" / "settings.json"
        data = json.loads(s.read_text())
        data["model"] = {"name": "mine"}
        s.write_text(json.dumps(data))
        gen(self.root, self.home, "--uninstall")
        self.assertEqual(json.loads(s.read_text()), {"model": {"name": "mine"}})

    def test_install_from_before_the_manifest_is_refused_until_uninstalled(self):
        agents = self.home / ".qwen" / "agents"
        agents.mkdir(parents=True)
        (agents / "qa.md").symlink_to(self.root / "local-agents" / "qwen" / "agents" / "qa.md")
        r = gen(self.root, self.home, "--install")
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("from before the manifest", r.stderr)
        self.assertEqual(gen(self.root, self.home, "--uninstall").returncode, 0)
        self.assertFalse((self.home / ".qwen" / "agents").exists())  # ~/.qwen itself: unrecorded, so left
        self.assertEqual(gen(self.root, self.home, "--install").returncode, 0)


class UserChangesSurvive(unittest.TestCase):
    """What the user changes after the install belongs to the user: a rerun leaves it, --uninstall leaves it."""

    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.root = copy_library(pathlib.Path(self.tmp) / "lib")
        self.home = make_home(self.tmp)
        self.s = self.home / ".qwen" / "settings.json"

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def run_ok(self, *args):
        r = gen(self.root, self.home, *args)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        return r.stdout

    def edit(self, change):
        data = json.loads(self.s.read_text())
        change(data)
        self.s.write_text(json.dumps(data, indent=4))

    def test_theme_and_closed_network_survive_sync_and_uninstall(self):
        """The reviewer's case: ui.theme added and executionSandbox.network closed after the install."""
        self.run_ok("--install")
        self.edit(lambda d: (d.setdefault("ui", {}).update(theme="Dracula"),
                             d["tools"]["executionSandbox"].update(network="closed")))
        out = self.run_ok("--sync")
        data = json.loads(self.s.read_text())
        self.assertEqual(data["tools"]["executionSandbox"]["network"], "closed")
        self.assertEqual(data["ui"], {"theme": "Dracula"})
        self.assertIn("kept", out)
        self.assertIn("tools.executionSandbox", out)
        self.run_ok("--uninstall")
        self.assertEqual(json.loads(self.s.read_text()),
                         {"ui": {"theme": "Dracula"},
                          "tools": {"executionSandbox": {"backend": "auto", "filesystem": "workspace-write",
                                                         "network": "closed"}}})

    def test_sync_leaves_a_file_with_only_unowned_edits_byte_for_byte(self):
        self.run_ok("--install")
        self.edit(lambda d: d.update(ui={"theme": "Dracula"}))
        before = self.s.read_bytes()
        self.run_ok("--sync")
        self.assertEqual(self.s.read_bytes(), before)

    def test_removed_list_item_is_not_added_back(self):
        self.run_ok("--install")
        self.edit(lambda d: d["context"]["fileName"].remove("SKILLS.md"))
        self.assertIn("not added back", self.run_ok("--sync"))
        self.assertNotIn("SKILLS.md", json.loads(self.s.read_text())["context"]["fileName"])
        self.run_ok("--install")
        self.assertNotIn("SKILLS.md", json.loads(self.s.read_text())["context"]["fileName"])

    def test_edited_skills_index_and_repointed_link_are_left(self):
        self.run_ok("--install")
        index, link = self.home / ".qwen" / "SKILLS.md", self.home / ".qwen" / "agents" / "qa.md"
        index.write_text(index.read_text() + "\nMy note.\n")
        mine = self.home / "my-qa.md"
        mine.write_text("my role\n")
        link.unlink()
        link.symlink_to(mine)
        new = self.root / "skills" / "new-skill"  # so the sync has a new SKILLS.md to write
        new.mkdir()
        (new / "SKILL.md").write_text("---\nname: new-skill\ndescription: A skill added after the install.\n---\n")
        out = self.run_ok("--sync")
        self.assertIn("My note.", index.read_text())
        self.assertEqual(os.readlink(link), str(mine))
        self.assertIn(f"kept {index}", out)
        self.run_ok("--uninstall")
        self.assertIn("My note.", index.read_text())
        self.assertEqual(os.readlink(link), str(mine))

    def test_crlf_bom_settings_round_trip_byte_identical(self):
        qwen = self.home / ".qwen"
        qwen.mkdir()
        self.s.write_bytes(b'\xef\xbb\xbf{\r\n  "model": {"name": "x"},\r\n  "general": {"enableAutoUpdate": false}\r\n}')
        before = hashlib.sha256(self.s.read_bytes()).hexdigest()
        self.run_ok("--install")
        installed = self.s.read_bytes()
        self.assertTrue(installed.startswith(b"\xef\xbb\xbf"))
        self.assertNotIn(b"\n", installed.replace(b"\r\n", b""))  # every line ending still CRLF
        self.run_ok("--uninstall")
        self.assertEqual(hashlib.sha256(self.s.read_bytes()).hexdigest(), before)

    def test_jsonc_settings_stop_the_install_with_nothing_changed(self):
        qwen = self.home / ".qwen"
        qwen.mkdir()
        self.s.write_text('{\n  // mine\n  "model": {"name": "x"}\n}\n')
        before = snapshot(self.home)
        r = gen(self.root, self.home, "--install")
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("not plain JSON", r.stderr)
        self.assertEqual(snapshot(self.home), before)


def killed_at(root, home, n, *args):
    """Runs the generator with a SIGKILL at its nth interruption point (gen_local_agents.fault); its return code
    is -9 if it was killed, else it ran past its last point."""
    env = dict(os.environ, HOME=str(home), GEN_LOCAL_AGENTS_KILL_AT=str(n))
    return subprocess.run([sys.executable, str(root / "tools" / "gen_local_agents.py"), *args],
                          capture_output=True, text=True, env=env, cwd=root).returncode


class Interrupted(unittest.TestCase):
    """A run killed at each of its points (the journal write, each change, the middle of each file write, the
    manifest write): settings.json is never empty or partial, the next run finishes the killed one, and --uninstall
    then leaves HOME byte-identical to before the install."""

    PRIOR = b'\xef\xbb\xbf{\r\n  "model": {"name": "x"},\r\n  "general": {"enableAutoUpdate": false}\r\n}'

    def setUp(self):
        self.tmp = pathlib.Path(tempfile.mkdtemp())
        self.root = copy_library(self.tmp / "lib")
        self.template = make_home(self.tmp)
        (self.template / ".qwen").mkdir()
        (self.template / ".qwen" / "settings.json").write_bytes(self.PRIOR)
        (self.template / ".qwen" / "settings.json").chmod(0o600)
        self.before = snapshot(self.template)
        self.home = self.tmp / "run"

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def reset(self, src):
        shutil.rmtree(self.home, ignore_errors=True)
        shutil.copytree(src, self.home, symlinks=True)

    def ok(self, *args):
        r = gen(self.root, self.home, *args)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        return r.stdout

    def settings_whole(self, n):
        raw = (self.home / ".qwen" / "settings.json").read_bytes()
        if raw != self.PRIOR:
            data = json.loads(raw.lstrip(b"\xef\xbb\xbf").decode())  # raises on a partial file
            self.assertTrue(data, f"point {n}: settings.json is empty")

    def every_point(self, start, args, after):
        """For n = 1, 2, ...: copy `start` to HOME, run `args` killed at point n, check, then `after`; stops at the
        first n the run gets past (so every point is covered) and returns how many points there were."""
        for n in range(1, 500):
            self.reset(start)
            rc = killed_at(self.root, self.home, n, *args)
            if rc != -9:
                self.assertEqual(rc, 0)
                return n - 1
            with self.subTest(point=n):
                self.settings_whole(n)
                after(n)
        self.fail("never got past the last point")

    def finish_then_uninstall(self, n, first):
        out = self.ok(first)
        self.assertFalse((self.home / ".local/state/gen_local_agents/journal.json").exists(), out)
        self.ok("--install")
        self.assertEqual(gen(self.root, self.home, "--check-install").returncode, 0, f"point {n}")
        self.ok("--uninstall")
        self.assertEqual(snapshot(self.home), self.before, f"point {n}: {out}")

    def test_install_killed_at_each_point(self):
        points = self.every_point(self.template, ["--install"], lambda n: self.finish_then_uninstall(n, "--sync"))
        self.assertGreater(points, 15)

    def test_sync_killed_at_each_point(self):
        """The sync a pull runs: a new role, a new skill and a new owned settings key since the install."""
        self.reset(self.template)
        self.ok("--install")
        installed = self.tmp / "installed"
        shutil.copytree(self.home, installed, symlinks=True)
        role = (self.root / "agents" / "qa.md").read_text().replace('name: qa', 'name: zz-new', 1)
        (self.root / "agents" / "zz-new.md").write_text(role)
        (self.root / "skills" / "zz-skill").mkdir()
        (self.root / "skills" / "zz-skill" / "SKILL.md").write_text("---\nname: zz-skill\ndescription: New.\n---\n")
        gen_py = self.root / "tools" / "gen_local_agents.py"
        gen_py.write_text(gen_py.read_text().replace(
            '(s, "privacy.usageStatisticsEnabled", False),',
            '(s, "privacy.usageStatisticsEnabled", False), (s, "general.newOwnedKey", True),'))
        self.assertEqual(gen(self.root, self.home).returncode, 0)
        points = self.every_point(installed, ["--sync"], lambda n: self.finish_then_uninstall(n, "--sync"))
        self.assertGreater(points, 5)
        self.reset(installed)
        self.ok("--sync")
        self.assertIn("newOwnedKey", (self.home / ".qwen" / "settings.json").read_text())  # the fixture took effect

    def test_uninstall_killed_at_each_point(self):
        self.reset(self.template)
        self.ok("--install")
        installed = self.tmp / "installed"
        shutil.copytree(self.home, installed, symlinks=True)

        def again(n):
            self.ok("--uninstall")
            self.assertEqual(snapshot(self.home), self.before, f"point {n}")
        self.assertGreater(self.every_point(installed, ["--uninstall"], again), 15)


class Concurrent(unittest.TestCase):
    def setUp(self):
        self.tmp = pathlib.Path(tempfile.mkdtemp())
        self.root = copy_library(self.tmp / "lib")
        self.home = make_home(self.tmp)
        self.env = dict(os.environ, HOME=str(self.home))
        self.cmd = [sys.executable, str(self.root / "tools" / "gen_local_agents.py")]

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def test_a_held_lock_makes_a_sync_wait(self):
        import fcntl
        self.assertEqual(gen(self.root, self.home, "--install").returncode, 0)
        with open(self.home / ".local/state/gen_local_agents/lock", "a") as f:
            fcntl.flock(f, fcntl.LOCK_EX)
            p = subprocess.Popen(self.cmd + ["--sync"], env=self.env, stdout=subprocess.DEVNULL,
                                 stderr=subprocess.DEVNULL)
            with self.assertRaises(subprocess.TimeoutExpired):
                p.wait(timeout=1.5)
        self.assertEqual(p.wait(timeout=30), 0)

    def test_two_runs_at_once(self):
        before = snapshot(self.home)
        for trial in range(8):
            with self.subTest(trial=trial):
                runs = [subprocess.Popen(self.cmd + [a], env=self.env, stdout=subprocess.PIPE,
                                         stderr=subprocess.STDOUT, text=True)
                        for a in (["--install", "--install"], ["--sync", "--install"])[trial % 2]]
                outs = [r.communicate()[0] for r in runs]
                self.assertEqual([r.returncode for r in runs], [0, 0], outs)
                self.assertEqual(gen(self.root, self.home, "--check-install").returncode, 0)
                if trial % 2:
                    self.assertEqual(gen(self.root, self.home, "--uninstall").returncode, 0)
                    self.assertEqual(snapshot(self.home), before)


class StatePrivate(unittest.TestCase):
    """The journal and manifest hold copies of settings.json, which can hold Qwen's API key: the state folder is
    0700 and every file in it 0600, on every run, also over looser ones an older version left."""

    KEY = "sk-PLANTED-123"

    def setUp(self):
        self.tmp = pathlib.Path(tempfile.mkdtemp())
        self.root = copy_library(self.tmp / "lib")
        self.home = make_home(self.tmp)
        (self.home / ".qwen").mkdir()
        self.s = self.home / ".qwen" / "settings.json"
        self.s.write_text(json.dumps({"security": {"auth": {"apiKey": self.KEY}}}))
        self.s.chmod(0o600)
        self.state = self.home / ".local/state/gen_local_agents"

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def ok(self, *args):
        r = gen(self.root, self.home, *args)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)

    def assert_private(self, where):
        self.assertEqual(stat.S_IMODE(self.state.stat().st_mode), 0o700, where)
        files = list(self.state.iterdir())
        for f in files:
            self.assertEqual(stat.S_IMODE(f.stat().st_mode), 0o600, f"{where}: {f.name}")
        return files

    def test_no_state_file_is_readable_by_group_or_other(self):
        self.ok("--install")
        names = {f.name for f in self.assert_private("install")}
        self.assertIn("manifest.json", names)
        self.assertIn(self.KEY, "".join(base64_of(self.state / "manifest.json")))  # the key is in the state
        gen_py = self.root / "tools" / "gen_local_agents.py"  # a new owned settings key since the install
        gen_py.write_text(gen_py.read_text().replace(
            '(s, "privacy.usageStatisticsEnabled", False),',
            '(s, "privacy.usageStatisticsEnabled", False), (s, "general.newOwnedKey", True),'))
        self.ok("--sync")
        self.assert_private("sync")
        self.assertIn("newOwnedKey", self.s.read_text())  # the sync did rewrite the manifest
        self.assertEqual(stat.S_IMODE(self.s.stat().st_mode), 0o600)
        env = dict(os.environ, HOME=str(self.home), GEN_LOCAL_AGENTS_KILL_AT="5")
        subprocess.run([sys.executable, str(self.root / "tools" / "gen_local_agents.py"), "--uninstall"],
                       env=env, capture_output=True)
        self.assertTrue((self.state / "journal.json").exists())  # killed run: its journal holds settings copies
        self.assert_private("killed uninstall")
        self.ok("--uninstall")  # finishes the killed one, then removes the state folder
        self.assertFalse(self.state.exists())
        self.assertEqual(stat.S_IMODE(self.s.stat().st_mode), 0o600)

    def test_an_existing_loose_state_is_tightened_on_the_next_run(self):
        self.ok("--install")
        self.state.chmod(0o775)
        for f in self.state.iterdir():
            f.chmod(0o664)
        self.ok("--sync")
        self.assert_private("sync over 0664/0775")

    def test_a_replaced_loose_manifest_comes_out_0600(self):
        self.ok("--install")
        (self.state / "manifest.json").chmod(0o664)
        g.atomic_write(self.state / "manifest.json", b"{}", mode=g.PRIVATE)
        self.assertEqual(stat.S_IMODE((self.state / "manifest.json").stat().st_mode), 0o600)


def base64_of(manifest):
    """Every base64 string in the manifest decoded: the key sits in the settings copy, not in plain text."""
    out = []

    def walk(x):
        if isinstance(x, dict):
            for v in x.values():
                walk(v)
        elif isinstance(x, list):
            for v in x:
                walk(v)
        elif isinstance(x, str):
            try:
                out.append(base64.b64decode(x, validate=True).decode())
            except Exception:
                pass
    walk(json.loads(manifest.read_text()))
    return out


class Hooks(unittest.TestCase):
    """A clone with the hooks pulls a commit that adds a skill; another without them pulls the same commit."""

    def git(self, cwd, *args):
        r = subprocess.run(["git", "-C", str(cwd), *args], capture_output=True, text=True,
                           env=dict(os.environ, HOME=str(self.home), GIT_AUTHOR_NAME="t", GIT_AUTHOR_EMAIL="t@t",
                                    GIT_COMMITTER_NAME="t", GIT_COMMITTER_EMAIL="t@t"))
        self.assertEqual(r.returncode, 0, r.stderr)
        return r.stdout

    def setUp(self):
        self.tmp = pathlib.Path(tempfile.mkdtemp())
        self.home = make_home(self.tmp)
        src = copy_library(self.tmp / "src")
        self.git(src, "init", "-q", "-b", "main")
        self.git(src, "add", "-A")
        self.git(src, "commit", "-qm", "library")
        self.git(self.tmp, "clone", "-q", "--bare", str(src), "origin.git")
        self.src = src

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def pull_new_skill(self, hooks):
        clone = self.tmp / "clone"
        self.git(self.tmp, "clone", "-q", str(self.tmp / "origin.git"), "clone")
        if hooks:
            self.assertEqual(gen(clone, self.home, "--install-hooks").returncode, 0)
        self.assertEqual(gen(clone, self.home, "--install").returncode, 0)
        new = self.src / "skills" / "new-skill"
        new.mkdir()
        (new / "SKILL.md").write_text("---\nname: new-skill\ndescription: A skill added upstream, for this test.\n---\n")
        self.git(self.src, "add", "-A")
        self.git(self.src, "commit", "-qm", "add a skill")
        self.git(self.src, "push", "-q", str(self.tmp / "origin.git"), "main")
        self.git(clone, "pull", "-q", "--ff-only")
        return clone

    def test_pull_with_hooks_updates_skills_index(self):
        clone = self.pull_new_skill(hooks=True)
        self.assertIn("new-skill", (self.home / ".qwen" / "SKILLS.md").read_text())
        self.assertEqual(gen(clone, self.home, "--check-install").returncode, 0)

    def test_pull_without_hooks_goes_stale(self):
        clone = self.pull_new_skill(hooks=False)
        self.assertNotIn("new-skill", (self.home / ".qwen" / "SKILLS.md").read_text())
        r = gen(clone, self.home, "--check-install")
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("SKILLS.md: missing or stale", r.stdout)


class HooksKeepTheClonesOwn(unittest.TestCase):
    """--install-hooks adds to .git/hooks; the clone's own hooks keep running, and --uninstall-hooks puts .git/hooks
    and .git/config back byte for byte."""

    def git(self, *args, check=True):
        r = subprocess.run(["git", "-C", str(self.clone), *args], capture_output=True, text=True,
                           env=dict(os.environ, HOME=str(self.home), GIT_AUTHOR_NAME="t", GIT_AUTHOR_EMAIL="t@t",
                                    GIT_COMMITTER_NAME="t", GIT_COMMITTER_EMAIL="t@t"))
        if check:
            self.assertEqual(r.returncode, 0, r.stderr)
        return r

    def setUp(self):
        self.tmp = pathlib.Path(tempfile.mkdtemp())
        self.home = make_home(self.tmp)
        self.clone = copy_library(self.tmp / "clone")
        self.git("init", "-q", "-b", "main")
        self.git("add", "-A")
        self.git("commit", "-qm", "library")
        self.hooks = self.clone / ".git" / "hooks"
        for name in ("pre-commit", "post-merge"):  # the clone's own hooks, from before
            (self.hooks / name).write_text(f'#!/bin/sh\necho ran >> "$(git rev-parse --git-dir)/{name}.log"\n')
            (self.hooks / name).chmod(0o755)

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def state(self):
        return snapshot(self.hooks), (self.clone / ".git" / "config").read_bytes()

    def ran(self, name):
        log = self.clone / ".git" / f"{name}.log"
        return log.read_text().count("ran") if log.exists() else 0

    def commit_and_merge(self):
        (self.clone / "f.txt").write_text(str(self.ran("pre-commit")))
        self.git("add", "f.txt")
        self.git("commit", "-qm", "change")
        self.git("checkout", "-q", "-b", "side")
        (self.clone / "g.txt").write_text("x")
        self.git("add", "g.txt")
        self.git("commit", "-qm", "side")
        self.git("checkout", "-q", "main")
        self.git("merge", "-q", "--no-edit", "--no-ff", "side")
        self.git("branch", "-qD", "side")

    def test_existing_hooks_still_run_and_uninstall_restores(self):
        before = self.state()
        r = gen(self.clone, self.home, "--install-hooks")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(self.git("config", "--get", "core.hooksPath", check=False).stdout, "")
        self.commit_and_merge()
        self.assertEqual((self.ran("pre-commit"), self.ran("post-merge")), (2, 1))
        self.assertIn("gen_local_agents.py", (self.hooks / "post-checkout").read_text())
        r = gen(self.clone, self.home, "--uninstall-hooks")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(self.state(), before)

    def test_reinstall_keeps_one_original(self):
        before = self.state()
        for _ in range(2):
            self.assertEqual(gen(self.clone, self.home, "--install-hooks").returncode, 0)
        self.commit_and_merge()
        self.assertEqual(self.ran("post-merge"), 1)
        self.assertEqual(gen(self.clone, self.home, "--uninstall-hooks").returncode, 0)
        self.assertEqual(self.state(), before)

    def test_earlier_hookspath_is_cleared_so_the_clones_hooks_run_again(self):
        self.git("config", "core.hooksPath", "tools/hooks")  # what --install-hooks did before
        self.assertEqual(gen(self.clone, self.home, "--install-hooks").returncode, 0)
        self.commit_and_merge()
        self.assertEqual(self.ran("pre-commit"), 2)

    def test_another_hookspath_is_refused_with_nothing_changed(self):
        self.git("config", "core.hooksPath", ".husky")
        before = self.state()
        r = gen(self.clone, self.home, "--install-hooks")
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("core.hooksPath is .husky", r.stderr)
        self.assertEqual(self.state(), before)


def set_core(root, rid, text, scope="all"):
    """Sets row rid's `core` and `scope` cells in root's docs/REQUIREMENTS.tsv."""
    p = root / "docs" / "REQUIREMENTS.tsv"
    lines = p.read_text().split("\n")
    head = lines[0].split("\t")
    for i, line in enumerate(lines[1:], 1):
        cells = line.split("\t")
        if cells[0] == rid:
            cells[head.index("core")] = text
            cells[head.index("scope")] = scope
            lines[i] = "\t".join(cells)
            return p.write_text("\n".join(lines))
    raise AssertionError(rid)


class CoreSheet(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.root = copy_library(pathlib.Path(self.tmp) / "lib")
        self.home = make_home(self.tmp)

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def test_lines_are_the_core_cells_tagged_with_their_rows(self):
        import csv
        with open(ROOT / "docs" / "REQUIREMENTS.tsv", newline="") as f:
            rows = {r["id"]: r for r in csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE)}
        for sheet in (g.core_sheet(ROOT), (ROOT / g.CORE_SHEET).read_text()):  # generated, and the committed copy
            lines = [l for l in sheet.splitlines() if l.startswith("- ")]
            self.assertEqual(lines, [f"- {r['core']} [{i}]" for i, r in rows.items() if r["scope"] == "all"])
            self.assertGreaterEqual(len(lines), 6)
            self.assertTrue(sheet.rstrip().endswith(g.FULL_POINTER))

    def test_edited_core_row_makes_the_sheet_stale(self):
        set_core(self.root, "A09", "Secrets are fine in logs.")
        r = gen(self.root, self.home, "--check")
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertIn(f"{g.CORE_SHEET}: stale", r.stdout)

    def test_rows_past_the_budget_fail_check(self):
        for rid in ("A02", "A03", "A04", "A06", "A07", "A08", "A12", "A13", "A16", "A18", "A19", "A20"):
            set_core(self.root, rid, "Keep this line short enough to read, and follow it every time you work here.")
        self.assertEqual(gen(self.root, self.home).returncode, 0)  # regenerated, so only the budget can fail
        r = gen(self.root, self.home, "--check")
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertIn("over the budget of 450", r.stdout)

    def test_within_budget_by_the_endpoint_tokenizer(self):
        text = g.core_sheet(ROOT)
        est, n = g.estimate_tokens(text), g.endpoint_tokens(text)
        how = "endpoint tokenizer" if n is not None else f"estimate ({g.CHARS_PER_TOKEN} chars/token; endpoint unreachable)"
        print(f"\ncore sheet: {n if n is not None else est} tokens by {how}; estimate {est}", file=sys.stderr)
        self.assertLessEqual(n if n is not None else est, g.CORE_BUDGET)
        if n is not None:  # the estimate --check uses offline must count high, or it would pass an oversized sheet
            self.assertGreaterEqual(est, n, f"CHARS_PER_TOKEN {g.CHARS_PER_TOKEN} undercounts: recalibrate")


def requirement_rows(root):
    import csv
    with open(root / "docs" / "REQUIREMENTS.tsv", newline="") as f:
        return {r["id"]: r for r in csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE)}


def tagged(text):
    """The [id] tags of a generated file's core-rule lines ("- ... [ID]")."""
    import re
    return [m.group(1) for m in re.finditer(r"^- .* \[([A-Z]\d\d)\]", text, re.M)]


SHARED_SOURCES = ("AGENTS.md", "tools/gen_local_agents.py", "skills/")  # read by (or about) every role


class CoreScope(unittest.TestCase):
    """The shared sheet holds only the rules every role keeps; a role's own core rules go in its core-mode file only
    (producer, 2026-10-08: the developer's "never merge, push" was on every role's sheet)."""

    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.root = copy_library(pathlib.Path(self.tmp) / "lib")
        self.home = make_home(self.tmp)

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def assert_scoped(self, root, files):
        rows = requirement_rows(root)
        for rid in tagged(files[g.CORE_SHEET]):
            self.assertTrue(rows[rid]["file"].startswith(SHARED_SOURCES),
                            f"{g.CORE_SHEET}: {rid} comes from {rows[rid]['file']}, one role's rule")
        roles = sorted(p.stem for p in (root / "agents").glob("*.md"))
        for role in roles:
            text = files[f"{g.OUT}/qwen/agents-core/{role}.md"]
            want = ["L01"] + [i for i, r in rows.items() if r["core"] and r["file"] == f"agents/{role}.md"]
            self.assertEqual(tagged(text), want, f"agents-core/{role}.md")
        return roles

    def test_each_role_has_its_own_core_rules_and_no_other(self):
        committed = {rel: (ROOT / rel).read_text() for rel in g.generate(ROOT)}
        for files in (g.generate(ROOT), committed):
            self.assert_scoped(ROOT, files)
            dev = files[f"{g.OUT}/qwen/agents-core/developer.md"]
            self.assertEqual(tagged(dev), ["L01", "V06", "V07", "V24", "V25", "V26", "V28"])  # not vacuous
            self.assertIn("see it fail, and keep that negative control with it. [V07]", dev)

    def test_a_role_rule_scoped_to_all_or_another_role_fails(self):
        for scope in ("all", "qa"):
            set_core(self.root, "V24", "Never merge, push or touch another branch.", scope)
            files = g.generate(self.root)
            with self.assertRaises(AssertionError, msg=scope):
                self.assert_scoped(self.root, files)

    def test_identity_line_in_every_core_file(self):
        line = requirement_rows(ROOT)["L01"]["core"]
        for f in ("user.*", "-c user.*", "--author", "GIT_*", "never as the user", "project's configured identity"):
            self.assertIn(f, line)
        files = g.generate(ROOT)
        core = [rel for rel in files if rel == g.CORE_SHEET or "/agents-core/" in rel]
        self.assertEqual(len(core), 1 + len(list((ROOT / "agents").glob("*.md"))))
        for rel in core:
            for text in (files[rel], (ROOT / rel).read_text()):
                self.assertIn(line, text, rel)
                if rel != g.CORE_SHEET:
                    self.assertIn("says to commit with the project's identity or as the user, that is for Claude Code"
                                  " sessions, not you", text, rel)

    def test_planted_project_identity_line_is_overridden(self):
        lib = library(pathlib.Path(self.tmp) / "plant", {"AGENTS.md": RULES})
        qa = lib / "agents" / "qa.md"
        qa.write_text(qa.read_text() + "- Commit on your branch with the project's identity.\n")
        text = g.core_agent(lib, qa)
        planted = text.index("- Commit on your branch with the project's identity.")
        override = text.index("Commit as local-agent <local-agent@forge.local>; never as the user. [L01] Where the text"
                              " below says to commit with the project's identity")
        self.assertLess(override, planted)

    def test_core_files_name_their_sources_blob_hashes(self):
        tsv = g.blob(ROOT / g.REQUIREMENTS)
        committed = {rel: (ROOT / rel).read_text() for rel in g.generate(ROOT)}
        for files in (g.generate(ROOT), committed):
            self.assertIn(f"from {g.REQUIREMENTS} (git blob {tsv})", files[g.CORE_SHEET])
            for role in sorted((ROOT / "agents").glob("*.md")):
                self.assertIn(f"from agents/{role.name} (git blob {g.blob(role)}) and {g.REQUIREMENTS} (git blob {tsv})",
                              files[f"{g.OUT}/qwen/agents-core/{role.name}"])


class RulesMode(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.root = copy_library(pathlib.Path(self.tmp) / "lib")
        self.home = make_home(self.tmp)
        self.qwen = self.home / ".qwen"

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def ok(self, *args):
        r = gen(self.root, self.home, *args)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        return r.stdout

    def target(self, name):
        return os.readlink(self.qwen / name)

    def test_core_links_the_core_sheet_and_roles(self):
        self.ok("--install", "--rules", "core")
        self.assertEqual(self.target("AGENTS.md"), str(self.root / g.CORE_SHEET))
        self.assertEqual(self.target("AGENTS-full.md"), str(self.root / "local-agents/qwen/AGENTS.md"))
        self.assertEqual(self.target("agents/qa.md"), str(self.root / "local-agents/qwen/agents-core/qa.md"))
        files = json.loads((self.qwen / "settings.json").read_text())["context"]["fileName"]
        self.assertEqual(files, ["QWEN.md", "AGENTS.md", "CLAUDE.md"])
        manifest = self.home / ".local" / "state" / "gen_local_agents" / "manifest.json"
        self.assertEqual(json.loads(manifest.read_text())["rules"], "core")
        self.ok("--check-install")  # the recorded mode
        r = gen(self.root, self.home, "--check-install", "--rules", "full")
        self.assertEqual(r.returncode, 1)
        self.assertIn("installed with --rules core, not full", r.stdout)

    def test_sync_keeps_the_chosen_sheet(self):
        self.ok("--install", "--rules", "core")
        self.ok("--sync")
        self.assertEqual(self.target("AGENTS.md"), str(self.root / g.CORE_SHEET))

    def test_default_is_full(self):
        self.ok("--install")
        self.assertEqual(self.target("AGENTS.md"), str(self.root / "local-agents/qwen/AGENTS.md"))
        self.assertFalse((self.qwen / "AGENTS-full.md").is_symlink())

    def test_switching_back_and_uninstalling_restores_home(self):
        (self.qwen).mkdir()
        (self.qwen / "settings.json").write_text('{"context": {"fileName": ["MINE.md"]}, "ui": {"theme": "x"}}\n')
        before = snapshot(self.home)
        self.ok("--install")
        full = snapshot(self.home)
        self.ok("--install", "--rules", "core")
        self.assertNotEqual(snapshot(self.home), full)
        files = json.loads((self.qwen / "settings.json").read_text())["context"]["fileName"]
        self.assertEqual(files, ["MINE.md", "QWEN.md", "AGENTS.md", "CLAUDE.md"])
        self.ok("--install", "--rules", "full")
        self.ok("--check-install")
        self.assertEqual(snapshot(self.home), full)
        self.ok("--install", "--rules", "core")
        self.ok("--uninstall")
        self.assertEqual(snapshot(self.home), before)


class ScriptedModel(http.server.BaseHTTPRequestHandler):
    """An OpenAI-compatible model that answers "ok" and keeps every request body (class attribute `bodies`)."""
    bodies = []

    def log_message(self, *a):
        pass

    def do_POST(self):
        body = json.loads(self.rfile.read(int(self.headers.get("Content-Length") or 0)) or b"{}")
        ScriptedModel.bodies.append(body)
        if body.get("stream"):
            self.send_response(200)
            self.send_header("Content-Type", "text/event-stream")
            self.end_headers()
            for delta, stop in (({"role": "assistant", "content": "ok"}, None), ({}, "stop")):
                chunk = {"id": "x", "object": "chat.completion.chunk", "created": 0, "model": "scripted",
                         "choices": [{"index": 0, "delta": delta, "finish_reason": stop}]}
                self.wfile.write(f"data: {json.dumps(chunk)}\n\n".encode())
            self.wfile.write(b"data: [DONE]\n\n")
            return
        data = json.dumps({"id": "x", "object": "chat.completion", "created": 0, "model": "scripted",
                           "choices": [{"index": 0, "message": {"role": "assistant", "content": "ok"},
                                        "finish_reason": "stop"}],
                           "usage": {"prompt_tokens": 1, "completion_tokens": 1, "total_tokens": 2}}).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)


@unittest.skipUnless(shutil.which("qwen"), "Qwen Code (qwen) isn't installed here")
class QwenLoadsTheChosenSheet(unittest.TestCase):
    """A real Qwen Code run (-p, one turn) against ScriptedModel, in a HOME installed by --install: the request's
    text must carry the chosen sheet whole and not the other one."""

    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.root = copy_library(pathlib.Path(self.tmp) / "lib")
        self.home = make_home(self.tmp)
        self.server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), ScriptedModel)
        threading.Thread(target=self.server.serve_forever, daemon=True).start()
        ScriptedModel.bodies = []

    def tearDown(self):
        self.server.shutdown()
        self.server.server_close()
        shutil.rmtree(self.tmp)

    def prompt(self, *install):
        r = gen(self.root, self.home, "--install", *install)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        work = pathlib.Path(self.tmp) / "work"
        work.mkdir()
        env = {"HOME": str(self.home), "PATH": os.environ["PATH"], "LANG": "C.UTF-8", "TERM": "dumb",
               "OPENAI_BASE_URL": f"http://127.0.0.1:{self.server.server_port}/v1", "OPENAI_API_KEY": "scripted",
               "OPENAI_MODEL": "scripted"}
        q = subprocess.run(["qwen", "-p", "say ok", "--auth-type", "openai", "--output-format", "text"], cwd=work,
                           env=env, capture_output=True, text=True, timeout=300)
        self.assertEqual(q.returncode, 0, q.stderr[-2000:])
        self.assertEqual(q.stdout.strip(), "ok")
        chats = [b for b in ScriptedModel.bodies if "messages" in b]
        self.assertTrue(chats, "Qwen Code sent no chat request")
        return "\n".join(m["content"] if isinstance(m["content"], str) else json.dumps(m["content"])
                         for b in chats for m in b["messages"])

    def test_core(self):
        text = self.prompt("--rules", "core")
        self.assertIn((self.root / g.CORE_SHEET).read_text().strip(), text)
        self.assertNotIn("7. **Name the distinct cases.**", text)  # the full sheet
        self.assertNotIn("## Claude-specific text, and how to read it", text)  # LOCAL-TOOLS.md

    def test_full(self):
        text = self.prompt()
        self.assertIn(g.rules_file(self.root).read_text().strip(), text)
        self.assertIn("## Claude-specific text, and how to read it", text)
        self.assertNotIn("[A05]", text)  # the core sheet


if __name__ == "__main__":
    unittest.main()
