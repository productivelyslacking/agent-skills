# ground-truth: notes

Read on demand. Holds the incidents, numbers, dates and sources behind the rules in `SKILL.md`, under its section
headings.

## 2. Verify against the real thing, not the description of it

- **Three failed fixes:** one bug took six landings because two fixes passed every gate on a path the device didn't
  use.

## 3. The plausible generic answer is the default failure mode

- **Stale "current" lists:** a research agent named a model family as the newest, months after its successor
  shipped. Seen on two projects.

## 4. Never assert what you cannot demonstrate

- **The way out (D11, `docs/DECISIONS.md`):** ImpossibleBench (arXiv 2510.20270): an explicit abort option cut
  GPT-5's cheating from 54% to 9%.

## 6. Check with something that can fail - and know how checks lie

- **Controls that lied** (seen on four projects): a checker that crashed on a missing dependency looked like a
  control working; a patch aimed at a stale anchor removed nothing and the control reported PASS; a crashed count
  read as "nothing left"; one model ranked two genres correctly and scored white noise 0.95.
- **A check nobody sees fail:** one project's automated drift checker became a no-op that passed every run and was
  retired.
- **Flaky gate:** on one project a test with 85% reliability cascaded failures across the system.
- **Fixture satisfying the property by chance:** a name whose checksum already had the top bit set let a missing
  `| 0x80000000` pass every test.

## 10. Design for a human with little time and attention

- Further owner quotes, 2026-10-08: "i need to get it super simplified and organized for a lazy human";
  "everything needs to be laid out in a simple structure that we can reuse so all our repos are familiar."
- 2026-10-07: a multi-step account setup was half done while the user believed it finished.

## 11. Build so someone else could take it over tomorrow

- Full owner quote, 2026-10-21: "we will probably manage it going forward still, but we should always build like
  we might win the lottery tomorrow and someone else would have to pick it up."

## A passing check covers only what it checks (rule 6): further sightings

Recurred across projects; moved from the candidate list on 2026-11-13 (D29).

- **2026-10-03, action-rpg - Comparing bytes against a reference library's output fails a correct
  writer.** A popular parser's text output (vdf) differs from the real format's (Steam's tabs).
  Check what an independent parser *reads back*, not its formatting. Target: ground-truth (rule 2).
- **2026-10-05, asset-pipeline - Run a quality gate on the hand-made reference before on the generated thing.** A
  design set "99.5% of edges within 0.5-2x their rest length in every clip" for a creature rigged onto a
  CC0 wolf's skeleton; the artist's wolf itself scored 98.1-99.4% in 7 of its 12 clips, so the gate could
  only ever say no. Score the reference first, print its numbers beside every result, and set the bar
  from them. Seen twice the same day: the replacement suggestion, "reach at most 1.5 times the bone's own
  length", failed the wolf too (short shoulder bones weight 6.8 times their length); the bar that held is
  relative to the reference's own value for the same part. Target: ground-truth (rule 6) or game-assets.
- **2026-10-21, home-network - A tool's preview or dry run validates the tool's schema, not what the server will accept.** Seven firewall-rule previews passed; the controller then rejected three on apply (defaults the server forbids for that target: an auto "allow replies" rule toward the gateway, and ICMP with IP version "both"). Apply changes one at a time, read each result, and treat a passing preview as evidence about the request's shape only. Target: ground-truth rule 6 (a green gate is evidence only about what it checks).
