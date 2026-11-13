# game-simulation-testing: notes

Facts seen on one project, kept for whoever hits the same thing. They haven't recurred enough to be rules, so check them against your versions. Moved from `docs/CANDIDATES.md` on 2026-11-07 (D21).

- **2026-10-04, action-rpg - A bot that plans over "all unhandled" but acts on "the nearest" stalls.** The pilot walked to an unsearched body; the act step only looked at the nearest body in reach,
  already searched (full bags), so it stood there until the body faded. Planning and acting must
  filter the same set. Found by histogramming the bot's status over a long run. Target: game-simulation-testing.
- **2026-10-04, action-rpg - A state-setting command needs an owner who clears it.** A unit's movement
  direction stayed set after one controller (fleeing a hazard) handed over to another (fighting) that
  expressed "stand still" by sending nothing; the unit walked into a corner and every cast was
  refused, for good. Unrelated dice changes exposed it in one simulated run. Controllers that intend
  "no movement" should say so explicitly. Target: game-simulation-testing.
- **2026-10-05, action-rpg - A negative control reverted with `mv` leaves the broken build running.** Copy a file aside, break it, run the test, `mv` the copy back: the copy keeps its old modification time, older than the assembly built from the broken file, so the next incremental build sees nothing newer and keeps the broken code (12 passing tests failed). `touch` the restored file, or restore with `git checkout`. A suite that fails right after a revert is a stale build first. Target: game-simulation-testing (negative controls) or ground-truth.
- **2026-10-05, action-rpg - A green parity gate can be checked with a diff, not only an assertion.** "Feature off leaves every existing result unchanged" was shown by running the suite on the base commit and on the branch (TRX logger) and diffing every result line the existing tests print (45 lines, identical), then failing it on purpose by ignoring the off switch. Prints that carry the numbers (times, deaths, levels) make that possible. Target: game-simulation-testing.
- **2026-10-05, action-rpg - An encounter that every configuration wins proves little about the configurations.** 28 sworn-Cleric pairings all beat the boss, and still did with every Cleric amount ×0.2; only zeroing them lost 3. Before reporting coverage runs as balance evidence, break the varied thing hard and see whether any run loses. Target: game-simulation-testing.
- **2026-10-05, action-rpg - Linear per-level scaling of a "-x%" modifier crosses -100%.** Item effects grew linearly with item level; a unique's -25% hazard damage at item level 10 was -100% at 40, and past it the factor went negative, so burning pools healed. Nothing showed it until a debug invariant (HP above max) fired on the first climb to the new cap of 80. Floor each reduction and each stack of them (as armor already was), and run the long climbs to any new cap with invariants on before trusting the cap. Target: game-simulation-testing.
- **2026-10-05, action-rpg - A pilot needs the exits a player has, and the stalemate it hides is a finding.** Climbing to 80, a solo tank fought a Shielding Regenerating elite for 12,000 game-seconds: printing the stuck state showed it out-sustained (about 240 HP/s healed and shielded), not frozen units. The pilot now walks out of a rift with no kill for 600 s, a failure that lowers its tier, as a player would; the out-sustain itself is reported for the designer, not tuned away. Target: game-simulation-testing.
- **2026-10-05, action-rpg - When rewards per run shrink, give long pacing tests a stated multiplier and measure the real pace once.** Rifts went from a level each to a fifth; the climbs to the cap would have run five times longer. The ladders now take x5 rift XP (stated in the test, with why), which restores the old rate and keeps them measuring whether gear and scaling meet at the cap; the real pace (x1) was measured once by a throwaway probe and recorded in the decision. Target: game-simulation-testing.
## Property tests: check the plants reach, and that inputs are mostly valid (a Linux service project, 2026-10-21)

Seen adding Hypothesis to a Linux service project (S7): a derandomized (fixed-example) property catches a planted bug only if its
generated inputs actually reach the planted line, so a plant that passes may mean the generator never gets there, not
that the code is right; re-run the plants after any generator change. And a generator that makes nearly every input
invalid exercises only the first validation check: measure what share of generated inputs gets past the first gate.
Candidate home: game-simulation-testing or ground-truth (checks that can fail).

## Build the game so it can be played without the engine

- An action RPG with AI companions, where these rules were learned, ran its rules at a 30 Hz tick.

## An AI that plays the real content

- **Compositions:** damage dealers that "waited for the tank" never attacked in duos without one; 9 of 16 pairings sat at
  full boss HP.
- **Long runs:** a merchant change once stalled every climb, and only the long runs showed it.

## AI movement: kiting, bodies and bands

- **Kiting:** two simple tries failed (a healer that ran stopped healing; monsters dragged past their leash reset and
  healed, forever). The deaths were to slow bosses, and healers never needed kiting.
- **Boss reach:** a boss whose melee hit was scripted listed only its ranged bolt, so a test measuring time in its reach
  couldn't fail.
- **Bands:** "stand 2.5 ± 1 m away" was harmless until units got bodies and pushed each other to 1.4 m; then a healer
  stepped back every tick, cancelling every cast, and a rift climb stalled.

## Diagnosing: read the trace before touching numbers

- **Weak class:** a solo Ranger's 12 deaths were all the same telegraph, which its escape search was too small to leave.
- **Healerless party survives:** the tank AI stood in a pool because no ideal spot existed.
- **Stalled run:** a level climb stuck for 25,000 s looked like an elite regenerating too fast. Printing positions every
  200 s showed both units frozen: a hazard centred on the monster kept the melee AI out of reach, and neither side
  attacked. Lowering regeneration "fixed" nothing.
- **Timer:** a 90 s respawn trapped a solo character who cleared a pack, walked back to heal, and found the packs back.

## Tests lie in game-specific ways

- **Refusal:** an equip refused by a new level rule left a test asserting on a naked character, still green.
- **Same result, other mechanic:** a leash test passed with the leash removed: moving the mob wiped its threat, and a
  nearby pack killed the player, which wipes threat too.
- **Fight-end:** once a side had fallen, `Step()` returned at once; a test with no enemies froze, a
  `while (dodging) Step()` loop hung the run for ten minutes, and a "the dead don't block" test passed because nothing
  moved.

## Measured numbers in docs

- An action RPG's pacing table was wrong by 300 s and three deaths before anyone noticed.
