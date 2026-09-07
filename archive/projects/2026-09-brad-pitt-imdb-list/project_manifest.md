# Project manifest: Brad Pitt IMDb list

## Status

- Status: Rendered / publication draft
- Started: 7 September 2026
- Last updated: 7 September 2026
- Owner: Adam Green
- Repo project slug: `2026-09-brad-pitt-imdb-list`

## Story

- Working title: Brad Pitt IMDb list
- Final title: Brad Pitt films reward patience
- Core question: What patterns in this 54-film IMDb list connect runtime, repeat directors and ratings over time?
- Main takeaway: Longer films in the list tend to rate better; David Fincher has the highest average among repeat directors; 1995–99 is the strongest rolling five-year run.
- Audience: coffeetableviz readers and social audience
- Blog/social use: WordPress post, LinkedIn, Instagram and feature image

## Sources

| Source | URL | Notes | Date accessed |
|---|---|---|---|
| IMDb list export supplied by Adam Green | N/A — supplied CSV export | 54 film rows. Analyse as the contents of this list; do not claim a complete Brad Pitt filmography. | 7 September 2026 |

## Data files

| File | Purpose | Created by | Notes |
|---|---|---|---|
| `data/brad_pitt_imdb_films.csv` | Source IMDb list export | Supplied by Adam Green | 54 rows |
| `data/brad_pitt_chart_02_repeat_directors.csv` | Repeat-director ranking | `build_story_datasets.py` | Directors split from comma-separated credits; retain 2+ films |
| `data/brad_pitt_chart_03_timeline.csv` | Timeline and peak-window flag | `build_story_datasets.py` | Flags the strongest eligible rolling five-year window, 1995–99 |

## Scripts

| File | Purpose | Inputs | Outputs |
|---|---|---|---|
| `scripts/build_story_datasets.py` | Build Chart 02 and Chart 03 derived datasets | `data/brad_pitt_imdb_films.csv` | `data/brad_pitt_chart_02_repeat_directors.csv`, `data/brad_pitt_chart_03_timeline.csv` |

## Chart configs

| File | Chart | Output | Status |
|---|---|---|---|
| `config/chart_01_runtime_vs_rating.py` | Brad Pitt films reward patience | `brad_pitt_runtime_vs_rating.png` | Config complete; final archived renderer output still required |
| `config/chart_02_repeat_directors.py` | Fincher gets the best-rated Pitt | `brad_pitt_repeat_directors.png` | Real `render_538.py` QA passed on run #390; archived copy still required |
| `config/chart_03_timeline.py` | From 4.6 to 8.8 | `brad_pitt_timeline_ratings.png` | Real `render_538.py` QA passed on run #391 |

## Workflows

| File | Purpose | Status |
|---|---|---|
| `.github/workflows/render-538.yml` | Render active `src/chart_config.py` with `src/render_538.py` | Cleaned to project-agnostic workflow; used successfully for Charts 02 and 03 |

## Outputs

| File | Purpose | Notes |
|---|---|---|
| `output/brad_pitt_timeline_ratings.png` | Current active rendered output | Merged via PR #19; should move/copy into project archive at final closeout |
| Chart 02 renderer artifact | Verified Chart 02 render | Run #390 passed visual QA; active output was later cleared by Chart 03 render |
| Chart 01 preview | Story/config QA | Not treated as final archived renderer output |

## Content package

| Asset | File or text location | Status |
|---|---|---|
| Blog post | `content/publication_package.md` — WordPress Gutenberg section | Draft for Adam review |
| Blog excerpt | `content/publication_package.md` — Blog excerpt | Draft for Adam review |
| LinkedIn post | `content/publication_package.md` — LinkedIn post | Draft for Adam review |
| Instagram caption | `content/publication_package.md` — Instagram caption | Draft for Adam review |
| Cartoon scene | `content/publication_package.md` — Cartoon scene text | Draft for Adam review |
| Image prompt | `content/publication_package.md` — Locked stencil-style feature image prompt | Draft for Adam review |
| Chart captions / alt text | `content/publication_package.md` | Draft for Adam review |

## QA notes

- Data checked: Yes — 54-row source scope retained; key calculations documented in `content/story_plan.md`.
- Config checked: Yes — all three saved configs use exact derived/source column names.
- Render checked: Chart 02 and Chart 03 passed the real `src/render_538.py` path. Chart 01 still needs a final real-render archive gate before publication closeout.
- Labels/margins checked: Yes for Charts 02 and 03 actual renders.
- Source text checked: Yes — charts use `Source: IMDb list export`; publication copy states the source-scope caveat.
- Archive checked: Partial — project data/scripts/config/content are archived; final PNG set is not yet fully archived.

## Decisions and caveats

- Treat the analysis as a story about the supplied 54-film IMDb list, not a verified complete Brad Pitt filmography.
- Runtime/rating is an association, not a causal claim.
- Repeat-director rule: split comma-separated director credits into individual directors, count one credit per film and retain directors with at least two films.
- Rolling-window rule: compare every five-year period containing at least three films; 1995–99 is highest at 7.63 across seven films.
- Chart 02 detail was deliberately simplified after real-render QA: director names remain on the y-axis, average plus film count sits beside each dot, and Fincher's three film ratings are carried in the subtitle.

## Closeout

- Published URL: TBC
- Final archive PR: TBC
- Merge commit: TBC
- Project is not yet marked Published/Archived because Chart 01 still needs a final real render and the complete PNG set still needs to be copied into the project archive.