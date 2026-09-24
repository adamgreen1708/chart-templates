# Project manifest: David Bowie reinvention

## Status

- Status: Main three-chart package staged; Chart 3 gap refinement and exploratory Chart 4 rendered/QA passed; awaiting Adam final chart-selection review
- Started: 23 September 2026
- Last updated: 24 September 2026
- Owner: Adam Green
- Repo project slug: `2026-09-david-bowie-reinvention`
- Working branch: `project/2026-09-david-bowie-reinvention`
- Draft PR: #65

## Story

- Working headline/angle: **How do you measure a chameleon?**
- Core question: can Bowie's repeated musical shifts be shown with transparent data without pretending genre metadata is an objective creativity score?
- Focus artist: David Bowie.
- Audience: coffeetableviz readers plus music/data audiences.
- Current recommendation: Bowie-only three-chart story first; retain the wider long-career artist cohort as a later extension.

## Validated focus scope

- 26 lifetime solo studio albums.
- 1967 debut through *Blackstar* (2016).
- 49-year difference between first and last album years.
- Six named calendar decades: 1960s through 2010s.
- Include *The Buddha of Suburbia* (1993): official Bowie store calls it the 19th studio album.
- Exclude *Toy* from the lifetime sequence: official Bowie archive describes it as previously unreleased and released separately in 2022.
- Exclude live albums, compilations, *Peter and the Wolf* and Tin Machine.

## Sources

| Source | URL | Use |
|---|---|---|
| David Bowie official site/store | https://www.davidbowie.com/ | Canonical Bowie scope and catalogue edge cases |
| MusicBrainz | https://musicbrainz.org/ | Reproducible identity/release-group chronology and supplemental genre metadata |
| AllMusic | https://www.allmusic.com/artist/david-bowie-mn0000531986 | Primary album-level Styles vocabulary for like-for-like style turnover |
| Official Charts | https://www.officialcharts.com/artist/19138/david-bowie/ | Optional later UK chart context; not used in the current reset metric |

## Analytical dataset

AllMusic exposes Styles metadata for 25 of the 26 scoped studio albums. *The Next Day* currently has no AllMusic Styles values, so:

- 25 albums have comparable AllMusic style sets;
- 23 of 25 adjacent transitions can be scored;
- the two transitions touching *The Next Day* remain missing rather than being imputed;
- MusicBrainz genres for *The Next Day* are stored as supplemental context only.

The adjacent-album measure is:

`style reset score = 1 - Jaccard similarity`

where Jaccard similarity is the number of shared AllMusic Styles divided by the union of the two style sets.

This is a metadata-turnover score, not a creativity/quality/influence score.

## Key analytical findings

- 24 distinct AllMusic style labels occur across the 25 tagged albums.
- Contemporary Pop/Rock appears on 24 of 25 tagged albums.
- Art Rock appears on 23 of 25.
- Experimental Rock appears on 22 of 25.
- Median measurable adjacent-album reset = 0.3333.
- Calendar-year gap vs reset score across 23 measurable transitions: Pearson r = 0.3568 (shown as 0.36).
- The 6-year gap before *Black Tie White Noise* produces a 0.3333 / 33% reset; the highest measured reset, *Space Oddity*, follows a 2-year gap.
- The 10-year *Reality* → *The Next Day* hiatus cannot be included in that relationship because *The Next Day* has no comparable AllMusic Styles score.
- Highest reset = 1967 debut -> *Space Oddity* at 0.8889.
- *Diamond Dogs* -> *Young Americans* = 0.6667.
- *Scary Monsters* -> *Let's Dance* = 0.6000.
- *Station to Station* -> *Low* = only 0.3333 because broad umbrella labels remain shared.

That final result is central to the recommended editorial angle: metadata can reveal movement while still failing to capture the full artistic significance of a well-known pivot.

## Recommended three-chart sequence

1. **Six decades. Twenty-six albums.** — studio-album timeline establishing longevity/cadence.
2. **The labels rarely sit still.** — album × style dot matrix showing labels entering, disappearing and returning.
3. **A reinvention score gets awkward.** — adjacent-album style-reset score, using the unexpected results to explain why taxonomy is not artistic truth.

Full rationale and QA risks: `content/story_plan.md`.

## Files

| File | Purpose | Status |
|---|---|---|
| `data/artist_cohort_seed.csv` | Optional later peer cohort seed | Created |
| `scripts/build_musicbrainz_dataset.py` | MusicBrainz acquisition scaffold with Bowie scope overrides | Updated |
| `content/research_plan.md` | Final scope/methodology and QA findings | Updated |
| `data/david_bowie_studio_albums.csv` | 26-album chronology plus AllMusic styles/source audit | Created |
| `scripts/analyse_allmusic_styles.py` | Reproducible adjacent-style Jaccard calculation | Created |
| `data/david_bowie_style_transitions.csv` | 25 adjacent transitions; 23 scored, 2 explicitly missing | Created |
| `content/story_plan.md` | Ranked story options and recommended three-chart route | Created |
| `data/artist_album_spans.csv` | Optional wider-cohort output | Deferred |
| `data/bowie_chart_01_timeline.csv` | Chart 1 derived chronology | Created |
| `data/bowie_chart_02_style_matrix.csv` | Chart 2 derived album/style matrix | Created |
| `data/bowie_chart_03_style_reset.csv` | Chart 3 reset rows plus calendar-year gap context | Created |
| `data/bowie_chart_04_gap_vs_reset.csv` | Chart 4 measurable gap-vs-reset rows | Created |
| `scripts/build_story_datasets.py` | Rebuild derived Bowie chart datasets | Updated |
| `config/chart_01_six_decades.py` | Chart 1 locked-renderer config | Created and rendered |
| `config/chart_02_style_matrix.py` | Chart 2 locked-renderer config | Created and rendered |
| `config/chart_03_reinvention_score.py` | Chart 3 locked-renderer config with gap labels | Updated and rendered |
| `config/chart_04_gap_vs_reset.py` | Exploratory Chart 4 scatter config | Created and rendered |
| `output/bowie_01_six_decades.png` | Final Chart 1 render | QA pass |
| `output/bowie_02_style_matrix.png` | Final Chart 2 render | QA pass |
| `output/bowie_03_reinvention_score.png` | Revised Chart 3 render with gap context | QA pass |
| `output/bowie_04_gap_vs_reset.png` | Exploratory gap-vs-reset scatter | QA pass |
| `content/qa_report.md` | Data, config, renderer and visual QA record | Updated |

## Build status

Adam approved the recommended editorial route on 23 September 2026.

Created:
- `data/bowie_chart_01_timeline.csv`
- `data/bowie_chart_02_style_matrix.csv`
- `data/bowie_chart_03_style_reset.csv`
- `scripts/build_story_datasets.py`
- `config/chart_01_six_decades.py`
- `config/chart_02_style_matrix.py`
- `config/chart_03_reinvention_score.py`

Renderer/template improvement:
- added reusable explicit `x_tick_labels` / `y_tick_labels` support for numeric-position matrix/scatter charts;
- updated spec, config template, prompt and tests;
- enabled archived-project rendering on `project/**` branches so charts can be QA'd before merging.

PR #65 remains draft. Final chart QA passed; Adam's visual approval is the remaining gate before the publication package.


## Publication staging

- Adam approved the final three-chart set on 23 September 2026.
- Publication package staged at `content/publication_package.md`.
- Jekyll post staged at `site/_posts/2026-09-23-how-do-you-measure-a-chameleon.md`.
- Exact approved chart PNGs copied into `site/assets/migrated/david-bowie-reinvention/`.
- Deterministic story-specific feature artwork staged as `site/assets/migrated/david-bowie-reinvention/feature.svg`.
- Feature metaphor: a chameleon stretched across a measuring ruler, expressing the tension between visible reinvention and imperfect measurement.
- Pages PR build passed in run `35918449198`.
- PR #65 must remain draft until Adam reviews the exact feature asset and site post.


## Gap-analysis extension — 24 September 2026

- Chart 3 now adds the calendar-year gap since the previous album directly to each destination-album label.
- Same-year album pairs are labelled `same year`.
- Exploratory Chart 4 asks whether longer release gaps coincide with larger style resets.
- Across 23 measurable transitions, Pearson `r = 0.3568` (0.36): a modest positive relationship, not a rule.
- The 6-year wait before *Black Tie White Noise* has only a 33% reset.
- The 10-year *Reality* → *The Next Day* hiatus is the largest calendar-year gap but cannot be scored and is therefore not plotted in Chart 4.
- Final extension render/QA: GitHub Actions run `35961245532` — success.
- Chart 4 remains a spin-off candidate and is not yet included in the live Jekyll article.
