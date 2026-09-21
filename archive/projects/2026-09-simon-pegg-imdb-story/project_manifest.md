# Project manifest: Simon Pegg IMDb story

## Status

- Status: Story plan awaiting approval
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

## Deliberately absent at this gate

- chart-specific derived datasets
- chart configs
- rendered images
- blog and social copy
- site publication files

These follow only after editorial approval.

## Palette constraint

The project is locked to the seven colours stated in `content/story_plan.md`; no additions or substitutions are authorised.
