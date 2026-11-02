# Bauhaus Poster Composer v3 — prototype and editorial QA

**Scope:** a focused experiment in the existing \`/resources/bauhaus-art-studio/\` page. This is not a replacement for the existing free-play, Patchwork, Orbit, Ribbon or CSV/GitHub loading tools. Review as a PR before merging.

## Problem observed

In Data Art v2, every row became an isolated shape, with palette and layout choices that still created broadly similar compositions. Equal or close values gave nearly identical circles. It looked like a chart with decorations, not a Bauhaus-inspired poster with its own editorial logic.

## Two genuinely separate composition engines

### Data Mosaic

- **Visual grammar:** an edge-to-edge arrangement of rectangular tiles, produced by a deterministic binary treemap. It is not another cell grid.
- **Data mapping:** each **tile's bounding-box area** = row value / sum of **positive** plotted values × total mosaic area. All source values are retained and used; zero-valued rows have no drawable area and the studio explicitly says how many are invisible.
- **Colour:** existing median, four equal-width bands, category or decorative-sequence rule. For decorative colour the UI explains that colour does not encode data.
- **Decoration:** inset gaps and occasional corner arcs are artistic treatment only; they do not encode measurements. The external tile boundary, **not the inked shape or arc**, carries the proportional area.
- **Labels:** optional, shown within tiles only if there is sufficient space; user can tap any tile to inspect the actual source label and numeric value.
- **Composition:** meaningful tiling plus negative space and variable geometry. The original row order or selected sorting determines the sequence of treemap splits.

### Typographic Broadside

- **Visual grammar:** large dark editorial hero panel containing the largest selected observation and its actual value, followed by a compact series of aligned bars.
- **Data mapping:** bar length = row value / maximum displayed value × full available width; baseline starts at zero. The maximum value is also represented typographically. Ties are legitimate; highlight is not a claim of exclusivity.
- **Colour:** primary accent highlights every bar equal to the maximum, and secondary ink describes all other bars. No extra colour metric is implied.
- **Labels:** optional left-hand captions, or values or displayed indices, where the layout permits. Tap any bar row for the original label and number.
- **Composition:** asymmetric emphasis, typographic contrast and clear hierarchy instead of a uniform tile arrangement.

### Editorial behaviour

- For Data Mosaic, automatic text names the measure and the number of selected observations and explicitly says **rectangle area** encodes value.
- For Typographic Broadside, automatic text identifies the largest observation from the chosen metric (no invented story) and says **bar length** encodes value.
- All text remains editable; previously saved custom fields are respected until a different dataset is loaded or the user clicks **Restore automatic text**.
- The optional v2 scale-contrast control is **disabled for both new engines**: v3 uses original values with zero-based magnitude. Shape family control is also disabled in both; the broadside additionally disables unrelated colour-rule controls.
- Preserve source row-count / first-64 disclosure, selected filter, and CSV filename in the automatic source line.

## Verified example: Bowie 1967 debut album

Repository dataset:
\`archive/projects/2026-09-david-bowie-track-distributions/data/bowie_track_distribution_rows.csv\`.

Filter \`album_title = David Bowie\`. Label \`track_title\`, measure \`duration_seconds\`.

Exactly 14 tracks; total duration **2,353 seconds**; shortest **Maid of Bond Street, 106 seconds (1:46)**; longest **Silly Boy Blue, 234 seconds (3:54)**. These are **source rows** from the verified GitHub CSV and not sample estimates.

The finished **static design previews** checked into the PR are:

- [Data Mosaic (SVG)](previews/bauhaus-v3-bowie-mosaic.svg)
- [Typographic Broadside (SVG)](previews/bauhaus-v3-bowie-broadside.svg)

These two SVGs are *deterministic illustrative renders using the same source values*, not pixel captures from a hosted canvas. The live feature is implemented with HTML Canvas, so a preview cannot substitute for browser screenshot QA.

## Tests completed for the prototype

- Embedded JavaScript compiles.
- Actual Bowie CSV imported through the existing GitHub selector; 275 source rows, filtered to 14 tracks for the original album.
- Mosaic draws 14 rectangular tiles with per-row area proportions. Numeric areas can be checked independently.
- Broadside draws 14 zero-based bars and identifies the maximum as **3:54 — Silly Boy Blue**.
- The existing label checkbox, sorting, palettes, local CSV and GitHub CSV source selection remain wired into the new modes.
- Reverting to Patchwork still renders the existing engine; no chart renderers, blog output or data files are altered.

## Category filter interaction — regression

- After the user creates an artwork from a mapped CSV, changing **Select category** must automatically reapply the same source, label, numeric measure, category subset and current poster mode. The headline, row count, source credit and marks redraw together.
- Changing **Optional category filter** back to all rows must also update the artwork and disclose the first-64 limit if relevant.
- A local or GitHub CSV **newly loaded but not yet created** must not silently replace the previously rendered artwork. The user maps it and presses Create once; subsequent category changes are live.
- Confirm the count and live update alongside the filter selector on mobile, rather than relying on a status message below the canvas.
- Regression datasets: Bowie `album_title` (first album 14 tracks; second album 10; third album 9), plus the current site-analytics CSV. Test Mosaic, Broadside and an original creative layout. Preserve custom editorial text until the user explicitly restores automatic text.

## Before approving merge

- Test *actual mobile Safari* interactions: GitHub file link and local upload, changing filters/modes, touch-to-inspect, optional labels and Save PNG.
- Perform pixel QA for minimum and maximum row counts (1, 14, 24, 64), all palettes, extreme numeric ranges, zeros and tied maxima.
- Verify Mosaic tile sums against source sums, and Broadside bar ratios against zero-based values.
- Inspect safe margins, clipping, legend clarity, colour contrast, footer overflow, dense labels, title lengths, and visual rendering in square output.
- Dense datasets are deliberately shown in a 64-row poster at most (existing rule); suggest filtering to roughly 8–24 records for print-like results. Do **not** silently drop rows beyond that existing cap.
- Do not describe previews as screenshots of deployed renderers; do not claim iPhone QA has passed without a real test.

## Later ideas, out of scope

Dedicated visual legend layout, side-by-side poster compare-and-save, selected hero metric, optional thematic type treatments, multi-measure story mode, SVG export and an automated recommendation between Mosaic and Broadside.
