# dependency-policy: notes

Read on demand. Holds the evidence behind `SKILL.md`'s rules: the owner's words, incidents and numbers.

## The bar for adding anything

- **Licences at the source.** Page summaries invented one non-commercial dependency and missed another; a popular
  repackaging was tagged Apache-2.0 while upstream carried revenue-threshold terms, and the wrong tag was what every
  search returned. One permissively licensed model's dataset came from a commercial provider whose terms its licence
  didn't cover.
- **Keep the tree small.** One framework brought 103 of a project's 104 locked packages, every licence needing review.

## Before building a tool, look for an established one

- The owner, 2026-10-07 (D10): "In the future, i want to make sure we research whether a well known open source
  tool exists that fits our need instea dof building our own tool as a reflex every time." An action RPG's studio had
  built its own job router, GPU lock, review and landing scripts, evidence pages and board before asking whether
  Windmill, a CI runner, a dashboard or a tracker already did the job; each then needed its own fix and review rounds.
- The owner, 2026-10-07, on ranking: "the most permissable licenses should be weighted as better options when making
  decisions if the intended perpose if each tool is similar. community size and online resource availability should
  count as well."

## Before checking by hand, look for a tool that checks

- The owner, 2026-10-10: "should we have a rules that has one of the agents look for open source tools to improve qa
  like we just did when working on codebases?" On a Linux service project, five review rounds of one milestone were
  spent probing by hand for crashes on odd input, races, unbounded reads and tests that never failed.

## The check: run it, don't reason about it

- Version numbers filled in from memory were a year or more out of date and passed review, because nothing checked them.
