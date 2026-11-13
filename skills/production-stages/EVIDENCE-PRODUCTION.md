# Evidence: when to commit to what in production

Input for `production-stages/SKILL.md`, edited from two research passes dated 2026-11-06 (D25 in `docs/DECISIONS.md`). Evidence, not
rules. Cite as `[G-C3]` (Part G, games, 48 claims) or `[F-C3]` (Part F, film, TV, animation and motion comics, 52 claims). The numbers
are the research passes' own and stay stable: a claim dropped later keeps its number retired.

**Read this before relying on any claim.**
- **Most sources were reached second-hand.** The film part read almost everything through a summarising fetch ("extract"), mainly
  Wikipedia and trade press; its largest primary sources (Catmull's *Creativity, Inc.*, Goetz's *Audience-ology*, Price's *The Pixar
  Touch*) were not opened. Pixar's numbers and stories are second-hand: one editor's interview, press, Wikipedia. The games part read
  more at source, but GDC talks were not watched, and most papers were read as abstracts.
- **Nothing here is a controlled comparison of production orders.** Postmortems and interviews come from work that shipped, told by its
  makers. Winners are over-represented, in both parts.
- **Each part's status words are its own.** Part G uses opened, opened-part, extract, not opened. Part F uses opened, extract, not
  opened. Both say what they mean at the top of the part. Neither gives a strength rating beyond status and kind. Don't raise either.
- **Every "Would change" and "Producer" line is the research author's inference,** aimed at a small team of AI agents plus one owner.
- **Edits from the research files:** claim numbers prefixed so the two parts can share a file; project-specific words generalised; paths
  to the research session's scratch folder removed. Nothing was added to a claim, and no status or kind was changed, except one correction: the research took G-C26's 0.57 for mid-production change; the D25 review opened the source's figure, and G-C26 and the "Answer first" line now say what it shows.

Disagreements, weak-support lists and unanswered questions are kept in full: Part G sections 6, 8 and 9; Part F "Where practitioners
disagree", "Famous stories with weak support", "Status of each question" and each "Unanswered within" entry.

---

# Part G: games

Scope is games; Part F covers film, TV and animation. The research was aimed at a small team of AI agents plus
one human owner, making a story-heavy browser game of layered stills and voices. Anything aimed at that case is
marked **inference**.

**Answer first.** The evidence base is thin and mostly self-report. It supports the owner's instinct in one
important form: frequent change to core design correlated -0.44 with outcome in the only large outcome
survey (G-C26), and teams do report expensive presentation or tech sunk into things later dropped (G-C3, G-C37). It does not support the
form "lock the story, then build": narrative studios cited here found story through play, kept text changeable
late, and in one case rewrote an ending after shipping it in the 1.0 release (G-C33, G-C37, G-C38). No controlled study was found on whether
rough assets mislead testers about mood or story. No game-specific measurement of the cost of late change
was found either. Both are recorded as unknown, not filled in.

---

## 1. Method and how to read this

**Status of a source**
- `opened`: I fetched the raw page or PDF and read its text. Copies stayed in the research session's scratch folder; they are not in this repo.
- `opened-part`: raw text, but read by keyword filter or excerpt, or only the abstract. The limits say which.
- `extract`: seen only through a search tool's summary. Wording not checked; never quoted here.
- `not opened`: named so a later pass can find it. Nothing here rests on it.

**Kind of evidence**
- `measured`: counts or statistics exist. Almost all are retrospective self-report or non-game; see limits.
- `practitioner`: a named person's account or opinion, with no data offered.
- `demonstrated`: a specific project did this and reported what happened. One case each; winners over-represented.
- `inference`: mine.

**Search budget:** 12 of 12 used; none refused. Everything after that used direct fetches of known pages. Log in section 9.

**Bias that applies to nearly everything below (inference from the sources' own caveats):** postmortems and
interviews come from games that shipped, written by the people who made them, often at promotional moments.
Studies of them count what authors chose to mention. Nothing here is a controlled comparison of production
orders on game outcomes; I found none.

---

## 2. What this adds to or contradicts in the existing skills

Read before D25 changed them: `agent-team/SKILL.md`, `gamedev-team-practices/SKILL.md`. The "skill says" column is the
text at that date.

| Skill says | Evidence here | Effect |
|---|---|---|
| agent-team Phases: vertical slice = "one section at final quality, which also tests the process", with everyone involved | Gilbert calls slices wasteful (G-C6). Manuel warns of "demo hell" eating production time (G-C1). A vendor's process doc describes a slice with some voice and rough or borrowed effects (G-C8) | **Contradicts as a default.** Final quality is one disputed option. Nothing measured supports it |
| agent-team Phases: prototype = "is the core mechanic fun, placeholder art" | Says nothing about story. Bromley separates comprehension from appeal and tests comprehension from storyboards, before code (G-C20) | **Adds** a story test before and alongside the mechanic prototype |
| agent-team: "Art and audio join once behaviour is stable" | Owner's direction adds story stability. Edith Finch: mechanics first, story late (G-C37). X7: art before story was reported as a serious problem (G-C16) | **Adds, with a dispute.** Order is contested; see section 6 |
| agent-team: "The user keeps the judgement of feel and look ... a human playtest is a milestone gate" | Bromley: tests synced to alpha or beta gates find problems too late to act on (G-C23). Internal players cannot test tutorials, new-player experience or difficulty (G-C24) | **Contradicts in part.** Owner judgement stays for look and feel; it cannot stand in for comprehension or appeal, and a milestone-only test is too late |
| agent-team: "Confirm a look or feel direction before the full build", one still first | Consistent with the "visual minimum" idea (G-C10) and the owner's direction | **Agrees** |
| team-practices: Alpha = features in, content may be placeholder. Beta = content complete | Agrees with the core of G-C2, but Mullich reports a client who believed alpha means final art, and one source puts all art final at beta and another adds "no changes" | **Adds:** the vocabulary is unsafe unless each milestone is written down, which the skill already says |
| team-practices: fresh players as often as possible; watch, don't explain; one tester's suggestion isn't a decision | Corroborated by Valve and Birdwell (G-C17, G-C18) | **Agrees.** Adds a hard constraint: story testers are one-shot and cannot be reused (G-C20) |
| team-practices: localization-ready; UI tolerates 30-40% longer text | Different quantity from the 10-20% voice-length figure in G-C14. Not a contradiction | **Adds:** string lock and its cost (G-C13); no contradiction |
| Neither skill | Kill criteria; order of locks; focus groups versus playtests; early release as a test; fix versus taste | **New** |

---

## 3. Answers by question

Each answer points to claims in section 4. Synthesis in these answers is **inference** unless a claim is cited for it.

### Q1. Stages and gates: answered in part
No published publisher milestone document was found. Definitions below come from a reference article, practitioner
blogs and one studio's own process, and they disagree (G-C1, G-C2, G-C3).

| Stage | Commonly meant to prove | Frozen at this point | Where sources disagree |
|---|---|---|---|
| Pre-production | The plan and the core idea | Nothing formally | End can mean a long design doc, a greybox plus art demo, or a polished slice (G-C1) |
| Prototype or greybox | One risky question | Nothing; throwaway | Whether it may look rough (G-C10, G-C11) |
| First playable | Representative play and assets | Nothing | Sometimes merged with alpha; "a few minutes" versus "major elements working" (G-C2) |
| Vertical slice | Quality bar, pipeline; often buyer approval | Often look and quality target | Whether it should exist, and how final (G-C1, G-C6, G-C8) |
| Alpha | Features complete, start to finish | New major features | Whether art may be placeholder (G-C2) |
| Code freeze | Stability | New code | Only Wikipedia's sources opened define it: 3-4 months before release, ahead of beta (G-C2) |
| Beta | Content and assets complete, bug-fixing only | Features, assets; one source says code too | Whether all art must be final (G-C2) |
| Content lock, script lock | Not defined by any source opened | Strings, for localization (G-C13) | **Unanswered as a formal definition** |

Gates in a studio's own process (G-C3) were kill points. Disconfirming: gates can pull testing late (G-C23) and slices can eat production time (G-C1). **No measurement of gates slowing teams was found.**

### Q2. Slice, prototype, greybox, and how polished a test must be: answered, with the key point unknown
- What each answers: a prototype answers one risky question; a slice answers "can we hit this quality with this pipeline, and will a buyer accept it" (G-C1, G-C6). Greybox answers layout and mechanics (G-C10). Storyboards answer story comprehension (G-C20).
- **Does rough art mislead testers about mood or story? Not known.** No controlled games study found (G-C9). Nearest evidence: non-game prototype studies find usability problems survive low fidelity (G-C11) but aesthetics affect emotion and how people rate looks (G-C12). One director reports his own team didn't feel a story's emotional weight until assets came together (G-C7). A vendor argues from a hypothetical (G-C10).
- Both sides: rough is fine for comprehension and usability (G-C11, G-C20). Rough can hide or distort emotional response (G-C7, G-C12) and public exposure while rough has cost real sales (G-C31).

### Q3. Order of work and locks: answered in part
- Measured late-change cost: **no game-specific measure found.** The largest software study found no general delayed-issue effect (G-C15). This is not creative rework, so it weakens the folk multiplier without replacing it.
- Script lock: Ingold reports the norm as about six months before ship, and rejects it (G-C33). Michet shows what lock is for: translators, loc QA and engineering, and that text can't lock early because design, art and voice keep changing it (G-C13).
- Voice: original-language recording normally starts before the game is finished, in several rounds that absorb script changes (G-C8). Vendors advise batching changes and using dummy voices (G-C14). Supergiant tried sample voices and had team members voice roles (G-C39). ZA/UM added full voice only in a later edition, after first release (G-C40). **What a story-led indie does per update was not established:** the Hades GDC talk was not watched.
- When art goes final: **no source gives a rule.** Evidence is indirect (G-C3, G-C12, G-C16, G-C37).
- Localization: starts from locked strings (G-C13). Vendors say to clean the source first since errors multiply per language (G-C14). Standard handbook not opened.
- Late changes handled: decoupled text pipelines (G-C33, G-C34), batched change sets (G-C14), as-recorded script tracking (G-C8), all-stakeholder decisions with reasons communicated (G-C26).

### Q4. Testing: answered for method; thin for narrative; nothing measured on fix versus taste
- Playtests versus focus groups: Valve excludes focus testing as a goal (G-C17). NN/g: groups report what people say, not do, and are only for discovering wants (G-C19). I found no games practitioner defending focus groups for design decisions; absence, not disproof.
- Sample: 6 / 12 / 100 by purpose (G-C21). 5 is contested (G-C22). Rounds matter more than round size (G-C21, G-C22). Large labs ran about 20 every other week (G-C18).
- Whom: target genre players, screened by making them recount story beats; not friends, family or industry; **never reused for story** (G-C20). Disputed by practice (G-C25).
- What to ask and measure: open "what just happened, what will happen next" per beat; rated interest in what happens next over time; emotion word list against intent; not "do you like it" or "any ideas" (G-C20). Avoid leading (G-C17, G-C20).
- Fix versus taste: **no study found.** Practitioner material suggests a split between observed failure against stated intent and preference (G-C17, G-C18, G-C20, G-C32). Proposed test in section 7, **inference**.
- Owner who is also the designer: cannot test what depends on not knowing the game (G-C24). A designer's certainty counted for nothing until the next test at Valve (G-C18). A vision holder resisted likely-popular feedback and thought it right (G-C32). No study of owner-designer feedback found.

### Q5. Why projects go wrong: answered, with weak data
Counted causes: G-C27, G-C28, G-C29. Production and management dominate; scope is reported in 71% of a 24-postmortem sample but about 12.5% of coded items in a 200-postmortem one, which count different units. Pre-production blame is asserted (G-C30), with no percentage found. Contradictions to common wisdom: methodology and team size show no correlation (G-C26). Crunch: G-C35.

### Q6. Small and narrative studios: answered for Failbetter, Supergiant, Inkle, Giant Sparrow; partial for ZA/UM; Annapurna via Edith Finch only
G-C31 to G-C42. Episodic and early release as test: Hades (G-C38), Sunless (G-C31, G-C32), Broken Age (G-C41), BG3 (G-C42), Lin et al. (G-C43). Inkle's Sorcery episodes: searched, nothing usable.

### Q7. What a producer does: answered weakly
Useful with some support: a short running log tied to a playable build (G-C44), kill gates with stated criteria (G-C3, G-C45), communicating changes with reasons (G-C26), real public roadmap (G-C46). Risk registers: **no credible small-team evidence found**; search 12 returned only low-quality pages. **Overhead at this size was not measured by anyone found.**

---

## 4. Claims

### Stages and gates

**G-C1. Milestones must be defined with stakeholders, and "end of pre-development" can mean very different deliverables; a polished slice can eat production time and trap a team in repeated client feedback ("demo hell").**
- Source: David Manuel (senior producer, Sony Computer Entertainment Europe), quoted in Game Developer, https://gamedeveloper.com/production/do-you-have-a-firm-definition-of-your-milestones- . Original feature page 1 via archive: https://web.archive.org/web/2013/http://www.gamasutra.com/view/feature/167831/a_producers_10_lessons_learned_.php
- Status: opened (news piece); opened-part (feature, first page only). Kind: practitioner.
- Corroboration: Mullich on client confusion (G-C2). Gilbert on waste (G-C6). Independent persons, no data.
- Limits: publisher-developer contract setting, larger teams, opinion. Early-2010s.
- Would change (inference): the producer writes what each milestone's deliverable is before work starts, and treats "one more demo pass" as a warning sign.

**G-C2. The vocabulary varies. Wikipedia's cited sources: first playable has representative play and assets, 12-18 months before release; alpha feature-complete with assets part-done; code freeze 3-4 months before; beta feature- and asset-complete with no changes, 2-3 months before. Mullich: first playable is a few minutes showing fun; alpha plays start to finish with much placeholder; beta has all art, audio and text final. His client had been told alpha means final art.**
- Source: https://en.wikipedia.org/wiki/Video_game_development ; David Mullich, https://davidmullich.com/tag/project-management/page/6
- Status: opened-part (both). Kind: practitioner and reference.
- Corroboration: search 7 returned blogs varying the same way (extract). **No publisher's own guideline was found.**
- Limits: timings reflect console and retail schedules. Mullich negotiates placeholder percentages, but his beta example as printed ("no more than 90% placeholder") looks garbled; don't reuse the figure.
- Would change (inference): never use a bare stage name in a brief; write what is frozen and what may be placeholder. Browser delivery has no certification window, so the months-before figures don't transfer.

**G-C3. One studio's gates are explicit kill points: market and persona research; concept with art styles and proof of concept; white-box prototype with select concept art and internal playtests; minimum viable product; soft launch on metrics. Its stated origin is a licensed project where high-polish narrative cutscenes came first, a payment model was retrofitted, and the project was cancelled.**
- Source: Mike Inglehart (Hothead Games), 2016, https://gamedeveloper.com/business/the-5-stages-of-greenlight-how-to-know-when-it-s-time-to-launch-your-game
- Status: opened. Kind: demonstrated, self-reported.
- Corroboration: for presentation-first failing, G-C16 is loosely similar. For gates, Cook (G-C45).
- Limits: mobile free-to-play; metrics gates don't apply to a premium story game before launch. Studio's own account of its own process, with success asserted and no comparison. The cutscene case failed on business model, not on story testing.
- Would change (inference): the closest thing here to a direct case for the owner's worry: expensive presentation before the thing it depends on was proven.

**G-C4. Valve's guidance: Early Access is for a playable alpha or beta. Too early if you are still finding what is fun or have only a tech demo; too late if gameplay is defined and you only need bug testing. It suggests keys to a small group of fans for the first case.**
- Source: https://partner.steamgames.com/doc/store/earlyaccess
- Status: opened-part. Kind: practitioner (platform policy).
- Corroboration: Failbetter on going too early (G-C31). Kasavin on timing (G-C38).
- Limits: says nothing specific to story games in what I read. Platform has its own interest.
- Would change (inference): a public test is a stage with entry conditions, not a cheap substitute for a private one.

**G-C5. Half of 24 shipped projects reported last-minute or very late feature additions or changes; six production problems were critical events happening later than they should have.**
- Source: Ara Shirinian, https://gamedeveloper.com/audio/dissecting-the-postmortem-lessons-learned-from-two-years-of-game-development-self-reportage
- Status: opened. Kind: measured (one analyst's count). Corroboration: Politowski's delays category, 3% of items (G-C28).
- Limits: see G-C27.
- Would change (inference): plan for late change as normal rather than assuming a lock will hold.

### Slice, prototype, fidelity

**G-C6. Ron Gilbert calls vertical slices one of the industry's dumbest ideas: wasted time and money, done to satisfy publishers. He supports careful pre-production and prototypes for risky play or tech. Games, he says, are built up in layers, not finished strip by strip; he notes some publishers don't ask for a slice.**
- Source: https://grumpygamer.com/vertical_slice (2011)
- Status: opened (full). Kind: practitioner.
- Corroboration: Manuel partly (G-C1). Against: the skill's table and common convention; Unity's vendor case for looks in tests (G-C10).
- Limits: opinion, one short post; written while working with a publisher that didn't want one; no data.
- Would change (inference): a producer doesn't default to a final-quality slice. If there's no buyer to convince, much of its stated purpose goes.

**G-C7. Ian Dallas says that until the parts came together late, What Remains of Edith Finch didn't seem emotionally demanding, because the team looked at crude models with no sound in a crashing build and didn't take it seriously as a prototype.**
- Source: Edge, reprinted at PC Gamer, https://www.pcgamer.com/uk/the-making-of-what-remains-of-edith-finch/
- Status: opened-part. Kind: practitioner, about one project.
- Corroboration: Sauer and Sonderegger (G-C12), weakly and from another domain. None in games.
- Limits: about the developers' own perception, not testers'. One retrospective. Hindsight.
- Would change (inference): don't conclude from a rough build that a scene lacks weight, or that it is safe. Sound and image may carry the emotion; test that scene separately.

**G-C8. In a localization vendor's description of normal audio production: prototypes have little original sound; a slice has some voice and rough or borrowed effects; recording for the original language starts before the game is complete and is rarely one session; further rounds absorb changed or added script and retakes; the recording team may change lines; changes get tracked as an as-recorded script.**
- Source: Lionbridge Games, https://games.lionbridge.com/content/dam/lionbridge-games/games-pages/insights/blogs/video-game-audio-from-start-to-localization-to-finish/recording-process-in-action-infographic-long-english.pdf
- Status: opened-part. Kind: practitioner (vendor).
- Corroboration: Supergiant's samples (G-C39). Michet: voice process changes text (G-C13).
- Limits: vendor, sells this service, generic; says it isn't one-size-fits-all.
- Would change (inference): "voice only after story lock" is stricter than normal practice. Normal is rounds, with a tracked as-recorded script as the source of truth.

**G-C9. No controlled study was found comparing placeholder and final art on testers' judgement of story or mood in games.**
- Source: searches 2 and 8 (section 9); the search tool's own summary also found none.
- Status: searched, absent. Kind: a "not known" result.
- Corroboration: none; nothing opened claims otherwise. G-C7, G-C11 and G-C12 are adjacent evidence only.
- Limits: 12 searches, not a systematic review. The Games User Research book (Drachen, Mirza-Babaei, Nacke, OUP 2018) was not opened and might address it. A juiciness literature exists but wasn't reached (G-C10).
- Would change (inference): the studio can't look this up. It can cheaply run its own: same scene, rough and finished, separate fresh testers, same questions. See section 7.

**G-C10. Unity argues that greybox skews playtest feedback and proposes a "visual minimum": recognisable silhouettes, colour separation, basic material variation. It says greybox stays right for pure mechanics, first-week concepts and layout tests. It argues generated art removes the old trade-off.**
- Source: https://unity.com/blog/placeholder-asset-problem
- Status: opened. Kind: practitioner (vendor).
- Corroboration: the "Juice It or Lose It" talk, cited by Unity, is about added effects, not fidelity and testers; not opened. Against: Cook says kill graphics and plot to get a playable (G-C44); Virzi (G-C11).
- Limits: **sells the asset store and AI generators it recommends.** Key example is a hypothetical ("might rate"). Says research supports it without giving a controlled comparison. Author and date not established.
- Would change (inference): useful as a checklist of what a rough test still needs, not as evidence that it works.

**G-C11. In two experiments (an electronic book, a voice-response system), low- and high-fidelity prototypes found substantially the same usability problems at correlated rates.**
- Source: Virzi, Sokolov, Karis, CHI 1996, https://doi.org/10.1145/238386.238516
- Status: opened-part (abstract via OpenAlex). Kind: measured.
- Corroboration: Bromley's use of storyboards for comprehension (G-C20), not as evidence.
- Limits: usability only, not mood, appeal or games. Old. Abstract only.
- Would change (inference): rough assets are probably safe for "do they get it, can they operate it". Doesn't extend to "do they feel it".

**G-C12. In a 60-person between-subjects study of mobile-phone tasks, a computer prototype overstated task time; users compensated for poor looks by overrating aesthetics of reduced-fidelity prototypes; emotions were more positive with the more attractive phone.**
- Source: Sauer and Sonderegger, Applied Ergonomics 2009, doi 10.1016/j.apergo.2008.06.006, https://pubmed.ncbi.nlm.nih.gov/18691696/
- Status: opened-part (abstract via PubMed). Kind: measured.
- Corroboration: G-C7, weakly.
- Limits: phones, not stories or games. Small. Abstract only. Doesn't show a rough test misranks story options.
- Would change (inference): treat ratings of looks on rough builds as unreliable. Attractive presentation may raise emotion scores, so don't compare scores across fidelity levels.

### Order of work and locks

**G-C13. Laura Michet: string lock means no text changes, usually for localization. Translators' time, loc QA and cost mean a line can no longer be freely fixed: a small phrasing fix could cost thousands of dollars across languages, engineering, QA and release. On Skin Deep, earlier locking would have been impossible because text kept being blocked or changed by design, art and the voice process. Many indie narrative games are never localized and can still change text in minutes.**
- Source: https://blog.lauramichet.com/ive-been-string-locking-since-september/ (2025)
- Status: opened (full). Kind: practitioner. Corroboration: Ingold (G-C33) on the same pressure; vendors (G-C14).
- Limits: the dollar figure is a rough impression, not a measurement. One writer.
- Would change (inference): lock order follows who depends on the words. Whether to localize is itself a decision about when text stops being cheap. With generated or machine translation the cost changes; **unknown by how much.**

**G-C14. Vendors: errors multiply by language count; voice startup fees make one-session recording cheaper; use dummy voices; send script changes in large batches; Russian runs about 10% longer and French or Spanish about 20% than English, which matters where video length is fixed.**
- Source: Alconost, https://www.gamedeveloper.com/audio/9-tips-on-localizing-audio ; Epic Sound, https://www.epicsound.com/game-localization/
- Status: opened-part. Kind: practitioner (vendors).
- Corroboration: each other, G-C13. Limits: selling these services; percentages unsourced and about general audio.
- Would change (inference): batch change sets instead of a stream, even with cheap generation, because each batch triggers review attention.

**G-C15. In 171 software projects (2006-2014), no evidence was found for a delayed-issue effect: issues resolved later did not consistently or substantially take more effort.**
- Source: Menzies, Nichols, Shull, Layman, https://arxiv.org/abs/1609.04886
- Status: opened-part (abstract). Kind: measured.
- Corroboration: none opened in games. The authors say the effect may occur intermittently in some project types, so it isn't refuted everywhere.
- Limits: **not games**; defects, not creative rework; effort, not assets redone. A rule built on a 10x late-change multiplier has no support here, but neither is late change shown to be cheap.
- Would change (inference): don't cite a multiplier. Estimate the actual downstream dependents of the change.

**G-C16. Former ZA/UM staff report X7 had no pre-production: other teams started production as soon as the writing pitch was approved, with art concepts underway before the story and characters were known. Lead writer Tuulik calls this a major problem for a narrative-led game. It was cancelled and the team laid off, despite a well-received internal demo.**
- Source: PC Gamer, 13 June 2024, https://www.pcgamer.com/gaming-industry/game-development/for-a-while-it-seemed-like-miracles-were-possible-and-with-them-redemption-a-follow-up-to-the-legendary-disco-elysium-might-have-been-ready-to-play-within-the-next-yearzaums-devs-loved-it-management-canceled-it-and-laid-off-the-team/ ; summary at GamesRadar.
- Status: opened-part. Kind: practitioner (reported, some anonymous).
- Corroboration: Hothead (G-C3) on presentation before foundation.
- Limits: ex-staff in a bitter dispute; **no single cause of cancellation is established**, and management decisions are heavily implicated, so this can't be read as "art before story kills games". The demo was liked anyway.
- Would change (inference): a warning about parallel starts with undefined story. Not evidence for a strict sequence.

### Testing

**G-C17. Valve's Ambinder: the playtest goal is fun, not bugs, not balance, "DEFINITELY not focus testing". Designs are hypotheses, playtests experiments. Direct observation is the richest, but observers and salient events bias it. Think-aloud gets at why, but disturbs play. Q&A suffers group biases, and people don't know why they do things. Valve's order: survey, individual Q&A, group Q&A, cautiously.**
- Source: Mike Ambinder, GDC 2009, https://media.steampowered.com/apps/valve/2009/GDC2009_ValvesApproachToPlaytesting.pdf
- Status: opened (slides). Kind: practitioner (experimental psychologist).
- Corroboration: NN/g (G-C19), Birdwell (G-C18), Bromley (G-C21).
- Limits: slides, not the talk; shooters and multiplayer; large-company resources. Pros and cons are listed, not measured.
- Would change (inference): the owner's phrase "focus group feedback" should become playtests. Anything said in a group follows individual answers.

**G-C18. Half-Life test sessions: one outside volunteer for two hours, a designer and level owner behind them, forbidden to speak or hint. About 100 action items a session; over 200 sessions, about half with repeat players; the first 20-30 taught the most. Testing settled design arguments: personal certainty counted for nothing until the next session.**
- Source: Ken Birdwell, https://www.gamedeveloper.com/design/the-cabal-valve-s-design-process-for-creating-i-half-life-i-
- Status: opened-part. Kind: demonstrated.
- Corroboration: Ambinder. Halo 3 also tested frequently: about 20 people every other week, 3,000+ hours from about 600 players, per Wired 2007 (https://www.wired.com/2007/08/ff-halo-2/, opened-part). Wired also reports the lab couldn't catch everything under Halo 2's time limits.
- Limits: linear shooter; repeat players are fine for mechanics, not for story (G-C20). Winners. Lab scale isn't available here.
- Would change (inference): the first sessions carry the most learning, so they should happen before investment. Silence is the rule that transfers; the volume doesn't.

**G-C19. NN/g: focus groups capture what people say, not what they do; run 6-9 people, more than one group; their proper role is finding out what users want, not evaluating use. To see whether people can operate something, watch one at a time.**
- Source: https://www.nngroup.com/articles/focus-groups/
- Status: opened-part. Kind: practitioner. Corroboration: Ambinder (G-C17).
- Limits: **not games**, and not story. Doesn't address whether a group can judge tone. No game-specific comparison of group and individual methods was found.
- Would change (inference): groups only for early wants, and with concrete examples; never to choose between story options.

**G-C20. Steve Bromley on story playtests. Two questions: comprehension and appeal. Comprehension can start from a storyboard or slide deck with one player at a time, asking open questions at each beat; repeat at milestones because format changes results (boards, greybox and final differ). Appeal: don't ask whether they like it or for ideas, which he says produces generic stories; ask interest in what happens next repeatedly and look for drop-off, and check a word list of feelings against the intended emotion. Time appeal tests for late pre-production or early production, when beats exist and change is still possible. Recruit from competing narrative games and make recruits recount story beats to prove attention. Players get one first time, so never reuse them. Exclude industry people, friends and family. Note that lab sessions don't simulate gaps between sessions; check back weeks later.**
- Source: https://gamesuserresearch.com/how-to-playtest-your-games-story/
- Status: opened (full). Kind: practitioner (named games researcher; sells services).
- Corroboration: Valve on open questions. **None measured, and nothing else specific to narrative was found.** The Busselle-Bilandzic scale (G-C47) is the nearest validated instrument, from film and TV.
- Limits: no data. Oriented to larger, often linear and secure-lab projects; he runs appeal tests quantitatively across many seats, which a small team may not reach. Against practice: G-C25.
- Would change (inference): **the single most directly usable source.** It makes the first test of a story game a slide deck, before any stills are final, and it makes fresh target players a scarce consumable to budget.

**G-C21. Bromley's per-round numbers: 6 to find problems (so a no-show leaves 5), 12 per user type to understand players, 100 for quantitative questions (about 10% margin; 400 for 5%). He says 5 is often misapplied to complex games. Multiple scoped rounds; Destiny reportedly over 150 playtests.**
- Source: https://gamesuserresearch.com/how-many-players-do-i-need-for-a-playtest/
- Status: opened-part. Kind: practitioner; the numbers are pragmatic and he says others may differ.
- Corroboration: Nielsen and Faulkner (G-C22). A primer by Graham McAllister reportedly suggests six per cohort (extract only; https://grahammcallister.notion.site/19-How-Many-Players-Are-Needed-0f37d27f41114790a1b64f3fbd925b40).
- Limits: not derived from narrative tests.
- Would change (inference): no percentage claims about appeal from six players. Six find failures; they don't size preference.

**G-C22. Nielsen: five users find about 85% of usability problems; run many small tests. Faulkner tested 60 users and sampled from them: random sets of 5 found between 55% and 99%; 10 raised the floor to 80%, 20 to 95%.**
- Source: https://www.nngroup.com/articles/why-you-only-need-to-test-with-5-users/ ; Faulkner 2003, https://link.springer.com/content/pdf/10.3758/BF03195514.pdf
- Status: opened-part. Kind: measured.
- Corroboration: they agree on 85% average and disagree on what that means.
- Limits: usability tasks, not games or story.
- Would change (inference): five is a floor with bad luck built in. Don't read a clean round of six as proof; a second fresh round is cheap insurance on a costly commitment.

**G-C23. Bromley: teams that treat testing as a tick-box sync it to alpha or beta, run one big study, and find problems they can't act on because of dependencies, expensive assets already invested or no time. Better: frequent small studies driven by a ranked list of assumptions.**
- Source: https://gamesuserresearch.com/when-should-i-run-playtests/
- Status: opened-part. Kind: practitioner.
- Corroboration: Birdwell's early sessions (G-C18). Disagrees with milestone gate as sole test (section 2).
- Limits: opinion; consultant's interest in more testing.
- Would change (inference): tests attach to commitments ("before we finish this scene's stills") rather than calendar milestones.

**G-C24. Internal playtests cannot test tutorials, the new-player experience or difficulty; "you are not your players". Community testers skew too: Discord members are more engaged, and teams that tuned difficulty on community feedback reportedly made games too hard and hurt new-player retention.**
- Source: https://gamesuserresearch.com/run-better-internal-playtests/ ; https://gamesuserresearch.com/run-a-playtest-with-your-discord-community/
- Status: opened-part. Kind: practitioner; the retention case is hearsay with no named team.
- Corroboration: Sunless Sea (G-C32) is a named instance of community skew.
- Limits: not owner-designer specific. **No study of owner-designer feedback found.**
- Would change (inference): the owner's notes are valuable for vision, look and feel, and invalid for "would a stranger understand this".

**G-C25. Edith Finch's credited playtesters included industry peers (Barlow, Druckmann, Hunicke, Kasavin, Killian), and Dallas says the team brought in parents for the infant story because parents reacted differently from non-parents.**
- Source: https://gameinformer.com/b/news/archive/2017/04/27/what-remains-of-edith-finch-had-some-of-the-best-playtesters-in-the-industry ; https://mcvuk.com/when-we-made-what-remains-of-edith-finch/
- Status: opened-part. Kind: demonstrated.
- Corroboration: none on peers; contradicts G-C20 on excluding industry.
- Limits: credit lists don't say how much weight peer views had. Winner.
- Would change (inference): two distinct cases. Experts give craft critique; they can't give naive comprehension data. And specific audience subgroups can be a required test where a scene depends on life experience.

### Why projects go wrong

**G-C26. Game Outcomes Project (2014 survey, 771 responses, 273 usable on shipped projects). Category correlations with an aggregate outcome: design risk management over 0.57 (Figure 1, read by the D25 review: the 0.57 is 'final game closely resembled the initial vision'; 'core elements frequently changed' is -0.44; explaining changes 0.45; stakeholders 0.32; a design document 0.17), team focus 0.50, crunch avoidance 0.44, team stability, communication, attitudes to failure, respect, planning, technology risk 0.36-0.39. Changes mitigated by involving stakeholders and explaining them. No significant correlation for methodology (waterfall, agile, Scrum, ad hoc; p=0.46), team size, duration, outsourcing, or team structure. Design documents under 0.2, significant for timeliness but not ROI or reviews. Detailed planning helps ROI and timeliness but not reviews. Treating deadlines as life and death: negative, and no gain on timeliness.**
- Source: Paul Tozour et al., parts 1 and 3, https://www.gamedeveloper.com/business/the-game-outcomes-project-part-1-the-best-and-the-rest , https://www.gamedeveloper.com/business/the-game-outcomes-project-part-3-game-development-factors , methodology http://intelligenceengine.blogspot.com/2014/11/game-outcomes-project-methodology-in.html
- Status: opened (part 3); opened-part (others). Figures showing exact questions and values are images I did not read. Kind: measured (survey).
- Corroboration: production dominance in G-C27 to G-C28. Against: none opened tests this directly.
- Limits, all material: **retrospective self-report by volunteers, not peer reviewed.** Outcomes are respondent-rated. Cancelled and abandoned projects excluded. Average team 48.6, range to 500, minimum about 3. **Category figures are the highest single question in a category, so inflated by selection.** Correlation only; the authors say turnover may be cause or effect, and that they did not measure innovation, so low design change may partly mean low ambition (they themselves say design often must evolve). A co-author leads a studio partly owned by a company whose executive is quoted against crunch, disclosed by them. Team-effectiveness results don't transfer to agents (inference).
- Would change (inference): the best available support for the owner's worry about change, and against spending effort choosing a process. It does not show that design shouldn't change: it shows disruptive change during development correlates with bad outcomes. Testing before commitment is one reading; "don't change" is another. The data can't separate them.

**G-C27. Shirinian counted 24 successive Game Developer postmortems, Feb 2008-Jan 2010, 120 "wrongs": 68 (56%) production. 16 of those 68 were scope, creep or resources (23%), 8 communication. Across postmortems, 17 of 24 (71%) reported scope problems; 9 (38%) time extensions; 9 crunch; 18 (75%) found iteration or rapid prototyping valuable; 5 used an agile process; 5 of 24 deliberately planned around team skills, all finishing under 2 years.**
- Source: as G-C5. Status: opened. Kind: measured.
- Corroboration: G-C28 on production share; Petrillo per Politowski on scope.
- Limits: 24 shipped games, one coder, one magazine, format forces exactly five wrongs and five rights; absence of mention means nothing, as the author says. Teams 5-265, averaging 2.4 years. He cannot separate publisher pressure from poor estimates. The 5-of-24 skill-planning finding is suggestive with tiny n and no causation.
- Would change (inference): assume a first estimate is too small. Don't treat "scope" as a single known cause.

**G-C28. Politowski et al. coded 200+ postmortems (1998-2018) into 1,035 problems: design 13%, technical 12%, team 10%, planning 8%, tools 8%, marketing 7%, testing 5%, communication 5%, feature creep 5%, cutting features 4%, bugs 4%, scope 4%, delays 3%, crunch 3%, budget 2%, documentation 2%, **prototyping 2%**. Groups: management and production about 45% each, business about 10%.**
- Source: https://arxiv.org/pdf/2001.00491
- Status: opened-part. Kind: measured.
- Corroboration: Ullmann (G-C29). Disagreement with Shirinian is apparent only; units differ: share of postmortems versus share of items. Scope, creep and cuts together are 129 of 1,035, about 12.5% (my arithmetic).
- Limits: only "what went wrong"; authors say problems are abstract; manual coding. Random sample of public postmortems.
- Would change (inference): design and technical problems outnumber scope in this count. "Lack of prototyping" may be underreported because a team can't easily see what it never tried; that's speculation, not a finding.

**G-C29. Ullmann et al. mapped 440 management problems to anti-patterns, from a curated dataset of 927 problems in 200 projects (the paper says management is 45%; 440 of 927 is 47%, so one figure is rounded or filtered differently): feature creep 33 cases and feature cuts 27 are the most common without a literature equivalent. Their suggested remedy for cuts: prototyping and playtesting to prioritise, and documented decisions made with all developers.**
- Source: https://arxiv.org/pdf/2202.06183 ; Status: opened-part. Kind: measured, then authors' interpretation for the remedy.
- Corroboration: G-C26 on involving stakeholders. Limits: their threats section: database doesn't represent the whole industry; manual mapping; not all pairs documented. Remedy isn't tested.
- Would change (inference): cuts are a distinct failure from creep, and a cut after assets exist is the costly form.

**G-C30. Pre-production is often blamed, but no count was found. Callele et al. say many failures trace to the transition from pre-production to production, specifically turning documents into production-ready form and catching implied information. A bachelor's thesis on postmortems names schedule, specification and scope, and lack of pre-production as a common cause. Politowski has prototyping at 2%, planning at 8%.**
- Source: Callele, Neufeld, Schneider, IEEE RE 2005, https://doi.org/10.1109/re.2005.58 ; Paulaharju, https://jyx.jyu.fi/handle/123456789/73536
- Status: opened-part (abstracts only). Kind: practitioner-grade (qualitative research, no counts in the abstracts); the thesis is bachelor level. Sample size for Callele not in the abstract.
- Corroboration: PC Gamer's X7 (G-C16) anecdotally.
- Limits: **a percentage for how often pre-production is blamed: not found.** Kasurinen et al., "Is Requirements Engineering Useless in Game Development?", was seen by title only: not opened; its title suggests a possible counterpoint and it needs checking.
- Would change (inference): the phrase "not enough pre-production" should not be cited as a measured cause.

### Small and narrative studios

**G-C31. Failbetter's Sunless Sea: core team three, about a dozen in all; development stretched from 6 to about 15 months as Kickstarter and Early Access money came in; roughly 90K raised (currency not stated in the postmortem), seven months in Early Access. Sold 50,017 during Early Access and 54,210 in the 31 days after release, against estimates of 5,000-50,000. Two major updates barely moved sales: one about 30% over the prior week, the real-time combat update about 200 sales. Sunless Skies, the sequel: Early Access sold about 15% of Sunless Sea's in the comparable period, and the studio said it went in too early and lost its promotional moment, also citing a changed market and a big Kickstarter having pre-sold copies. Four people were made redundant. The studio's public roadmap was the same as its internal one.**
- Source: Alexis Kennedy, March 2015, https://www.gamedeveloper.com/audio/postmortem-failbetter-games-i-sunless-sea-i- ; PCGamesN on the sales post, https://www.pcgamesn.com/sunless-sea/sunless-sea-doubles-most-optimistic-sales-estimates-but-big-updates-arent-the-cause ; Failbetter, https://www.failbettergames.com/news/failbetter-update-weathering-a-storm ; PC Gamer, https://www.pcgamer.com/au/failbetter-games-lays-off-employees-sunless-skies-delayed
- Status: opened (postmortem, Failbetter post); opened-part (others). Failbetter's original sales post not opened; figures come via PCGamesN. Kind: demonstrated, with reported numbers.
- Corroboration: Valve's too-early warning (G-C4); Kasavin on timing (G-C38).
- Limits: 2014 market; the studio attributes Skies to several causes and can't apportion them. Not a test of story at all; early-access gain here is mostly funding and systems.
- Would change (inference): distinct cases: private rough test is cheap; **public rough exposure can spend a one-time launch moment.** The owner's "don't over-invest early" doesn't apply to what goes on a store page.

**G-C32. Sunless Sea feedback: every Early Access review complained about combat, and the team threw it out and rebuilt it, delaying release; Kennedy thinks it saved a worse outcome, but it stayed less polished than if done from the start. Promising every old save would keep working meant veteran forum regulars stayed in the mid-game and the game got balanced for them; the early game stayed rough. He held ship speed slow against likely fun because he believed the mood depended on it, and thought a shared thematic vision the thing that went best; he calls wavering between CRPG and roguelike the biggest mistake.**
- Source: as G-C31. Status: opened (full). Kind: demonstrated.
- Corroboration: G-C24 on community skew.
- Limits: one retrospective written within weeks of launch; the author was creative director.
- Would change (inference): the cleanest named case here of fix versus taste: "dull and disruptive, in every review" was acted on; "go faster" was overruled on stated vision; the save promise shows a process choice can corrupt feedback. Don't let long-running testers set the opening.

**G-C33. Ingold on Heaven's Vault: 10 weeks before ship, in beta, he rewrote a whole scene in half a day alone, tested in isolation, with no other discipline involved. He says games are expected to lock scripts about six months ahead, which he calls a big ask, that films rewrite on the shooting day, that every scene was "traded up" late, and that this freedom costs fidelity. Authoring the pattern took about a year. About 30,000 dialogue lines, about four years.**
- Source: https://gamedeveloper.com/design/knockin-on-i-heaven-s-vault-i-how-inkle-designed-its-first-3d-game (May 2019); https://www.mcvuk.com/heavens-vault-how-inkle-wrote-its-own-herstory/
- Status: opened-part. Kind: demonstrated, practitioner claim of "no cost".
- Corroboration: G-C13 on the same dynamic; Kasavin on changing late (G-C38). Development length conflicts across sources: four years (MCV), or since 2014 (extract only).
- Limits: his own account; "no cost" means no coordination cost, and ignores the fidelity he concedes. I did not confirm the game's voice status from opened sources; his point rests on characters not needing reanimation. Tiny team with its own engine and language. Not representative.
- Would change (inference): **the key architectural lesson for layered stills: late story change is cheap only if the text is decoupled from image and voice.** Voice is what reintroduces lock pressure. Decide per scene which is bound to which.

**G-C34. Inkle chose 2D hand-drawn characters over 3D environments, animated only in keyframes, spending saved effort on more characters, gestures and places. Ingold says the look is what newcomers mention, but after 30 minutes they talk about what happened. The game had started as a 2D graphic novel. Failbetter's writers iterated through a web CMS whose data the client pulled, and that worked until hand-edited configuration grew painful; Kennedy wished they'd spent more on tools up front.**
- Source: MCV as G-C33; Kennedy as G-C31. Status: opened-part; opened. Kind: practitioner; demonstrated.
- Corroboration: each other on pipeline. Limits: Ingold's anecdote isn't a measurement; style reception was described as divisive.
- Would change (inference): limited motion can be a style rather than a placeholder, and that's an early commitment worth testing on its own terms. Tools for story iteration are worth early spend; the amount is project-specific.

### Crunch and other wisdom

**G-C35. Game Outcomes: crunch correlates negatively with aggregate outcome (-0.24, -0.30, -0.47, -0.36 by question; voluntary overtime +0.36) and with ROI. Testing the "salvage" explanation, a crunch-free model's residual showed no lift with crunch (-0.07, -0.1; p=0.24, 0.1). Edholm et al., by contrast, classify four types of crunch from postmortems and interviews and find one with only positive effects on product and schedule, while all raise stress; crunch is less pronounced where prioritising features is regular.**
- Source: https://www.gamedeveloper.com/business/the-game-outcomes-project-part-4-crunch-makes-games-worse ; Edholm et al., ICSE-SEIP 2017, https://doi.org/10.1109/icse-seip.2017.18
- Status: opened-part; Edholm abstract only. Kind: measured.
- Corroboration: Kennedy refused crunch and considered the game fine (G-C46), one case. Limits: as G-C26. Edholm's abstract doesn't describe the type or its frequency.
- Would change (inference): agents don't tire, so this doesn't transfer directly. Owner attention is the analogue: end-of-project review surges likely risk owner fatigue and bad calls, unmeasured.

**G-C36. Developers hesitate to automate tests because creative change makes tests quickly obsolete (14 interviews, 364 survey respondents).**
- Source: Murphy-Hill, Zimmermann, Nagappan, ICSE 2014, https://doi.org/10.1145/2568225.2568226
- Status: opened-part (abstract). Kind: measured (survey).
- Corroboration: G-C37's changing content. Limits: general game dev, older, not story content.
- Would change (inference): write checks against stable structure (story graph reachable, every line has audio or a scratch flag), not exact text, until a lock.

### Small and narrative studios, continued

**G-C37. Giant Sparrow on Edith Finch: started as a scuba simulator, abandoned because stories were hard to tell there. Built many prototypes with the story arriving "pretty late". Stories cut before characters were written, for confusing mechanics, technical difficulty or lack of an ending. A whole generation was cut late, with roles moved. Infinite-terrain tech took months and was never reused. The frame story arose from need, and existing stories then had to change to fit it. The hardest stories (Gregory, Lewis) were not sure things, and a stricter schedule would likely have cut them. Gregory's script draft was cut back once the situation itself carried the feeling.**
- Source: PC Gamer as G-C7; MCV as G-C25; https://gamingtrend.com/interviews/interview-ian-dallas-talks-about-ambiguity-cut-features-and-magic-in-what-remains-of-edith-finch ; GDC 2018 talk summary, https://www.gamedeveloper.com/design/video-weaving-13-prototypes-into-1-game-for-i-what-remains-of-edith-finch-i-
- Status: opened-part; the GDC talk itself not watched. Kind: demonstrated.
- Corroboration: Sunless (G-C32) on writing changing with art. Against: X7's complaint (G-C16).
- Limits: anthology with mechanics per story, publisher support, unusual time; the "stricter schedule" counterfactual is his judgement.
- Would change (inference): **a counterexample to "script first, then everything".** The studio should test the highest-risk scenes first, and cut before characters and art attach. In a game of stills and voice, those attach late, after the interaction carrying the scene works.

**G-C38. Supergiant: fewer than 20 staff, more than 22,000 voiced lines, Hades in Early Access, against the convention that Early Access suits story-rich games poorly. Kasavin treated launch as a pilot episode, updating every month or two, holding back the final outcome. Compared with Pyre, where three years of testing with dozens or hundreds of people still left him unsure, he got immediate reads on which characters and what humour worked. Hades 2 launched Early Access later with more content; main story beats were set early while details were explored; it spent 18 months there (about four fewer than the first); per GamesRadar, player feedback led to rewriting the divisive ending after it shipped in 1.0; script over 400,000 words, over 30,000 voice lines. He says launch far enough to play without many caveats, but not so late you can't respond.**
- Source: GDC session text, https://gdcvault.com/play/1026975/Breathing-Life-into-Greek-Myth ; GeekDad 2019, https://geekdad.com/2019/10/narrative-and-early-access-supergiants-greg-kasavin-discusses-hades-development/ ; GamesRadar 2025, https://www.gamesradar.com/games/hades/weve-learned-to-love-and-trust-the-process-how-hades-2-built-on-supergiants-early-access-legacy-to-deliver-the-best-roguelike-of-2025 ; Inven interview, https://www.invenglobal.com/datalab/articles/14783/supergiant-games-how-indie-developers-made-goty-hades
- Status: opened (session text); opened-part (rest). The talk was not watched. Kind: demonstrated.
- Corroboration: Valve on timing. Against: G-C31 Skies.
- Limits: **a replayable, non-linear roguelike with lines delivered by game state, where the loop works without story, and a famous studio.** A linear story spends its surprise once. Voice was partly in-house; recording-per-update workflow not established.
- Would change (inference): the pattern to take is structural: spine fixed, characters and details tested, ending last. Whether a linear stills-and-voice game can do this at all is **unknown.** Serialised release would be the nearest analogue.

**G-C39. Supergiant chose sample voices for each character to check the effect before committing, and team members voiced some roles, with Korb directing recordings and voicing the lead.**
- Source: Inven interview as G-C38. Status: opened-part. Kind: demonstrated.
- Corroboration: G-C8, G-C14 on scratch and dummy voices. Limits: one interview answer, little detail.
- Would change (inference): scratch voice is established practice in some form. Testing a voice before final casting is a cheap commitment; generated scratch voices can fill this role, with **unknown** effect on testers.

**G-C40. Disco Elysium's The Final Cut, after the 2019 release, added complete voicework: nearly 100 characters, about 1.2 million words, roughly 14 months of casting and recording, directed in-house, guided by player input. The game sold over five million copies. The original had only partial voice.**
- Source: https://en.wikipedia.org/wiki/Disco_Elysium (citing Hindpere) Status: opened-part. Kind: demonstrated, via a secondary source. Searches for budget and iteration found nothing usable.
- Corroboration: none on doing this as a strategy.
- Limits: this is not evidence of a test-then-voice plan; it's a success funding an upgrade. Survivorship is extreme. Writing process on the original: **not found.**
- Would change (inference): a text-first version that works can later earn voice. Full voice need not be at launch for a story game to succeed, which matters to an early-access decision.

**G-C41. Broken Age: a $3.45M Kickstarter (goal $400k). In July 2013 Schafer found the game wouldn't finish until 2015 and funds would run out; the game was split into two acts so sales of the first funded the second. Act 1 feedback led to harder puzzles in Act 2, which arrived about 15 months later than Act 1, later than first expected.**
- Source: https://en.wikipedia.org/wiki/Broken_Age Status: opened-part. Kind: demonstrated, via a secondary source.
- Corroboration: Sunless on money-driven scope growth (G-C31). Limits: **split for money, not as a test.** Secondary source.
- Would change (inference): episodic release is a financing and test option, but Part 1 fixes what Part 2 must honour, and a long gap is a cost. Kentucky Route Zero's episodes ran from January 2013 to January 2020 (https://en.wikipedia.org/wiki/Kentucky_Route_Zero, opened-part); cause not studied here.

**G-C42. Baldur's Gate 3: Larian released the first act in Early Access in October 2020; 2.5M+ players; revenue sustained the studio; Halsin was promoted to a companion because players liked him; scope grew; reviews fell below 75% at one point, which Vincke called a disaster.**
- Source: https://en.wikipedia.org/wiki/Baldur%27s_Gate_3 Status: opened-part. Kind: demonstrated, secondary.
- Corroboration: Kasavin on character reads (G-C38). Limits: large studio, licensed IP, very unlike this use. Secondary source.
- Would change (inference): an audience can change character weight, which is a story change. Only Act 1 was exposed, so later acts could still absorb the change.

**G-C43. Lin et al. studied 1,182 Early Access games: 15% of Steam at that time, 88% indie. Developers update more often during it; a lower share of players review, but ratings are higher, suggesting tolerance; positive review rate doesn't correlate with its length or update frequency.**
- Source: https://link.springer.com/article/10.1007/s10664-017-9531-3 (EMSE). Status: opened-part (abstract). Kind: measured.
- Corroboration: none on story games. Limits: reviews, not quality or sales. Not narrative-specific. Pre-2018 market.
- Would change (inference): early tolerance means early-release praise is not a clean signal of final reception. Don't over-update on either a high EA rating or update frequency.

### Producer practice

**G-C44. Daniel Cook argues long design docs actively harm games, and that a running design log, kept above a short concept, works better: daily play notes on the current build, each issue with a proposed solution, prioritised next steps, tasks done, and big experiments. Make a playable as soon as possible, killing graphics, features or plot if they stand in the way. Teams still need a repository of decisions and a shared vision.**
- Source: https://lostgarden.com/game-design-logs/ Status: opened-part. Date not confirmed. Kind: practitioner.
- Corroboration: Game Outcomes on documents (<0.2) in part (G-C26). Against: Manuel's plan-ahead stance (G-C1), and that same survey's timeliness correlation.
- Limits: opinion; no data; designer-led game loops, not narrative. A log of play notes is not a decision log in the formal sense.
- Would change (inference): the existing skill's decision logs and board already cover this. The add is tying entries to a played build. **Plot** as something to kill for a playable is exactly wrong if plot is the product; replace with what the test isn't about.

**G-C45. Cook: stage gates add iteration to portfolio thinking, with kill gates every few iterations and stated constraints; for a single product, treat features or scenarios as the units killed; kill gates that actually kill are what matter. Costs slightly more, and can cull long-term projects before they show promise unless gates are tailored. The Game Outcomes series reports Supercell celebrating kills: two launched, three killed that year.**
- Source: https://lostgarden.com/2007/02/19/rockets-cars-and-gardens-visualizing-waterfall-agile-and-stage-gate/ ; Supercell quote via Game Outcomes part 3 (the original 2012 interview not opened).
- Status: opened-part. Kind: practitioner, with one borrowed anecdote.
- Corroboration: Hothead (G-C3). Disconfirming: Edith Finch's fragile stories could have been cut under a harder gate (G-C37).
- Limits: 2007, portfolio and software; a one-game studio with one owner can't recycle resources to a sibling project. No measure.
- Would change (inference): in a single game, kill **units of story** rather than projects. Gate criteria should be written before the test so the owner cannot move them afterward. Set a protected list for high-risk, high-reward scenes.

**G-C46. Kennedy kept a public roadmap identical to the internal one; he says it helped sales and kept them realistic, though Valve then discouraged roadmaps. He told staff near launch not to crunch, cutting instead. Manuel says a skeleton crew of about 10% can lay foundations before staff join, and all projects, including cancelled ones, need postmortems with recommendations checked later.**
- Source: as G-C31 and G-C1. Status: opened; opened-part. Kind: practitioner.
- Corroboration: none opened on either point.
- Limits: Valve's current stance not checked here; Manuel writes for a large publisher. Skeleton crew doesn't translate to agents started per task (inference).
- Would change (inference): the board already serves as the internal roadmap; a player-facing one is a choice at public launch. A postmortem on each cut scene is likely overhead; one entry in the decision log is enough.

**G-C47. Instruments, not used directly in games here: Busselle and Bilandzic's validated narrative engagement scale has four dimensions (narrative understanding, attentional focus, emotional engagement, narrative presence), developed on film and TV. Mirza-Babaei et al. found observation finds most usability issues, while biometrics found up to 63% more in some categories concerning feeling and immersion.**
- Source: https://doi.org/10.1080/15213260903287259 ; https://doi.org/10.26503/dl.v2011i1.520 . Status: opened-part (abstracts). Kind: measured.
- Corroboration: none opened for either in story games.
- Limits: scale not validated on games here. Biometric result is from one study with lab equipment (size not in the abstract).
- Would change (inference): the scale's dimensions could shape a short survey. Biometrics are overhead at this size.

**G-C48. RITE: when a problem and fix are clear, change the prototype immediately, sometimes after a single participant, and retest with the remaining people; decision-makers join the research. Defined by Medlock, Wixon and others; publicly championed in Microsoft's games work.**
- Source: https://en.wikipedia.org/wiki/RITE_Method . Medlock et al. 2002 not opened. Status: opened (stub). Kind: practitioner via secondary source.
- Corroboration: frequent small studies (G-C23), loosely.
- Limits: known-good usability method by report; effect sizes not seen. Conflict with one-shot story testers is manageable because later testers get the fixed scene.
- Would change (inference): cheap agent turnaround fits this well: fix a comprehension failure between testers. But change only what's clear, or each tester sees a different story and appeal can't be compared.

---

## 5. Where traditional cost assumptions may not transfer (all inference)

No opened source measures any of this for an AI-agent studio. Treat each as a hypothesis to test.

1. **Art cost.** Greybox arose because decent art was slow (Unity says so, and sells the alternative). Per-piece generation weakens that reason. It does not remove what remains: owner attention per review, consistency across a set, and regeneration when a story change touches many scenes.
2. **Sunk cost shifts.** Traditionally money sunk is the reason not to change. Here a beautiful still may anchor the owner and agents to a scene even though it was cheap. Polish also shifts reviewers' attention to surface. Unmeasured.
3. **What's scarcest.** Likely not asset production but fresh target testers (one-shot; G-C20), the owner's attention, and consistency. A producer should budget those explicitly.
4. **Voice.** If actors are used, the traditional cost and lock logic hold (G-C8, G-C14). If generated, per-line retake cost falls, but direction, sync and continuity across versions remain. Whether testers respond differently to generated scratch voices is **unknown**. Voice laws, union terms and platform disclosure rules were not researched here and need separate checking before any commitment.
5. **Lock becomes consistency, not money.** A "lock" may be mostly about keeping dependents coherent and reviewed. Ingold's model (G-C33), isolated scene test plus decoupled assets, likely matters more than a date.
6. **Localization.** Machine translation may reduce per-language change cost; review burden and quality are **unknown**. Michet's dynamic (G-C13) applies to whatever remains human.
7. **Test cost doesn't fall with generation.** Human playtests cost the same, so the ratio shifts: building many variants is cheap and testing them isn't. Over-generating options that can't be tested is a likely new failure.
8. **Not transferable:** team-size, turnover, morale and crunch correlations (G-C26, G-C35), since agents aren't teams in this sense. Vision clarity and change communication may transfer as brief quality.

---

## 6. Where practitioners disagree

1. **Should a vertical slice exist, and how final?** Convention and the agent-team skill: one section at shipping quality. Gilbert: wasteful, done for publishers (G-C6). Manuel: agree it up front; polished slices can eat production (G-C1). Lionbridge: a slice has some voice and rough effects (G-C8). No measurement either way.
2. **How rough may a test be?** Cook: kill graphics and even plot to play sooner (G-C44). Bromley: storyboards for comprehension, changing the format changes results (G-C20). Unity: greybox poisons feedback, reach a visual minimum (G-C10, vendor). Dallas: rough builds hid weight from the team itself (G-C7). Virzi: usability survives low fidelity (G-C11). These may be answering different questions: comprehension and usability versus feeling (inference).
3. **Lock early or late?** Ingold: six-month locks are a big ask, late rewriting makes the game (G-C33). Michet: lock costs real money, and she wishes she'd locked sooner, while saying she couldn't (G-C13). Vendors: stabilise source before translation (G-C14). Likely resolved by what's bound to the text (inference).
4. **Story first or play first?** Edith Finch: prototypes first, story late (G-C37). Tuulik: art and production before story is a big problem for a narrative game (G-C16). Kennedy: began writing-led, then art and music changed the writing (G-C34). Supergiant: main beats early, details through feedback (G-C38).
5. **Who should test?** Bromley: target genre players, no industry, friends or family, no repeats (G-C20). Valve: half repeat players on a shooter (G-C18). Edith Finch: industry peers credited, parents for one story (G-C25). Sunless and Hades: public community (G-C32, G-C38), with Discord warning (G-C24). Likely separate purposes (inference).
6. **How many?** 5 (Nielsen), 6/12/100 (Bromley), 20 for robustness (Faulkner) or per lab round (Wired), 25-35 in a Microsoft approach as paraphrased by Short in 2009 (https://emshort.blog/2009/06/22/putting-together-a-play-test/, opened-part; the underlying article not identified).
7. **Do players decide?** Valve: "we don't know what's best, players do" for fun in shooters (G-C17). Bromley: don't defer artistic decisions (G-C20). Kennedy overruled likely feedback on pace (G-C32). Supergiant rewrote an ending because of it (G-C38). Hothead: kill on metrics (G-C3).
8. **Is Early Access good for story?** Convention: no, per Supergiant's own session text. Kasavin: a huge boon for Hades (G-C38). Failbetter: helped once, hurt once (G-C31). Valve: conditions (G-C4). Linear story is unaddressed by anyone opened.
9. **Plan or iterate?** Manuel: build the dam before the flood, and agile doesn't remove the problems (G-C1, G-C46). Cook: long plans are a stake through a good process (G-C44). Game Outcomes: method doesn't correlate; design stability does; detailed plans help ROI and schedule, not reviews (G-C26).
10. **Crunch.** Spector and Rubin (quoted in part 4) versus Paxton; Game Outcomes finds no lift, Edholm finds one beneficial type (G-C35).

---

## 7. What a game's first playable test should contain (draft, all inference)

Draft for a story-heavy, layered-stills, voiced browser game. No part is validated. Thresholds are placeholders to set per project: **no source gives pass numbers for story comprehension or appeal.**

**Before anything playable: a slide test.** The whole story as beats on slides, one fresh player at a time, open questions per beat (G-C20). Cost: a beat sheet and rough frames. Find out what's misunderstood before any scene gets stills.

**The build answers three questions, written down beforehand with pass and kill criteria:**
1. Comprehension: do they know who wants what, and what just happened? Asked per beat, open.
2. Appeal: do they want to know what happens next? Rated repeatedly; the shape over time is the finding (G-C20).
3. Interaction: does what the player does add to the story, or interrupt it? Observed behaviour (hesitation, skipping, abandon points).

**Content**
- The opening at length, enough to show drop-off (roughly 15-30 minutes is my guess; no source).
- The hardest scene on the plan, not the easiest: the one most likely to fail or be cut (G-C37). Easy scenes prove nothing.
- A real branch or choice if the game has them, so consequences can be tested.
- Everything on the target: a real browser and device, with a build stamp (existing skill).

**Fidelity**
- Visual minimum: consistent style, readable characters and expressions, clear staging (G-C10). **Generated stills are fine and are not final.** No retouching, movement polish or finishing.
- One style throughout, so the test measures story and not inconsistency.
- Scratch voice on lines where tone matters, flagged as scratch in the build. Rough or properly licensed music and ambience where mood is being tested (G-C7, G-C8). Otherwise text (G-C40).
- **One calibration:** the same scene in rough and finished form, given to separate fresh testers, same questions. Nothing published tells us how much rough misleads for this format; this measures it for the game under test and informs every later commitment. Keep it to one scene.

**Protocol**
- About six fresh players per round, screened from comparable narrative games by making them recount a story beat (G-C20, G-C21). Not friends, family, industry or returning testers.
- Observers silent (G-C18). Individual answers before any group talk (G-C17).
- Ask: what just happened; what do they want; what do you expect next; how interested are you in what happens next; pick words for how you feel, checked against the intended emotion. Do not ask: did you like it, what would you change, what if the story did X.
- Log time per beat, skip, replay, abandon point, choice taken.
- Optional check-in days later on what they remember (G-C20).
- Fix clear comprehension failures between testers (G-C48), but keep the story constant within an appeal comparison.

**The owner**
- Writes down predictions before the round, then watches. Plays separately, and their notes go in the log as taste or vision.
- Owner decides vision questions (G-C32). Owner cannot pass comprehension or first-impression questions (G-C24).

**Fix or taste (proposed test)**
| Signal | Call |
|---|---|
| Observed failure against written intent: misunderstood beat, abandoned scene, wrong emotion against target | **Fix.** Single sighting: investigate. Repeated across a round: act |
| Interest falls at the same point for several testers | **Fix or cut.** It is a measure, not an opinion |
| Stated preference with no effect on behaviour or understanding | **Taste.** Record; owner decides |
| Popular request that conflicts with a written vision point | **Owner decision,** with the reason logged (G-C32) |
| Suggested solution from a tester | Treat as evidence of a problem, not as the fix (team-practices skill) |
| A subgroup differs, for example parents (G-C25) | Ask whether that subgroup is the audience or a sensitivity to handle. Not a vote |

The "repeated" threshold isn't sourced; pick one per project and write it before the round.

**Not in this test:** final art, movement, touch-up, finishing, final VO, music final mix, localization, marketing assets, public release.

**What it can release:** a pass commits the next scenes' story and rough assets only, not their finishing. Finishing a scene waits for its own evidence. A fail changes or cuts the unit (G-C45), and is cheaper here than anywhere later. Public or store exposure is a separate gate with its own quality bar (G-C4, G-C31).

---

## 8. Common wisdom with weak support

| Common belief | What was found | Status |
|---|---|---|
| Late change costs 10x or exponentially more | No game measure found. Largest software study found no general effect (G-C15) | Weak in software; unmeasured in games |
| Methodology choice matters | No correlation in Game Outcomes (G-C26). Manuel agrees agile didn't remove problems | One self-report survey, but it is the only one found |
| Scope creep is the top cause | Common in postmortems (71% of 24), a modest share of problems (about 12.5% of 1,035). Units differ. Publisher pressure not separable (G-C27, G-C28) | Real, overstated as "the" cause |
| Weak pre-production causes most failures | Asserted (G-C30). No count found. Prototyping 2% of items, with reporting doubts | Unmeasured |
| Vertical slice at final quality is the proper proof | No evidence found for it; named opposition (G-C1, G-C6) | Convention |
| Rough tests are fine, or rough tests are poison | Neither shown for mood or story (G-C9) | Unknown |
| Five testers is enough | Sets of five ranged 55-99% in one study (G-C22) | Average holds, single-round confidence doesn't |
| Focus groups are how you test games | Practitioners opened argue against for design (G-C17, G-C19). No comparison in games | Weak, one-sided, not disproved |
| Early Access doesn't suit story | Hades suggests otherwise for one structure (G-C38) | Unknown for linear stories |
| Big updates drive Early Access sales | Small effect at Failbetter (G-C31) | One case, reported |
| Crunch rescues a late project | No lift in Game Outcomes (G-C35); Edholm finds one positive type | Contested, leaning against |
| Detailed design documents secure quality | Under 0.2; timeliness only (G-C26) | One survey |
| Small teams are an advantage | Team size no correlation (G-C26); cited in 7 of 24, including teams of 30-40 (G-C27) | Unsupported as a general claim |
| Lock the script, then build | Studios here change late, or get story from play (G-C33, G-C37, G-C38) | Not the practice of those opened |

---

## 9. What was searched, what is incomplete

**Searches used (12):**
1. Vertical slice criticism, polish versus prototype. Gilbert plus many unsigned SEO blogs (ignored).
2. Story playtesting and placeholder assets. Unity and small devlogs; no controlled study.
3. Script lock, scratch VO, localization timing, late change. Michet, vendors; no measured cost.
4. Postmortem cause counts. Shirinian, Politowski, Ullmann, thesis.
5. Failbetter Early Access. Postmortem and sales.
6. Hades Early Access and voice. GDC session text, interviews. Per-update recording workflow not found.
7. Milestone definitions. Blogs and Manuel; no publisher doc.
8. Playtester numbers, leading questions, narrative comprehension. Bromley, Short.
9. Edith Finch iteration, Firewatch. Edith Finch only; nothing on Firewatch.
10. Inkle iteration, Sorcery episodic. Heaven's Vault; nothing on Sorcery's release.
11. Disco Elysium production. Mostly studio-dispute coverage.
12. Producer decision logs, kill criteria, risk registers. Low quality; Hothead only worth keeping.

**Incomplete or unanswered**
- Q1: formal publisher milestone definitions and any formal content-lock definition. **Not found.**
- Q2: effect of rough assets on mood and story judgement in games. **Not known.**
- Q3: measured cost of late change in games. **Not found.** Rule for when art goes final: **not found.** Standard localization handbooks not opened.
- Q4: nothing measured on fix versus taste, or on owner-designer feedback. Microsoft sources reached only through Wired, Wikipedia and a 2009 paraphrase. Only Bromley is narrative-specific.
- Q5: percentage blaming pre-production. **Not found.** Washburn's figures known only via Politowski's summary: obstacles 37%, schedule 25%, process 24%, design 22% (abstract opened, https://doi.org/10.1145/2889160.2889253). Petrillo's 20-postmortem result known only via Politowski (https://doi.org/10.1145/1486508.1486521).
- Q6: Firewatch, Inkle's Sorcery, ZA/UM's writing process on the original: **not found.** GDC talks were not watched (Vault gated; Dallas 2018, Kasavin and Korb 2021).
- Q7: overhead of gates, logs or risk registers at this size: **not measured by anything found.** No named producer's account of small-team kill criteria was found. Gates slowing teams: only opinion (G-C1, G-C6, G-C23).
- Disconfirmation found: Manuel, Gilbert, Bromley on process; Dallas, Failbetter's Skies on being too rough; Kennedy on holding against feedback. Heavy-process failure with numbers: **none found.**

**Not opened; nothing here rests on them**
- Tim Cain on voice-over (wiki mirror behind a login). Side on audio localization (page didn't render; a 50-70% audio share of localization budget surfaced only in a search summary; not used). Polygon's slice definition (dsogaming, refused). Medlock et al. 2002 RITE. Kasurinen et al. 2017. Hicks et al. on juicy design. Heather Chandler's production and localization handbooks. Drachen, Mirza-Babaei and Nacke, Games User Research (OUP 2018). Mark Cerny's Method talk. Larian's own accounts. Wayline and other unsigned blogs in search results, deliberately.

**Reliability note:** the strongest source for production-order questions is a retrospective volunteer survey; the strongest for story testing is one consultant's guide. A rule written from this file should say that plainly, and where it picks a side, say it picked.

---

# Part F: film, TV, animation and motion comics

Scope: film, TV, animation, motion comics; Part G covers games. The research was aimed at a small team of AI agents plus one
human owner, making voiced layered stills with small accent movement inside a game, for example a serial with a free first
episode. Where a "Producer (inference)" line says "the free first episode", read that example.

## Read this first

**What the evidence can bear.** Most of it is practitioner testimony and single productions. I found no measured figure for what a change costs at each pipeline stage, none for how often films overrun, and none showing that testing improves films. "Change gets more expensive at each stage" is universally stated and reasonable, but in what I read it is never measured. A skill should not present it as a measured curve.

**The owner's rule, tested (inference).** "Finish only when we're happy with the story" matches what big animation does (F-C1 to F-C4) and what the closest small precedents report (F-C37, F-C38, F-C42). Three limits apply:
1. Holding back finishing does not make the story right. Lightyear had about seven full reviews and still lost an estimated $106M (F-C6).
2. A story reel cannot test how the finished look lands. Sonic's design failure showed up in a trailer of near-final work (F-C47).
3. At Pixar, peers review early and the public comes late. Reels are mostly tested by experts, not focus groups (F-C4, F-C5). A small team's early "audience test" has little direct precedent.

**Four different things are called "testing" (inference).** Rules should keep them apart, because they have different evidence and different uses:

| Case | Who sees it | When | What it can do |
|---|---|---|---|
| Peer review (Braintrust, Story Trust) | Experienced makers | Repeatedly, from early reels | Find story problems (F-C1 to F-C5) |
| Recruited test screening | 300-400 target viewers plus about 20 in a focus group | Late, on a cut | Find confusion, endings, pacing (F-C14, F-C15) |
| Pilot test | Sample audience | After a pilot exists | Diagnose elements and appeal; weak forecast (F-C26 to F-C28) |
| Exit poll (CinemaScore) | Paying opening-night viewers | After release | Forecast late earnings; too late to change anything (F-C22) |

## Access and kind labels

- **opened**: I read the source's own text directly.
- **extract**: read only through a summarising fetch. The wording is not checked, so nothing here should be treated as a quote.
- **not opened**: known only from a search-result summary or a citation on another page.
- Wikipedia pages are extracts. The sources they cite are **not opened** unless stated, even when named.
- **Kinds:** measured, practitioner, demonstrated in a production, inference. Numbers reported by the trade about one production count as "demonstrated in a production", not "measured".

---

## Numbered claims

### Q1. The pipeline as commitments

**F-C1. Pixar builds the whole film as a story reel (boards, scratch dialogue, temp sound and music) before animating, and remakes it about seven times.**
- Source: Steve Hullfish, Art of the Cut interview with Lightyear editor Anthony Greenberg, 2022-07-28, https://borisfx.com/art-of-the-cut-editor-anthony-greenberg-buzzes-through-lightyear
- Access: extract. Kind: practitioner.
- Corroboration: a Pixar editor says 7-8 full screenings before animation (Hollywood Reporter, https://hollywoodreporter.com/behind-screen/inside-editor-reveals-pixars-secret-803108, **not opened**, paywalled, search summary only). Hoppers had 8 (F-C3).
- Limits: one editor describing one film. These are recent Pixar productions at $150-200M. The count is not a studio rule.
- Producer (inference): plan for several full rebuilds of the story version, and budget for them as the job rather than as failure. Don't copy the number.

**F-C2. Brave's director rebuilt the reel four times in 18 months, tearing it down when it wasn't working. Animation followed the completed reel, and until the story worked nothing was safe, including characters.**
- Source: Jeffrey Peterson, KTAR, 2012-07-01, https://ktar.com/arizona-news/pixar-filmmaking-a-process-of-alchemy-says-brave-director-mark-andrews
- Access: extract. Kind: practitioner.
- Corroboration: consistent with F-C1.
- Limits: Brave is also a case of a replaced director (F-C24), so this describes a rescue rather than a normal run. The cost of the reel is not stated. The extract infers "far less expensive" rather than reporting a figure.
- Producer (inference): show the reel rather than argue from a script or outline. A problem should be seen and felt before it is debated.

**F-C3. Hoppers: six years of development, eight Brain Trust screenings, public tests starting around year three or four. Audience tests led to a scene being added because viewers didn't understand the lead's home life.**
- Source: Drew Taylor, TheWrap, 2026-03-06, https://www.thewrap.com/creative-content/movies/pixar-hoppers-making-of-process
- Access: extract. Kind: demonstrated in a production.
- Corroboration: a single film, in the same pattern as F-C1.
- Limits: promotional-window press. No comparison with a version that wasn't changed.
- Producer (inference): audience diagnostics can be cheap to act on when they lead to a small added scene. That only works if story changes are still cheap at that point.

**F-C4. Lightyear's reviews ran about 12-18 weeks per cycle. The editor started in May 2018, and the first public previews were two screenings in October 2021, about eight months before the June 2022 release.**
- Source: as F-C1. Release date from https://en.wikipedia.org/wiki/Lightyear_(film).
- Access: extract. Kind: demonstrated in a production.
- Corroboration: story artist Kelsey Mann describes screenings about every three months (Screen Rant, https://screenrant.com/pixar-onward-storytelling-high-bar-story-artists-kelsey-mann/, **not opened**).
- Limits: one film's timeline, and the elapsed-time reading is mine. COVID may have shifted the schedule; not checked.
- Producer (inference): a rhythm of review, rebuild, review seems to be the unit of work. For a small team, the cycle should shrink to fit the work, not stay at months.

**F-C5. The Braintrust gives suggestions and the director decides.**
- Source: Longreads excerpt of a Fast Company piece drawn from Catmull & Wallace, *Creativity, Inc.*, https://longreads.com/2014/03/13/the-secret-behind-pixars-storytelling-process/
- Access: extract. Kind: practitioner.
- Corroboration: Greenberg says only directors and creative leadership attend, no executives (F-C1). But see F-C24, which limits this.
- Limits: Catmull describes his own company. The book, the Harvard Business Review article (https://hbr.org/2008/09/how-pixar-fosters-collective-creativity, only the opening came through) and the Fast Company piece (403) were not read in full.
- Producer (inference): separate who advises from who decides, and write that down.

**F-C6. Reels don't guarantee a good result. Lightyear had about seven reviews, cost about $200M, and lost an estimated $106M.**
- Source: Wikipedia, Lightyear, citing Deadline, https://en.wikipedia.org/wiki/Lightyear_(film); review count from F-C1.
- Access: extract. Kind: demonstrated in a production.
- Corroboration: The Good Dinosaur (F-C24, F-C33) and Gigantic (F-C33) also went wrong at studios using this style of review.
- Limits: analysts blamed competition, the missing Toy Story characters and marketing confusion, not necessarily story. One film; no counterfactual. Deadline's loss figure is an estimate.
- Producer (inference): passing peer review means the story is coherent, not that an audience wants it. A rule shouldn't treat the two as the same.

**F-C7. Anime's order: script, storyboard, layout, revisions, key animation, in-betweens, finishing and backgrounds, photography and edit, dialogue and music, final master. Key animators draw layouts that the director and animation supervisor correct, then supervisors correct key frames too.**
- Source: Kanzenshuu, unnamed author, last modified 2019-12-30, https://kanzenshuu.com/animation-production/process. Stage order also in ANIME FREAKS / Abema studio tour report, 2026-03-06, https://times.abema.tv/en/articles/-/10229971?page=2
- Access: extract. Kind: practitioner (fansite drawing on official guidebooks and Toei's site; the Abema piece is a press tour).
- Corroboration: the two agree on order.
- Limits: the first is mainly Toei's Dragon Ball pipeline. The fansite gives drawing counts (3,000-5,000 per older episode, 3,000-4,000 now with about 300 backgrounds), which aren't independently checked.
- Producer (inference): layout is a separate checked gate between story and movement. The motion comic equivalent is the layered composition of a shot, checked before any motion is made.

**F-C8. Anime records dialogue after animation, sometimes during it if behind, unlike US pre-recording.**
- Source: Kanzenshuu, as F-C7. Abema report also places voice recording in post.
- Access: extract. Kind: practitioner.
- Corroboration: the two sources agree on Japan. The contrast with the US matches F-C1's scratch dialogue, but I opened nothing that states the US order as a general rule.
- Limits: Toei practice; other studios were not checked.
- Producer (inference): voice order is a choice, not a law. It depends on which is cheaper to change, voices or pictures. On a project with unknown voice costs, decide this explicitly.

**F-C9. A TV anime episode typically takes two to three months, with teams rotating so that a series fits in a year. Storyboarding counts as pre-production, often without a binding budget. Real schedules rarely follow the sample, with early episodes overworked and late ones rushed. Delays are more common than announced.**
- Source: kViN, Sakuga Blog, 2021-11-28, https://blog.sakugabooru.com/2021/11/28/anime-production-schedules/
- Access: extract. Kind: practitioner (critic drawing on industry conversations, little data).
- Corroboration: Abema mentions late material being pushed to meet the V-edit deadline.
- Limits: mostly the author's reporting. Single-title examples. The author warns that averages hide wide variation.
- Producer (inference): a serial's danger is spending on the first episodes and starving the later ones. The free first episode may make this worse. Budget all planned episodes together before finishing the first one.

**F-C10. Anime handles schedule pressure by planning where quality drops. Kaguya-sama let one skit sag so it could be solo-animated, and Mob Psycho 100 II scheduled a key episode early around a director's military service. Wonder Egg Priority finished episodes hours before broadcast and ended over three months behind.**
- Source: as F-C9. Access: extract. Kind: demonstrated in a production.
- Corroboration: none independent.
- Limits: the author's readings of productions he didn't run.
- Producer (inference): decide in advance which shots get the money and which may stay plain, instead of letting the deadline decide.

**F-C11. Miyazaki works against the rule: production starts before the story is finished, the story develops while he storyboards, and he doesn't plan the ending. Spirited Away was planned at about 1,200 shots and needed 1,415. He admits the method is risky and that he would prefer another way.**
- Source: Tom Mes, Midnight Eye, 2002-01-07 (Paris press debate, December 2001), http://www.midnighteye.com/interviews/hayao-miyazaki/
- Access: extract. Kind: practitioner.
- Corroboration: none opened.
- Limits: this is an exceptional auteur with his own studio. Audience testing isn't discussed. Staff have to adapt to him.
- Producer (inference): the sharpest counterexample, and it worked because one author held the story and the studio absorbed the risk. It does not support finishing art early in a small team, where a rework costs the same people's time.

### Q2. Locks

**F-C12. Practitioners say a true picture lock has been eroding for decades. One mixer describes a network ordering recuts after ten episodes had aired, changing 25-33% of each 22-minute episode. The least-cut episode of one series had 211 changes to fix.**
- Source: Production Expert panel, 2020-08-27, https://www.production-expert.com/home-page/2020/8/27/re-conforming-how-do-we-handle-the-lack-of-a-picture-lock-expert-panel
- Access: extract. Kind: practitioner.
- Corroboration: CineMontage (Jennifer Walden, 2022-07-07, https://cinemontage.org/?p=58831) says picture, sound and VFX increasingly run in parallel and new cuts arrive during the final mix. Detective Pikachu's VFX changes arrived after the printmaster, described as rare.
- Limits: sound people's view, in an article about reconforming. No frequency given. No costs given.
- Producer (inference): a lock is a coordination agreement, not a physical barrier. A rule should state what happens when it breaks, rather than pretending it can't.

**F-C13. The cost of reconforming after a lock runs from routine to severe. On a small job, regenerating files and conforming a late change takes about a day. Clients assume it takes minutes, and re-versions are often under-booked. 5.1 takes far longer than stereo. New material may have to be rebuilt from scratch.**
- Source: Jeffrey Fisher, ProSoundWeb, 2012-09-14, https://www.prosoundweb.com/in-the-studio-the-audio-post-workflow/3/; Production Expert panel, as F-C12.
- Access: extract. Kind: practitioner.
- Corroboration: two independent sources agree on the direction. Glossary pages agree too but carry no figures (Wikipedia Picture lock, https://en.wikipedia.org/wiki/Picture_lock, where key sentences are tagged citation needed).
- Limits: **nothing measured**. One figure ("about a day") is from one small-scale engineer. No dollar figures for reconform, ADR or final mix were found.
- Producer (inference): before enforcing a lock, measure what a change costs in this pipeline. In a digital layered project it may be small for some layers and large for others (hand-tuned timing to voice, for example).

**Unanswered within Q2.** What I searched: one search on picture lock, reconform, ADR, mix cost. No source I opened defines "sound lock", gives an ADR percentage, or documents when colour is finished. Wikipedia's Dubbing page covers ADR's purpose without figures (https://en.wikipedia.org/wiki/Dubbing). Wikipedia's claim that colour and VFX finish from the locked cut is tagged citation needed. Lock-breach costs: no measured data found. Reshoot cases in F-C47 to F-C49 are single productions. Treat this question as partly answered.

### Q3. Testing stories before finishing

**F-C14. How a recruited test works: 300-400 people, with spec'd demographics, excluding those who reject the genre. About 1,400 confirms for 300 attendees. A questionnaire, then a focus group of about 20. Scores are the percent who would definitely or probably recommend.**
- Source: Matt Maytum interview with Kevin Goetz, Total Film, January 2022, https://kevingoetz360.com/wp-content/uploads/2022/01/Kevin-Goetz-Total-Film-Magazine-Jan-2022.pdf
- Access: opened. Kind: practitioner.
- Corroboration: Il Post (2022-03-08, https://www.ilpost.it/2022/03/08/film-test-screenings/, extract) relays the same two questions from BBC. Goetz's Substack (2025-06-24, https://kevingoetz360.substack.com/p/inside-the-room-how-audience-test, extract) repeats the method.
- Limits: Goetz sells this service and promotes a book. He says fewer than 10 of about 7,000 titles needed no change, a number from someone paid to find changes.
- Producer (inference): a team of this size can't get a score that means anything. With a few viewers, use confusions and retellings, and don't calculate a percentage.

**F-C15. About 90% of widely released US studio films go through at least one test screening, averaging three, with some reaching ten or fifteen.**
- Source: Goetz to Nicholas Barber, BBC Culture 2022 (https://www.bbc.com/culture/article/20220124-the-iconic-hollywood-films-transformed-by-test-audiences, **not opened**, blocked), relayed by Il Post and by Wikipedia (https://en.wikipedia.org/wiki/Test_screening).
- Access: extract. Kind: practitioner.
- Corroboration: **none independent**; both relays trace to one interested person.
- Limits: applies to major studio wide releases. Self-reported.
- Producer (inference): near-universal use shows that studios pay for it, not that it works.

**F-C16. Scores can flatter. A "90" may be top-two boxes only. Goetz advises asking for "excellent" and "definitely recommend" separately, comparing against genre norms, and telling good confusions (intrigue) from frustrating ones.**
- Source: Goetz Substack, as F-C14. Access: extract. Kind: practitioner.
- Corroboration: Bader says dramas generally test better than comedies, so scores aren't comparable across formats (F-C26).
- Limits: unvalidated distinctions. The article has no data.
- Producer (inference): for a story that withholds information on purpose, keep the good/frustrating confusion distinction. A viewer not knowing something can be the point.

**F-C17. Goetz says "definitely recommend" predicts word of mouth and is a reliable indicator of commercial success. He offers no data.**
- Source: as F-C16. Access: extract. Kind: practitioner.
- Corroboration: **I found no study of recruited-screening scores against box office.** Searched twice (see Q3 status); academic database APIs returned 429s, so this is "not found", not "doesn't exist".
- Limits: commercial interest. Test results are generally proprietary.
- Producer (inference): don't treat a positive test as a prediction of the free episode's conversion rate.

**F-C18. Film revenue is Pareto-distributed with infinite variance over 2,000+ films. The authors conclude forecasts have essentially no precision and that the audience decides, through word of mouth that follows too many paths to attribute causes.**
- Source: De Vany & Walls, *Journal of Cultural Economics* 23(4), 1999, abstract via https://ideas.repec.org/a/kap/jculte/v23y1999i4p285-318.html
- Access: extract, abstract only. Kind: measured.
- Corroboration: consistent with TV executives in F-C26. F-C20 and F-C19 argue the other way.
- Limits: theatrical box office; the paper's sample is 1999 and earlier. I read the abstract only, so I can't say whether pre-release audience measures were among its predictors. Measured for revenue distribution, not for story quality.
- Producer (inference): commit in small stages because no one can know the outcome, not because tests will reveal it.

**F-C19. MOVIEMOD: a roughly three-hour consumer clinic forecast Groundhog Day at $69.4M against an actual $70.8M (n=140), and Shadow Conspiracy in Rotterdam at 19,352 attendees against 18,612. Hollywood had not adopted it by 2001.**
- Source: Knowledge at Wharton, 2001-03-19, https://knowledge.wharton.upenn.edu/article/marketing-science-meets-hollywood/; paper: Eliashberg, Jonker, Sawhney & Wierenga, *Marketing Science* 19(3), 2000, https://econpapers.repec.org/RePEc:inm:ormksc:v:19:y:2000:i:3:p:226-243 (**not opened**).
- Access: extract. Kind: measured, on two films.
- Corroboration: none independent.
- Limits: two films, reported by the authors' institution. The Rotterdam figure used an updated media plan. It forecasts marketing response to a finished film; it does not test story.
- Producer (inference): the forecast method does not apply before finishing. Use only as a counterweight to "nothing can be predicted".

**F-C20. Script text alone may help greenlight: a model combining screenwriting expertise, natural-language processing and statistical learning improved holdout gross ROI over current practice.**
- Source: Eliashberg, Hui & Zhang, *Management Science* 53(6), 2007, abstract via https://ideas.repec.org/a/inm/ormnsc/v53y2007i6p881-893.html
- Access: extract, abstract only. Kind: measured, per the authors.
- Corroboration: not searched further.
- Limits: the abstract gives no sample size or accuracy. Commercial vendor claims (for example Slated, https://help.slated.com/en/articles/31569, **not opened**) are unpublished and uncheckable.
- Producer (inference): low priority. Don't adopt script scoring on this evidence.

**F-C21. Testing unfinished work is routine, and I found no account of how results are corrected for it. Goetz says effects-heavy films are tested before scenes are finished (The Invisible Man before the invisible man existed, Planet of the Apes with Serkis visible, Beauty and the Beast at about 5% animated), and that those versions already have music and story.**
- Source: Il Post, as F-C14, relaying BBC. Access: extract. Kind: practitioner.
- Corroboration: F-C23 and F-C34 show audiences responding to work in a mixed state of finish.
- Limits: which Beauty and the Beast is unclear from the relay (5% conflicts with 70% in F-C23 if it's the same event). **No source found on whether unfinished effects lower scores, or how researchers correct for it. No controlled comparison found. This sub-question is unanswered.** Searched once specifically. Goetz's book wasn't available.
- Producer (inference): don't assume a viewer discount, and don't publish scores across finish levels. Compare like with like. Prototype-fidelity research in software might help (lead only: Walker, Takayama & Landay 2002, https://journals.sagepub.com/doi/10.1177/154193120204600513, **not opened**, 403; its content is not verified and nothing here rests on it).

**F-C22. CinemaScore polls paying opening-night viewers on cards, about 400 per film in five cities, and its grades track later earnings. From 2004-2014, A+ films earned about 4.8 times opening weekend, A films 3.6, C films 2.5. Grades are inflated toward fans and vary by genre. The founder's forecasts ranged from exact to off by about half (Taken: predicted $70M, earned $145M).**
- Source: Wikipedia CinemaScore (citing Busch, Deadline 2014), https://en.wikipedia.org/wiki/CinemaScore; Goldstein, LA Times 2009, reprinted on CinemaScore's own site, https://www.cinemascore.com/press/cinemascores-box-office-swami/
- Access: extract. Kind: measured (the multiples, by a trade analyst, method not seen), practitioner (forecasts).
- Corroboration: the two sources overlap; the accuracy examples were chosen by the article and the company. No independent audit.
- Limits: measures finished films, too late to change anything. The search tool also surfaced r=0.51 over 249 films from a blogger I couldn't identify; I have **not used** that figure.
- Producer (inference): after-release data can guide later episodes in a serial, which films can't do. That's the transferable idea, not the grade.

**F-C23. Beauty and the Beast (1991) played at the New York Film Festival about 70% finished, with storyboards and pencil tests for the rest, and reportedly drew a ten-minute standing ovation.**
- Source: Wikipedia, citing Solomon 1991 and others, https://en.wikipedia.org/wiki/Beauty_and_the_Beast_(1991_film)
- Access: extract. Kind: demonstrated in a production.
- Corroboration: none opened.
- Limits: festival crowd and publicity event, not a recruited test. Some finished sequences had been reverted to earlier stages for the screening. Applause is not a measure of comprehension.
- Producer (inference): mixed-finish work can hold an audience. It does not show that rough work tests fairly.

**F-C24. Peer-review advice is not the whole authority. Directors have been replaced on several films: Brave (Chapman to Andrews, 2010; reasons disputed, she says not creative), Ratatouille (Pinkava, then Bird, 2005), The Good Dinosaur (Peterson removed by mid-2013), Toy Story 2 (Lasseter took over), Kingdom of the Sun (Allers stepped down).**
- Source: Wikipedia, https://en.wikipedia.org/wiki/Brave_(2012_film), https://en.wikipedia.org/wiki/Ratatouille_(film), https://en.wikipedia.org/wiki/The_Good_Dinosaur, https://en.wikipedia.org/wiki/Toy_Story_2, https://en.wikipedia.org/wiki/The_Emperor%27s_New_Groove
- Access: extract. Kind: demonstrated in a production.
- Corroboration: each from named press via Wikipedia; underlying sources not opened. Chapman's and management's accounts differ.
- Limits: selected failures. Number of films where no change occurred not counted here.
- Producer (inference): "the director decides" holds until leadership stops trusting the story. In a studio where the owner holds both roles, no such backstop exists (see "Unanswered within Q8").

**F-C25. Testing can mislead or be misused.**
- The Magnificent Ambersons: after previews RKO cut over 40 minutes, reshot the ending and destroyed the negatives. Rosenbaum counted the 125 original cards and found 53 positive, about 42%, challenging the standard "hostile audience" story. Cuts and reshoots: $104,164; loss $620,000.
- Kingdom of Heaven: about 45 minutes were cut at the studio's request. Scott blamed over-attention to previews, and the longer director's cut was reviewed far better.
- Troy: a score was replaced after test audiences found it too brassy; later critics preferred the original (fan-site sources).
- Source: Wikipedia, https://en.wikipedia.org/wiki/The_Magnificent_Ambersons_(film), https://en.wikipedia.org/wiki/Kingdom_of_Heaven_(film), https://en.wikipedia.org/wiki/Test_screening
- Access: extract. Kind: demonstrated in a production.
- Corroboration: Ebert (2004, via Wikipedia) distinguishes filmmaker use from executive use as a weapon. Ang Lee's Picasso objection (Total Film, opened).
- Limits: the longer-cut comparisons are later reviews by a self-selected audience. Scott's attribution is his own. No counterfactual for any case.
- Producer (inference): read the cards, not the mood in the room. Test results should never go straight into destructive changes; keep every earlier version.

### Q4. TV development

**F-C26. Pilot testing forecasts poorly but diagnoses usefully. ABC's Bader says it will never tell you if something will succeed, but helps with tone and what people latch onto. Fox's Beckman says unconventional pilots usually test poorly and aren't necessarily dropped. An unnamed NBC executive says hits often sit in the middle to upper-middle range. The WB skipped testing in 2004 and later resumed.**
- Source: Christopher Lisotta, TVWeek, 2005-05-02, https://www.tvweek.com/?p=45166
- Access: extract. Kind: practitioner.
- Corroboration: F-C27 says the same about diagnostics, disagrees on forecasting.
- Limits: network executives in 2005. One unnamed.
- Producer (inference): the WB's trip out and back is the interesting part: dropping testing didn't stick, and neither did trusting it.

**F-C27. A network researcher reports strong-testing pilots were more than twice as likely to succeed as moderate ones in one network's study; weak ones rarely succeed; most test poorly. TV's success rate was around 25% most seasons. He advises testing individual elements, asking many questions, not using results as a report card or a weapon, and that concept tests rarely kill a show.**
- Source: Tim Brooks, NBC, 1983, https://timbrooks.net/?p=156 and USA Network, 1991, https://timbrooks.net/program-research-1991/
- Access: extract. Kind: practitioner reporting a measured internal study.
- Corroboration: the study itself isn't published; Brooks refuses to give norms.
- Limits: a researcher defending his field. 1980s-90s broadcast TV. The study's method isn't given. NBC tested 35 pilots in 1983, with pilots costing $500,000 to over $1M then.
- Producer (inference): test elements (who do you follow, what confused you) rather than a single "would you watch?".

**F-C28. Famous "tested badly" stories hide changes made after the test. Brooks says Hill Street Blues tested poorly is only half true: the bottom line was negative, viewers liked some characters, and changes followed. The Seinfeld pilot's 400-household test was very poor, and an executive gave up development money to get four more episodes.**
- Source: Brooks 1991 as F-C27; https://en.wikipedia.org/wiki/The_Seinfeld_Chronicles (citing TV Guide 2014, https://www.tvguide.com/News/Seinfeld-Research-Memo-1083639.aspx, **not opened**).
- Access: extract. Kind: demonstrated in a production.
- Corroboration: TVWeek (F-C26) also notes Seinfeld tested poorly.
- Limits: survivorship. Shows that tested badly and failed aren't retold.
- Producer (inference): a weak result is a reason to find out why before cutting anything. It doesn't excuse ignoring the result. Keep the list of what would have to change.

**F-C29. Babylon 5 planned five years in advance, with a trap door for every character. It used them when actors left, kept scripts about six episodes ahead, filmed a finale during season four in case of cancellation, and re-planned season four when its network closed.**
- Source: Wikipedia, citing Straczynski interviews among others, https://en.wikipedia.org/wiki/Babylon_5
- Access: extract. Kind: demonstrated in a production.
- Corroboration: none independent opened; one writer's account.
- Limits: Straczynski wrote 92 of 110 episodes himself. A single-author show. Self-reported.
- Producer (inference): a long plan and a hedge against early cancellation can coexist. For a serial with a free first episode, plan the arc, give each major character an exit, and know where the story could end.

**F-C30. Breaking Bad had a direction (Mr. Chips to Scarface) but deliberately no fixed roadmap. Gilligan dropped a planned early death of Jesse once he saw Aaron Paul's performance. The 2007-08 strike cut season one from nine to seven episodes, and a writer later said that saved the show.**
- Source: Wikipedia, citing Gilligan and Gould interviews, https://en.wikipedia.org/wiki/Breaking_Bad
- Access: extract. Kind: practitioner.
- Corroboration: none independent opened.
- Limits: retrospective attribution by the show's own team to a hit show. Disagrees with F-C29 on method, but both shows succeeded.
- Producer (inference): commit to direction and end state, not to each beat. Performance can change the story, which is a reason to lock late.

**F-C31. Audience response can restructure a serial. Steve Urkel began as a minor character, joined the main cast in season two, and a scene was added to an earlier episode and new gags to finished episodes for him. Ratings reportedly rose. Co-stars report damage: one said it hurt the show, and one character was written out.**
- Source: Wikipedia, citing LA Times 1992 and Entertainment Tonight 2022, https://en.wikipedia.org/wiki/Steve_Urkel
- Access: extract. Kind: demonstrated in a production.
- Corroboration: the page's ratings paragraphs are uncited. Co-stars' accounts are their recollections.
- Limits: one sitcom, 1989. Possible rewrite of the show's purpose, not just an adjustment.
- Producer (inference): serials can respond, which films can't. Decide up front what audience response is allowed to change (emphasis, screen time) and what it isn't (the ending, the point).

**F-C32. A bible has at least two types: a sales bible for buyers and a maintained one for writers, updated with everything established on air. Script coordinators and assistants may act as walking bibles.**
- Source: Wikipedia Bible (screenwriting), citing Jane Espenson 2007 and Nagel, AWN 2014, https://en.wikipedia.org/wiki/Series_bible
- Access: extract. Kind: practitioner.
- Corroboration: none opened.
- Limits: brief definition only.
- Producer (inference): for agents, the maintained bible is the one that matters: continuity facts established in finished episodes. A pitch document going stale counts as a real risk, not an administrative one.

**Unanswered within Q4.** Searched once on pilots, Amazon voting, bibles and arcs; then fetched Wikipedia pages. How a writers' room runs, mini-rooms, WGA terms, and how much is written before shooting: Wikipedia's Writers_room URL failed and I had no search left. Table reads: nothing opened except Archer's choice not to hold them (F-C39). Amazon's pilot voting: Wernicke's TED talk gave only a summary, so this is **not opened**. Weekly Shōnen Jump reader polls, a likely close analogue for serial cancellation: the page extract did not cover them, so this is **not verified** and worth a look if it matters.

### Q5. Greenlight and stage funding

**F-C33. Late kills happen, and the stated reason is usually just "it isn't working". Disney ended Gigantic in October 2017, about two years after announcement; the Wall Street Journal reported nearly $98M written off. Pixar's Good Dinosaur producer said the story wasn't working when it was delayed from November 2013 to November 2015, with an estimated $85M loss after release.**
- Source: Wikipedia, https://en.wikipedia.org/wiki/Gigantic_(unproduced_film) citing WSJ 2017; https://en.wikipedia.org/wiki/The_Good_Dinosaur citing Collider, Hollywood Reporter.
- Access: extract. Kind: demonstrated in a production.
- Corroboration: each by named trades, not opened.
- Limits: write-off numbers may include more than story work. 67 layoffs at Pixar in 2013 were linked to the delay in press but attributed by Pixar to refocusing.
- Producer (inference): **I found no published numeric kill criteria used by any studio; decisions are described in judgement language.** A small studio can do better by writing down in advance what would stop the project. That is my suggestion, not an established practice.

**F-C34. Kills and restarts at the reel stage are the cheap kind. Disney scrapped Beauty and the Beast after 1989 storyboard reels and restarted it as a musical, with the schedule compressed to about two years instead of the usual four. Kingdom of the Sun was halted at $25-30M with about a quarter animated; six months of retooling produced The Emperor's New Groove for a final budget of about $100M.**
- Source: Wikipedia, https://en.wikipedia.org/wiki/Beauty_and_the_Beast_(1991_film), https://en.wikipedia.org/wiki/The_Emperor%27s_New_Groove (citing Hill 2001, Leigh 2001, Kuklenski 2000, The Sweatbox).
- Access: extract. Kind: demonstrated in a production.
- Corroboration: limited. The Sweatbox hasn't been officially released. "Hill 2001" is probably Jim Hill, a fan-press writer (my reading; the full citation wasn't in the extract).
- Limits: costs of the scrapped Beauty and the Beast aren't given. "Cheap" is my inference, and these were still expensive.
- Producer (inference): a reel is the natural place to restart. Budget and schedule should allow for a restart rather than treat it as a catastrophe.

**F-C35. Completion guarantees: fee usually 2.5-3% of the strike price, sometimes 2% over $20M. The guarantor approves producer, director and lead cast for reliability, not creatively. It can take over if the picture goes substantially over budget or behind schedule, but rarely does because takeover means assuming the producer's obligations. A representative may be on set. Weekly accounting reports expended and cost to complete. A director's final cut can be lost if the picture threatens to go substantially over budget. Delivery disputes can turn on whether the screenplay was substantially shot as approved.**
- Source: Gary O. Concoff, UCLA Entertainment Symposium syllabus 2008, https://www.troygould.com/wp-content/uploads/2018/03/Pub-056.pdf
- Access: opened. Kind: practitioner (entertainment lawyer).
- Corroboration: Wikipedia cites a 3-5% range (https://en.wikipedia.org/wiki/Completion_guarantee; page tagged for missing citations). A "fewer than 2%" takeover rate attributed to an "International Film Finance Monitor (2023)" came from a commercial blog in a search summary: **unverified, not used**.
- Limits: 2008 US independent practice. No takeover frequency.
- Producer (inference): the weekly "cost to complete" is the most transferable idea here. For a small team that means a weekly estimate of remaining work, not spend so far.

**F-C36. Turnaround means a studio drops a project and another can take it by repaying development costs plus interest. Cited examples: E.T., Home Alone, Pulp Fiction, Ed Wood. The Thief and the Cobbler shows what a takeover looks like: in development from 1964, about $28M, full production from 1989, more animation than an 87-minute feature needed, but key story sequences missing. Warner Bros. backed out after a May 1992 workprint, and the completion bond company removed Williams. A cheaper bidder finished it, recasting voices and cutting about 18 minutes of completed animation. The Miramax cut grossed $319,723 on 510 screens.**
- Source: Wikipedia, https://en.wikipedia.org/wiki/Turnaround_(filmmaking) (citing NYT 2008), https://en.wikipedia.org/wiki/The_Thief_and_the_Cobbler (citing Dobbs 1996; LA Times 1992; not opened).
- Access: extract. Kind: demonstrated in a production.
- Corroboration: for Thief, Persistence of Vision documentary exists, not viewed. Wikipedia tags one earlier claim failed verification.
- Limits: a turnaround hit is a selected success. No interest rate is given. Williams's own creative ambitions are outside this; I'm using only the sequence of events. No data found on what share of developed projects get made.
- Producer (inference): Thief is the strongest single warning for a project of this kind: spectacular finished work, unfinished story. A producer agent should treat "lots of finished art, story not resolved" as the top alarm.

### Q6. Motion comics and limited animation

**F-C37. Max Payne, a game, chose comic panels with voice-over for its story because they were cheaper than animated cinematics, more effective in the developers' view since readers fill in nuance, and easier to reorganise if the plot changed.**
- Source: Wikipedia, citing Edge, "The Making of Max Payne", https://en.wikipedia.org/wiki/Max_Payne_(video_game)
- Access: extract, Edge **not opened**. Kind: practitioner, demonstrated in a production.
- Corroboration: none opened. Wikipedia's Motion comic page lists other game tie-ins (Dead Space, Uncharted, Danganronpa) with no citations.
- Limits: 2001. Developers' retrospective. No numbers.
- Producer (inference): this is the closest precedent for story inside a game. Don't assume voiced stills are second-best; they may suit the medium. It also suggests panels are cheap to reorder, if movement hasn't yet been tied to them.

**F-C38. An academic study of motion comic creators: 86.2% (50 of 58) reported frequent changes, and 46 of those 50 said they were time-consuming. 93.1% used pre-existing assets. An expert said rework is common. A coded sample of 95 online motion comics (mean 5.79 minutes) had 1,945 action-operation combinations: path movement 45%, rotation 24%, appearance 22%, scale 4.5%. Reported order: story and segmentation, visuals, static frames, animation, audio, refinement.**
- Source: Chen, Li, Li & Li, "DancingBoard", arXiv 2503.09061, 2025, https://arxiv.org/html/2503.09061v1
- Access: extract, first 100,000 characters. Kind: measured, on a narrow sample.
- Corroboration: E3's rework statement agrees with F-C13 in spirit.
- Limits: respondents recruited through social networks and mostly students (30 undergraduates, 26 master's, 2 PhD). Four experts from allied universities. Corpus from keyword search. Coding partly by GPT-4o. The paper presents its own authoring tool, so it has an interest in showing that current workflows are hard. Not professional productions.
- Producer (inference): most movement in the field is simple movement. Movement planning can use a short list of operations and need not be new per shot. Audio last, as this reports, conflicts with F-C1 and F-C39; for a voiced story I'd follow voice earlier.

**F-C39. Archer (limited digital puppet animation, layered and rigged art): voices recorded separately, with no table reads or rehearsals. About three weeks scripting and 11-13 weeks of animation from storyboard per episode, with four episodes staggered. About 150 artists.**
- Source: Wikipedia, citing Rolling Stone 2014, AWN 2014, *The Art of Archer* (2016), https://en.wikipedia.org/wiki/Archer_(2009_TV_series)
- Access: extract. Kind: demonstrated in a production.
- Corroboration: not opened.
- Limits: staffed, broadcast series. Cost not reported. 150 is a later headcount.
- Producer (inference): even limited animation takes months per episode, with teams. Don't assume "stills with accents" is trivial just because it's limited. Separate per-line voice recording suits generated voices or remote cast, and fits a pipeline that changes lines.

**F-C40. Sparks (2009 motion comic): episodes of 6-8 minutes; elements isolated and backgrounds filled in with After Effects and Photoshop; faces on 3D meshes; attention on mid-ground motion such as smoke and trash cans; 150 sound effects in the first episode; lip sync added.**
- Source: NY 411 blog, unsigned, 2009-09-14, https://ny411.com/blog/post/motion-capture-comics-take-on-new-frontiers
- Access: extract. Kind: demonstrated in a production.
- Corroboration: Wikipedia's Motion comic page confirms the general method (panels expanded, sound and voice added, 10-20 minutes per issue; no budgets), https://en.wikipedia.org/wiki/Motion_comic
- Limits: low-quality, possibly promotional, source. No budget, team size or schedule.
- Producer (inference): a useful detail: 150 effects in one episode is a real cost line for sound. Plan sound as well as movement.

**F-C41. Illustrated films that created new art from scratch were slower than adapting existing comics. Godkiller's maker said its 200 pages of art and a dozen voice performers made it slower than Watchmen. An artist who was hesitant about a motion comic was won over by test footage, and said quality varied among motion comics he'd seen.**
- Source: Wikipedia Motion comic, citing Bloody Disgusting 2010 and others; https://en.wikipedia.org/wiki/Motion_comic
- Access: extract. Kind: practitioner.
- Corroboration: none opened. Wikipedia's dedicated Godkiller and Watchmen motion comic URLs failed (404).
- Limits: promotional interviews. Two sibling illustrated films (Black Sky, Hack/Slash) were reported in limbo in 2010.
- Producer (inference): most famous motion comics adapted art that already existed and had been proven in print. A project making new art can't reuse their timelines.

**F-C42. A vendor recommends: comic panels, animatic approval, selective layer separation, motion comic. Separate only hero panels (its test: 3 of 6), use animatic timing before decorative motion, and promote only approved shots. It treats the animatic as the choice when story order is still changing.**
- Source: LlamaGen.AI blog, https://llamagen.ai/sv/blogs/motion-comic-vs-animatic
- Access: extract. Kind: practitioner (**vendor selling a generated-video tool**).
- Corroboration: F-C37 agrees on panel reordering. Otherwise unsupported. Its six-panel test has no measurements and says so.
- Limits: marketing. Not independent.
- Producer (inference): the order is reasonable and matches the owner's rule. Its only weight is that it agrees with the rest.

**F-C43. Small-team budgets and free-first models. Sita Sings the Blues: one main maker, an estimated 9,360 hours, listed budget $290,000; a $220,000 music licence demand negotiated to $50,000 late, with a loan. Hazbin Hotel's Patreon-funded pilot took over six months writing and over two years animating, was free on YouTube in 2019, reached about 32M views by May 2020, and got an A24 pickup in August 2020. Its series arrived in January 2024 with pilot voices not retained, four characters redesigned, and season one limited to eight episodes. Lackadaisy's 27-minute Kickstarter-funded short came out in 2023; a later campaign raised over $2M and led to a planned series.**
- Source: Wikipedia, https://en.wikipedia.org/wiki/Sita_Sings_the_Blues (citing Paley's blog), https://en.wikipedia.org/wiki/Hazbin_Hotel, https://en.wikipedia.org/wiki/Lackadaisy
- Access: extract. Kind: demonstrated in a production.
- Corroboration: not opened. Sita's $132,000 return is tagged citation needed; I don't rely on it.
- Limits: survivorship: the three that became known. No general success rate for free pilots was found. Hazbin had a Patreon following first, and Lackadaisy appears to have had an existing comic audience (my reading, not stated in the extract). These aren't games.
- Producer (inference): a free first episode can work as a funding gate, and the pilot may not bind the later series (Hazbin recast and redesigned). Clear rights and music before picture finishes.

**F-C44. Copyright: for an 18-page comic, the US Copyright Office recognised the text and the selection, coordination and arrangement as authored, but refused the Midjourney images. Effort didn't change this. Minor lip and mouth edits were too small to qualify, though sufficiently creative human edits can qualify.**
- Source: US Copyright Office letter to Van Lindberg on Zarya of the Dawn, 2023-02-21, https://www.copyright.gov/docs/zarya-of-the-dawn.pdf
- Access: opened. Kind: demonstrated in a production (a decision on one work).
- Corroboration: not searched. Later Office guidance exists; **not opened**.
- Limits: US, one work, one tool, 2023. Not legal advice. Law may have moved since.
- Producer (inference): if stills are generated, what the studio can clearly own may be the script, arrangement, and creative additions. Flag this to the owner before any sale or fundraising.

**F-C45. Generated image accounts are thin and mostly about video consistency, not stills. Corridor's Anime Rock, Paper, Scissors used Stable Diffusion over footage; frame-to-frame instability was the core problem, handled by training on the cast and post-processing, and critics complained of warping. For the sequel, a Tildes commenter reports Corridor hired an artist for a model sheet; warping was reduced but not gone, and direction suffered from too many showy effects. A creator's 2023 walkthrough made a short in a couple of hours and left writing, voice, music, sequencing and assembly manual. Netflix's Dog and Boy drew backlash for generated backgrounds.**
- Source: Corridor search summaries (https://80.lv/articles/turning-video-footage-into-anime-with-stable-diffusion extract: says it was solved but not how); Tildes post, 2023-08-14, https://tildes.net/~tech/19cb/skipping_a_step_corridor_digital_and_ai_anime (extract, forum commentary); Nejc Susec, 2023-03-21, https://nejcsusec.beehiiv.com/p/ai-supported-animation-free-download (extract, promotional); Dog and Boy from search summary, Creative Bloq and TechRadar **not opened**, page bodies didn't come through.
- Access: mixed, as marked per source; no primary making-of viewed. Kind: practitioner, weak.
- Corroboration: weak on all counts.
- Limits: 2023 tools, now old. **I found no first-hand post-mortem on a generated-image comic or motion comic, and no measurement of rework.** The making-of video was not viewed.
- Producer (inference): don't infer current tool capabilities from this. Test character consistency across stills in the project's own pipeline (rules 2 and 3 of the owner's working rules).

**Unanswered within Q6.** Motion comic budgets: none found after one search and page fetches. Published audience testing of motion comics: none found. Watchmen and Astonishing X-Men production details: not reached. Astro Boy's reuse economics: Wikipedia's series page doesn't cover them. Limited animation's cost history: only one figure surfaced (A Charlie Brown Christmas, $76,000 and four months per Wikipedia, https://en.wikipedia.org/wiki/Limited_animation, not used as evidence).

### Q7. What goes wrong

**F-C46. No general measure of overruns found. A Stephen Follows study of 29 blockbusters reports real costs about 12.5% over public figures, which is about misreporting, not overruns.**
- Source: Follows newsletter, November 2025, relayed at https://groups.google.com/g/studio-ni_org/c/WccXfaLeDIQ
- Access: **not opened**, search summary only. Kind: measured, per the author, narrow.
- Corroboration: none. Academic APIs returned 429s, and one search for overrun data found only list articles.
- Limits: 29 films.
- Producer (inference): famous budget numbers are unreliable by double digits. Don't calibrate from them.

**F-C47. Late big changes, with numbers. World War Z: planned over $125M, about $190M after reshoots per Paramount (some outlets say up to $269M), 30-40 minutes of new footage after a rewritten third act, about $540M gross; one trade called it a hit, another said it barely broke even. Fatal Attraction: original ending swapped, $14M budget, $320-344M worldwide; Goetz says scores rose 25 points and estimates $50-75M without it. Bourne Supremacy: a new ending at $200,000 tested 10 points higher. Sonic: redesign announced two days after the online trailer's backlash, delayed three months, about $5M reported, about $320M worldwide on $85-90M.**
- Source: Wikipedia (citing Reuters, EW, Deadline, Vanity Fair: https://www.vanityfair.com/hollywood/2013/06/brad-pitt-world-war-z-drama, **not opened**, blocked), https://en.wikipedia.org/wiki/World_War_Z_(film); https://en.wikipedia.org/wiki/Fatal_Attraction; Total Film (opened, for the Goetz claims); https://en.wikipedia.org/wiki/Test_screening (citing Guardian 2008); https://en.wikipedia.org/wiki/Sonic_the_Hedgehog_(film)
- Access: extract, plus one opened. Kind: demonstrated in a production.
- Corroboration: varies. Goetz's counterfactual is an unmeasurable estimate from an interested party. Sonic's redesign-cost citation was cut off in the extract.
- Limits: all have no real counterfactual, and survivorship applies. Some outcomes were probably not caused by the change. Reshoot cost for Fatal Attraction isn't reported.
- Producer (inference): a late change can be worth it and shouldn't be banned. The rule should be about the price and who agrees to it.

**F-C48. Late story rescues had real human costs. Toy Story 2: theatrical from February 1998; after Pixar decided it couldn't ship as it was, a revised story came in about a weekend and the film was finished in nine months; Catmull reportedly said about a third of staff had a repetitive strain injury. Frozen: rewrites ran into June 2013 for a November release, with about 17 months to finish after the reset, under 12 months of animation, and heavy overtime. Zootopia: lead swapped in November 2014 for a March 2016 release, about 16 months out.**
- Source: Wikipedia, citing Price, *The Pixar Touch* (2008), Iwerks documentary (https://en.wikipedia.org/wiki/Toy_Story_2); https://en.wikipedia.org/wiki/Frozen_(2013_film); https://en.wikipedia.org/wiki/Zootopia
- Access: extract. Kind: demonstrated in a production.
- Corroboration: Price is a book, not opened. Zootopia: whether animation had started is not stated, and cost not given.
- Limits: box office isn't checked here, and I don't claim the changes caused any later success. Selected successes, retold by winners.
- Producer (inference): famous rescues cost a lot of people's health and needed slack to pay for them. With agents, the limit moves to the owner's time and attention. A rescue that relies on the owner reviewing heavily for weeks is the same cost in a different place.

**F-C49. Finishing too early and starving the rest. Cats: reports say six months went on a two-minute trailer, leaving about four months for the other 110 minutes; staff worked 80-90-hour weeks. Effects were finished hours before premiere, and a patched version went to cinemas after opening. Net loss estimated at $113.6M.**
- Source: Wikipedia, citing Variety, Daily Beast, Guardian, Deadline, https://en.wikipedia.org/wiki/Cats_(2019_film)
- Access: extract. Kind: demonstrated in a production.
- Corroboration: not opened.
- Limits: the trailer timing is from reports, not production records. Poor reviews and competition also contributed.
- Producer (inference): a polished showcase shot is a real allocation risk. This matters for the free first episode: budget for a look test, but don't spend the series on it.

### Q8. What a producer does

**F-C50. Notes that work are framed as questions around a shared goal, and pushback is explained. Screenwriters describe an executive who asks "what if" and "what did you mean", who frames notes around the movie being made rather than judging the writer, and who accepts reasoned refusals. A good executive levels honestly about outside pressure.**
- Source: John August & Craig Mazin, Scriptnotes ep. 171, 2014, https://johnaugust.com/2014/scriptnotes-ep-171-finishing-a-script-and-the-perfect-studio-executive-transcript
- Access: extract. Kind: practitioner.
- Corroboration: Catmull's framing is similar (F-C5). Brooks warns against research as a weapon (F-C27). Goetz says studios use him as a blunt instrument to deliver hard notes (Substack). Bevan says test results make edit-room conflict less combative (Wikipedia Test screening).
- Limits: anecdote about one executive, on a podcast. The transcript doesn't use the phrase "the note behind the note", which I also haven't sourced.
- Producer (inference): agent notes to the owner should name the problem seen, ask what was meant, propose but not demand, and log what was declined and why. Results should be shown, not used as leverage.

**F-C51. Plussing has weak public support. Secondary sources credit Walt Disney with the term and Pixar with adopting it with improv's "yes, and". The only worked example opened is one anecdote about an unnamed creative director and Woody's eyes, by a feedback-book author. No study or Pixar statement opened.**
- Source: Joe Hirsch, LEADx, 2017-06-20, https://leadx.org/articles/pixar/ (extract). Randy Nelson piece, https://dzone.com/articles/pixars-randy-nelson-learning (**not opened**, 403). Jim Hill Media (**not opened**, 403).
- Access: extract for LEADx only. Kind: practitioner, weak.
- Corroboration: repeated widely, apparently from a few sources.
- Limits: business-writing retellings. Pixar itself not read on this.
- Producer (inference): harmless as a form, but no evidence it works, and it could blunt a note that should say "this doesn't work". Catmull's own emphasis is candour (F-C5). Keep room for a plain "no".

**F-C52. What a producer owns in a film or series is documented mostly at the edges: weekly costs and cost to complete; reliability checks; delivery lists (F-C35); change lists for departments after a lock (F-C13, and the search summary of the Production Expert panel, which says they won't proceed without at least a paper change list); and pushing back on schedule, as with Miyazaki's producer threatening to add a year to get him to work faster (F-C11, Miyazaki's reading).**
- Source: as cited. Access: mixed. Kind: practitioner.
- Corroboration: partial.
- Limits: **I did not find a practitioner account of decision logs as such.** The Producers Guild page failed (404). The nearest documents are change notes in post (CineMontage: tools tracking changes across sound, picture and VFX).
- Producer (inference): a change list is the established form of decision log in post. Use it across the whole pipeline.

**Unanswered within Q8.** No source found directly on notes when the note-giver is also the author. Searched once. Adjacent material: creators losing perspective (F-C5), and Miyazaki's friction with his producer (F-C11), and leadership replacing directors (F-C24). Where the owner is the top authority, there's none to fall back on, so this looks like a real gap (inference).

---

## Q1 stage table: what each stage tests, and what's cheap to change

Stage names and order are sourced from F-C1, F-C2, F-C7, F-C13. **The cost columns are my inference unless a claim is cited. I found no measured stage costs.**

| Stage | What it tests | Cheap to change here | Expensive here | Motion comic equivalent |
|---|---|---|---|---|
| Script and outline | Premise, arc, what happens | Nearly everything | Little | Same |
| Storyboard | Shots, order, what's shown | Shots, order | Characters and world if design has been finished early | Beat list with placeholder stills |
| Story reel with scratch voice | Whether the story plays in time; felt, not argued (F-C2) | Scenes, order, whole structure (F-C1, F-C2) | Nothing yet except people's attachment | Timed reel, see draft below |
| Layout (F-C7) | Framing and staging | Composition, panel order | Timing that has been built around shots | Layered composition of each still |
| Final voices | Performance, which can change the story (F-C30) | Depends on cast and tool: **unknown here** | Retakes, if the cast is expensive or unavailable | Depends on voice method |
| Final animation | Movement | Small timing | Story order, shot length, dialogue length (F-C13) | Accent movement tied to voice |
| Compositing | Whether the look holds | Tweaks | Upstream shots | Layer effects, light, parallax |
| Colour and final mix | Finish | Levels, grades | Picture and line changes, every one (F-C13) | Same; plus in-game playback |

Disconfirmation: stages didn't protect Gigantic (F-C33), Lightyear (F-C6) or Elio (see weak stories), and Miyazaki skips them (F-C11).

## Transfers to a small agent team, and what's specific to big budgets (inference throughout)

**Transfers**
- Build the whole story in a cheap, timed form, and show it rather than argue (F-C1, F-C2).
- Rebuild several times as planned work (F-C1, F-C2).
- A separate layout gate between story and movement (F-C7).
- A change list whenever something after a gate changes (F-C12, F-C52).
- A weekly estimate of remaining work (F-C35).
- Test elements and confusion, not a score (F-C16, F-C27).
- Each character has an exit; know where the serial could stop (F-C29).
- Decide where quality may drop (F-C10).
- Post-release data shapes later episodes (F-C22, F-C31).

**Doesn't transfer, or changes meaning**
- Test scores with 300-400 recruited viewers, genre norms, and a research firm (F-C14). Too few people here to produce a number.
- Bonds, guarantors and turnaround (F-C35, F-C36). Only the logic carries over: an outsider's check, and a way to stop.
- Multi-year cycles and 12-18-week reviews (F-C4). Cycles should be far shorter.
- Replacing a director as a safety valve (F-C24). The owner is the author and funder.
- Overtime as the rescue cost (F-C48). Here, the limit is the owner's attention and possibly compute or generation budget.
- Peer review by experienced makers (F-C5). Agents aren't a Braintrust. They may agree with each other or share blind spots; this needs testing on a real project, and I found no evidence on it.

**Unknown**
- Whether viewers of a game-embedded motion comic respond like theatre or TV viewers. Nothing found.
- What generation changes about rework costs. Regenerating a still may be cheap while keeping a character consistent is not (F-C45). Measure in this pipeline.

---

## Where practitioners disagree

1. **Should audiences shape the work?** Goetz and producer Tim Bevan say the audience's voice is decisive or nearly so (F-C14, Wikipedia on Bevan). Ang Lee's Picasso line, Kevin Smith and Scott push back, and Scorsese objects to CinemaScore (F-C25, F-C22). Ebert takes the middle: valid for filmmakers, abused by executives. Il Post notes nobody knows how many directors value testing and how many just tolerate it.
2. **Can tests predict?** Goetz: yes, without data (F-C17). Bader: never (F-C26). Brooks: strong pilots do more than twice as well, in an unpublished study (F-C27). De Vany & Walls: forecasts have no precision (F-C18). MOVIEMOD and Eliashberg: yes, in narrow academic tests (F-C19, F-C20).
3. **Plan the serial or discover it?** Straczynski planned five years (F-C29). Gilligan deliberately had no fixed roadmap (F-C30). Miyazaki doesn't know the ending, and calls that risky (F-C11). Each made work its supporters admire, so this may be about author temperament.
4. **Voice before or after picture?** US animation records scratch and final dialogue first (F-C1). Japan records after (F-C8). DancingBoard's creators add audio late (F-C38). Archer has no table reads, while table reads were the default assumption in the brief; nothing opened describes their value.
5. **Is a lock real?** Editors' glossaries treat it as firm. Mixers say it's been eroding for decades (F-C12). Costs reported range from about a day to rebuilding acts (F-C13).
6. **Who decides?** Catmull: the director (F-C5). Practice: leadership removes directors when it stops trusting the story (F-C24). Chapman disputes that her removal had a creative reason.
7. **Is a poor test a stop signal?** A weak test rarely succeeds (Brooks), yet hits often test mid-range (unnamed NBC executive) and unconventional pilots test poorly without being dropped (Beckman). The WB stopped testing, then resumed (F-C26).
8. **Was the change worth it?** World War Z was a hit (Variety) or barely broke even (Deadline) (F-C47).
9. **How much motion?** The vendor recommends few hero panels (F-C42). Sparks describes layering each cell with a lot of sound (F-C40). Max Payne argues readers' imagination does the work, so less may be better (F-C37). No testing of this exists that I could find.

## Famous stories with weak support

- **"Seinfeld proves tests are useless."** The poor test is reported (F-C28). The conclusion doesn't follow: survivorship, and a producer's stock defence per one search summary (Showbuzz Daily, https://showbuzzdaily.com/?p=111, **not opened**, 526 error).
- **"Hill Street Blues tested poorly."** Half true, per a network researcher (F-C28).
- **"Ambersons' audience hated it."** The cards were 42% positive on one recount (F-C25). The recount comes via TCM via Wikipedia, so it needs checking too.
- **"Fatal Attraction made hundreds of millions because of the new ending."** Worldwide figures are documented. The "$50-75M otherwise" is the tester's own estimate (Total Film, opened).
- **"90% of films are tested."** One interested source relayed twice (F-C15).
- **"Harold Lloyd invented test screening."** Wikipedia's claim has no citation.
- **"The Braintrust has no power."** Catmull's framing is real, but directors get replaced (F-C24). I couldn't read Catmull's text in full.
- **"Plussing."** A widely repeated practice with thin evidence and an unverified Disney origin (F-C51).
- **"Let It Go fixed Frozen."** Del Vecho credits the song with changing Elsa, but rewrites continued through June 2013, with other songs and test screenings still to come (F-C48). A one-song story is too neat.
- **Elio's silent test room.** "Not one hand raised" and the "masculinize" account come from unnamed insiders via a blog relaying the Wall Street Journal (https://www.worldofreel.com/blog/2026/3/7/pixar-boss-pete-docter-defends-pixars-elio-rewrite-after-original-gay-character-was-cut-were-making-a-movie-not-therapy, extract; WSJ **not opened**). The motive is contested. Budget estimates of $150M and about $300M conflict.
- **"Beauty and the Beast tested at 5%."** One relayed remark, ambiguous about which version (F-C21).
- **"Takeovers happen on under 2% of bonded films."** Traced only to a commercial blog citing a source I couldn't find (F-C35). A lawyer's "rarely" is what I'd keep.
- **Saved-by-testing stories in general.** All come from the people who sold or did the test, and none has a comparison version shown to a comparable audience.

**Overall:** most of these are unverified rather than disproved. Hill Street Blues and Ambersons are the two with direct counter-evidence.

## What a story reel for a motion comic should contain (draft, inference)

This is my own draft, adapted from F-C1, F-C2, F-C7, F-C14, F-C16, F-C27, F-C29, F-C37, F-C42. No source describes this format for this medium. Treat it as a proposal to test.

**Contains**
1. The full episode at real length, timed. Plus a written arc for the season and where it could end (F-C29).
2. One placeholder image per beat, rough enough that nobody mistakes it for final. Fine if generated. Characters only need to be recognisable.
3. Scratch voice on every line: all in one voice, or simple distinct voices. Line lengths must be real so the timing is true (F-C1).
4. Temporary music and sound only where the story depends on them (F-C1).
5. Movement as notes, not as work: on-screen text or simple cuts stating the planned accent ("rain moves", "eyes close"), each with a cost class (none, simple, custom) (F-C38 suggests most need only simple operations). Show movement only where it carries story information.
6. A visible label on the reel: version, date, and what changed since last time.
7. A shot sheet alongside it: for each shot, its assets, any reuse, its planned layers and movement, and whether it's a "hero" shot (F-C42, F-C10).
8. One separate look test of a couple of finished shots, reviewed separately, because the reel can't test the look (F-C47, F-C49). Don't merge it into the reel.
9. Playback inside the real game context at least once, with its skip and pause controls and at its real moment in play. The closest precedent is a game (F-C37), but this step is my judgement, not its documented practice.

**Leaves out**
- Finished art, layer separation, lip sync, parallax, effects, colour, final mix, final voices. If any of these is already done, that is a warning sign rather than a bonus (F-C36).

**Review steps**
- Peer read first: agents and the owner, against stated questions. Notes framed as what's seen, then a suggestion (F-C50). The owner decides and the decision is logged.
- Then viewers who didn't make it, told it's unfinished. Ask them to retell the story, say where they were confused, whether the confusion was intriguing or annoying (F-C16), who they would follow, and whether they want the next episode. Use counts of who said what, with names of scenes. No percentages from small groups (F-C14).
- Note that a wish to see more from a rough reel is not a forecast of real behaviour (F-C17, F-C18).

**Finish condition (for the owner to set)**
- Which questions must have acceptable answers, how many rebuilds are allowed before stopping or restarting, and what happens to a change after the gate (a change list, a stated cost, the owner's yes) (F-C12, F-C33).

---

## Status of each question

| Q | Status | Main gaps |
|---|---|---|
| 1 Pipeline | Answered, except stage costs | No measured stage costs. Disney reel counts not found. Anime's rework is only partly sourced |
| 2 Locks | Partly answered | Sound lock, ADR share, colour timing, measured costs not found |
| 3 Testing | Mostly answered | No study of screening scores vs results found. Corrections for unfinished work unanswered. Braintrust known through secondary and practitioners. Research firms: Screen Engine/ASI and CinemaScore covered, PostTrak only mentioned, NRG's history not reached |
| 4 TV | Partly answered | Writers' rooms, mini-rooms, table reads, Amazon voting not reached |
| 5 Greenlight | Partly answered | Attrition rates, greenlight committee practice, numeric kill criteria not found |
| 6 Motion comics | Partly answered | Budgets, motion comic testing, first-hand accounts of generated-image comics not found |
| 7 What goes wrong | Answered by cases | No general overrun measure |
| 8 Producer | Partly answered | Decision logs; notes when author and note-giver are the same person; Pixar's own account of plussing |

## Search and fetch log

**Searches used: 12 of 12. None refused.**
1. Pixar reel counts. 2. Test screening vs box office. 3. MOVIEMOD and academic prediction. 4. Goetz on unfinished effects. 5. Anime pipeline. 6. Picture lock costs. 7. Motion comic budgets and limited animation. 8. Pilot testing, Amazon, arcs. 9. Follows and overruns. 10. Completion bonds and turnaround. 11. Plussing and notes. 12. Generated-image accounts.

**Fetches that failed or came back partial, so the source is not read:** BBC Culture (blocked), Vanity Fair (blocked), Hollywood Reporter (402), HBR Catmull (opening only), Fast Company (403), TED Wernicke (summary only), Web Archive (blocked), INFORMS (403), SAGE (403), Springer (login redirect), DZone (403), Jim Hill Media (403), Showbuzz Daily (526), Creative Bloq and TechRadar (no body), OpenAlex and Semantic Scholar (429; I stopped rather than retry), Producers Guild (404), and Wikipedia's Writers_room, Newt, Watchmen motion comic and Godkiller URLs (404).

**Largest unread primary sources:** *Creativity, Inc.* (Catmull); *Audience-ology* (Goetz); *The Pixar Touch* (Price); academic literature on prerelease testing, which I couldn't reach through database APIs. A later pass with access to these is the most likely way to change a claim above.
