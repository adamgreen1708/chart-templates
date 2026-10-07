# Project manifest: Lionel Messi — Argentina farewell

## Status

- Status: Rendered — ready for Adam visual review
- Started: 7 October 2026
- Last updated: 7 October 2026
- Owner: Adam Green
- Repo project slug: 2026-10-lionel-messi-argentina-farewell

## Story

- Working title: The ending changed the story
- Final title: Pending Adam review
- Core question: What does Lionel Messi's full Argentina career look like now that it is complete?
- Main takeaway: The career was extraordinarily long, but its defining team success and a much higher scoring rate were concentrated in the final six calendar years.
- Audience: coffeetableviz readers; beginner/intermediate data-viz audience
- Blog/social use: Three-chart editorial story; publication package after chart approval

## Sources

| Source | URL | Notes | Date accessed |
|---|---|---|---|
| National-Football-Teams | https://www.national-football-teams.com/player/12066/Lionel_Messi.html | Annual appearance/goal spine through pre-Benin 207/125 | 2026-10-07 |
| Opta Analyst | https://theanalyst.com/players/10705/lionel-messi/national | Post-farewell 2026 and career totals | 2026-10-07 |
| FIFA | https://www.fifa.com/en/tournaments/mens/worldcup/articles/lionel-messi-argentina-international-career | Farewell and 208/126 cross-check | 2026-10-07 |
| Reuters | https://www.reuters.com/sports/soccer/messi-signs-off-tears-after-one-last-argentina-master-class-2026-10-07/ | Benin farewell match cross-check | 2026-10-07 |
| FIFA | https://www.fifa.com/en/articles/lionel-messi-argentina-career | Senior-title and career narrative | 2026-10-07 |
| FIFA | https://inside.fifa.com/tournaments/mens/worldcup/2018russia/news/messi-calls-time-on-international-career-2803995 | Four pre-2021 lost senior finals | 2026-10-07 |

## Data files

| File | Purpose | Created by | Notes |
|---|---|---|---|
| data/messi_argentina_yearly.csv | Annual appearances/goals and cumulative totals | ChatGPT | 2026 row reconciled post-Benin |
| data/messi_argentina_major_finals.csv | Nine senior finals reached | ChatGPT | Finalissima included as senior trophy |
| data/messi_argentina_era_split.csv | Pre/post-2021 comparison | scripts/build_story_data.py | Same metric/scope across both periods |

## Scripts

| File | Purpose | Inputs | Outputs |
|---|---|---|---|
| scripts/build_story_data.py | Recompute split and validate story totals | Yearly + finals CSVs | Era split + assertions |

## Chart configs

| File | Chart | Output | Status |
|---|---|---|---|
| config/chart_01_yearly_appearances.py | Annual Argentina appearances | output/messi_01_yearly_appearances.png | Rendered; QA pass |
| config/chart_02_major_finals.py | Senior-finals reversal | output/messi_02_major_finals.png | Rendered after highlight fix; QA pass |
| config/chart_03_scoring_acceleration.py | Pre/post-2021 scoring rate | output/messi_03_scoring_acceleration.png | Rendered; QA pass |

## Workflows

| File | Purpose | Status |
|---|---|---|
| .github/workflows/render-archived-project.yml | Reusable archived-project renderer | Existing; unchanged; runs 37678465723 and 37678949173 succeeded |

## Outputs

| File | Purpose | Notes |
|---|---|---|
| output/messi_01_yearly_appearances.png | Chart 1 | Visual QA pass |
| output/messi_02_major_finals.png | Chart 2 | Visual QA pass after numeric row-match correction |
| output/messi_03_scoring_acceleration.png | Chart 3 | Visual QA pass |

## Content package

| Asset | File or text location | Status |
|---|---|---|
| Blog post |  | Not started |
| Blog excerpt |  | Not started |
| LinkedIn post |  | Not started |
| Instagram caption |  | Not started |
| Cartoon scene |  | Not started |
| Image prompt |  | Not started |

## QA notes

- Data checked: Yes — totals and split recomputed.
- Config checked: Yes — source paths/columns/chart types reviewed.
- Render checked: Yes — both archived-project runs succeeded.
- Labels/margins checked: Yes — final PNGs visually reviewed at 1600 × 1600; no clipping/collisions.
- Source text checked: Yes.
- Archive checked: Yes — project-scoped only.

## Decisions and caveats

- Senior Argentina A internationals only for cap/goal analysis.
- AFA's farewell totals are internally inconsistent; they are not the controlling career count.
- No claim is made that trophy success caused the higher late-career scoring rate.
- No reusable renderer/template changes made.

## Closeout

- Published URL:
- Final archive PR: Draft PR pending creation
- Merge commit:
