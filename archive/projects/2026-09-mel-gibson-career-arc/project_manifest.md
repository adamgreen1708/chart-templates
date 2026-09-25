# Project manifest: Mel Gibson career arc

## Status

- Status: In progress
- Started: 2026-09-25
- Last updated: 2026-09-25
- Owner: Adam Green
- Repo project slug: 2026-09-mel-gibson-career-arc

## Story

- Working title: Riggs built the star. Braveheart changed the job.
- Final title:
- Core question: What happened after the Lethal Weapon / Braveheart era, and where did Mel Gibson take his career?
- Main takeaway: The discovery data suggests a career that changed shape rather than simply stopped: star acting first, then a second track as an infrequent high-profile director, followed by a post-2006 return to acting with much more volume than the nostalgic memory suggests but less major-studio/tentpole visibility.
- Audience: coffeetableviz readers
- Blog/social use: intended after dataset validation, chart approval and publication QA

## Sources

| Source | URL | Notes | Date accessed |
|---|---|---|---|
| Mel Gibson filmography | https://en.wikipedia.org/wiki/Mel_Gibson_filmography | Discovery-only role chronology; final actor analysis must be rebuilt from official IMDb exports | 2026-09-25 |
| IMDb non-commercial datasets | https://datasets.imdbws.com/ | Required final actor/rating acquisition route | 2026-09-25 |
| The Numbers | https://www.the-numbers.com/ | Current box-office snapshot for six released feature directing credits | 2026-09-25 |
| Variety | https://au.variety.com/2024/film/news/andrew-garfield-mel-gibson-deserves-second-chance-hollywood-18220/ | Context on the post-2006 change in Hollywood career and later acting work | 2026-09-25 |
| Variety | https://au.variety.com/2026/film/news/resurrection-of-the-christ-first-look-release-date-delay-mel-gibson-36851/ | Current directing context and Resurrection release plans | 2026-09-25 |

## Data files

| File | Purpose | Created by | Notes |
|---|---|---|---|
| data/mel_gibson_filmography_roles.csv | Discovery chronology and role flags | Manual transcription from cited filmography table | 72 released feature-film rows through 2025; excludes unreleased 2027/2028 titles |
| data/mel_gibson_director_box_office_snapshot.csv | Directing-career scale snapshot | The Numbers | Current lifetime worldwide box office; nominal dollars |

## Scripts

| File | Purpose | Inputs | Outputs |
|---|---|---|---|
| Pending | Official IMDb acquisition adapted from the repo actor-project pattern | IMDb official TSV exports | joined analytical CSV, exclusions audit, source metadata |

## Chart configs

None yet. Story approval and official IMDb validation come first.

## Workflows

No project-specific workflow added.

## Outputs

No charts rendered yet.

## Content package

No blog/social/site package created yet.

## QA notes

- Data checked: discovery layer row count and role totals checked; The Numbers director values individually sourced.
- Config checked: not applicable.
- Render checked: not applicable.
- Labels/margins checked: not applicable.
- Source text checked: sources recorded.
- Archive checked: project-specific material is contained under archive/projects/2026-09-mel-gibson-career-arc/.

## Decisions and caveats

- The Wikipedia filmography is a discovery layer, not the final analytical source.
- Before chart configs, run the repo's official IMDb actor acquisition pattern and preserve exclusions/audit metadata.
- IMDb title ratings, when added, describe titles rather than Gibson's individual acting or directing performance.
- Box-office values are current lifetime nominal figures and should not be treated as inflation-adjusted cross-era comparisons.
- The Passion of the Christ current lifetime total includes 2026 re-release activity.
- The causal explanation for the post-2006 career shift is contextual reporting, not something the film-count data proves by itself.

## Closeout

- Published URL:
- Final archive PR:
- Merge commit:
