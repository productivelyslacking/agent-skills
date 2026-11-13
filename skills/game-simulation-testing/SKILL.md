---
name: game-simulation-testing
description: Testing game rules, AI, balance and pacing without a human: deterministic simulation, bots that play the real content, balance guards. Use when changing combat, AI or tuning, or when a simulated run stalls or a balance test fails.
---

# Game simulation testing

Assumes **ground-truth**. A game's rules can be tested like any code if they live outside the engine, and its balance
and pacing can be measured if something plays it. The failure this guards against: tuning numbers to fix what was
really an AI or rules bug, which looks like progress and fixes nothing. The incidents behind these rules, and traps
seen once, are in `NOTES.md` beside this file; read it when a simulated run stalls or a control behaves oddly.

## Build the game so it can be played without the engine

- **Put the rules in a plain library with a fixed tick:** same seed and inputs give the same result. The engine draws
  state and sends input, and decides nothing.
- **Route all behaviour through commands the world validates:** player input, AI and tests issue the same commands, so
  an AI can't cheat and a test exercises the real path.
- **Check invariants every tick in debug builds and test on debug** (HP within bounds, no unit in a wall, threat only on
  the living). A firing invariant found a real bug; never weaken it to pass a test.
- **Seeded randomness only,** with the seed in every log line, so a failing run can be replayed.

## An AI that plays the real content

- **A pilot plays the actual campaign start to finish** (quests, fights, shops, levels, loot, points); its time to
  level, deaths and failures are your pacing metrics, and it finds deadlocks and economy stalls no unit test can.
- **Run it for every composition the design allows:** AI written for one party breaks silently under another.
- **Run whole-area tests for mutual waits and threshold gaps:** two AIs each waiting for the other deadlock, and "heal
  below 90%, attack above 90%" does nothing at exactly 90%; 1-on-1 tests can't see either.
- **Keep long runs as a tagged suite** (`Category=Slow`) and run it whenever the pilot, economy or progression changes:
  only long runs show a change that stalls every climb.
- **Say the pilot dodges perfectly wherever its numbers are quoted:** they are a floor on difficulty, and difficulty
  needs a human.

## AI movement: kiting, bodies and bands

- **Kite only inside four limits:** foes clearly slower than your *current* speed (slows switch it off), well inside
  every chaser's leash, clear of enemies not yet fighting, ignoring ranged chasers. Simpler kiting stops healing or drags
  monsters past their leash to reset forever. Measure who dies to what before designing it.
- **Take a scripted boss's reach from its script, not its ability list:** a scripted melee hit isn't listed, so derived
  reach and "is ranged" are wrong, and tests built on them can't fail.
- **Give melee position bands no floor:** a band with a floor plus anything that pushes makes a unit that never stands
  still, which cancels every cast.

## Guards that prove the fight is a fight

- **Pair every "this wins" test with a "this loses" test:** a party that ignores the mechanics loses; one with no damage
  loses to the enrage; one with no healer wipes. Without the losing half, a boss that does nothing passes. Never loosen
  a guard to make a change pass.

## Diagnosing: read the trace before touching numbers

- **Balance bugs show up as AI behaviour:** "the class is weak" and "the party without a healer survives" were both AI
  bugs. Log damage taken by source, healing done, and position at each death first.
- **When a run stalls, print the stuck state before guessing:** periodic positions show frozen units that a tuning
  change would only hide.
- **Measure a whole loop before picking a timer:** timers interact with travel time, and a respawn shorter than the walk
  back to heal traps a solo character.
- **Probes are throwaway tests:** print the metric across all compositions before and after a change, compare the tables
  side by side, delete the probe, record the numbers.

## Tests lie in game-specific ways

- **Assert every action succeeded unless the refusal is the point:** game actions return a refusal instead of throwing,
  so a refused action leaves a test green on the wrong state.
- **Isolate the mechanism, then break it once to see red:** another mechanic can produce the same result.
- **Turn the fight-end rule off in test worlds unless the outcome is the point, and cap every loop on a step:** a world
  that has ended a fight stops stepping, so tests freeze, hang or pass because nothing moved.
- **Check against the data, never the code under test's own answer:** that test can't fail.
- **Test prediction features against the real effect:** compare a stat preview by equipping the item.

## Measured numbers in docs

- **Date a measured pacing table, name the test that prints it, and re-measure after any AI or balance change:** it is a
  copy of a test log, so it drifts.
