# Project manifest: Taron Egerton IMDb story

## Status

- Status: Publication-ready
- Started: 20 September 2026
- Last updated: 21 September 2026
- Owner: Adam Green
- Repo project slug: `2026-09-taron-egerton-imdb-story`

## Story

- Working title: Taron Egerton is strongest when the character is real
- Core question: What does the current IMDb title-rating snapshot reveal about the shape of Taron Egerton's film work?
- Current recommendation: build from the career timeline into the top-billed Biography-versus-Action comparison, then finish on the opposing *Kingsman* and *Sing* sequel movements.
- Audience: coffeetableviz readers and film/data audiences
- Blog/social use: Proposed three-chart WordPress story plus social package

## Sources

| Source | URL | Notes | Date accessed |
|---|---|---|---|
| IMDb non-commercial datasets | https://developer.imdb.com/non-commercial-datasets/ | Official `name.basics`, `title.principals`, `title.basics`, `title.ratings` and `title.crew` exports; exact run dates recorded in build metadata | 20 September 2026 |

## Data files

| File | Purpose | Notes |
|---|---|---|
| `data/taron_egerton_imdb_principal_actor_movies.csv` | Joined principal actor movie records | 21 records; 14 pass the disclosed 1,000-vote analytical floor |
| `data/taron_egerton_imdb_exclusions.csv` | Audit trail | Non-movie actor credits and movie-level exclusion reasons |
| `data/taron_egerton_imdb_build_metadata.json` | Provenance and controls | Resolved person ID, source headers, counts and scope note |
| `data/taron_egerton_chart_01_timeline.csv` | Timeline chart dataset | All 14 eligible movies |
| `data/taron_egerton_chart_02_lead_lanes.csv` | Lead-lane comparison | Three Biography and three Action films selected by explicit rules |
| `data/taron_egerton_chart_03_franchises.csv` | Franchise comparison | Two Kingsman and two Sing films |

## Scripts

| File | Purpose | Inputs | Outputs |
|---|---|---|---|
| `scripts/build_imdb_actor_dataset.py` | Stream-filter and join the official IMDb exports | Actor name plus official IMDb gzip files | Joined dataset, audit CSV and metadata JSON |
| `scripts/build_story_datasets.py` | Validate the analytical set and derive chart datasets | Joined actor-movie CSV | Three chart-specific CSVs |

## Publication files

- `config/chart_01_timeline.py`
- `config/chart_02_lead_lanes.py`
- `config/chart_03_franchises.py`
- `output/taron_egerton_01_timeline.png`
- `output/taron_egerton_02_lead_lanes.png`
- `output/taron_egerton_03_franchises.png`
- `content/publication_package.md`
- `site/_posts/2026-09-21-taron-egerton-is-strongest-when-the-character-is-real.md`
- `site/assets/migrated/taron-egerton/`

## Current gate

Local data validation, chart rendering, visual QA, editorial copy and story-specific feature artwork are complete. The remaining gate is GitHub review, CI and live-site verification.

## Brand constraint

Use the current coffeetableviz palette exactly as documented in `content/story_plan.md`. No colour additions or substitutions.
