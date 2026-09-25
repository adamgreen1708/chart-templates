# Project manifest: Mel Gibson career pivot

## Status

- Status: Render build
- Started: 2026-09-25
- Last updated: 2026-09-25
- Owner: Adam Green
- Repo project slug: 2026-09-mel-gibson-career

## Story

- Working title: Riggs made the star. Braveheart changed the job.
- Final title:
- Core question: What happened to Mel Gibson's career after the Lethal Weapon / Braveheart peak, and where did he take it?
- Main takeaway: The verified IMDb data shows a real acting gap followed by a high-volume but lower-rated acting return, while directing became a sparse second career with several major peaks.
- Audience: coffeetableviz readers
- Blog/social use: Potential live coffeetableviz.com post after chart approval

## Sources

| Source | URL | Notes | Date accessed |
|---|---|---|---|
| IMDb non-commercial datasets | https://datasets.imdbws.com/ | Planned source of truth for reproducible acting/directing chronology and ratings | 2026-09-25 |
| IMDb Mel Gibson | https://www.imdb.com/name/nm0000154/ | Identity, current credits summary, directed-title checks | 2026-09-25 |
| Academy Awards 1996 | https://www.oscars.org/oscars/ceremonies/1996 | Braveheart: 10 nominations, 5 wins; Gibson won Directing and shared Best Picture | 2026-09-25 |
| Academy Awards 2017 | https://www.oscars.org/oscars/ceremonies/2017/H | Hacksaw Ridge: Gibson nominated for Directing; film nominated for Best Picture | 2026-09-25 |
| Reuters via VOA | https://www.voanews.com/a/gibson-career-rebounds-with-hacksaw-ridge/3581763.html | Contemporary reporting on the 2006 career break and 2016 return | 2026-09-25 |
| The Numbers | https://www.the-numbers.com/box-office-star-records/worldwide/lifetime-acting/top-grossing-leading-stars | Current worldwide leading-role box-office context | 2026-09-25 |

## Data files

| File | Purpose | Created by | Notes |
|---|---|---|---|
| data/mel_gibson_imdb_career_movies.csv | Clean joined acting/directing movie dataset | scripts/build_imdb_actor_director_dataset.py | Created and validated from official IMDb exports |
| data/mel_gibson_imdb_exclusions.csv | Audit trail of excluded/unrated/non-movie credits | scripts/build_imdb_actor_director_dataset.py | Created; 41 audit rows |
| data/mel_gibson_imdb_source_metadata.json | Source and validation metadata | scripts/build_imdb_actor_director_dataset.py | Created; identity and coverage validated |

## Scripts

| File | Purpose | Inputs | Outputs |
|---|---|---|---|
| scripts/build_imdb_actor_director_dataset.py | Stream-filter official IMDb exports for both acting and directing lanes | IMDb TSV gzip exports | Clean career CSV, exclusions CSV, metadata JSON |

## Chart configs

| File | Chart | Output | Status |\n|---|---|---|---|\n| config/chart_01_acting_ratings.py | Acting-rating timeline | output/mel_gibson_01_acting_ratings.png | Build |\n| config/chart_02_annual_acting_count.py | Annual acting-film counts | output/mel_gibson_02_annual_acting_count.png | Build |\n| config/chart_03_directing_ratings.py | Directing-rating chronology | output/mel_gibson_03_directing_ratings.png | Build |

## Workflows

| File | Purpose | Status |\n|---|---|---|\n| .github/workflows/build-archived-imdb-career-data.yml | Reusable official IMDb acquisition for archived actor/director projects | Added on project branch |\n| .github/workflows/render-archived-project.yml | Locked archived-project rendering | Existing reusable workflow |

## Outputs

None yet.

## Content package

Not started. Site publication is deliberately outside this discovery-stage PR.

## QA notes

- Data checked: Official IMDb exports acquired; 62 analytical rows, 41 audit rows, 100% basics join coverage, no duplicate analytical tconst values.
- Config checked: Not applicable.
- Render checked: Not applicable.
- Labels/margins checked: Not applicable.
- Source text checked: Research sources recorded.
- Archive checked: Project-specific files contained under archive/projects/2026-09-mel-gibson-career/.

## Decisions and caveats

- Treat acting and directing as separate career lanes.
- Do not describe IMDb title ratings as ratings of Gibson's individual performance.
- Do not treat IMDb title.principals as a guaranteed complete filmography.
- Any link between public controversies and career outcomes must remain sourced and descriptive; the charts should show chronology, not claim causation.
- No chart config should be created until the downloadable IMDb data has been acquired and the story route re-tested.

## Closeout

- Published URL:
- Final archive PR:
- Merge commit:
