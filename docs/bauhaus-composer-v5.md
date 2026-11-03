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

## 02 / Typographic Broadside — expressive type revision

Revised following user feedback that the previous Architectural/Diagonal options were too ordinary. The previous composition was essentially a large number beside a small bar-chart rail; the new poster integrates the data marks into the graphic construction and gives the original words and number most of the art region.

**Type Monument** (replaces the old Architectural Type):
- The actual largest value becomes a monumental typographic object. Its actual source label is split into high-contrast display lines; an actual record count provides a secondary text anchor.
- The 14 (or selected N) thin **upright measured stripes** form a graphic rhythmic roof, aligned from the same zero baseline. Each height is `172 × value / selected maximum`, within the fixed art region.
- A red (finish-defined) disc, overprinting, alignment rules and contrast are **unencoded editorial geometry**, expressly not a fictitious numerical category.
- The source label may be shortened only if even the fitted large font cannot fit the reserved composition, while the exact original remains inspectable in the source rows.

**Cut-up Type** (replaces the old Diagonal Type):
- The actual original source label is repeated at different scales and rotations, intersecting original red/blue/ochre planes. Huge numerical type gives the true maximum.
- A tilted **measured stripe field** is integrated into the letterforms: each stripe has a common origin line, identical rotation and length `236 × value / selected maximum`. The diagonal position and colour planes are graphic decisions, not numeric encodings.
- Every stripe remains interactive through the original source row, including automatic re-filtering when another category is selected.
- Make text dramatic, but keep the bounded headline/deck/source, correct hue contrast and a measurable stripe field.

**Both compositions:** the default small headline is now `TYPE / <metric>` rather than redundantly repeating `Largest: <source title>`. The deck identifies the actual maximum, exact formatted value, row count and which measure the stripes carry. Neither font size, glyph rotation, decorative circles nor block shapes encode quantity.

**QA:** the two Bowie previews and interactive canvas renderer were updated together. JS syntax and simulated tests pass for both modes: 14 upright data stripes in Monument and 14 diagonal data strokes in Cut-up, accurate 3:54 / Silly Boy Blue from the selected album; changing category to Space Oddity updates the maximum to 9:36 / Cygnet Committee. Original free-play/Patchwork still renders.

**Review gate:** compare the two revised poster images with the uploaded reference artworks for boldness, asymmetry and typography. The two saved SVGs are independent data-derived concept previews, not captures from the hosted canvas. Real mobile/browser PNG QA remains outstanding.

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

Safe bands (canvas coordinates): masthead 35–105, headline 110–203, deck 211–275, artwork 285–835, footer 849–915. Full source text remains editable; printed overflow is ellipsised within band limits. If a mark label cannot fit it may be omitted, but interactive inspection must still provide original values. Circle min/max keys can also be tapped, including for zero-valued records. All-zero datasets remain valid; they produce no positive-area marks and a clear status message rather than fabricated geometry.

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
