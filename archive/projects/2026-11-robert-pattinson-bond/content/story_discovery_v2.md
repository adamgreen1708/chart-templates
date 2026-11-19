# Editorial reset: From Twilight to 007
**19 November 2026 — research revision after visual review; not an approved chart or post.**

## Why the first three charts are not sufficient
The initial rating-median bars, generic rating-vote scatter and Bond-actor-era counts passed rendering checks but failed the editorial test. They hid the specific films, turning points and personal connections. **Do not publish or re-use the first three PNGs as approved visuals.** Preserve configs only for comparison during redesign.

The key error in Chart 3 was treating 14 cast-to-Bond-film pair rows as if six real people could usefully be summarised by Bond actor. Multiple entries for Ralph Fiennes, Pierce Brosnan and Jeffrey Wright count their various Bond films, not additional collaborators. Zero matches in earlier eras are a limitation of the coverage rather than proof of no connections.

## Verified quantitative discoveries
Source: official IMDb TSV.gz extraction, [successful v1 review run](https://github.com/adamgreen1708/chart-templates/actions/runs/44478261914), 18 November 2026 frozen study date; 33 released, rated titles, IMDb weighted movie ratings and film-level vote counts, not judgements of individual performances.

- The five **Twilight** movies have ratings **4.8, 5.0, 5.1, 5.4 and 5.6** (median **5.1**). Their title-vote counts sum to **1,723,898**, approximately **24.8%** of the 6,939,190 total title-vote counts across all 33 eligible films. A sum of title votes is not unique voters.
- The other 28 rated titles have a median movie rating of **6.65**. This is an observed film-group difference, **not** a causal estimate of his acting quality.
- **The Batman** has IMDb rating **7.8 / 10** and **958,793** votes. **The Odyssey** has **8.4 / 10** and **575,218** votes. These are the **only two non-dominated records** when comparing both rating and IMDb vote count across the 33 eligible titles: the Pareto frontier in this snapshot. This does not mean they are the only acclaimed or watched films, or that the metrics represent unique moviegoers.
- The earlier 2005 *Harry Potter* credit and the 2023 English voice dubbing credit for *The Boy and the Heron* are real supplementary roles, but not evidence of Pattinson's leading-role film appeal. Handle role prominence transparently.

## Six concrete cast bridges worth visualising
De-duplicate the 14 Bond film-pair rows by connected person + Pattinson film. Represent **six unique people** and their actual Pattinson film and Bond role. The Bond titles below are illustrative confirmed appearances, not an assertion of all appearances.

| Pattinson film | Connected person | Bond character / example film |
|---|---|---|
| *Harry Potter and the Goblet of Fire* (2005) | Ralph Fiennes | M — *Skyfall* (2012) |
| *Remember Me* (2010) | Pierce Brosnan | James Bond — *GoldenEye* (1995) |
| *Water for Elephants* (2011) | Christoph Waltz | Blofeld — *Spectre* (2015) |
| *Cosmopolis* (2012) | Mathieu Amalric | Dominic Greene — *Quantum of Solace* (2008) |
| *The Twilight Saga: Breaking Dawn – Part 2* (2012) | Rami Malek | Safin — *No Time to Die* (2021) |
| *The Batman* (2022) | Jeffrey Wright | Felix Leiter — *Casino Royale* (2006) |

All six are established in the official IMDb research extract plus audited full-cast supplements. Role checks: [Bond movies character listing](https://www.bondmovies.com/movies/overview/cast/), [007.com No Time to Die characters](https://www.007.com/page/5/?cat=trailers&id=tb), [Remember Me full cast](https://www.rottentomatoes.com/m/1211619-remember_me/cast-and-crew).

**Fresh editorial hook:** On 18 November 2026, former Bond Pierce Brosnan publicly welcomed Pattinson to 007 and specifically recalled their shared film *Remember Me*. Reporting: [Variety, 19 Nov](https://au.variety.com/2026/film/global/robert-pattinson-pierce-brosnan-james-bond-42741/) and [Radio Times, 19 Nov](https://www.radiotimes.com/movies/pierce-brosnan-pattinson-bond-verdict-newsupdate/).

**Production relationships, separately from on-screen co-stars:** David Heyman (producer of *Harry Potter and the Goblet of Fire*) and Denis Villeneuve (director of the upcoming *Dune: Part Three*) are attached to the new Bond production. Amazon MGM's [16 Nov 2026 announcement](https://www.aboutamazon.com/news/entertainment/james-bond-robert-pattinson-cast-amazon-mgm-film) confirms their Bond roles. The Dune film is **not yet released** at the study cutoff. None of these overlaps is evidence of why Pattinson was cast.

## Ranked editorial routes
1. **A famous vampire, a string of reinventions, and a Bond already in the family** — combines a measurable franchise/reputation paradox with six human cast connections and Brosnan's direct greeting. Recommended.
2. **High visibility doesn't guarantee high IMDb ratings — until the breakthrough films** — measures votes versus ratings, including the two-film Pareto frontier. Strong secondary analytical thread, not the entire article.
3. **What do new Bonds look like before their first Bond film?** — potentially more novel, but requires a new, comparable pre-debut dataset for previous Bond actors (no retrospective rating snapshots exist); not supported by current project data. Research candidate only.
4. **A simple ranked Pattinson IMDb chart** — low editorial value. Do not pursue in this project.

## Proposed NEW chart sequence (editorial, not configs)
**Chart 1 — 'Five Twilight hits; five modest ratings'.**
A data-driven distribution of all 33 eligible titles by film IMDb rating, with all five Twilight films distinctly highlighted and vote volume encoded transparently (e.g. area, not fictional unique viewers). Label the 5.1 vs 6.65 film median and show the full distribution, not three arbitrary career period bars. **Reader takeaway:** the franchise that made him ubiquitous was relatively poorly scored on IMDb.

**Chart 2 — 'The Batman and The Odyssey break the old pattern'.**
A ratings-versus-title-votes graphic that *actually makes a finding*: show all 33 titles, highlight the 5 Twilight points, mark the two genuine Pareto-frontier films and identify a few career pivots (e.g. *Good Time*, *The Lighthouse*) without label clutter. State both metrics and timing caveat. **Reader takeaway:** major audience attention and high film ratings coincide in later titles. Avoid pretending the IMDb vote-count frontier measures box office.

**Chart 3 — 'He had already met Bond. And his villains.'**
A genuine relationship graphic, not a bar or dot count: six labelled Pattinson film → shared actor → Bond role/film pathways in chronological Pattinson-film order. Use **red only for the former Bond himself** (Pierce Brosnan), blue for other cast links; identify the three villains, M and Felix Leiter. Conclude with the verified **Brosnan *Remember Me* 2026 message**, and explain the production-team links in the prose rather than inventing cast influence.

For more editorial heft, an alternate Chart 2 should be considered: a chronological 33-title rating+vote-volume timeline with supported labels, rather than another uninformative generic scatter.

## QA and publishing gates
- Real data only; calculations reproduced from CSV rows, not retyped display figures.
- Full 25 Eon + two distinct non-Eon Bond film checks retained. Never treat the absence of a chosen principal credit as a universal absence of an actor connection.
- No claim that cast connections influenced the casting decision unless separately documented.
- Chart 1 is **film ratings**, not Pattinson acting ratings, and supporting/voice roles must be clearly labelled where relevant.
- Freeze IMDb snapshot version/date; weighted scores and vote counts change.
- For publication chart builds use GitHub `src/render_538.py`, the locked `social_square` profile and 1600px/390px/320px final-pixel QA. Network schematic requires a **data-driven, opt-in registered specialist** or a comparably deterministic renderer, not generative re-drawing.
- Retain draft PR #221 unmerged and do not edit site publishing files until the new evidence-led visuals and story have passed editorial review.
