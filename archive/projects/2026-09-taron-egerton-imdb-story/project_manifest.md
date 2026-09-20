# Project manifest: Taron Egerton IMDb story

## Status

- Status: Story selection
- Started: 20 September 2026
- Last updated: 20 September 2026
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

## Scripts

| File | Purpose | Inputs | Outputs |
|---|---|---|---|
| `scripts/build_imdb_actor_dataset.py` | Stream-filter and join the official IMDb exports | Actor name plus official IMDb gzip files | Joined dataset, audit CSV and metadata JSON |

## Current gate

The dataset and recommended three-chart narrative are ready for review. Chart-specific CSVs, configs and renders should begin only after story approval.

## Brand constraint

Use the current coffeetableviz palette exactly as documented in `content/story_plan.md`. No colour additions or substitutions.
