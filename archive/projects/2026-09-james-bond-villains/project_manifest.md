# Project manifest: James Bond villains

## Status

- Status: Archive complete / publication draft
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

## Scope and definitions

- Scope: Eon Productions' 25 Bond films from `Dr. No` (1962) to `No Time to Die` (2021).
- Villain grain: enriched source work uses one row per villain × film appearance; the core age story uses the first-listed villain identity per film for a consistent film-level comparison.
- `is_first_listed_villain` is a consistency rule, not a claim that the selected character is objectively the film's sole or definitive main villain.
- IMDb ratings are film ratings, not villain ratings, and are retained only as optional companion context.
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
| `data/bond_villains_companion_imdb_ranking.csv` | Optional IMDb companion ranking | Film rating context only; rounded vote snapshot |

## Chart configs

| File | Chart | Output | QA status |
|---|---|---|---|
| `config/chart_01_actor_age.py` | Bond villains range from 32 to 65 | `bond_villains_actor_age.png` | Real renderer visual QA passed after title/subtitle fix |
| `config/chart_02_age_gap.py` | Bond used to fight his elders | `bond_villains_age_gap.png` | Real renderer visual QA passed; categorical annotation renderer fix verified in Actions runs #4 and #5 |
| `config/chart_03_era_age.py` | Bond grew into his villains | `bond_villains_era_age.png` | Real renderer visual QA passed after same-age-label and annotation fixes |

## Story findings

- First-listed villain portrayals span roughly 31.7 to 65.0 years old at UK release.
- Across films 1–7 (1962–1971), first-listed villains averaged 14.3 years older than Bond.
- Across 1973–2021, first-listed villains averaged 2.6 years younger than Bond.
- Bond-era average villain-minus-Bond age gaps: Connery +13.76; Lazenby +17.62; Moore -2.15; Dalton -1.98; Brosnan -7.59; Craig +0.37 years.
- The strongest editorial interpretation is relative-age change, not a simplistic claim that villains themselves steadily became younger.

## Rejected / secondary story routes

- SPECTRE chronology was demoted because Eon film release order does not equal Fleming publication chronology; using film order to imply literary villain evolution would be misleading.
- IMDb ranking remains a companion idea: `Who got the best Bond film to be evil in?` It must always be framed as the film's IMDb rating, not a villain rating.
- A villain-fate route remains possible but was not part of the core three-chart age story.

## Workflow / outputs

| Item | Status |
|---|---|
| `requirements-render.txt` | Pins the renderer stack used by GitHub Actions so production renders do not change when upstream libraries release new versions |
| `.github/workflows/render-538.yml` | Existing single-active-config renderer retained; uses the pinned renderer requirements |
| `.github/workflows/render-chart.yml` | Generated-config workflow uses the same pinned renderer requirements |
| `.github/workflows/render-archived-project.yml` | Archived-project renderer uses the pinned renderer requirements and commits project PNGs back to the archive |
| `output/` inside this project | Complete: all three final PNGs verified in `main` after PR #27 |

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
- Actions branch QA run #4 (`34417695088`) completed successfully: all three configs rendered, archived output listing passed, artifact upload passed and output commit-back passed.
- The run #4 artifact was visually inspected: Chart 1 title/subtitle and category labels fit; Chart 2 Klebb and Graves/Moon annotations render correctly with no clipping; Chart 3 equal-age diagonal and era labels remain clear and unclipped.
- PR #27 merged at commit `5949d09fe5c88c4f3e38dbf8b73cd655cdc35873`.
- Main archived-project run #5 (`34418280094`) completed successfully after the merge.
- All three PNGs are verified under `archive/projects/2026-09-james-bond-villains/output/` on `main`.
- The production stack remains pinned at NumPy 2.3.5, pandas 2.2.3 and Matplotlib 3.10.8 for reproducible rendering.

## Content package

- Story plan: `content/story_plan.md`
- Publication package: `content/publication_package.md`
- Publication draft status: ready for Adam review

## Closeout

- Published URL: TBC
- Final archive/output PR: #27
- Final archive/output merge commit: `5949d09fe5c88c4f3e38dbf8b73cd655cdc35873`
- Archive complete: Yes
- Publication complete: No — publication package is drafted and awaiting review/publishing.
