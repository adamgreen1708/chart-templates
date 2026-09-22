# Project manifest: Simon Pegg IMDb story

## Status

- Status: Publication draft prepared; awaiting Adam approval
- Started: 21 September 2026
- Last updated: 22 September 2026
- Owner: Adam Green
- Repo project slug: `2026-09-simon-pegg-imdb-story`

## Story

- Published headline: Simon Pegg's highest-rated films keep familiar company
- Core question: What does IMDb's current title-rating snapshot reveal about the shape of Simon Pegg's principal movie credits?
- Current recommendation: start with the full timeline, quantify the three recurring partnership groups against the remaining eligible movies, then show how those partnerships unfolded film by film.
- Audience: coffeetableviz readers and film/data audiences
- Blog/social use: three-chart Jekyll story plus social package

## Sources

| Source | URL | Notes | Accessed |
|---|---|---|---|
| IMDb non-commercial datasets | https://datasets.imdbws.com/ | Official `name.basics`, `title.principals`, `title.basics`, `title.ratings` and `title.crew` gzip exports; exact upstream run dates are recorded in the metadata JSON | 21 September 2026 UTC |

`title.akas` was not used because regional or alternative titles do not affect the recommended analysis. `title.episode` was not used because television episodes are outside scope.

## Analytical summary

- 33 eligible principal-actor movies from 2004 to 2025.
- 12 films in three mutually exclusive recurring groups: Mission: Impossible (6), Star Trek (3), Edgar Wright (3).
- Combined recurring-team mean: 7.43.
- Other 21 eligible movies mean: 6.09.
- Difference: 1.34 IMDb rating points.
- Ratings source upstream run date: 20 September 2026.

## Files

| File | Purpose |
|---|---|
| `scripts/build_imdb_actor_dataset.py` | Retry, stream-filter, join, validate and document the official IMDb exports without saving the global files |
| `data/simon_pegg_imdb_principal_actor_movies.csv` | Clean analytical dataset: released principal actor movies with ratings and at least 1,000 votes |
| `data/simon_pegg_imdb_exclusions.csv` | Audit of non-acting principal rows and excluded acting-credit titles |
| `data/simon_pegg_imdb_source_metadata.json` | Resolved identity, URLs, access time, upstream run dates, stage counts and join/coverage validation |
| `content/story_plan.md` | Ranked story angles, risks and approved connected three-chart narrative |
| `scripts/build_story_datasets.py` | Validate the approved route and build the three chart-specific datasets |
| `data/simon_pegg_chart_01_timeline.csv` | All 33 eligible films for the timeline |
| `data/simon_pegg_chart_02_groups.csv` | Four mutually exclusive group summaries with sample sizes |
| `data/simon_pegg_chart_03_partnership_sequences.csv` | Twelve films across the three recurring partnerships |
| `config/chart_01_timeline.py` | Full locked-renderer config for chart 1 |
| `config/chart_02_groups.py` | Full locked-renderer config for chart 2 |
| `config/chart_03_partnership_sequences.py` | Full locked-renderer config for chart 3 |
| `output/simon_pegg_01_timeline.png` | 1600 × 1600 chart 1 render |
| `output/simon_pegg_02_groups.png` | 1600 × 1600 chart 2 render |
| `output/simon_pegg_03_partnership_sequences.png` | 1600 × 1600 chart 3 render |
| `content/qa_report.md` | Data, config, renderer and visual QA record |
| `content/publication_package.md` | Headline, excerpt, social copy, chart captions/alt text and feature-art specification |
| `site/_posts/2026-09-22-simon-peggs-highest-rated-films-keep-familiar-company.md` | Live-site Jekyll post draft |
| `site/assets/migrated/simon-pegg/` | Story-specific feature artwork plus copied approved chart assets |

## Current gate

The publication package, site post and web assets are staged in a draft pull request. Do not merge until Adam explicitly approves publication. After merge, verify the Pages workflow and final coffeetableviz.com URL before calling the post live.

## Palette constraint

The three charts remain locked to the seven colours stated in `content/story_plan.md`; no chart palette additions or substitutions are authorised.
