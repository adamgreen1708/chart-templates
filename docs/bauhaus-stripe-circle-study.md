# Bauhaus Poster Composer v4 — Stripe Study and Circle Study

## Status and PR dependency

Stage 2 feature branch built from `fix/bauhaus-gallery-copy-ink-refinement` (Stage 1, PR #180). **Merge Stage 1 first**, then review or retarget Stage 2 to `main`. No direct writes to `main`.

Source of truth: `docs/bauhaus-gallery-v2-revision-brief.md`. Preserve all earlier creative and Data Art modes, live category selection, local/GitHub CSV loading, editable captions and square PNG export.

## New composition: Stripe Study

- **The primary data mark is stripe length**, measured from a common left-hand zero line. At maximum: `length = availableWidth × value / max(selectedValues)`.
- All source values must be finite and non-negative (existing importer guardrail).
- For 1–26 or so rows, each row contains three parallel, **identical-length** strokes for a rhythmic Bauhaus look. Every row has the same number of strokes. At higher densities the design uses one stroke per row to avoid collisions. The count of strokes and thickness are **not** additional measurements.
- Red/brick accent highlights **all tied maxima**; dark stripes show the remaining rows. Colour is a highlight, not an independently mapped metric.
- Sorting, selected category and optional Label / Value / Both / displayed index all affect only the appropriate aspects of the poster. Labels and the entire row area remain tappable.
- Large or dense datasets (up to existing 64-row cap) retain their full plotted values but recommend a filtered 8–24-row selection for legibility.
- On-poster auto copy explicitly says `stripe length ∝ <selected metric>` and identifies red as maximum. Footer retains actual source, filter and row count.

## New composition: Circle Study

**Data-driven outer rings, not arbitrary decoration.** The large concentric outlines on the left summarise four statistics computed from the **currently selected displayed records**: **maximum, upper quartile (75th percentile), median (50th percentile), minimum**. Quartiles use the linear-interpolation percentile rule at index `(n-1) × p` on sorted source values. They are recomputed whenever a category, measure or selected record set changes. The built-in on-poster key names and displays each statistic; fractional-second summaries are rounded only when *displayed* as time.

The right-hand circles/arcs represent the individual observations, using the same selected encoding as the summary. The left hero shows the real maximum and its original record label.

**Disc Area setting (default):**
- Right-hand filled discs: `discRadius_i = rMax × sqrt(value_i / maxValue)`.
- Left-hand summary outlines: `ringRadius_j = summaryMaxRadius × sqrt(stat_j / maxValue)`.
- Thus **area enclosed by an outline ring**, just like the **area of a filled disc**, is proportional to its underlying source-derived value. Stroke width and hue are not measures.
- If a selected statistic is zero, it has no visible ring; if several statistics are equal, their outlines overlap because that is the truthful equal area. The labels still report each statistic.

**Arc Sweep setting:**
- Right-hand observed arcs use one constant radius and stroke width. `sweep_i = 2π × value_i / maxValue`.
- Left-hand summary arcs use four **fixed** track radii, shared stroke width and `summarySweep_j = 2π × stat_j / maxValue`. Differences in ring radius are for distinguishing the four named statistics, **not** value encoding.
- A faint circular track on each row/ring represents 100%; the coloured part communicates the measured fraction. The deck and chart caption say **arc sweep**, never area.

**Legend and framing:**
- On-canvas labels `MAX`, `UPPER Q`, `MEDIAN`, `MIN` show the four values, paired to the corresponding ring colours.
- The header over the main rings says `SUMMARY / ENCLOSED AREA` or `SUMMARY / ARC SWEEP`, according to mode. Individual marks are labelled `INDIVIDUAL DISCS` or `INDIVIDUAL ARCS`.
- No artificial full circles, centre dot or rings whose appearance is unrelated to the dataset. Identical values are allowed to make some summary outlines coincide.
- Maximum and tied maxima receive the available red/brick accent in all gallery finishes. The rest are darker/secondary with legible contrast.
- Tap the right-hand data cell to inspect the actual record. Optional labels appear only where space permits; dense cases rely on tapping.
- Shape family, manual size/contrast and unrelated colour mapping controls remain disabled in Circle Study.
- The source row values and summary computations are unchanged by changing Gallery Finish.

## What remains unchanged

- Legacy free-play / Hidden Miles / Cutout geometry and the old Patchwork, Orbit, Rhythm Ribbon and Minimal Blocks modes.
- Data Mosaic and Typographic Broadside encodings.
- Local CSV and public GitHub URL/commit import.
- Instant category re-filter and current sorting.
- Optional label content, auto-generated editable poster headline/deck/footer and PNG export.
- Stage 1 bounded text safe zones and open, lightweight Ink Study styling.

## Verified real-data example

`archive/projects/2026-09-david-bowie-track-distributions/data/bowie_track_distribution_rows.csv`, `album_title = David Bowie` (14 rows), `track_title` and `duration_seconds`.

- Total time: **2,353 seconds**, across 14 tracks.
- Maximum: **Silly Boy Blue, 234 seconds (3:54)**.
- Minimum: **Maid of Bond Street, 106 seconds (1:46)**.
- Summary rings (linear-interpolated percentiles, raw seconds): **max 234**, **upper quartile 195.5**, **median 168.5**, **min 106**. Displayed duration labels are 3:54, 3:16, 2:49 and 1:46 respectively.

- Stripe Study generates 14 groups of three proportional line strokes (42 strokes in the simulated canvas).
- Circle Study generates 14 data discs. Arc mode generates a full reference track and a proportional swept arc for each row.

Deterministic, original, source-based SVG design previews, **not deployed app screenshots**:

- [Bowie Stripe Study](previews/bauhaus-v4-bowie-stripe-study.svg)
- [Bowie Circle Study: disc area](previews/bauhaus-v4-bowie-circle-area.svg)
- [Bowie Circle Study: arc sweep](previews/bauhaus-v4-bowie-circle-arcs.svg)

## Typography system — pre-merge editorial QA

The poster now has one shared type hierarchy across **Data Mosaic, Typographic Broadside, Stripe Study and Circle Study**, independent of colour finish. Keep the data labels small, but avoid solving collisions by shrinking them below legibility.

| Text role | Canvas type | Rule |
|---|---|---|
| Headline | 42px preferred, fitting down to 30px | Up to two lines, confined to the top headline band |
| Explanation/deck | 16px preferred, fitting down to 14px | Up to two lines, below headline |
| Source | 12px | Up to two lines, entirely below plotted data |
| Small section headings | 11px bold | Same size for SUMMARY, INDIVIDUAL ARCS/DISCS and MAXIMUM |
| Summary statistic names | 11px bold | MAX / UPPER Q / MEDIAN / MIN are consistently aligned |
| Summary statistic values | 11px normal | Right-aligned against a common edge; source numbers unchanged |
| Data mark labels | 11px normal | Constant size in Mosaic, Broadside, Stripe and Circle |
| Featured maximum | Larger editorial type | The deliberate focal number, not an annotation |

**Fitting and omission:** All small labels are measured using Canvas font metrics at a fixed 11px size. A too-long label receives a width-safe ellipsis; no tiny 8–9px fallback. A label is omitted where the cell or row lacks the necessary height, preserving interactive tap-to-inspect for the full original name and numerical value. In dense 64-row layouts, individual labels are intentionally suppressed rather than drawn on top of one another. The Ring Summary key remains visible even when individual labels are suppressed.

**Contrast and consistency:** Normal data annotations are calm, not all bold. Section headings and key names are semantically distinct through weight rather than inconsistent size. The controlled source and title layout from Stage 1 remains in place, and the original free-play studio's typography is unchanged.

**Tests completed in the branch:** embedded JS syntax; actual Bowie CSV with 14 rows; 14 small labels each in Mosaic, Broadside, Stripe; 11px summary key and 11px individual labels in Circle, including area and arc modes; all Label / Value / Both / Index mappings; 64-row label suppression in Stripe and Circle; same dataset/source footer, category changes, PNG action and legacy Patchwork regression. Refreshed the three Bowie SVG design previews to match the small-label typography.

**Further visual gate:** Inspect rendered PNG output on mobile Safari and a desktop browser to confirm font weight, truncation, caption spacing and the four statistic labels remain readable. The automated Canvas tests verify draw operations, not real-device font rasterisation.

## Completed checks

- Embedded JavaScript syntax valid on the Stage 2 branch.
- Simulated Canvas/UI flow imported actual 275-row Bowie CSV, applied original album category, created new Stripe/Circle engines and switched between area/arc encodings without changing source data.
- Verified 14 measured marks for each composition, 42 decorative stripe strokes for the 14-row example, automatic text mode changes, gallery finish changes, full-data selection after filtering, optional labels, PNG generation control, category redrawing to a different album, and regression to old Patchwork.
- A separate imported site-analytics CSV (29 current rows at test execution) worked without remapping regressions.

## Further release checks (not yet completed)

- Run actual browser screenshot/pixel QA for every finish in all four current poster engines, ideally testing 1, 14, 24 and 64 rows.
- Numerically verify exported **stripe length ratios**, **disc area ratios**, **outline ring enclosed area ratios**, and **individual/summary arc sweeps** against their original values; inspect zeros, tied maxima and exactly equal summary statistics.
- Check dense labels, overlong headlines and provenance, clipping, selected colour/contrast and poster size.
- Test mobile Safari category selection, toggles, touch inspection and Save PNG on a real iPhone.
- Obtain explicit approval before merge/publish.
