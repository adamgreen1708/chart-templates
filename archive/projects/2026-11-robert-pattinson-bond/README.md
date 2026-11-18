# Robert Pattinson: From Twilight to 007

**Coffeetableviz research project** · checkpoint 18 November 2026 · **draft research, not a published article**.

## Verified news hook
On 16 November 2026 Amazon MGM Studios confirmed Robert Pattinson as the next James Bond; Denis Villeneuve is directing from Steven Knight's screenplay, with producers Amy Pascal and David Heyman and executive producer Tanya Lapointe.

Primary source: https://www.aboutamazon.com/news/entertainment/james-bond-robert-pattinson-cast-amazon-mgm-film

## What is being collected
IMDb's official, daily refreshed **non-commercial** dataset (https://developer.imdb.com/non-commercial-datasets/), using the verified IMDb identity Robert Pattinson `nm1500155`.

The workflow streams, filters and joins:
- `title.principals.tsv.gz`: his principal acting credits, featured co-stars, and the principal casts of five Daniel Craig Bond movies
- `title.basics.tsv.gz`: movie types, titles, release years, genres and runtime
- `title.ratings.tsv.gz`: IMDb weighted average user rating and count of votes
- `title.crew.tsv.gz`: directors
- `name.basics.tsv.gz`: names and verification of Pattinson's IMDb identity

**Collection scope:** movie titles on which Pattinson has a principal acting credit, not every film in which archived footage of Pattinson might appear. IMDb `title.principals` is not the exhaustive full cast. IMDb producer credits are not present in `title.crew`.

**Release cutoff:** 18 November 2026. Most entries dated 2026 must be manually audited for release status; the studio statement explicitly documents that *The Odyssey* and *The Drama* have opened already. Upcoming *Dune: Part Three* must not be counted as a released film. The still-unreleased Bond film has no rating in this study.

## Collect and validate
1. `python -m pip install requests`
2. `python archive/projects/2026-11-robert-pattinson-bond/collect_imdb_pattinson.py --out archive/projects/2026-11-robert-pattinson-bond/generated --as-of 2026-11-18`
3. `python archive/projects/2026-11-robert-pattinson-bond/qa_imdb.py --data archive/projects/2026-11-robert-pattinson-bond/generated`

The GitHub Actions workflow `.github/workflows/pattinson-imdb-research.yml` runs these steps for the PR, and uploads the small derived results as a **temporary, review-only artifact**. Raw IMDb global datasets are streamed rather than committed or stored. Verify terms and permissions before public redistribution of derived IMDb data.

Expected files in the Action artifact:
- `filmography.csv` — Pattinson's principal acting movie rows, release status, directors, rating and votes
- `cast_edges.csv`, `director_edges.csv`, `collaborators.csv` — named film links
- `bond_overlap.csv` — person × Pattinson film × Craig Bond film, no inference of causality
- `metadata.json` and `qa_report.json` — scope, count, exclusions and QA
- `chart_01_film_rating_timeline.csv`, `chart_02_rating_vs_votes.csv`, `chart_03_craig_bond_connections.csv` — **chart inputs for editorial consideration, not approved publication charts**

## Three-chart editorial hypothesis (subject to live data)
**One possible argument:** The road from franchise teenage fame to James Bond wasn't a straight line, and the Bond world had already crossed Pattinson's path.

1. **A career in three acts.** Plot every eligible released principal-acting film, by year and IMDb film rating. Compare genuinely observed periods, not a cherry-picked handful. Inspect missing ratings, votes, film type and exceptional 2026 releases before asserting trends.
2. **Fame and acclaim don't always agree.** Scatter each film's IMDb rating against vote count, with a log vote scale if justified. A film rating measures a *film*, not his performance; votes are not ticket sales or a statistically representative opinion poll.
3. **Bond was already in the room.** A compact, *data-derived* map of shared Craig-era Bond actors, plus separately sourced editorial notes about producers/directors. These connections establish shared credits, **not that they caused the casting**.

The strongest discovered pattern may change after the full extraction; do not generate final chart configs or blog claims from the ten-film starter sample.

## Already documented crossover leads
See `verified_bond_connections.csv` for links and source URLs.

- **Jeffrey Wright:** Pattinson in *The Batman* (2022); Felix Leiter in Daniel Craig's Bond films.
- **Christoph Waltz:** Pattinson in *Water for Elephants* (2011); Blofeld in *Spectre* (2015) and *No Time to Die* (2021).
- **Rami Malek:** Pattinson in *The Twilight Saga: Breaking Dawn – Part 2* (2012); Safin in *No Time to Die* (2021).
- **David Heyman:** producer of *Harry Potter and the Goblet of Fire* (2005) and the announced Bond film, confirmed by Amazon MGM.
- **Denis Villeneuve:** director of upcoming *Dune: Part Three* and announced Bond film, confirmed by Amazon MGM. The Dune film is future-facing, **not a released-rating overlap**.

## Workflow guardrails
- GitHub repository source of truth: `docs/project_kickoff_prompt.md`, `docs/story_discovery_and_3_chart_flow.md`, `spec/538_template_rules.md`, `docs/chart_qa_checklist.md`.
- Complete actual dataset inspection (row counts, duplicates, missingness, years, votes, film eligibility) and challenge the story before chart configs.
- All subsequent charts use `render_profile: social_square`, via `src/render_538.py`, with full-size, 390px and 320px pixel QA.
- No site assets or Jekyll posts are changed. Blog publication requires approval, a separate PR, merge and Pages verification.
- This project-specific CI workflow is for research; reconsider/remove it before merging completed research to `main` to keep reusable workflows clean.

## Status / limits as at initial commit
- Bond announcement: **independently confirmed**.
- Official full dataset: **not yet successfully extracted**. The local ChatGPT container cannot resolve the IMDb download host; execution is delegated to GitHub Actions once a review PR opens.
- Ten film ratings from earlier research: **a seed, not full-population evidence**. Recheck against the current official IMDb dataset.
- Three cast and two crew overlaps: **specific independently documented leads**, to be reconciled with IMDb's principal credits; no casting-influence claim.
