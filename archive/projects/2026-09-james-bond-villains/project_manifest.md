# Project manifest: James Bond villains

## Status

- Status: Archive complete / IMDb companion chart QA passed / merge pending
- Started: 9 September 2026
- Last updated: 10 September 2026
- Owner: Adam Green
- Repo project slug: `2026-09-james-bond-villains`

## Story

- Working title: James Bond villains
- Final working title: Bond finally grew into his villains
- Core question: How did the age relationship between Bond and his first-listed villains change across the 25 Eon films?
- Main takeaway: Bond villains did not simply get steadily younger. Early Eon Bond usually faced much older first-listed villains; later Bond actors increasingly met villains close to their own age or younger.
- Audience: coffeetableviz readers and social audience
- Blog/social use: WordPress post, excerpt, LinkedIn, Instagram and feature image
- Bonus companion: `Le Chiffre got the best Bond film to be evil in` — a film-level IMDb ranking framed explicitly as context, not villain quality.

## Scope and definitions

- Scope: Eon Productions' 25 Bond films from `Dr. No` (1962) to `No Time to Die` (2021).
- Villain grain: enriched source work uses one row per villain × film appearance; the core age story uses the first-listed villain identity per film for a consistent film-level comparison.
- `is_first_listed_villain` is a consistency rule, not a claim that the selected character is objectively the film's sole or definitive main villain.
- IMDb ratings are film ratings, not villain ratings, and are retained only as companion context.
- `Die Another Day` has a dual portrayal for Gustav Graves / Colonel Tan-Sun Moon. Chart 1 retains Toby Stephens and Will Yun Lee separately; film-level and Bond-era age calculations use their mean so the film counts once.

## Sources

| Source | Purpose | Notes |
|---|---|---|
| 007.com official film pages | UK release dates | Used for the corrected exact-date age analysis |
| Wikipedia `List of James Bond villains` | Villain table / ordering | Defines the antagonist-table scope and first-listed consistency rule |
| Wikipedia actor biographies | Actor dates of birth | Used to calculate exact ages at UK release |
| IMDb title pages | Film rating context | Snapshot dated 9 September 2026; vote counts are approximate / rounded |

## Data files

| File | Purpose | Notes |
|---|---|---|
| `data/bond_villains_chart_01_actor_age.csv` | Actor-portrayal age spread | 26 portrayal rows across 25 films; `Die Another Day` has two rows |
| `data/bond_villains_chart_02_age_gap.csv` | Film-level villain minus Bond age gap | 25 films; `Die Another Day` uses mean of two portrayer ages |
| `data/bond_villains_chart_03_era_age.csv` | Bond-era age comparison | Six Bond actor eras |
| `data/bond_villains_companion_imdb_ranking.csv` | Verified IMDb companion ranking | Film rating context only; rounded vote snapshot |
| `data/bond_villains_chart_04_imdb_companion.csv` | Chart-ready IMDb companion data | 25 first-listed villain identities; display label derived from verified villain and film fields |

## Chart configs

| File | Chart | Output | QA status |
|---|---|---|---|
| `config/chart_01_actor_age.py` | Bond villains range from 32 to 65 | `bond_villains_actor_age.png` | Real renderer visual QA passed after title/subtitle fix |
| `config/chart_02_age_gap.py` | Bond used to fight his elders | `bond_villains_age_gap.png` | Real renderer visual QA passed; categorical annotation renderer fix verified in Actions runs #4 and #5 |
| `config/chart_03_era_age.py` | Bond grew into his villains | `bond_villains_era_age.png` | Real renderer visual QA passed after same-age-label and annotation fixes |
| `config/chart_04_imdb_companion.py` | Le Chiffre got the best Bond film to be evil in | `bond_villains_imdb_companion.png` | Real archived-project Actions and visual QA passed on branch run #8 |

## Story findings

- First-listed villain portrayals span roughly 31.7 to 65.0 years old at UK release.
- Across films 1–7 (1962–1971), first-listed villains averaged 14.3 years older than Bond.
- Across 1973–2021, first-listed villains averaged 2.6 years younger than Bond.
- Bond-era average villain-minus-Bond age gaps: Connery +13.76; Lazenby +17.62; Moore -2.15; Dalton -1.98; Brosnan -7.59; Craig +0.37 years.
- The strongest editorial interpretation is relative-age change, not a simplistic claim that villains themselves steadily became younger.
- IMDb companion: `Casino Royale` is highest in the 25-film snapshot at 8.0, followed by `Skyfall` at 7.8 and `Goldfinger` at 7.7; `Die Another Day` is lowest at 6.1. These are film ratings, not villain ratings.

## Rejected / secondary story routes

- SPECTRE chronology was demoted because Eon film release order does not equal Fleming publication chronology; using film order to imply literary evolution would be misleading.
- IMDb ranking is promoted to a small bonus chart: `Who got the best Bond film to be evil in?` It remains explicitly film-level context, not a villain-quality ranking.
- A villain-fate route remains possible but is not part of the current publication package.

## Workflow / outputs

| Item | Status |
|---|---|
| `requirements-render.txt` | Pins the renderer stack used by GitHub Actions so production renders do not change when upstream libraries release new versions |
| `.github/workflows/render-538.yml` | Existing single-active-config renderer retained; uses the pinned renderer requirements |
| `.github/workflows/render-chart.yml` | Generated-config workflow uses the same pinned renderer requirements |
| `.github/workflows/render-archived-project.yml` | Archived-project renderer uses the pinned renderer requirements and commits project PNGs back to the archive; temporary branch QA trigger removed before PR |
| `output/` inside this project | Four-chart set complete on the companion branch; Chart 04 awaits merge/main verification |

## QA notes

- Data paths and config columns checked against the archived CSVs.
- Config syntax checked.
- Visual QA covered title/subtitle spacing, safe margins, clipping, annotations, reference lines, axes and footers.
- Chart 1 required a title/subtitle spacing fix.
- Chart 2 passed visual QA unchanged at config level.
- Chart 3 required moving the `Same age` label inside the plotting area and adjusting the Roger Moore annotation.
- PR #21 duplicate/older files were removed by cleanup PR #23; PR #22 remains the canonical analytical version.
- Automated archived-project run #1 selected the correct Bond project and rendered Chart 1, then failed while saving Chart 2 because Matplotlib 3.11.1 rejected the categorical y-value used by the row-matched annotation.
- Automated archived-project run #2 reproduced the same Chart 2 failure under the pinned QA stack, proving dependency drift was not the root cause.
- Renderer fix: `_plot_annotations` now resolves categorical dot y-values through the same numeric y-position lookup used by `_plot_dot` and `_plot_labels`.
- Actions branch QA run #4 (`34417695088`) completed successfully for the core three charts.
- PR #27 merged at commit `5949d09fe5c88c4f3e38dbf8b73cd655cdc35873`.
- Main archived-project run #5 (`34418280094`) completed successfully after the core merge.
- The production stack remains pinned at NumPy 2.3.5, pandas 2.2.3 and Matplotlib 3.10.8 for reproducible rendering.
- Chart 04 real branch QA: archived-project Actions run #8 (`34531970658`) completed successfully, including render, output listing, artifact upload and commit-back.
- Run #8 artifact `archived-project-render` (`10173855946`) contained the three unchanged core PNGs plus `bond_villains_imdb_companion.png` (261,203 bytes).
- Chart 04 visual QA passed: all 25 ranked rows are present; long villain/film labels fit; Le Chiffre is the sole red highlight at 8.0; Skyfall 7.8 and Goldfinger 7.7 follow correctly; `Die Another Day` is 6.1; title, subtitle, axis, source and footer are unclipped.

## Content package

- Story plan: `content/story_plan.md`
- Publication package: `content/publication_package.md`
- Publication draft status: updated with the approved bonus IMDb chart section, Chart 04 caption and alt text.

## Closeout

- Published URL: TBC
- Final core archive/output PR: #27
- Final core archive/output merge commit: `5949d09fe5c88c4f3e38dbf8b73cd655cdc35873`
- Core archive complete: Yes
- Companion extension complete: Branch QA passed; merge/main verification pending.
- Publication complete: No — awaiting publication and final live URL.
