# Project manifest: Mel Gibson career pivot

## Status

- Status: Published
- Started: 2026-09-25
- Last updated: 2026-09-26
- Owner: Adam Green
- Repo project slug: 2026-09-mel-gibson-career

## Story

- Working title: Riggs made the star. Braveheart changed the job.
- Recommended route: He didn't disappear. He changed jobs, then came back differently.
- Final title: Mel Gibson didn't disappear. His career changed shape.
- Core question: What happened to Mel Gibson's career after the Lethal Weapon / Braveheart peak, and where did he take it?
- Main takeaway: The verified IMDb data shows a real acting gap followed by a high-volume but lower-rated acting return, while directing became a sparse second career with several major peaks.
- Audience: coffeetableviz readers
- Blog/social use: Live coffeetableviz.com post published

## Sources

| Source | URL | Notes | Date accessed |
|---|---|---|---|
| IMDb non-commercial datasets | https://datasets.imdbws.com/ | Source of truth for reproducible acting/directing chronology and title ratings | 2026-09-25 |
| IMDb Mel Gibson | https://www.imdb.com/name/nm0000154/ | Identity cross-check | 2026-09-25 |
| Academy Awards 1996 | https://www.oscars.org/oscars/ceremonies/1996 | Braveheart: 10 nominations, 5 wins; Gibson won Directing and shared Best Picture | 2026-09-25 |
| Academy Awards 2017 | https://www.oscars.org/oscars/ceremonies/2017/H | Hacksaw Ridge: Gibson nominated for Directing; film nominated for Best Picture | 2026-09-25 |
| Reuters via VOA | https://www.voanews.com/a/gibson-career-rebounds-with-hacksaw-ridge/3581763.html | Context for the post-2006 career period; not used as a causal chart variable | 2026-09-25 |
| The Numbers | https://www.the-numbers.com/box-office-star-records/worldwide/lifetime-acting/top-grossing-leading-stars | Optional scale context only; not used in the three charts | 2026-09-25 |

## Data files

| File | Purpose | Created by | Notes |
|---|---|---|---|
| data/mel_gibson_imdb_career_movies.csv | Clean joined acting/directing movie dataset | scripts/build_imdb_actor_director_dataset.py | 62 analytical rows |
| data/mel_gibson_imdb_exclusions.csv | Audit trail of excluded/unrated/non-movie credits | scripts/build_imdb_actor_director_dataset.py | 41 audit rows |
| data/mel_gibson_imdb_source_metadata.json | Source and validation metadata | scripts/build_imdb_actor_director_dataset.py | Identity and coverage validated |
| data/mel_gibson_chart_01_acting_ratings.csv | Chart 1 acting-film timeline | scripts/build_story_datasets.py | 58 acting rows |
| data/mel_gibson_chart_02_annual_acting_count.csv | Chart 2 annual eligible-film counts | scripts/build_story_datasets.py | Explicit zero years retained |
| data/mel_gibson_chart_03_directing_ratings.csv | Chart 3 directing sequence | scripts/build_story_datasets.py | 6 released directing features |

## Scripts

| File | Purpose | Inputs | Outputs |
|---|---|---|---|
| scripts/build_imdb_actor_director_dataset.py | Stream-filter official IMDb exports for acting and directing lanes | IMDb TSV gzip exports | Career CSV, exclusions CSV, metadata JSON |
| scripts/build_story_datasets.py | Build the three editorial chart datasets | Verified career CSV | Three chart CSVs |

## Chart configs

| File | Chart | Output | Status |
|---|---|---|---|
| config/chart_01_acting_ratings.py | The peak is where memory puts it | output/mel_gibson_01_acting_ratings.png | QA passed |
| config/chart_02_annual_acting_count.py | He didn't stop acting. He got busier. | output/mel_gibson_02_annual_acting_count.png | QA passed |
| config/chart_03_directing_ratings.py | Directing became the second career | output/mel_gibson_03_directing_ratings.png | QA passed |

## Workflows

| File | Purpose | Status |
|---|---|---|
| .github/workflows/build-archived-imdb-career-data.yml | Reusable official IMDb acquisition for archived actor/director projects | Added on this branch |
| .github/workflows/render-archived-project.yml | Locked archived-project rendering | Existing reusable workflow; passed |

## Outputs

| File | Purpose | Notes |
|---|---|---|
| output/mel_gibson_01_acting_ratings.png | Acting-title rating timeline | 1600×1600; QA passed |
| output/mel_gibson_02_annual_acting_count.png | Annual acting activity | 1600×1600; QA passed |
| output/mel_gibson_03_directing_ratings.png | Directing-title sequence | 1600×1600; QA passed |

## Content package

Publication package: `content/publication_package.md`. Live Jekyll post: `site/_posts/2026-09-25-mel-gibson-didnt-disappear-his-career-changed-shape.md`. The three QA-passed chart assets are copied into `site/assets/migrated/mel-gibson/`. Story-specific feature artwork is `site/assets/migrated/mel-gibson/feature.svg`, derived from the saved publication-package metaphor and prompt and used as both card and hero image.

## QA notes

- Data checked: 62 analytical rows; 41 audit rows; 100% title-basics join coverage; no duplicate analytical tconst values; no missing year/runtime/rating in the analytical set.
- Config checked: all configs rendered successfully with the current locked renderer; dict sorting and descriptive output paths used.
- Render checked: final render workflow run 36197297368 completed successfully.
- Labels/margins checked: first render exposed title clipping in Charts 1 and 3; copy was shortened and the second render was visually rechecked with no title/subtitle clipping.
- Source text checked: IMDb dataset date/vote floor shown on Charts 1–2; IMDb + Academy shown on Chart 3.
- Dimensions checked: all three final PNGs are 1600×1600.
- Archive checked: project-specific material remains under archive/projects/2026-09-mel-gibson-career/.
- Mobile handoff: data acquisition, derivation and rendering are committed directly to GitHub; no copy/paste step required.

## Decisions and caveats

- IMDb ratings describe titles, not Gibson's individual acting or directing performance.
- IMDb title.principals is a principal-credit subset, not a guaranteed complete filmography.
- The 1,000-vote floor is a coverage rule, not a claim that all included titles are equally comparable.
- The 2020–25 comparison covers six calendar years, not a full decade.
- IMDb principal ordering is supporting context only and must not be described as screen time or formal billing.
- Public controversy remains sourced historical context; the charts do not claim causation.
- The reusable acquisition workflow was added because the local runtime cannot directly consume IMDb's binary gzip exports and the repo already benefits from repeated IMDb actor projects.
- No renderer/template code was changed; the chart QA issue was project copy length, not a reusable renderer defect.

## Closeout

- Published URL: https://coffeetableviz.com/stories/mel-gibson-didnt-disappear-his-career-changed-shape/
- Final archive PR: #74
- Archive merge commit: adeb9d5fa7e7351eb3676d147e1f17a9f1804cc7
- Publication PR: #75
- Publication merge commit: 62b1bc407f27eac6a6014e4db156e054c13fb601
- Pages deployment run: 36198776377 — success
