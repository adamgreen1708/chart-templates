# David Bowie reinvention — QA report

## Gate

Status: **PASS — ready for Adam visual review**

GitHub Actions render:
- workflow: `Render archived project`
- final extension QA run: `35961245532`
- conclusion: success
- branch: `project/2026-09-david-bowie-reinvention`

## Data QA

### Chart 1 — chronology

- 26 rows.
- One row per scoped lifetime solo studio album.
- Sequence runs 1–26.
- Album years run 1967–2016.
- `The Buddha of Suburbia` retained under the documented official-catalogue override.
- `Toy` excluded under the documented posthumous-release rule.
- No mock or placeholder values.

### Chart 2 — style matrix

- 81 plotted album/style observations.
- All rows derive from the album-level AllMusic Styles sets in `david_bowie_studio_albums.csv`.
- The three near-universal context labels are intentionally omitted from the display only:
  - Contemporary Pop/Rock
  - Art Rock
  - Experimental Rock
- They remain in the underlying source data and in the reset calculation.
- 21 distinctive style rows are shown.
- `The Next Day` remains absent because its AllMusic page currently exposes no Styles values; no styles were imputed.

### Chart 3 — reset score

- 23 measurable adjacent-album transitions.
- Two transitions touching `The Next Day` are explicitly missing, not zero.
- Score is `1 - Jaccard similarity` on complete AllMusic Styles sets.
- Percentage axis correctly maps 0.0–1.0 to 0–100%.
- Median reference line = 0.3333 / 33%.
- *Space Oddity* reset = 0.8889 / 89%.
- *Station to Station* → *Low* reset = 0.3333 / 33%.

## Config QA

All three configs:

- use repo-relative real-data paths;
- use exact source column names;
- use dict-based sorting;
- include `sort_descending=False`;
- use descriptive output filenames;
- stay on the locked 8 × 8 canvas;
- retain the locked `#F3F4F6` background and house palette;
- include source/footer text.

## Renderer/template QA

This project exposed a reusable matrix-chart gap.

Implemented:

- `x_tick_labels` / `y_tick_labels` optional config support;
- renderer implementation in `src/render_538.py`;
- config-template documentation;
- locked 538 spec documentation;
- chart-config prompt documentation;
- a unit test covering explicit custom ticks.

The final Chart 2 render exercised the new y-axis tick-label behaviour successfully.

Workflow improvement:

- `render-archived-project.yml` now supports `project/**` branches as well as `main`.
- This allows visual QA before merge instead of requiring project work to reach main first.

## Visual QA

### Chart 1 — Six decades. Twenty-six albums.

PASS.

- title/subtitle clear and within bounds;
- all 26 album labels readable;
- no right-edge clipping;
- x-axis readable;
- 10-year gap annotation moved away from the *Blackstar* row after first visual QA;
- footer/source visible.

### Chart 2 — The labels rarely sit still

PASS after one refinement.

First render issues:
- red pivot columns were unexplained;
- 2013 and 2016 tick labels crowded at the right edge.

Final fix:
- removed unexplained red highlighting;
- removed the 2013 intermediate tick;
- retained 2016 endpoint.

Final render:
- 21 style labels readable;
- matrix fits square canvas;
- selected year ticks are readable;
- no clipping;
- no unnecessary legend or annotation clutter.

### Chart 3 — A reinvention score gets awkward

PASS after release-gap context refinement.

Final extension QA render:
- GitHub Actions run `35961245532`
- conclusion: success

Checks:
- all 25 destination-album rows are shown;
- 23 rows carry measured reset scores;
- each album label now includes the calendar-year gap since the previous release;
- same-year releases are labelled `same year` rather than `0y`;
- *The Next Day · 10y* and *Blackstar · 3y* remain grey missing-data rows;
- the two missing rows sit in a small non-data gutter left of 0%, so they cannot be read as zero reset scores;
- x-axis begins at -0.06 internally, while visible labelled ticks remain 0–100%;
- exact-zero measured dots retain breathing room and are not clipped;
- median reference line remains readable;
- Space Oddity and Low annotations remain inside safe margins;
- labels remain readable on the locked 8 × 8 canvas;
- source/footer visible.

### Chart 4 — More time doesn't guarantee a bigger reset

PASS — exploratory spin-off.

Data checks:
- 23 measurable transitions plotted;
- x-axis uses calendar-year difference (`to_year - from_year`), not exact elapsed release-date intervals;
- Pearson correlation independently reproduced as `r = 0.3568`, displayed as 0.36;
- the 10-year *Reality* → *The Next Day* gap is excluded from the scatter because no comparable reset score exists;
- *Black Tie White Noise* = 6-year gap / 33% reset;
- *Space Oddity* = 2-year gap / 89% reset.

Visual checks:
- final render from run `35961245532` succeeded;
- 0% reset and same-year observations have axis breathing room;
- trend line is visible but subordinate to the points;
- four selected annotations include album names, gap and reset;
- no annotation or title clipping;
- source/footer visible.

Editorial check:
- the chart supports a modest positive association, not a causal claim;
- the 6-year / 33% counterexample and unscored 10-year hiatus prevent a simplistic “more time means more reinvention” reading.

## Editorial QA

The main three charts form one connected argument:

1. longevity: 26 albums across six named decades;
2. stylistic movement: distinctive labels repeatedly enter and leave;
3. measurement caveat: a transparent score can still understate a famous artistic pivot.

The charts do not claim that the reset metric measures creativity, quality, influence or Bowie's intent.

Chart 4 is retained as an exploratory spin-off candidate. It is not yet part of the live-site story.

## Remaining gate

Adam review of the Chart 3 gap-label refinement and the Chart 4 spin-off. The live-site publication package is already staged in draft PR #65; do not merge until Adam confirms the final chart selection.
