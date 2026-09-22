# Project manifest: Simon Pegg IMDb story

## Status

- Status: Charts rendered and QA checked
- Started: 21 September 2026
- Owner: Adam Green
- Repo project slug: `2026-09-simon-pegg-imdb-story`

## Story

- Working title: Simon Pegg's highest-rated films keep familiar company
- Core question: What does IMDb's current title-rating snapshot reveal about the shape of Simon Pegg's principal movie credits?
- Current recommendation: start with the full timeline, compare three recurring partnerships with the remaining movies, then show how those partnerships unfolded.
- Audience: coffeetableviz readers and film/data audiences

## Sources

| Source | URL | Notes | Accessed |
|---|---|---|---|
| IMDb non-commercial datasets | https://datasets.imdbws.com/ | Official `name.basics`, `title.principals`, `title.basics`, `title.ratings` and `title.crew` gzip exports; exact upstream run dates are recorded in the metadata JSON | 21 September 2026 UTC |

`title.akas` was not used because regional or alternative titles do not affect the recommended analysis. `title.episode` was not used because television episodes are outside scope.

## Files

| File | Purpose |
|---|---|
| `scripts/build_imdb_actor_dataset.py` | Retry, stream-filter, join, validate and document the official IMDb exports without saving the global files |
| `data/simon_pegg_imdb_principal_actor_movies.csv` | Clean analytical dataset: released principal actor movies with ratings and at least 1,000 votes |
| `data/simon_pegg_imdb_exclusions.csv` | Audit of non-acting principal rows and excluded acting-credit titles |
| `data/simon_pegg_imdb_source_metadata.json` | Resolved identity, URLs, access time, upstream run dates, stage counts and join/coverage validation |
| `content/story_plan.md` | Ranked story angles, risks and recommended connected three-chart narrative |
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

## Deliberately absent at this gate

- blog and social copy
- site publication files

These remain separate follow-on deliverables.

## Palette constraint

The project is locked to the seven colours stated in `content/story_plan.md`; no additions or substitutions are authorised.
