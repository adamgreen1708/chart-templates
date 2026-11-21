# The A-Team — Adam, Adrian and Alex
Status: DRAFT RESEARCH; NOT PUBLICATION APPROVED.
Scope: England and Wales, boys, exact first names. Historical top-100 GRO/ONS rankings are ten-year snapshots only, not annual counts; absences do not imply rank 101. The 1996–2024 ONS-derived TidyTuesday extract is version-pinned; 2025 official ONS workbook is available but not imported here. Names fewer than three births are suppressed.

Source links:
- https://www.ons.gov.uk/peoplepopulationandcommunity/birthsdeathsandmarriages/livebirths/datasets/babynamesenglandandwalestop100babynameshistoricaldata
- https://www.ons.gov.uk/peoplepopulationandcommunity/birthsdeathsandmarriages/livebirths/datasets/babynamesinenglandandwalesfrom1996
- https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2026/2026-06-16/england_wales_names.csv

Three different hypotheses:
1. Adrian arrived first; Adam overtook; Alex appeared later — historical rank chart. Evidence: 1944–1994 observed ranks, not interpolated. Risk: decennial sample only.
2. Adam persisted longer in the rankings while Alex and Adrian changed differently — annual ranked series. Risk: ranks are not numbers of babies; verify clear three-name colour encoding.
3. A grew at J's expense among published boys' name registrations — annual shares of A/J first letters. Risk: denominator excludes suppressed names, not all births; cannot prove parents' motivations.
The preferred 3-chart sequence is historical setup, annual rivalry, alphabetical reversal if the data support it. Reject any filler chart after data audit.

Colours across charts: Adam/A: #1F8FA8; Alex/J: #C44E52; Adrian: #777777. The colour keys and different subjects must be stated clearly on each chart.
Production: GitHub render-archived-project workflow only, 1600px plus real 390px and 320px PNG review, no ChartGPT visual mock data, no publication without explicit approval.

## Current review render
GitHub Actions exact 1600px outputs plus QA mobile exports are required. A first render succeeded but its push collided with ongoing branch edits; repeat on current stable head and inspect the saved images before approval.

## Normalisation revision — 21 November 2026
At the editorial review stage, replace the raw annual rank chart (chart 2) with an actual **per-10,000 boys** comparison for 1996 and 2024; annual raw counts/ranks remain as audited background data. Chart 2 is now an explicitly 2-year rate-change scatter on a negative/positive axis, with each brother's colour maintained.

- Male-birth denominators are stored (with source URL per row) in `data/male_birth_denominators.csv`.
- **1996: 333,490** male births from historical GRO/ONS Table 1.1, England and Wales (1996 year of occurrence).
- **2024: 304,889** male births in the ONS baby-name release's 2024 cohort.
- Difference in birth-statistics population basis: historical 1996 live-birth occurrence vs 2024 ONS baby-names cohort; minor publication difference makes percentage-point precision approximate. The editorial conclusion is robust to this discrepancy.
- Rates: `exact-name births * 10000 / annual male births`. Relative change: `100 * ((rate2024 / rate1996) - 1)`, **not** a difference in percentage points.
- The calculated source rows feed `data/chart_02_normalised.csv`; no hardcoded measured value in plotting code.
- Chart 3 retains the different denominator of *published ONS baby-name registrations*, due to lack of a verified, fully aligned 29-year male-birth denominator series. Its axis and article must say so; do **not** call the annual A/J lines a share of all boy births.
- This comparison does not claim trends during intervening years — only measured endpoints. Reconsider adding an annual-rate chart only once annual male-birth denominators are fully sourced and imported.

Three-chart editorial arc now: historically Adrian arrived early → **Adrian is the only gainer by birth share** → the letter A overtakes J among published names.
The ranking chart, historical sources, archive-only status and publication approval gate otherwise remain unchanged.
