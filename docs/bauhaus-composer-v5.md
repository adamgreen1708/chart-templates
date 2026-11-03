# Bauhaus Poster Composer v5 — four agreed compositions

**Status:** Feature branch for review. Source of design decisions: the four-style user review and implementation brief in the Charting template conversation, November 2026. This document supersedes the v4 *Circle Study* specification wherever that earlier document mentions medians, quartiles, decorative central rings or the separate right-hand matrix. Do not directly merge or publish without approval.

**Website:** `site/resources/bauhaus-art-studio/index.html`. Existing browser-local CSV and public GitHub CSV import, live category selection, sorting, editorial controls, tap-to-inspect and 960×960 canvas export are retained. The free-play, Hidden Miles, Patchwork, Orbit and Rhythm Ribbon engines remain available.

## Composition vs finish

**Composition** decides the mathematical mapping and editorial structure. **Gallery Paper / Colour Study / Ink Study / Studio Original** decide colour and graphic treatment. Colour-only variations must not create redundant composition buttons. The drawing is original and inspired by user-supplied Bauhaus poster references rather than copying an existing commercial work.

## 01 / Data Mosaic

Keep the existing deterministic proportional binary treemap and palette rules.

- On **Label + Value**, line 1 is the original source label; line 2 is the original value as displayed, including duration formatting where relevant.
- Both lines use **11px** regular-weight type, independent width checks and safe left padding.
- Source labels may be shortened with an ellipsis. **Numeric values are never truncated.** If there is not enough space for the complete number or two lines, that specific printed value/label is omitted. The full row remains available on tap.
- No change to the underlying outer rectangle area: `area / total mosaic area = positive row value / total positive plotted values`. Gaps and occasional ornamental arcs are not additional measures.

## 02 / Typographic Broadside

Replace the previous thick hero band and conventional bar-chart treatment with two editable compositions.

- **Architectural Type:** large maximum number, oversized actual source label, vertical structural rule and small column of measured marks.
- **Diagonal Type:** original source label appears in large rotated/angled type with the actual maximum as a second focal point. Thin rules and counts establish an original modernist editorial hierarchy.
- Font size, rotation, counts and geometric scaffolding are *not* numerical encodings. The **mini bars** remain the quantitative evidence: length `= source value / displayed maximum × common available width` with a shared zero baseline; tied maxima retain the same scale and highlight.
- The maximum and source label are determined entirely from the selected mapped numeric field. Long words are fitted inside the art region; headlines, deck and footer retain the common text-safe bands.
- Show optional small index/value annotations only where row height permits. Tap a mini-bar row for its complete label and numeric value.

## 03 / Stripe Study

Three choices, of which the first two are the new creative modes:

1. **Stripe + Sun** (default). Every vertical stripe starts at a shared bottom baseline and its height is proportional to `value / maximum`. The red filled disc area, relative to the largest outlined reference disc, represents `actual minimum / maximum`. This is a real source-derived minimum, **not an arbitrary background circle**.
2. **Flow Lines.** Each original data row has a different elliptical U-shaped path, but **every full path is exactly 760 canvas units long** (within floating-point precision). The coloured portion has length `760 × value / maximum`. Straight-leg lengths are solved by subtracting a numerically integrated half-ellipse length from the constant total. The bend and path positions are aesthetic; the measured coloured length is the quantity.
3. **Classic** remains an accessible fallback for the previous straight horizontal stripes.

Flow colours use the currently selected finish. Where the category-colour rule and a source category field are explicitly mapped, Flow can colour paths by that actual category; otherwise colours are purely a maximum highlight and finish. The colour rule and source-category field are enabled for Flow but disabled where they would not encode anything.

**Interaction:** Sun stripes have per-column inspection. Flow lines have nearest-polyline inspection using the original path coordinates. Labels remain 11px and are omitted on dense layouts, rather than compressed.

## 04 / Circle Study

Two minimal, print-like concentric compositions, with a separate **scope** selector:

- **Concentric Area:** a circle's entire enclosed area is proportional to its original source value, using `radius = rMax × sqrt(value / maximum)`. For overlapping filled circles the visible colour ring/annulus is *not* itself the measurement. The largest disc is drawn first, then progressively smaller measured discs.
- **Concentric Arcs:** every track has an explicitly fixed radius and equal stroke width; the **angular sweep**, not the ring radius, represents `2π × value / maximum`. Faint tracks show the full 100% reference.
- **Record scope** (default): use individual records from the current filter/sort. **Maximum 16 visible records** for a legible concentric composition. If more than 16 exist, the canvas explicitly says **16 of N displayed; first 16 in current sorted order**. The source file and existing first-64 import disclosure remain intact.
- **Range scope:** show **only the actual minimum and maximum** from *all selected rows*. If the values are identical, the area composition has a single identical-size ring/disc with an explanatory min/max key; do not fabricate a difference.
- **Explicitly no median, upper quartile or any other unrequested statistical summary.** The key gives actual maximum and minimum values drawn from the selected scope. No decorative centre rings whose appearance could be mistaken for measurements.
- Measured circle/arc geometry uses the selected source data, with source values inspectable by radial/touch hit testing. Labels live in a small unobtrusive key, not cluttered inside the rings.

## Shared typography and visual QA

Canvas is **960 × 960**. Headline preferably 42px, shrinking to at least 30px when needed; deck 16px preferred (floor 14px); source 12px; section and mark labels 11px, with appropriate semibold/regular hierarchy.

Safe bands (canvas coordinates): masthead 35–105, headline 110–203, deck 211–275, artwork 285–835, footer 849–915. Full source text remains editable; printed overflow is ellipsised within band limits. If a mark label cannot fit it may be omitted, but interactive inspection must still provide original values.

## Real-data regression fixture and previews

Official repository CSV: `archive/projects/2026-09-david-bowie-track-distributions/data/bowie_track_distribution_rows.csv`; filter `album_title = David Bowie`; label `track_title`; value `duration_seconds`.

- **14 tracks**, **2,353 seconds** total, **maximum 234 seconds / 3:54** (*Silly Boy Blue*), **minimum 106 seconds / 1:46** (*Maid of Bond Street*).
- Use the same source across each composition so style differences can be judged separately from the data.
- Real-data, deterministic SVG concept previews are stored in `docs/previews/`:
  - [Data Mosaic, two-line labels](previews/bauhaus-v5-mosaic-two-line.svg)
  - [Broadside, Architectural Type](previews/bauhaus-v5-broadside-architectural.svg)
  - [Broadside, Diagonal Type](previews/bauhaus-v5-broadside-diagonal.svg)
  - [Stripe + Sun](previews/bauhaus-v5-stripe-sun.svg)
  - [Flow Lines](previews/bauhaus-v5-stripe-flow.svg)
  - [Circle Area](previews/bauhaus-v5-circle-area.svg)
  - [Circle Arcs](previews/bauhaus-v5-circle-arcs.svg)

These SVGs are **independent vector design previews**, not screenshots captured from the hosted canvas renderer. Do not use them as evidence of final browser pixel QA.

## Checks performed

- Embedded JavaScript syntax compiled after each stage of editing.
- Simulated DOM/Canvas imported the real 275-row Bowie CSV, filtered to 14, switched among all four composition families and their options, exercised the label-content controls, live category changes, source notes and PNG preview action. Existing Patchwork still renders and a separate `site_analytics_daily.csv` import still works.
- Original Mosaic label/value two-line output confirmed; numerical value is not ellipsised.
- The Flow path solver returned exactly **760** length to floating point precision for **1, 8, 14, 24 and 64** records (maximum deviation below `5e-13` canvas units). Flow extremes stay within the drawing band.
- Bowie minimum/maximum proportional Sun-circle area ratio: `106/234 = 0.452991…`. Filled Circle areas map to `value/max` using square-root radius; arc sweep maps to `value/max`.
- Tested the Circle Study 16-record visual cap and on-canvas disclosure when 64 rows are selected.
- No source-data files, site posts, analytics/CI pipelines or chart renderer code outside the Bauhaus Studio have been changed.

## Mandatory remaining review before production

- Inspect **actual exported PNG pixels** in a real desktop browser and mobile Safari: print-safe margins, rotated headline clipping, long source labels, type contrast, Mosaic two-line fit, line density and colour rendering. Simulated Canvas drawing is not real-device QA.
- Exercise zeros, near-equal values, all-tied maxima, one row, 8, 14, 24 and 64 records. In particular check Circle Area when values are identical, and whether cropped/ring-visibility behaviour is clearly explained.
- Verify full row inspection works with mobile touches on curved paths and concentric outlines.
- Confirm source-category mapping really updates Flow colours; ensure unrelated colours never imply an extra metric.
- Explicit approval is required before merging the branch into `main`.
