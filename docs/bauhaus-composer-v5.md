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

## 03 / Stripe Study — approved v2 base, November 2026 v3 review

Version 3 is a proposed follow-up to **merged PR #185**, retaining all three measured compositions while addressing the subsequent four-part design review. The 960 × 960 browser Canvas, live CSV source mappings and source attribution remain the same. The user will review a new pull request before publication.

### Sun Stripe — vertical source labels
- Vertical stripe **height** remains `419 × current_value / max`, from the same y=800 horizontal zero baseline.
- The source record **labels now run vertically upwards alongside each individual bar**, not along the bottom. Labels use the existing Show labels control; this control is **enabled on entry** to Sun Stripe (and can be switched off later). Use 11px at ordinary spacing, 9px for narrower spacing; fit to at most 305px along the rotated text axis, shrink and ellipsise when necessary. On dense selections with less than 23px per bar, omit labels rather than crowding. Tapping a bar still yields the full source name.
- **The main editorial headline is restored horizontally above the explanatory deck** in the same safely fitted x=82 / y=111 heading band as Flow and Classic. Sun also **retains the small vertical title on the 57px back bar**; the two are complementary, not alternatives. Both honour the currently edited or auto-generated headline. The source-derived minimum-filled-area circle and maximum outline remain unchanged. The descriptive deck remains visible below the horizontal headline.
- [Review SVG](previews/bauhaus-stripe-v3-sun.svg)

### Flow Snake — extended, thinner, still measured correctly
- Keep the horizontal 44px labelled start and the S-shaped lines, with **exactly matched colour and thickness along each complete series**, including its right-hand measured segment.
- Expand the artistic S across the composition: nominal x≈266–846 and y≈297–749 for multiple observations, while keeping within the 82px/878px sides, y275 art top and y827 art bottom.
- Thin each continuous snake/measurement stroke from 5/3/2px to **3.2px** for ≤16 records, **2.1px** for 17–28, **1.5px** for 29+.
- The right-hand straight segment uses the **common y=342 zero baseline** and height `390 × original_value / max`. The curved portion is never interpreted as quantity. A subtle shared zero rule remains a legitimate scale reference, unlike the removed decorative top rule.
- Keep 11–9px safely fitted left-hand track labels (omitted for >15 records) and nearest-line tap inspection. Restore the **small explanatory deck line above the artwork**.
- [Review SVG](previews/bauhaus-stripe-v3-flow.svg)

### Classic — data-driven MIN/MAX circles
- Retain the stacked bars: each width is `696 × current_value / max` from x=163, with track name and exact value integrated into each bar where they fit.
- Replace the old decorative background disc with **two source-data-driven concentric circles behind the bars**. The large outer **MAX** reference circle has radius 205 and a visible outline. The smaller filled **MIN** circle has radius `205 × sqrt(min/max)`. The **complete enclosed-area ratio** is therefore exactly **min/max**. The background circle geometry updates when the selected metric, data filter or records change.
- A small `MAX value / MIN value · CIRCLE AREA ∝ VALUE` legend appears under the bars, above the source footer; the bar field still leads. For all-zero values, draw no area circle rather than inventing an area.
- Restore the **small explanatory deck line** above the artwork and update the default deck copy to describe the actual MIN/MAX circle encoding.
- [Review SVG](previews/bauhaus-stripe-v3-classic.svg)

### Shared release requirements
- The **automatic or user-edited explanatory/deck line is printed in all three styles**, bounded by `x=83, y=210, width=793, height=60`. It fits within one or two lines at 11–14px and cannot overlap the artwork starting at about y=275. It can be edited through the existing deck field.
- Preserve the headline safe margins, footer and actual source-value ratio; no decorative line at the masthead. No changes to Circle Study, Data Mosaic, Typographic Broadside, repository publishing workflows or the dataset.
- Validate actual source import, live metric/category changes, missing-value exclusions, long labels, mobile render and PNG export before merge.
- See [v3 QA results and outstanding device checks](bauhaus-stripe-v3-qa.md). The three source-data SVGs are **review illustrations**, not actual Canvas screenshots.

## 04 / Circle Study — concentric geometry with editorial record catalogue

The **geometric encodings stay unchanged**:

- **Concentric Area:** entire original circle area, not the visible coloured annulus, is proportional to the source value. Radius uses `rMax × sqrt(value / maximum)`.
- **Concentric Arcs:** fixed-radius concentric tracks with consistent stroke width; measured angular sweep is `2π × value / maximum`. Faint full tracks show 100%.
- **Records scope (default):** first 16 selected values in the current source/sort order are plotted. The artwork reorders those selected values **largest to smallest** for outer-to-inner ring alignment. Do not silently substitute other rows.
- **Range scope:** actual minimum and maximum from all selected rows, with both explicitly identified; if equal, preserve the truthful coincident geometry.
- No quartiles, median or fabricated summary rings.

**Editorial text refinement (November 2026):**

- Remove the former upper-left `RECORDS / SOURCE VALUES` and `FULL CIRCLE AREA / VALUE` labels. The deck already explains the mathematical mapping.
- Replace them with a **narrow original editorial data catalogue on the left**, aligned beside the measured circles on the right. For every ring/arc, show its order, source label and **full formatted numeric value**. The list is largest-to-smallest, matching the geometric ordering of the rings. Small colour ticks correspond to the actual measured layers.
- **Quiet, condensed catalogue styling:** the source label and numeric value remain legible **11px**, but the ordinal steps down to **10px** and labels/headings use muted ink. Rows use dynamic 18.5–24px baseline spacing depending on the number of records, centred around the circle's vertical midpoint. This keeps the circle dominant rather than visually competing with a tall table. Long original source labels safely ellipsise. Numeric values are never shortened. List rows are touch-inspectable, giving the complete original label and unrounded value.
- **Rebalanced composition:** the primary measured circle is the focal point, centred at **(646, 534)** with outer radius **196px** (8.3% wider than the earlier 181px study), still entirely within the reserved art area. The catalogue has its own narrow column and is **vertically centred against the circle**, not aligned above the circle's top. For 11 records its heading is at y=394 and rows run y=429–639 while the circle spans y=338–730. For 16 records the heading is at y≈360 and rows y≈395–673. Both keep the footer and MIN/MAX blocks clear.
- **Final balancing adjustment:** group the two MAX/MIN stat blocks **side by side directly below the left-hand catalogue**, not spread across the poster beneath the circle. The compact blocks occupy x=111–254 (MAX) and x=278–416 (MIN), leaving the focal circles on the right entirely unobstructed. The blocks use small **10px** headings, complete values up to **19px**, and source labels at **11px**. Their vertical position follows the last catalogue row (+24px), so both short and 16-record lists remain balanced. Both blocks remain tappable.
- When a 16-record display limit applies, the statistic headings say `MAX / SHOWN` and `MIN / SHOWN`, so they do not imply extrema across undisplayed rows. In Range scope, they remain source-wide extrema.
- Remove the in-art `11 OF 11 RECORDS DISPLAYED` line. The full source credit/footer carries `all N records shown`, `first 16 of N records shown`, or `source MIN/MAX from N valid rows` as appropriate. Existing exclusions and first-64 CSV import disclosures remain visible in provenance.
- The default deck uses normal readable words (e.g. `Whole-circle area represents Spotify streams · largest first`), avoiding special symbols that may render poorly in some fonts.
- Do not introduce a decorative list panel or recreate an existing commercial poster; borrow only the general narrow editorial typography and balanced graphic layout from the supplied reference.

**Accurate data and responsive QA:** see [the Circle Study editorial QA checklist](bauhaus-circle-editorial-qa.md) and the two data-grounded [Area](previews/bauhaus-circle-editorial-ziggy-area.svg) / [Arcs](previews/bauhaus-circle-editorial-ziggy-arcs.svg) previews. These previews are original vectors, not screenshots of the deployed renderer.

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
