# Project manifest: Tom Hanks Colour Bank revisited

## Status

- Status: Rendered
- Started: 20 September 2026
- Last updated: 20 September 2026
- Owner: Adam Green
- Repo project slug: `2026-09-tom-hanks-colour-bank-revisited`

## Story

- Working title: Colour Bank No.6 revisited: Tom Hanks found another gear
- Final title: Pending
- Core question: What does a fresh IMDb snapshot reveal about the shape of Tom Hanks' film career?
- Main takeaway: Ratings changed sharply from 1992–2002, while every Toy Story film remained above the career median across 31 years.
- Audience: coffeetableviz readers and film/data audiences
- Blog/social use: Three-chart WordPress story plus social package

## Sources

| Source | URL | Notes | Date accessed |
|---|---|---|---|
| IMDb non-commercial datasets | https://developer.imdb.com/non-commercial-datasets/ | `title.principals`, `title.basics`, `title.crew`, `name.basics`, `title.ratings`; ratings upstream run date 19 September 2026 | 20 September 2026 |
| Original coffeetableviz post | https://coffeetableviz.com/2024/07/19/colour-bank-no-6-tom-hanks-filmography/ | Retrospective starting point only | 20 September 2026 |

## Data files

| File | Purpose | Created by | Notes |
|---|---|---|---|
| `data/tom_hanks_imdb_principal_actor_movies.csv` | Joined rated IMDb movie-type principal actor records | ChatGPT | 65 rows; includes four documentary rows retained for traceability |
| `data/tom_hanks_chart_01_timeline.csv` | Career timeline | Build script | 61 narrative-film rows |
| `data/tom_hanks_chart_02_period_comparison.csv` | Before/during/after comparison | Build script | Three period summary rows |
| `data/tom_hanks_chart_03_toy_story.csv` | Toy Story sequence | Build script | Five films, 1995–2026 |

## Scripts

| File | Purpose | Inputs | Outputs |
|---|---|---|---|
| `scripts/build_story_datasets.py` | Filter documentaries, validate scope and build chart datasets | Joined source CSV | Three chart CSVs |

## Chart configs

| File | Chart | Output | Status |
|---|---|---|---|
| `config/chart_01_timeline.py` | Hanks found another gear in 1992 | `output/tom_hanks_01_timeline.png` | Rendered and QA checked |
| `config/chart_02_period_comparison.py` | Ten hits in eleven years | `output/tom_hanks_02_period_comparison.png` | Rendered and QA checked |
| `config/chart_03_toy_story.py` | Woody outlasted the golden run | `output/tom_hanks_03_toy_story.png` | Rendered and QA checked |

## Workflows

| File | Purpose | Status |
|---|---|---|
| Existing reusable render workflow | Render configs through locked 538 renderer | Unchanged |

## Outputs

| File | Purpose | Notes |
|---|---|---|
| `output/tom_hanks_01_timeline.png` | Chart 1 render | 1600 × 1600; QA checked |
| `output/tom_hanks_02_period_comparison.png` | Chart 2 render | 1600 × 1600; QA checked |
| `output/tom_hanks_03_toy_story.png` | Chart 3 render | 1600 × 1600; QA checked |

## Content package

| Asset | File or text location | Status |
|---|---|---|
| Story plan | `content/story_plan.md` | Complete |
| Blog post | `content/publication_package.md` | Draft complete |
| Blog excerpt | `content/publication_package.md` | Draft complete |
| LinkedIn post | `content/publication_package.md` | Draft complete |
| Instagram caption | `content/publication_package.md` | Draft complete |
| Cartoon scene | `content/publication_package.md` | Draft complete |
| Image prompt | `content/publication_package.md` | Draft complete |

## QA notes

- Data checked: 65 rated source rows; 61 narrative-film rows; no duplicate IMDb IDs; no missing runtime in final analytical dataset.
- Config checked: Yes — full configs, exact columns, valid sort dictionaries and descriptive outputs.
- Render checked: Yes — all three configs rendered successfully through `src/render_538.py`; repository tests 6/6 passed.
- Labels/margins checked: Yes — second visual pass confirmed safe titles, annotations, axes, labels and footers.
- Source text checked: Yes — shortened after first render to prevent footer collision; ratings date retained.
- Archive checked: Project-specific files contained under project folder.

## Decisions and caveats

- Use the current coffeetableviz palette only; do not reuse the original Colour Bank No.6 palette.
- Treat the data as IMDb principal-credit scope rather than a guaranteed complete filmography.
- IMDb ratings are film-level audience ratings, not critical scores or actor-performance scores.
- Exclude four documentary records from the narrative-film story and six unrated/in-development titles from rating analysis.

## Closeout

- Published URL:
- Final archive PR:
- Merge commit:
