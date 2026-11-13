# Evidence: the director's job

Input for `directing/SKILL.md` and `agents/director.md`, edited from a research pass dated 2026-11-06 (D25 in `docs/DECISIONS.md`). Evidence, not rules. Cite as `[DR-54]`; the numbers are the research pass's own and stay stable. **Inside this file a bare number in a claim's fields or in a list ("Corroboration: 14, 16") means that DR claim.**

**Most sources were reached second-hand. No director's book was opened:** Lumet comes through one reviewer's excerpts, Murch's rules through secondary sites (one of his addresses was read at source), Catmull through a talk write-up and a free first paragraph, and Mackendrick and Katz weren't reached. All measured studies were read as abstracts only. Pixar's stories are second-hand and told by its own head. No source studied an AI director or an AI studio.

**Edits from the research file:** claim numbers prefixed; project-specific words generalised; paths to the research session's scratch folder removed. Nothing was added to a claim, and no status or kind was changed.

The research was aimed at a small team of AI agents plus one human owner, making a voiced motion comic of layered stills inside a game. The director makes story decisions without showing the owner the plot, and the owner judges by playing. Findings are meant to hold for game and story projects generally.

Two earlier research passes, on story and on art, are cited and not repeated: `story#N` and `art#N` are claims there. Those passes are not in this file and weren't re-checked for it, so treat those citations as leads.

## Most likely to change the role

All inference, drawn from the numbered claims. None has been tried on an AI studio.

1. **Making the call and recording it is the function with the most support; the "visionary" part has less.** The strongest failure account here is meetings ending with no verdict, not a bad vision (14, 15). Practitioners describe absence of a target as lost months (9).
2. **A usable statement is one that rejects things.** Lavigne's "vector of chaos" discards solutions on sight (11). A pitch people can project their hopes onto outlasted any plan to build it (15). Pillars that just name systems may build parts in isolation (13).
3. **The director can't judge its own surprise, and telling it to imagine not knowing is unlikely to be enough.** Outcome knowledge distorts judgement of what others believe (54), even for people warned of it (55). A maker misjudged how long his own levels took by a factor of two (56). So cold readers need to be other agents, kept from the plot (61).
4. **The owner's first play is a one-shot instrument that can't be rehearsed.** No source here shows AI cold readers predict human surprise. This is the role's largest open risk (61, 62).
5. **Trust confusion reports over preference scores.** Comprehension fixes have the cleaner stories (47). Preference results depend on who was recruited and when (46, 48, 49). Every test-audience case has no denominator (50).
6. **Reviews should advise; someone must still hold a veto, and that must be written down.** Pixar's Braintrust has no authority over a director, yet Pixar replaces directors (19, 20). The tie-breaker must be named before the fight.
7. **"A single strong vision predicts quality" is not shown.** The nearest evidence is team-level, stronger on self-report (66). Game revenue varies more with middle managers than with people in innovative roles (67). Half-Life had no director, but kept one continuity owner (39).
8. **"Directs without doing their jobs" has little precedent among the directors I read.** Miyazaki draws, Kon co-writes, Levine writes and directs (1, 3, 25). Creators forecast others' novel ideas better than pure managers do (52). If the role only evaluates, it may evaluate worse.

## How to read this

**Read status.**
- `opened`: I downloaded the raw page and read the cited passage myself. Short wording in quotation marks comes from these. Not a claim that I read a whole long page.
- `abstract only`: I read the study's abstract through Crossref, Europe PMC or OpenAlex, not the paper. Effect sizes not in the abstract were not seen.
- `extract`: seen through a summarising fetch. **No claim uses this status**: I used raw downloads throughout.
- `not opened`: known only from a search-tool summary, or from someone else's citation. Treat as a lead.

A book reached through a review or excerpt says so. Entries headed GAP are not claims: they record that a sub-question has no source here, what was searched, and any reasoning of mine, so the claim fields don't apply. **No book named in the brief was opened**: Lumet, Mackendrick, Murch and Katz are at best second-hand here.

**Kinds.** `measured` (a study with a sample), `practitioner` (a maker speaking about their own work), `demonstrated` (a work or production that did the thing; says nothing on whether that caused its success), `reported` (journalism or an encyclopedia about what others did; added as a fifth label, because merging it into practitioner would overstate it), `inference` (mine).

**Advice is not evidence that it works.** Nothing in Q1 to Q5 was tested. I give no quality ratings. Corroboration counts independent sources in this pass only; "none here" means none found within budget.

**Every "Would change" line is inference.** So are all statements about AI agents; no source here studied a director that is an AI, or an AI studio.

**Access limits.**
- Searches: 12 of 12 spent (list at the end). Each call counted once.
- Refused or absent: Fast Company's Braintrust excerpt (403); Medium's Braintrust piece (403); Backstage's voice director piece (403); the Lee et al. PDF (empty response); the Guardian Miyazaki address I tried (404); a Transom Murch address (404; the 2005 one worked); Edutopia's Nelson interview (404).
- The permission system refused a batch containing web.archive.org copies of two paywalled articles. I did not retry those. The HBR article is the free first paragraph only.
- The New York Times op-ed by Chapman was in that refused batch and was not retried; I read Cartoon Brew's quotation of it.
- Academic APIs rate-limited me (429) mid-run.
- Six of the 14 DOIs I recalled from memory resolved to unrelated papers. I re-found these by title, and only the DOIs below are checked. Treat any DOI recalled from memory as unverified.

---

# Q1. What a director does, by medium

**DR-1. Miyazaki says his films have no finished script at the start: the story develops as he draws storyboards, production starts while boards are still developing, and nobody knows where it will go. He calls this "dangerous", says he would like it to be different, and that staff are forced to accept it. His biggest problem, he says, is length, not empathy with characters: he argues about it with his producer, who threatens him with an extra year so he works faster. Spirited Away grew from an envisioned 1,200 shots to 1,415.**
- Source: Tom Mes report of Paris press event, Dec 2001. http://www.midnighteye.com/interviews/hayao-miyazaki/
- Read: opened.
- Kind: practitioner.
- Corroboration: none on this method here. Kon contrasts it (3).
- Limits: self-report, translated, at a press event. A rare talent describing his own habit, and he disowns it as a model. Mentions no film that failed this way.
- Would change: don't copy this as a method. Do copy that length and the draw order are the director's live problem, and that the board is where his decisions get made.

**DR-2. Miyazaki uses every asset staff make, even if it doesn't fit, and says supervising another director (Morita) is "a true test of patience" because that director wants to do things differently.**
- Source: same URL.
- Read: opened.
- Kind: practitioner.
- Corroboration: none here.
- Limits: a passing remark.
- Would change: directing someone else's work is named as hard by someone who could simply do it himself. Note the temptation to rewrite a writer's work in the director's own taste. For generated assets "use everything" doesn't transfer: generation is cheap, and discarding is the default.

**DR-3. Kon works the other way: finished screenplay, then storyboards, with animation running while boards are half done. At the board stage dialogue and details change as faces, locations and compositions are fixed, but scenes and plot don't. He took Perfect Blue only on condition he could change the script, and kept three elements demanded of him: idol, horror, stalker. He co-wrote the third draft of Millennium Actress.**
- Source: Tom Mes, 2002. http://www.midnighteye.com/interviews/satoshi-kon/
- Read: opened.
- Kind: practitioner.
- Corroboration: 1, on overlap of boarding and production; opposed on script.
- Limits: two interviews, both retrospective. Script-first versus script-free is settled by neither, since both directors are celebrated.
- Would change: a locked plot with an unlocked board is a defensible model for a project whose writers and director must not contradict a story's planted facts (story#14 to story#17). Board changes may touch dialogue, not facts.

**DR-4. In anime, a series director approves almost every stage, helps create boards and sets tone. The episode director (enshutsu) is the go-between: draws boards, checks drawings, attends recording, with control that depends on the series director. The sakuga kantoku ("animation director") is closer to a supervisor. Most directors rise through storyboarding or layout.**
- Source: https://gengaland.blogspot.com/2021/11/anime-staff-production-terminology.html ; https://kanzenshuu.com/animation-production/positions-and-roles
- Read: opened.
- Kind: reported (fan glossaries).
- Corroboration: two fan sources, agreeing; animecorner.me via search (not opened).
- Limits: low standing. The second is about Toei long runners. Search 8 returned no director's own account of the workflow.
- Would change: this is the nearest human analogue to the requested agent: direction through approvals on boards and takes, rather than presence on a set. It also suggests a delegated layer for long works.

**DR-5. Lumet: what the movie is about limits the work and is "the riverbed into which all subsequent decisions will be channeled"; theme determines style.**
- Source: Making Movies, as excerpted in Henry Sheppard's review. https://adelaidescreenwriter.blogspot.com/2013/04/book-review-making-movies.html . Same theme line on a quote site, https://quoteproject.com/quote/suffice-theme-movie-style-movie/ (opened, low standing).
- Read: opened for the review. **Book not opened**; these are the reviewer's selected passages.
- Kind: practitioner, second-hand.
- Corroboration: 11 in practice from game directors. Agreement isn't evidence it works.
- Limits: a live-action director, read only through a reviewer's selection; nothing shows a statement caused quality.
- Would change: the first question the director answers, in writing, before briefing anyone.

**DR-6. Lumet wants the writer at rehearsal, and to see the first cut, since writers can spot their own repetition. He says a movie "is constantly being rewritten" by everyone's contribution, and that no one knows the magic combination. He let Bergman take the smaller part she asked for instead of the one he wanted, and she won an Oscar.**
- Source: same review.
- Read: opened; book not opened.
- Kind: practitioner, second-hand.
- Corroboration: 25 on actors finding things.
- Limits: one winning anecdote, chosen by its teller. He does not report the times he yielded and it failed.
- Would change: writers see cuts rather than being done at script. Keep the writer agent in the loop for the assembled reel, in a fresh run if the plot is sealed from others.

**DR-7. Game directors asked by Polygon don't share a definition. Titles depend on "the studio, the country, or even the weather" (Cammisotto). Recurring: alignment (Rubyor), a target so people don't pull apart (Fox), advocate for a specific player experience and selling it upward (Adler), balancing collaboration with direction, which "won't solve or account for every problem" (Dracott), conductor of an orchestra (Fox).**
- Source: "What even is game direction? We asked 16 game directors." https://www.polygon.com/game-direction-explained-by-directors
- Read: opened (most of the 16).
- Kind: practitioner.
- Corroboration: 8.
- Limits: self-selected, promotional context near an awards show, all with shipping games. No one describes failure in detail except Rubyor and Cammisotto.
- Would change: don't import a game director's job description as if settled. State the role's powers in full in the project's own terms.

**DR-8. At Jackbox, directors are "the final word on game design and tone", producers track logistics, staffing and schedule, and most concepts originate with writers or engineers, not the director. One describes the role as halfway between conductor and gardener. Another says the director doesn't make all decisions but checks they fit a vision they crafted together.**
- Source: https://jackboxgames.com/blog/behind-the-scenes-of-pp10-directing
- Read: opened.
- Kind: practitioner (company blog).
- Corroboration: 7. Job-guide sites via search 12 say similar (not opened).
- Limits: a small-game, in-house, marketing voice. Conductor metaphors are unfalsifiable.
- Would change: a clean split: final word on design and tone versus logistics. Ideas can come from anyone; the director decides, not originates.

**How the job differs (inference from 1 to 8, 25 to 27, story#55).**

| | Film | Animation | Games |
|---|---|---|---|
| Decision point | On set, then in the edit | Storyboard and approval chain | Spec, playtest, edit of takes |
| Presence | With actors | Mostly through drawings | Often in a booth, otherwise remote |
| Audience position | Fixed path | Fixed path | Path partly chosen; lines can be heard in many contexts (26) |
| Failure seen before release | Rough cut | Reel | Playtest |

Transfer to a project of this kind, also inference: animation's board-and-approval model transfers best; film's set craft doesn't transfer at all; game's playtest loop transfers, except that the one tester who matters most must not be used up.

**GAP: Mackendrick's On Film-Making, Katz's Film Directing Shot by Shot, Murch's book text.** Search 5 and direct addresses returned no usable text. Wikipedia confirms only Mackendrick's career and CalArts post (https://en.wikipedia.org/wiki/Alexander_Mackendrick , opened). I make no claim on "activity versus action" or Katz's shot planning. Status: **unanswered at source.** Would change: nothing until read. The Disney and Pixar story-supervisor practice (reels, sweatbox) is also unanswered here.

---

# Q2. Holding a vision

**DR-9. Directors describe absent targets as expensive. Rubyor: projects that skipped this were "misaligned" and lost "many crucial development months". Fox: when the goal is murky each member is right from their own view, and they pull apart.**
- Source: https://www.polygon.com/game-direction-explained-by-directors
- Read: opened.
- Kind: practitioner.
- Corroboration: 14, 16.
- Limits: self-report by people who hold this job, which has an interest in its own importance.
- Would change: no brief goes out until the statement exists.

**DR-10. Mass Effect's team under Hudson was called the Enterprise, all following one captain; the Dragon Age team a pirate ship, meandering to its destination. The pirate ship shipped Inquisition, Game of the Year at the 2014 Game Awards, though by a "brutal" production mostly built in the final year.**
- Source: Jason Schreier, 2019. https://kotaku.com/how-biowares-anthem-went-wrong-1833731964 . Anonymous sources.
- Read: opened.
- Kind: reported.
- Corroboration: single.
- Limits: studio folklore relayed anonymously. Both teams were at one studio; neither is a controlled case.
- Would change: a useful counter to strong-director myth. A meandering process can produce an acclaimed game, at human cost that AI agents don't pay but token budgets do.

**DR-11. Usable statements in practice reject options. Lavigne: everything is a "vector of chaos", so he discards any solution toning it down. Rostal: "even a god needs help" plus "charmingly weird": a theme and a look serving as a shortcut. Petty: four words for Keeper (unexpected, atmospheric, companionship, metamorphosis), used to check work connects.**
- Source: https://www.polygon.com/game-direction-explained-by-directors
- Read: opened.
- Kind: practitioner.
- Corroboration: 5; art#28 on a tie-breaker in art bibles.
- Limits: not checked against what those teams actually did. Short statements are appealing to quote afterwards.
- Would change: test a statement by what it forbids. If no real option is rejected by it, it isn't doing work.

**DR-12. Kon's statement of what Perfect Blue was about (a girl maturing as her values are shattered) differs from how Western audiences read it (a comment on idols), and he says he "cares very little" about the stalker plot he was required to keep. Miyazaki tests every Chihiro task against whether his friend's ten-year-old daughter could do it, and names the first and last scenes as two portraits of her change.**
- Source: Midnight Eye, both interviews.
- Read: opened.
- Kind: practitioner.
- Corroboration: each other, loosely.
- Limits: stated after the event. Miyazaki also says logic isn't how he decides, and credits subconscious choice (Chihiro's ocean), so this may be tidy storytelling about his own process.
- Would change: name a concrete person as audience proxy, and name the change between first and last scene. The private intent need not match marketing or genre labels, or what a reader sees.

**DR-13. Design pillars are widely taught; the evidence on them is thin. Wagar lists real pillars (God of War: combat, father and son, exploration; Destiny has seven; Fallout's via Tim Cain) and argues that system-name pillars can promote an "atomistic" design, with parts built in isolation. Pears says 3 to 5 elements or emotions, and that an idea failing them may be removed, but off-pillar ideas can later subvert. His Last of Us "pillars" are his own reverse engineering.**
- Source: https://gamedesignskills.com/game-design/design-pillars/ ; https://www.gamedeveloper.com/design/design-pillars-the-core-of-your-game
- Read: opened. Pillars quoted by Wagar are not checked at source.
- Kind: practitioner (a teacher who sells bootcamps, and a blogger).
- Corroboration: search 6 summaries agree that vague pillars fail (not opened, low standing, repetitive content marketing).
- Limits: **search 6 and search 3 found no postmortem where pillars were ignored or failed. Unanswered.** Claims that pillars "work" are from those who teach them.
- Would change: state pillars as what the player feels and why, not as a system list. Don't claim pillars have been shown to work.

**DR-14. Anthem: 19 anonymous people describe "no vision, ... no clarity, ... no single director saying" how it fits together, after creative director Hudson left in 2014. The most common story was meetings on fundamentals ending with no verdict; decisions took a year or two since "no one really wanted to make a call". Staff saw many versions of the elevator pitch. Flying was removed, then put back over a weekend for a demo to an executive.**
- Source: https://kotaku.com/how-biowares-anthem-went-wrong-1833731964
- Read: opened.
- Kind: reported.
- Corroboration: Darrah, by PC Gamer (15). Executive producer's video itself not watched.
- Limits: anonymous sources, some with resentments; Schreier lists rival causes (Frostbite engine, understaffing, EA's fiscal deadline, two studios, "BioWare magic"). One staffer notes everything was new. Can't separate vision from these.
- Would change: decision latency is the measurable symptom. Log open creative questions with an age. A director that defers is failing even if its taste is excellent.

**DR-15. Darrah (Anthem's former executive producer) says Hudson's pitch gave just enough detail to seem real and left executives' imaginations to fill in the rest, and that such a story can outlast its teller: "maybe there wasn't anything behind the very evocative statement".**
- Source: PC Gamer on Darrah's video. https://www.pcgamer.com/games/third-person-shooter/anthems-former-executive-producer-says-bioware-was-so-good-at-telling-stories-that-its-original-anthem-pitch-convinced-ea-to-greenlight-a-game-it-couldnt-deliver-maybe-there-wasnt-anything-behind-the-very-evocative-statement
- Read: opened (article). Headline wording; the video is not opened.
- Kind: practitioner, reported.
- Corroboration: 14.
- Limits: a rival internal view, years later, about a colleague who has not answered here.
- Would change: an evocative statement that different readers complete differently is a defect, not a feature. Ask two agents to say what it rules out. Disagreement means it's not done.

**DR-16. Andromeda: a new creative director (Walters) brought a new vision in 2014 after Lehiany left; procedural planets from the early vision weren't dropped until the end of 2015, and the vertical slice "hadn't quite happened". Edmonton staff said the vision was too weak; Montreal staff thought Edmonton was sabotaging them.**
- Source: Schreier. https://kotaku.com/the-story-behind-mass-effect-andromedas-troubled-five-1795886428
- Read: opened.
- Kind: reported.
- Corroboration: single (14 is the same reporter and studio).
- Limits: anonymous; the engine is a large confound.
- Would change: a vision is a bet on what can be built. Check it against a slice before relying on it. Changing a director mid-project resets more than one document.

**DR-17. Half-Life's 200-page design document still left daily details vague; Birdwell says "big picture ideas" that didn't make it into any document spread only through the shared process.**
- Source: Ken Birdwell, 1999. https://www.gamedeveloper.com/design/the-cabal-valve-s-design-process-for-creating-i-half-life-i-
- Read: opened.
- Kind: practitioner.
- Corroboration: art#29 argues drift is the generated-art version of the same issue.
- Limits: human team in a room.
- Would change: **doesn't transfer simply.** Agents share no hallway and no memory across runs. What humans carried by being together must be written, or it doesn't exist. So the tone document needs examples of decisions already made, not just principles. That suggestion is untested.

**DR-18. Art bibles that seem usable have a stated tie-breaker, numbers, and a mistakes list.**
- Source: art#28, art#29, art#30 (see there: second-hand via a vendor blog; approved-and-rejected examples are weakly sourced).
- Read: not re-read at source; cited from that pass.
- Kind: practitioner, reported there.
- Corroboration: 32's explicit priority order is the same form.
- Limits: as listed there.
- Would change: for look, the director's statement can be checkable. For voice and pacing nothing comparable was found.

---

# Q3. Giving direction and notes

**DR-19. Catmull says the Braintrust "should have no authority": it "could not tell the director what to do", so directors don't arrive defensive. The write-up says copies formed for technical teams "didn't take". At Disney he told directors they need not listen to anyone's notes, even his. He says the group began by accident around Lasseter, Stanton, Docter, Unkrich and Ranft.**
- Source: First Round Review on his Stanford talk, 2015. https://review.firstround.com/spark-creativity-with-these-tips-from-pixars-president/ . MIT Sloan on his HBR piece, https://sloanreview.mit.edu/?p=4772 .
- Read: opened for both. **HBR article: only the first paragraph, which is the free preview. Book: not opened.**
- Kind: practitioner, his own account.
- Corroboration: Sloan and First Round report him, not independently. Mindset Online and Brainfacts repeat it (opened, low standing).
- Limits: told by the studio's head while promoting a book, about a hit-making period. No measured comparison, no denominators, no notes from a failed film. He says Disney's run of successes proves it; that is his own attribution.
- Would change: reviewers advise. The agent responsible decides what to do with a note, and records why.

**DR-20. Directors at Pixar still get replaced. Chapman, removed from Brave: animation directors have no guild protection, "We are replaced on a regular basis". Pinkava left Ratatouille (Wikipedia's wording: a departure "for lacking confidence in the story development"), and Bird took over and revised the story. Both films won the animated Oscar. Chapman says her vision still came through.**
- Source: Cartoon Brew quoting her NYT op-ed, https://www.cartoonbrew.com/animators/brenda-chapman-talks-about-brave-in-op-ed-68243.html ; https://en.wikipedia.org/wiki/Ratatouille_(film) ; scholar exchange at https://mediacommons.org/imr/node/2733
- Read: opened; **NYT op-ed itself not opened**.
- Kind: practitioner, reported.
- Corroboration: search 9 (several outlets, not opened).
- Limits: Pixar's reasons are not public beyond "creative differences". Can't tell if the swaps helped, since the alternative film doesn't exist. Whether the Braintrust influenced either is not established; one fan post claims so, unsourced.
- Would change: "advice only" describes the review forum, not the whole system. Write down who can replace or overrule the director. In a small studio that can only be the owner, which is a problem if the owner hasn't read the story (see the Draft).

**DR-21. Catmull's opening claim in the HBR piece is that a focus on the initial idea exaggerates its importance. He says confirmation bias is stronger than the term suggests, that "first conclusions are almost always wrong", and that new ideas "require protection".**
- Source: https://hbr.org/2008/09/how-pixar-fosters-collective-creativity (first paragraph); First Round as above.
- Read: opened for those passages.
- Kind: practitioner.
- Corroboration: his alone. Search 2's snippet that "every movie was terrible at inception" is not opened.
- Limits: slogans; written by a manager, not a director.
- Would change: an early draft isn't judged as final. Protect, then review. In AI-agent terms this matters less for feelings, and more for sequence: an early critique can freeze a draft's shape.

**DR-22. GAP: plussing, no source reached.**
- Search 2 didn't return it; Wikipedia has no page; the Fast Company piece I recalled was among the refused. From memory it is credited to Sims's Little Bets and a Pixar "yes, and"-style rule. **Unverified. Don't cite as Pixar's practice from this file.**
- Would change: nothing until read.

**DR-23. Note practice, problem not fix: ask non-experts what they feel, not what to change; a reviewer might say "she comes across too meek", while "make her outfit red" should be ignored as a fix. Robinson (a creative director) makes requested changes to show why they fail.**
- Source: art#61 (CGMA blog, Creative Bloq), read there.
- Read: from that pass.
- Kind: practitioner.
- Corroboration: 24 on actors. The aphorism on this usually credited to Gaiman: **not found in the Wikiquote page I opened; don't cite**.
- Limits: generic, with no outcome evidence.
- Would change: use it for owner's post-play reactions. Between skilled agents the case differs: see 28.

**DR-24. Kraak (writer and voice director): do script analysis first, finding each character's objective in first person; give little context, and no direction before take one, since actors may surprise you. Avoid "result" notes ("be angry", "more energy") and line readings. Use verbs ("intimidate"), facts about the scene, questions, and "as ifs"; use the language of permission.**
- Source: https://howtowriteagame.substack.com/p/how-to-direct-your-games-voice-actors
- Read: opened.
- Kind: practitioner (small-game voice director).
- Corroboration: repeats stage-acting doctrine; Weston, Stanislavski not opened. Gillmore on context (26).
- Limits: one indie director's advice; written for human actors, including "safe space", which doesn't apply to a text-to-speech engine or a writer agent. Whether verbs get better output from a voice model is untested. It's a cheap experiment.
- Would change: write direction per line as objective and verb, not adjective. Test verbs against adjectives on the actual voice engine. If adjectives win, drop the doctrine here.

**DR-25. Levine directed Infinite's leads himself. He gave them poles ("sees nothing and wants to see everything"), let them find the truth of it, and did not tell them where the plot goes: "I know what's going to happen to them, but I haven't told them yet." He does many takes because "I don't trust myself in the room" to pick, and chooses later, using sessions as a library, splicing lines from parts "almost like how a director works with a film editor". He balanced this with "all the other jobs I have".**
- Source: Gamasutra interview. https://gamedeveloper.com/design/ken-levine-on-the-storytelling-craft-of-i-bioshock-infinite-i-
- Read: opened. (This Ken Levine is the BioShock director; the TV writer at story#7 is a different person.)
- Kind: practitioner.
- Corroboration: Brown (story#55) says stop by about ten takes, and is opposed on count. Kraak (24) and Gillmore (26) want context given; he withholds plot and gives the character.
- Limits: said during production of a game whose schedule later needed rescue (38). Promotion interview.
- Would change: three transfers. (1) A performer can do good work without knowing the plot: voice agents could get beat and objective only. (2) Decide takes in the edit, against picture and neighbours, not at generation. (3) Don't hold writer and director jobs together on a big project; he lists this as a load.

**DR-26. Gillmore (Baldur's Gate 3 voice director): the job is interpreting the script and articulating context in a way useful to the actor and to the client. One line may need recording for several contexts ("Potentially your brother died; potentially he was rescued"). Actors' safety with hard material is part of the job.**
- Source: https://www.pcgamer.com/the-unique-challenge-of-directing-actors-in-an-open-ended-masterpiece-like-baldurs-gate-3-potentially-your-brother-died-potentially-he-was-rescued-were-going-to-do-all-those-options-its-a-lot
- Read: opened.
- Kind: practitioner.
- Corroboration: Brown (story#55, story#56), Kraak.
- Limits: large branching game. Human welfare doesn't transfer to synthetic voices; it does if humans are ever hired.
- Would change: a fixed motion comic needs far less of the many-contexts case. Where a line can follow two states, each state needs its own take or a neutral read.

**DR-27. Voice actors writing for directors disagree with parts of the above. Provide who is speaking, to whom, how; supply descriptive words such as "excited, reluctant", and Painter urges "colorful, terse" adjectives; if not working, suggest another role. Gilbert says too much backstory confuses because actors have built their own.**
- Source: https://gamedeveloper.com/audio/directing-the-voice-over-actor-tips-for-better-communication
- Read: opened.
- Kind: practitioner (actors, largely commercial voice-over).
- Corroboration: opposed to 24 on adjectives; agrees with 24 on not overloading.
- Limits: perspective of the actor; informal poll of friends; commercial work.
- Would change: don't write "never use adjectives" as a rule. The "who, to whom, how" triple is a minimal format for any voice direction.

**DR-28. Studies of feedback in dance and product design find that prescribing is one of several normal moves: providers personalise, puzzle, measure and prescribe; creators background, forecast and open. Patterns lead either to "excavations" (a return to old ideas, large changes) or "adjustments" (refinements).**
- Source: Harrison & Rouse, Academy of Management Journal (issued 2014 per OpenAlex). DOI 10.5465/amj.2012.0737
- Read: abstract only.
- Kind: measured, qualitative and inductive.
- Corroboration: none here.
- Limits: two domains, no outcome comparison of which moves were better. Doesn't show either fix or problem notes win.
- Would change: the note-form debate may be the wrong question. The director should say whether it wants an excavation or an adjustment, and pick the note to suit. That reading is mine, not the authors'.

**DR-29. Non-artists see what artists see in where they look, and are weak on how it was done; an owner's reaction is effect, not fix.**
- Source: art#61, art#66; list of owner questions at the end of the art pass.
- Read: from that pass.
- Kind: measured (old) and practitioner.
- Corroboration: 23.
- Limits: as listed there.
- Would change: the art pass's question list can be used for the owner on non-plot frames.

**Director's own words versus legend, for this section.** Own words read: Catmull via talk write-up, Chapman via quotation, Levine, Kraak, Gillmore. Legend here: the Pixar notes culture as a general recipe; the "plussing" rule (22); anything attributed to Catmull's book.

---

# Q4. Scene and sequence decisions

**DR-30. Murch's Rule of Six ranks what a cut should preserve: emotion, story, rhythm, eye trace, 2D plane, 3D space. If you can't have all, give up from the bottom. No Film School reports his weight of 51% for emotion, more than all others together.**
- Source: https://nofilmschool.com/2016/11/6-rules-good-cutting-according-oscar-winning-editor-walter-murch ; https://www.studiobinder.com/blog/walter-murch-rule-of-six/
- Read: opened, both. **In the Blink of an Eye not opened.** The remaining percentages (story 23, rhythm 10, eye trace 7, 2D 5, 3D 4) came from the search tool's memory-labelled note: not verified. Treat them as such.
- Kind: practitioner, second-hand.
- Corroboration: secondary sites agree; they likely copy one another.
- Limits: the numbers aren't measured; they express his priority. About the moment of a film cut, not a scene or a story. Nothing tested.
- Would change: the form transfers: a ranked sacrifice list. The last two criteria barely apply to layered stills, since no spatial cut continuity is at stake. Elsewhere it may work as tie-breaker language: emotion over story logic at a cut, but note the fairness of planted facts (story#14) can't be traded away this way. Name that exception.

**DR-31. Murch's rule on sound density: at any five-second moment, about five layers is the most an audience can follow while each stays distinct, and two and a half when layers fall in one tonal zone. To add one he had to remove another, and he dropped music when dialogue mattered. In the end the right thing is what serves the story.**
- Source: Murch, "Dense Clarity, Clear Density". https://transom.org/2005/walter-murch/
- Read: opened.
- Kind: practitioner, with demonstrated clips.
- Corroboration: none here.
- Limits: his observed threshold from one film and experience; not an experiment. He offers it as a suggestion, for practical purposes.
- Would change: a usable budget for a voiced comic's sound. Director's review could count concurrent layers under a line. Check by listening, not by count alone.

**DR-32. Murch argues film's strength in representation is its weakness: incomplete media let the audience complete what's only suggested, and sound separate from picture can reopen that gap.**
- Source: same URL.
- Read: opened.
- Kind: practitioner.
- Corroboration: story#57 (McCloud's closure, contested by Cohn).
- Limits: argument, not test. No one has tested this on motion comics.
- Would change: stills are incomplete by nature. Off-screen sound carries what a still can't, and the director may ask for sound for what isn't drawn rather than a drawing for what's said. Keep as a question to try.

**DR-33. What a scene must do, from practitioners here: each character has an objective (Kraak); it must keep you off balance, yet feel it had to turn out so (Lumet); no scene should be swappable with no loss (art#65); Miyazaki says every scene is pivotal for its moment, since each scene's problems shape the next.**
- Source: 24, 5 (review, line quoted as Lumet's), art#65, 1.
- Read: as listed.
- Kind: practitioner, and my inference for art#65.
- Corroboration: thin; each states something different.
- Limits: **no director's systematic scene criteria reached. McKee, Mamet, Mackendrick weren't opened. Partly unanswered.**
- Would change: a scene review with three questions: whose objective changes, what do we know now that we didn't, what breaks if cut. Those are mine, assembled from the above.

**DR-34. Half-Life's team measured pace: they logged player position, health and time across sessions and graphed where nothing happened or health sat too high or low; "experiential density" named the goal. Valve held 200+ sessions, each producing about 100 changes, half with repeat players. Disruptive changes got harder to push through late, filtering for most player effect at least work.**
- Source: Birdwell, as 17.
- Read: opened.
- Kind: practitioner, demonstrated.
- Corroboration: Klavins (story#24) on stall time.
- Limits: a shooter; one company's retrospective, written in triumph. A linear motion comic's dead time differs.
- Would change: pacing can be evidence, not only feel. Log per scene: word count, seconds, longest stretch with no player action, branch reach. See also story#73 on LLM acceleration.

**DR-35. Perceived length isn't runtime. Noyce on Clear and Present Danger: a trimmed version made more people think it was longer. Urban Ghost Story's filmmakers cut 15 minutes from the first 25, reluctantly, after industry viewers said it was too slow and they argued it out, and were amazed by how much they hadn't needed.**
- Source: https://en.wikipedia.org/wiki/Test_screening (opened), citing the filmmakers.
- Read: opened; primary sources not opened.
- Kind: reported.
- Corroboration: each is single.
- Limits: anecdotes, opposite directions.
- Would change: don't judge pace from runtime numbers alone (including from 34). Judge the assembled reel.

**DR-36. Whether "the real story is found in editing" is only partly supported here. Lumet says a film is always being rewritten. Levine says recording is a library edited later. Valve's prototype level was assembled from whatever already worked (51). Miyazaki discovered the reason for an ocean only when he reached the train scene, calling it luck. Blade Runner's versions and Murch's Apocalypse Now Redux (https://en.wikipedia.org/wiki/The_Conversations , opened; book not opened) show recuts as possible, not better.**
- Source: as cited.
- Read: as listed. **Murch's own account not read.**
- Kind: practitioner, demonstrated.
- Corroboration: several, each indirect.
- Limits: said after the fact. Nobody records stories that editing failed to find.
- Would change: an unlocked reel (still frames plus scratch voice) is where order and cuts can be changed cheaply. Lock in order: outline, reel, voice, final art. The cost slope for generated assets differs from film (regenerating a still is cheap, a contradiction in planted facts isn't), so reshoot thresholds should be re-derived. `production-stages` covers stages and schedule.

**DR-37. GAP: editors' role versus directors', beyond Murch's rules.**
- Search 1 returned mirror spam for the book. Nearest: Levine's team recommending takes (25). Status: unanswered.
- Would change: an AI studio can't assume an editor exists. Someone should own assembled-reel review. Separate from the writer of the scene seems wise, untested.

---

# Q5. Director, producer, writer

**DR-38. BioShock Infinite: staff feared it wouldn't finish; Thomas was hired in 2012 to help Levine cut scope with a roadmap; one developer said cut material could fill five or six games; final year was crunch. It shipped to critical acclaim.**
- Source: https://en.wikipedia.org/wiki/BioShock_Infinite (opened), citing reporting not opened.
- Read: opened secondary.
- Kind: reported.
- Corroboration: 25 on his load, from himself.
- Limits: "five or six games" is one person's phrase. The good reception and the cost are both real; no version exists with less scope.
- Would change: scope growth from a writer-director may need someone with the job of cutting, and that person may have a creative title. Who has authority to cut story content without the owner knowing the plot? The producer can't read a sealed plot: see Draft.

**DR-39. Half-Life had no director. Valve looked for a "godlike game designer" for 11 months, concluded the person didn't exist, and built the Cabal: at first three engineers, a level designer, a writer, an animator, four days a week, six hours a day for five months, then rotating people every month, mini-cabals including outsiders. Everyone had shipping responsibility, none were dedicated designers. Playtesters "settled" arguments, and "an authority that everyone could rebel against just didn't exist". Still, one person followed the whole story and held the document, and a professional writer was "key". A hierarchy, he argues, needs one person who understands everyone's work as well as they do, which isn't practical.**
- Source: Birdwell, as 17.
- Read: opened.
- Kind: practitioner, demonstrated.
- Corroboration: none here for the method. The award count is his own claim.
- Limits: told in 1999 by a winner, at a "fairly independent" studio that could afford a restart. Not all people suited it, he says. A single case; it doesn't show the method beats a director.
- Would change: **the main counterexample to the role.** A director isn't required for quality. Yet Cabal had what the role would hold: a keeper of the whole story, a written bible, and tests that overrule opinion. Those functions may matter more than a title. Also: "an agent who understands everyone's work at their level" is more achievable by a model than by a person, unverified.

**DR-40. Over-control: Duke Nukem Forever. Broussard switched engines weeks after a well-received trailer, an effective reboot. Couldn't tolerate shipping without the latest technology. Self-funded, so no publisher forced decisions; once said they could go five more years. Half the team left by 2006. Shut down 2009.**
- Source: Clive Thompson, Wired, 2009. https://www.wired.com/2009/12/fail-duke-nukem/ ; Daikatana (Romero) has a similar engine and departures pattern, https://en.wikipedia.org/wiki/Daikatana (intro only).
- Read: opened.
- Kind: reported.
- Corroboration: 2 in pattern; both are famous because they failed.
- Limits: mostly anonymous sources; Broussard refused interview amid a lawsuit. Hindsight.
- Would change: a director with no external stop and no end condition can loop indefinitely. AI agents can loop cheaply. A "done" definition set in advance and a budget are safeguards, owned by the producer, and may not be waived by the director.

**DR-41. Over-reach and over-budget: Heaven's Gate went from a $12 M estimate to about $36 M, and cost UA $44 M, earned $3.5 M, was recut and failed. Some historians, including Biskind, say it ended director-driven Hollywood and caused UA's sale.**
- Source: https://en.wikipedia.org/wiki/Heaven%27s_Gate_(film) ; on-page citations not opened; Bach's Final Cut not opened.
- Read: opened secondary.
- Kind: reported.
- Corroboration: https://en.wikipedia.org/wiki/Auteur_theory repeats the industry reading.
- Limits: a single-cause story for an industry shift is suspect. Some later critics favour the long version (not researched here).
- Would change: nothing beyond 40 by itself. A warning against the auteur story being tidy in either direction.

**DR-42. Loss of control in the other direction: RKO cut over an hour of The Magnificent Ambersons and shot a happier ending; the footage was destroyed; Welles's notes survive. Hence the film's supposed lost greatness can't be checked.**
- Source: https://en.wikipedia.org/wiki/The_Magnificent_Ambersons_(film)
- Read: opened secondary.
- Kind: reported.
- Corroboration: National article (50) mentions it as test-driven.
- Limits: unfalsifiable. A pure legend risk.
- Would change: keep every director's cut. Version the assembled reel, so that "what if" is checkable, unlike Ambersons.

**DR-43. The reverse of authority: Cammisotto says as a work-for-hire game director he was a "yes-man" shaping to milestones, and nearly quit. Adler credits pushing through objections for features like player radios.**
- Source: https://www.polygon.com/game-direction-explained-by-directors
- Read: opened.
- Kind: practitioner.
- Corroboration: opposite poles of 40.
- Limits: Adler's survivors speak; features that failed aren't named.
- Would change: if every story call is routinely bounced to review or to the producer, the director has the title and not the job. Conversely, "I believed anyway" is not evidence.

**DR-44. In US TV the showrunner, usually a writer, outranks episode directors and answers only to the network; in features the director normally holds creative control. Auteur theory (Sarris) was challenged by Kael, who stressed collaborators; Kipen's "Schreiber theory" gives authorship to the screenwriter; Harmetz points to Casablanca's producer and studio.**
- Source: https://en.wikipedia.org/wiki/Showrunner ; https://en.wikipedia.org/wiki/Auteur_theory
- Read: opened secondary. **Kael, Sarris, Kipen, Harmetz not opened.**
- Kind: reported.
- Corroboration: each other.
- Limits: encyclopedia summaries. Search budget went to other questions, and no working showrunner was reached (the story pass also failed at story#11). Partly unanswered.
- Would change: a serial story project looks more like a showrunner model (writer in charge, continuity first) than film's. Decide whether director and lead writer are one role, or two with a named tie-breaker. Evidence doesn't settle this.

**DR-45. How conflicts get settled, from these sources: playtests for Valve (39); Miyazaki's producer by a schedule threat (1); Catmull waits weeks and returns with arguments, and Jobs let him do it his way when they didn't converge (19); Fatal Attraction's director refused until Lansing offered another $1.5 M (46).**
- Source: as cited.
- Read: opened.
- Kind: practitioner, reported.
- Corroboration: not comparable with each other.
- Limits: no general account found.
- Would change: agents don't have weeks or pride. Pick one settlement path in advance: evidence if a test can decide; otherwise the named tie-breaker decides and records it.

---

# Q6. Deciding under uncertainty

**DR-46. Test-screening case: Fatal Attraction. Goetz, then in screening research, says the original ending made the air go out of the room, and that the reshoot turned a $50-75 M film into hundreds of millions. Wikipedia reports Lyne refused until paid an additional $1.5 M; several cast were against it.**
- Source: Kevin Goetz in Total Film, Jan 2022. https://kevingoetz360.com/wp-content/uploads/2022/01/Kevin-Goetz-Total-Film-Magazine-Jan-2022.pdf ; https://en.wikipedia.org/wiki/Fatal_Attraction
- Read: opened.
- Kind: practitioner (with commercial interest), reported.
- Corroboration: National article (50).
- Limits: the $50-75 M number is a counterfactual nobody can check. Revenue isn't quality. Says nothing about whether the film is better.
- Would change: a test measures reaction under one set of conditions, and money was the goal here. A project aimed at its owner's entertainment has another goal, so copying a film's revenue logic is wrong.

**DR-47. Comprehension fixes have cleaner stories. Moonstruck changed opening music to signal comedy (Goetz). La La Land reinstated its freeway opening after confused viewers (Wikipedia citing Audience-ology). Wilder dropped Sunset Boulevard's first reel after a test, per Ebert. Shaun of the Dead added a 15-second ending after "abrupt" comments.**
- Source: Goetz interview; https://en.wikipedia.org/wiki/Test_screening
- Read: opened; originals not opened.
- Kind: practitioner, reported.
- Corroboration: 4 cases, partly from one industry advocate.
- Limits: selected successes. The Audience-ology book isn't opened; Goetz picked examples to make his case, by his own word.
- Would change: separate "did you understand" (which a cold reader can report) from "did you like it" (for which the director may hold). Reading 47 with 48 is my inference.

**DR-48. Se7en: test audiences recruited on Freeman's and Pitt's earlier gentle films produced a screening called a "disaster"; results were middling; it was predicted to do badly. Fincher and Pitt kept the ending (Pitt's condition for joining, after Legends of the Fall's ending was changed by tests). It grossed $327 M.**
- Source: The National, https://thenationalnews.com/arts/the-cruellest-cuts-1.493245 ; https://en.wikipedia.org/wiki/Seven_(1995_film)
- Read: opened secondary.
- Kind: reported.
- Corroboration: Wikipedia and National partly; search 7 conflicts on details.
- Limits: one famous case, chosen because it paid off. Directors who kept endings and failed aren't listed. The test wasn't ignored completely: a longer epilogue was added, and tests preferred Mills killing Doe.
- Would change: check who the tester was before weighing the verdict. A cold reader briefed to expect another genre can sink a good scene.

**DR-49. Blade Runner: tests led to voice-over and a happier ending; a strong response to a workprint later led to the director's cut. So two test results point opposite ways a decade apart.**
- Source: https://en.wikipedia.org/wiki/Blade_Runner ; National.
- Read: opened secondary.
- Kind: reported.
- Corroboration: search 7 agrees.
- Limits: audience self-selected for the later version. Not a controlled comparison.
- Would change: a test audience isn't a single voice. Note date, audience and what they were told.

**DR-50. Sampling bias: every case above is known because the film is famous. Goetz claims 7,000 titles and says "lock it" fewer than 10 times, with no public outcome data. The National concludes "the jury is out". Spielberg shows rough cuts only to friends; Spike Lee tests while holding final cut; Luhrmann says tests didn't change Australia's ending, though reports said they did; Ebert says tests are valid for filmmakers but a "weapon" for executives; Ang Lee, per Goetz, said Picasso never tested paintings. Casablanca is said to have bombed in tests (National).**
- Source: https://thenationalnews.com/arts/the-cruellest-cuts-1.493245 ; Goetz; Ebert via https://en.wikipedia.org/wiki/Test_screening
- Read: opened; Ebert not opened; Casablanca claim unverified.
- Kind: reported, inference (the bias statement is mine).
- Corroboration: not applicable.
- Limits: **no study in this pass gives the rate at which following or ignoring tests helped. Unanswered.** Search 7 returned list articles; the MOVIEMOD-type marketing models weren't reached. **I found no documented case of a director ignoring a test and being shown wrong.** That absence is the bias at work, not evidence that it doesn't happen: such films are forgotten, or their failure is blamed on something else.
- Would change: never cite "they ignored the test and were right" as a reason. Weigh a test on its design.

**DR-51. Restart: same move, opposite outcomes. Valve scrapped Half-Life a year out, because nobody believed more time would help, and first built one fun prototype level from what worked, which then became "the vision". Broussard restarted to chase rivals' engines (40). BioWare trusted last-minute "magic" (14).**
- Source: Birdwell; Wired; Schreier, all opened.
- Read: opened.
- Kind: practitioner, reported.
- Corroboration: three cases.
- Limits: survivors and spectacular failures only. My distinction (a restart aimed at an experience already shown to work, versus one aimed at keeping up) is my reading.
- Would change: restart only with a small proof in hand that shows what would be restarted toward, and a named reason other than the state of the art.

**DR-52. Creators predict the audience success of others' novel ideas better than managers do, but not their own ideas. The advantage shrinks when a creator's previous poor ideas succeeded anyway. Lab work ties it to divergent thinking in the creator role. Field study: 339 circus professionals, 13,248 audience members.**
- Source: Justin Berg, 2016, Administrative Science Quarterly. DOI 10.1177/0001839216642211
- Read: abstract only.
- Kind: measured.
- Corroboration: none here on forecasting. 54 on own-knowledge bias is related.
- Limits: circus acts, live audiences, predictions of liking. Human careers. Doesn't speak to models.
- Would change: (1) the director's forecast of its own ideas is weak, so route own ideas to someone else. (2) A role that only judges may be less accurate than one that also makes. That pulls against "directs without doing their jobs". Consider the director drafting small alternatives, like a thumbnail or a rewrite of one line, as part of judging. Untested for AI.

**DR-53. Miyazaki says success doesn't change his method: "You never know how a film will play." Catmull says that saying "story is king" doesn't make it true, and that things that are true don't necessarily alter behaviour. A Jackbox director: "We learned a lot just by playing."**
- Source: Midnight Eye; First Round; Jackbox.
- Read: opened.
- Kind: practitioner.
- Corroboration: weak.
- Limits: slogans. Berg's finding (52) shows success can mislead, consistent with Miyazaki's stance.
- Would change: minor. Don't treat earlier wins as proof of the method.

---

# Q7. Surprise on behalf of an audience

**DR-54. Curse of knowledge, measured: adults who know an event's outcome reason worse about another person's false belief, and how plausible they find the outcome mediates this.**
- Source: Birch & Bloom 2007, Psychological Science. DOI 10.1111/j.1467-9280.2007.01909.x
- Read: abstract only.
- Kind: measured.
- Corroboration: 55.
- Limits: a false-belief task, not story judgement. Not on experts or on models. Effect sizes not seen.
- Would change: a director that knows the ending has a known bias on exactly the question "will they see it coming". Do not trust its own read. Plausibility mediating suggests a twist's apparent fairness to its author may itself distort the author's read; I can't say in which direction.

**DR-55. Fischhoff 1975 and Camerer et al. 1989: participants didn't know outcome knowledge affected them, and when told still couldn't ignore it; better-informed agents fail to predict the less informed.**
- Source: https://en.wikipedia.org/wiki/Curse_of_knowledge
- Read: opened secondary; originals not opened.
- Kind: measured, reported.
- Corroboration: 54.
- Limits: as reported in an encyclopedia.
- Would change: instructions like "imagine you don't know" aren't a sufficient mitigation for people. Whether they work for LLMs is an untested question.

**DR-56. A fresh player's time showed what the maker couldn't. Van Lierop, new at 3D Realms in 2007, took about five hours on levels Broussard thought took half that. He said it was a year from shipping; Broussard said two. Wired says Broussard had lost perspective.**
- Source: https://www.wired.com/2009/12/fail-duke-nukem/
- Read: opened.
- Kind: reported.
- Corroboration: 57.
- Limits: one person's recollection, friendly to himself; a new hire isn't a naive player.
- Would change: time measures from a first-time reader catch what the maker can't see.

**DR-57. Valve's silent playtest: outside volunteers play two hours, watched by the area's designer, who may not speak or hint. Birdwell: the "obvious" answer often proves arbitrary. Also mini-Cabals include someone from outside the problem, to keep a fresh perspective, and members rotate monthly.**
- Source: Birdwell.
- Read: opened.
- Kind: practitioner.
- Corroboration: Wolpaw (retelling; comedy harder to evaluate, story#48), Klavins (story#24).
- Limits: gameplay comprehension and fun; not twist surprise.
- Would change: rules for cold reads: tester gets only what the player gets, and no one explains. Ask for a retelling (story#48) rather than a rating.

**DR-58. Spoiler studies disagree. Leavitt & Christenfeld 2011 reported spoiled stories enjoyed as much or more. Johnson & Rosenbaum (N=412, within subjects) found unspoiled stories more fun, suspenseful, moving and enjoyable. Daniel & Katz failed to replicate the positive effect, and found spoilers hurt enjoyment for TV episodes but not short stories. Rosenbaum & Johnson and Levine et al. point to individual differences.**
- Source: DOI 10.1177/0956797611417007 ; DOI 10.1177/0093650214564051 ; preprint DOI 10.31234/osf.io/mgh8k
- Read: abstract only. The Leavitt abstract as returned has only background; its result is as summarised by the later two papers. Rosenbaum & Johnson and Levine et al. not opened.
- Kind: measured.
- Corroboration: contested by design.
- Limits: short stories and TV episodes, one-off exposure. No games or long serials. No test of play. The preprint isn't peer reviewed in what I read.
- Would change: supports the owner's wish to stay unspoiled, weakly. Also: a story that holds on re-reading isn't protected from a spoiled first read. Don't argue "it wouldn't matter if the owner found out".

**DR-59. Goetz says ambiguity sometimes intrigues and polarises, and answering it makes a film less exciting; "oftentimes" it doesn't.**
- Source: Goetz, Total Film, as 46.
- Read: opened.
- Kind: practitioner.
- Corroboration: Levine on leaving Infinite's ending open (https://en.wikipedia.org/wiki/BioShock_Infinite , opened).
- Limits: unfalsifiable as stated.
- Would change: cold readers' confusion needs a follow-up: are they curious or lost? Ask what they want to know next.

**DR-60. GAP: how directors themselves judge a twist they know.**
- Search 11 aimed at Johnson, Shyamalan, table reads and playtested twists; it returned writing-advice sites offering: ask readers when they guessed; check that clues hold on second reading (https://writing.codidact.com/posts/23627 , https://www.stage32.com/lounge/screenwriting/How-do-you-test-if-your-pilot-script-truly-hooks-the-audience , not opened; low standing). Fair-play checks are at story#14 to story#17, story#50. Hitchcock on bomb-under-the-table suspense: from memory, not opened.
- Would change: use "guess point" and "second-reading" as cheap tests, knowing they come from low-standing advice.

**DR-61. Compensations for the director's knowledge, as far as these sources go: outside people (56, 57); repeat testers kept apart from fresh ones (Valve's half and half; Klavins, story#24); someone who hasn't read the outline. Levine shows performers can be kept ignorant of plot (25). No source tests a context-isolated AI reader as a stand-in for a human.**
- Source: as cited.
- Read: as listed.
- Kind: inference, from practitioner sources.
- Corroboration: pattern only.
- Limits: AI readers differ from people: measured story failures (story#73 to story#83) suggest shared blind spots, and a model may report surprise it wasn't "feeling". **Rule 4 in the owner's working rules: do not claim a scene surprises, only report what a cold reader said.**
- Would change: cold-read agents are fresh, get only player-visible material in order, and report: retelling, current theory of what's going on, what they expect next, where they lost interest. The director compares these with intended reader state. If they all guess the same at the same panel, that's a finding; if none guess, that's only weak evidence, since fresh models may be credulous. Validation against any human is needed before trusting it.

**DR-62. GAP: the owner's own case has no direct precedent in this pass.**
- I found no account of a director keeping a plot from the person commissioning it, as a method. Nearest are Levine with actors (25), and Pixar directors who may ignore notes (19). Cammisotto (43) shows the opposite.
- Would change: treat as novel, and record what happens. The first play is single-use: it can't be repeated once spent. Consider asking the owner now whether a human stand-in may read ahead of time. This is the owner's call, not the director's.

---

# Q8. Measured work

**DR-63. Across 266 studies and 13 leadership variables, authentic, empowering and entrepreneurial leadership related most strongly to creative performance; for innovative performance, transactional (contingent reward) and supportive were most relevant. Authoritarian and destructive are in the set. "Directive" isn't.**
- Source: Lee, Legood, Hughes, Tian, Newman, Knight 2020, EJWOP. DOI 10.1080/1359432X.2019.1661837
- Read: abstract only; PDF returned empty; no effect sizes seen.
- Kind: measured.
- Corroboration: 64 only partly.
- Limits: correlational; typical data are workplace surveys, where followers rate leaders (I didn't confirm the mix). Doesn't study films or games.
- Would change: little on its own. Human motivation mechanisms (autonomy, trust) may not transfer to agents who have no motivation. Inference: this literature is least useful exactly where the agents differ from people.

**DR-64. Directive teams beat empowering ones early, empowered teams improved faster, and were comparable by the end, through learning, coordination and shared mental models.**
- Source: Lorinkova, Pearsall, Sims 2013, AMJ. DOI 10.5465/amj.2011.0132 ; digest and critique at https://bps.org.uk/research-digest/when-it-better-be-directive-or-empowering-leader
- Read: abstract and digest opened.
- Kind: measured.
- Corroboration: single.
- Limits: 60 five-person undergraduate teams, one roughly 3-hour computer battle task. Not creative. Digest writer calls the phases arbitrary. Performance, not quality.
- Would change: fresh agents never gain the "team learning" that made empowerment pay off here, since they restart each task. So one-shot agents may fit directive briefs better. Inference, untested, and it depends on what's in shared files.

**DR-65. A review of film success finds separate criteria: critics, money and awards are partly distinct, and predictors differ across them. In 1,327 films, impact was a function of a dramatic cluster (direction, acting, screenplay, editing, as I understand the list) and a visual cluster, the dramatic cluster primary.**
- Source: Simonton 2004, JASP, DOI 10.1111/j.1559-1816.2004.tb02016.x ; Simonton 2009, Psychology & Marketing, DOI 10.1002/mar.20280
- Read: abstract only. Cluster membership of direction not confirmed from the abstract.
- Kind: measured.
- Corroboration: Cattani & Ferriani 2008 (DOI 10.1287/orsc.1070.0350, abstract only): Hollywood creative achievement relates to intermediate core-periphery network position, 1992 to 2003.
- Limits: awards and guide ratings. Awards go together, so the cluster may reflect voters. Can't separate a director's vision from a good script. **It doesn't test whether a single vision predicts quality.**
- Would change: dramatic work has first claim on budget, weakly. Don't cite it as evidence for directors.

**DR-66. Team "vision" is one of the strongest correlates of team innovation (with support for innovation, task orientation and external communication; rho 0.4 to 0.5, 104 studies), but team variables show much stronger links to self-reported innovation than to independent or objective measures.**
- Source: Hülsheger, Anderson, Salgado 2009, J. Applied Psychology. DOI 10.1037/a0015978
- Read: abstract only (Europe PMC).
- Kind: measured.
- Corroboration: 9 in spirit.
- Limits: shared team vision as rated by members, not a director's strong personal vision, and correlational. Self-report inflation is stated by the authors. Mostly organisational work settings.
- Would change: shared understanding is the supported form. Can be checked: ask each agent what the work is for, and compare answers.

**DR-67. Across 854 games ($4 B revenue), variance among individuals explains more firm performance than assumed, and middle managers matter much more than those in innovative roles.**
- Source: Mollick 2012, Strategic Management Journal, DOI 10.1002/smj.1958 ; working paper 10.2139/ssrn.1630546
- Read: abstract only. The mapping of roles (producers as middle managers, designers as innovators) is from memory, not the abstract. Numbers beyond those above not seen.
- Kind: measured.
- Corroboration: none here.
- Limits: revenue, not quality. Multilevel variance doesn't tell what the person did. Doesn't isolate top creative directors.
- Would change: don't let a director role crowd out the producer. Together with 39 it undercuts "the director's vision is the main lever". It supports the existing studio arrangement of a strong producer.

**DR-68. Distinctive and acclaimed games come from teams with overlapping groups of people from cognitively distant backgrounds. 12,422 games; 139,727 developers.**
- Source: de Vaan, Vedres, Stark 2015, American Journal of Sociology. DOI 10.1086/681213
- Read: abstract only.
- Kind: measured.
- Corroboration: 39 in spirit.
- Limits: human career histories as proxies for cognitive style. Doesn't look at directors. Correlational.
- Would change: agents running one model may share too much. Different reference material, or a different model for one reviewer, might supply distance. That's speculation, with art#62 and story#73 pointing at convergence risks.

**DR-69. Psychological safety predicted learning behaviour in 51 manufacturing teams.**
- Source: Edmondson 1999, ASQ. DOI 10.2307/2666999
- Read: abstract only.
- Kind: measured.
- Corroboration: search 2's claim that Edmondson cites Pixar (not opened).
- Limits: manufacturing. Agents don't fear reprisal. The transferable risk is a reviewer agent agreeing too readily, which this study can't speak to.
- Would change: reviewers need instruction and an output format that can return "this fails". A check that can't fail isn't one.

**DR-70. GAP: whether a single strong vision predicts quality in films or games is not known from anything I found.**
- Search 4 plus title lookups found nothing that tests it. Uzzi & Spiro's Broadway study was found, abstract missing. Wu et al. 2019 (small teams disrupt) abstract missing. **A well-sourced "this isn't known" here, subject to limits of 12 searches.**
- Would change: rules must not say that strong direction improves quality. They can say it reduces decision delay and contradiction: those are checkable claims about process.

---

# Where directors disagree

1. **Script before boards, or boards before story.** Miyazaki no script, and calls that dangerous (1). Kon script first, board changes details (3). Levine outlines the whole, writes as late as he can (25). Budgets and the fairness of planted facts probably settle it for a story that depends on them: lock facts early.
2. **Strong vision or group.** Fox, Rubyor, Schreier's sources (9, 14) against Birdwell (39), Dracott (7), Jackbox (8). Valve's own document still kept a single story holder.
3. **Result notes.** Kraak says never (24). Painter asks for colourful adjectives (27). Harrison & Rouse suggest prescribing is normal (28). Untested for all.
4. **Context for performers.** Gillmore: articulate context (26). Gilbert: too much backstory fails (27). Levine: withhold plot (25). Kraak: small amount, none on direction before take one (24).
5. **Takes.** Levine: many, decide later (25). Brown: stop by about ten (story#55). Cost is different with synthetic voices.
6. **Braintrust as advice or authority.** Catmull: no authority (19). Chapman: directors get replaced anyway (20). Both can be true at different levels.
7. **Test audiences.** Goetz: 7,000 titles, nearly all improvable (46, 50). Ang Lee via Goetz: art isn't tested. Spielberg: friends only; Spike Lee: tests, keeps final cut. Ebert: valid for makers, weapon for executives.
8. **Believing against objections.** Adler: pushed through (43). Broussard pushed through too (40). Both believed. Difference visible only afterwards.
9. **Do spoilers hurt.** Leavitt & Christenfeld against Johnson & Rosenbaum, and Daniel & Katz (58).
10. **Who is the author.** Sarris, Kael, Kipen (44).
11. **Pillars.** Pears: mechanics may be removed if off-pillar; his own list reads as systems (13). Wagar: system-name pillars atomise (13). Nothing compares outcomes.

# Legends with weak support

Meaning weak in what I could open, not false.

1. **The auteur makes the film.** Cuts against 39, 65, 67, 68. Argued by Kael (44).
2. **Strong vision causes quality.** No test found (70). The best correlates are self-reported (66).
3. **Pixar's Braintrust as a recipe.** Told by its chief; copies inside Pixar failed; no denominators (19, 20).
4. **Plussing as a documented Pixar rule.** Not reached (22).
5. **Murch's percentages as findings.** Priority expressed as numbers; only 51 seen, and none at source (30).
6. **"The film is found in the edit" as general law.** Indirect here (36).
7. **"Ignored the test and was right."** Selected cases, no rates (48, 50).
8. **"Test audiences would have killed Casablanca, or made Fatal Attraction."** Unverifiable counterfactuals; the second is the tester's own (46, 50).
9. **Heaven's Gate ended the director era.** Single-cause story, from historians (41).
10. **BioWare magic.** Studio folklore: crunch can make it cohere. Inquisition is its survivor (10, 14).
11. **Pillars work.** Reported by teachers; no failure account found (13).
12. **Miyazaki's method as a model.** He says it's dangerous (1).
13. **"Directors should let creators find it."** Only winners tell it (6, 25).
14. **Empowering leadership wins.** The usual reading of 63 and 64. Neither shows it for creative work led by a director.

# What transfers to an AI director, and what doesn't

All inference.

| Practice | Transfers? | Why |
|---|---|---|
| Statement of what it's about, with what it rejects | Yes, and more than for people | Nothing else carries across fresh runs (17) |
| Named tie-breaker | Yes | Agents won't negotiate over time; fights must end |
| Advice-only review forum | Partly | The defensiveness it avoids isn't there. The separation of who decides still is |
| Silent observer | Yes | Easy to enforce: give cold readers only player-visible text |
| Verbs and objectives for voice | Test first | Doctrine is about human psychology; a voice model may respond differently |
| Takes library and decide in edit | Yes, cheaply | Generation is cheap; listening costs tokens or the owner's attention |
| Actor safety | No, unless humans are hired | |
| Set, blocking, camera crew | No | Except framing language for stills (art#11 to art#18) |
| Rehearsal | Partly | Scratch-voice reel plays its part |
| Team learning, trust, motivation | Weak | Agents restart; the studies measure people (63, 64) |
| "Fresh eyes" | Strongly different | People can only be fresh once. A context-free agent can be fresh repeatedly, but may be systematically unlike a player (61) |
| The director's own taste | Unknown | Models converge on generic choices (story#73, art#62). A director model may rate its own default as good |

# Draft: what a director agent decides, what it delegates, what it must escalate

**All inference from the claims above. Not tested. Not rule text.**

**Decides** (and records in a sealed file; each one with reason and date)
- What the work is about, what it rejects, who the proxy audience is, and what changes first to last (5, 11, 12).
- Which scenes exist, their order, what the reader should believe at each scene, and what they should be surprised by (33, 36).
- Tone, voice and look targets, ranked by what gets sacrificed first (18, 30).
- Which note a piece needs: excavation or adjustment (28), and which takes or frames go in (25).
- Whether a cold read's finding is taken or held, with the reason (47, 48, 52).

**Delegates** (never does it as a replacement)
- Prose and dialogue to writer, specs and mechanics to designer, assets and integration to presentation, verification to QA, schedule and budget to producer. Exception worth considering: small proofs like one rewritten line or a thumbnail to make a note clear, and to keep its own judgement honest (52). A proof is thrown away, never shipped.
- Cold reads to agents who haven't seen the plot (54, 55, 61).
- Judging its own ideas: a separate reviewer, since creators can't forecast their own (52).

**Must escalate to the owner, without spoilers**
- Changing what the owner set: audience, rating range or content limits (story#59 to story#72), length ceiling, budget, medium.
- A real person's likeness, a real organisation, sensitive subject matter beyond the owner's limits. These can be asked in general terms ("Should the game show X kind of content?") with the plot withheld.
- Anything spent or published, any irreversible choice on a shared system. Standing rule.
- A disagreement with the producer that didn't end in the named path after one round (45).
- Look and feel on non-plot frames: the existing agent-team skill keeps those with the owner, and says to confirm a look before a full build. Use frames with no plot content (a street, a style test), which can test look without spoiling anything.
- When cold reads repeatedly fail on something central, and when the plan was going to rely on the owner's first play to tell.
- Asking in advance: may a human stand-in read ahead? (62).

**Conflicts with the existing agent-team skill, to settle in the design, all inference**
1. **"The user keeps the judgement of feel and look"** and a "human playtest as a milestone gate". The owner keeps that, by playing. But if the human gate arrives only at the end, there's no earlier gate on story. Options: play chapter by chapter in order, so each chapter is both a spoiler-safe test and a real play. That spends the surprise, as intended, in small amounts.
2. **Status reports open with progress** and "every report to the user". Reports must not say what's in a scene. Use counts and states only ("episode 3: boards reviewed, cold read: 2 of 3 understood the turn").
3. **Spoilers leak through ordinary work.** Issue titles, branch names, commit messages, PR bodies, board entries, QA's bug reports, and file names in a repo the owner may read (scene names, asset names like `reveal_<who>.png`). Plot content needs its own location, named so the owner knows not to look, and neutral IDs. Merge-reviewer and QA need a form of evidence that doesn't reveal. **Stills-as-evidence is a spoiler route.**
4. **Take-over rule (rule 11).** Someone must be able to pick up a sealed plot. Sealed isn't lost: it lives in the repo, labelled, and the owner can break the seal at any time. Recording this is not a loss of the working rule "write it down".
5. **Who overrules the director?** Pixar's answer is the studio (20). Here the only person above the director has chosen not to read. Candidates: a second agent, reading the sealed file, as an independent review of the story bible's logic, with no authority (19), and the owner's option to break the seal. Producer can't overrule on story, but keeps budget and "done" (40, 67).
6. **Role overlap.** Today's `presentation` owns art direction, `designer` owns story outline, `writer` owns the bible and tone document. A director takes the top decision from each. Their definitions need to say so.
7. **Critical-path rule.** The director can generate endless "one more pass". Set a done condition per scene ahead of time. Two rounds in a row with nothing closed already triggers a stop (40, 36).

**Things the agent shouldn't claim** (rule 4)
- "This twist will surprise you." It can only report cold readers' results.
- "The owner will love this." The director has no measurement of that until play.
- "Strong direction will make it better." Not shown (70).

---

# Question status

| Q | Status | What's missing, and what was searched |
|---|---|---|
| 1 Director's job by medium | Partly answered | Anime and games: own words. Film: **Lumet through a review only; Mackendrick, Murch's book and Katz not reached.** Disney and Pixar story supervisors unanswered. Searches 1, 5, 8, 12 |
| 2 Holding a vision | Largely answered on practice | Failure of pillars specifically **unanswered** (searches 3, 6). Anthem and Andromeda from one reporter. Tone documents: only art#28 |
| 3 Direction and notes | Partly answered | Voice direction: good. Catmull: First Round and Sloan only, book not opened, HBR preview only. **Plussing unanswered.** Directing writers and artists specifically: art#61, thin. Searches 2, 9, 10 |
| 4 Scene and sequence | Partly answered | Rule of six via secondary; dense clarity at source. Murch's "film found in edit" and **editor's role not read**. Reel practice: inference. Search 1 |
| 5 Director versus producer, failures | Largely answered on cases, thin on showrunners | Daikatana intro only. MGS V: page opened, nothing usable taken. No working showrunner. Searches 3, 9, 12 |
| 6 Uncertainty, tests | Partly answered | Cases from Goetz, National, encyclopedia. **No rates; survivorship is stated.** Trust-test rates unanswered. Search 7 |
| 7 Surprise | Partly answered | Curse of knowledge and spoiler studies: abstracts. **Directors' own methods on twists unanswered** (search 11). Owner-blind case: no precedent found |
| 8 Measured | Partly answered | All abstract only. **Single vision and quality: not known.** Uzzi & Spiro and Wu et al.: abstract missing. Search 4 and title lookups |

# Searches spent (12 of 12)

1 Murch rule of six; 2 Catmull, Braintrust, plussing; 3 pillars, Anthem, Andromeda; 4 directive versus empowering; 5 Lumet, Mackendrick; 6 usable pillars and failures; 7 test screenings; 8 anime director's role; 9 Chapman and Pixar replacements; 10 voice direction, Hennig; 11 twist judgement; 12 game director's role, Hennig, Miyazaki, Barlog.

Search returned nothing usable for Hennig, Hidetaka Miyazaki or Barlog, so **those directors, often named for this topic, are absent**. Sakurai on director versus producer: a pointer page only (https://gonintendo.com/contents/37932-masahiro-sakurai-explains-the-difference-between-game-producers-and-directors , opened, no content), leaving his video not watched.

Raw downloads and lookup scripts stayed in the research session's scratch folder, not in this repo; downloads were treated as untrusted data and only read as text.

# Leads, not evidence

From memory or search-only; not opened, not claims: Lumet's chapters in full; Mackendrick's On Film-Making (Cronin ed.); Katz; Murch's In the Blink of an Eye, including its section on test screenings; Ondaatje's The Conversations; Catmull's Creativity, Inc., including what makes a good note; Sims's Little Bets on plussing; Weston's Directing Actors; Mamet's On Directing Film; Truffaut's Hitchcock on the bomb under the table; Goetz's Audience-ology; Schreier's Blood, Sweat, and Pixels and Press Reset; Darrah's Anthem video; Cory Barlog and Amy Hennig interviews; Zootopia's and Inside Out's late story changes (Wikipedia pages opened, nothing confirmed); Bach's Final Cut; Uzzi & Spiro 2005 (DOI 10.1086/432782, checked title only); Ely, Frankel & Kamenica on suspense and surprise.
