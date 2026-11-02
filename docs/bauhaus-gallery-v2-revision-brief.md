# Bauhaus Gallery v2 — revision brief

**Status:** design and engineering brief only. No functional renderer changes in this document. Approval of this brief is not approval to merge or publish. Follow the site's established PR and real-data QA workflow.

**Origin:** feedback on the Gallery Paper / Ink Study previews in PR #179, and general style inspiration from Gallerix's Bauhaus collection. Borrow colour, linework, geometry, negative space and hierarchy **without reproducing specific commercial images**.

## Scope and sequence

### P0 — Gallery Paper typography / clipping (must fix before merging the visual finish)

**Problem:** long auto-generated headlines, explanatory captions and source lines run into adjacent elements or canvas bounds. This fails the editorial intent, especially on iPhone screens.

**Implementation contract**
- Canvas remains a 960 × 960 square. Use deterministic text measurement (`ctx.measureText`) and a single layout engine with disjoint, documented safe regions:
  - masthead and top line: y=35–105
  - headline: y=112–202 (up to 2 lines)
  - explanation/deck: y=217–272 (up to 2 lines)
  - measured data artwork: y=292–826
  - source/footer: y=844–928 (up to 2 lines)
- Keep left/right safe margins >=80px for every text block. Never draw into another reserved band.
- Headline: start near 42 px; wrap at word boundaries; shrink only to a readable minimum (~30 px); do not solve collisions by squeezing to 10 px. Long single tokens need character-level fallback.
- Deck: 15–18 px with sensible line-height, maximum 2 lines.
- Footer: 12–14 px, maximum 2 lines, properly wrapped. Keep provenance truthful, including first-64 notice.
- If content still does not fit, use a clear ellipsis **in the poster only**, retaining the complete editable text in controls. Do not silently shorten source facts in the data.
- If the user supplies a custom headline or source line, preserve it across changes of finish; changing datasets continues to reset stale captions as currently specified.
- Rendering must be idempotent: switching Paper ↔ Ink ↔ original finishes, switching datasets, or saving PNG must not introduce extra line breaks or stale text.

**Acceptance:** no clipping or overlap at lengths of 5, 30, 65 and 90 characters for headlines and up to 220 characters for deck/source; check all palettes and 320–430 CSS-pixel mobile screens. Actual exported PNGs must be inspected.

### P1 — Ink Study: remove the clunky full-width dark hero band

**Problem:** the large `fillRect(82,288,796,164)` slab in Typographic Broadside dominates the ink finish. It reads as a dashboard banner rather than an elegant graphic print.

**Revised art direction**
- **Ink Study only:** replace this with open pale-stone paper, a large black/dark-ink hero figure at left and a compact red annotation/rule; no large black filled banner.
- Reserve the right-hand area for a **thin-line geometric study** (outlined circles/arcs and a few black construction strokes). Use clear, deliberate asymmetry and quiet space.
- Supporting observations appear as black slender horizontal stripes rather than chunky coloured bars; a red rule highlights all tied maxima.
- Ensure the reading order remains: highlighted value → source label → proportional detail marks → provenance.
- Other Poster Finishes may retain their existing hero treatments initially, but share the new safe text layout.
- Do not let red ornamental arcs or black stripes appear to represent additional measures unless documented.

**Acceptance:** no filled dark rectangle occupying >15% of canvas, all actual values can still be inspected, and the same source rows produce the same zero-based lengths.

### P2 — New engine: Stripe Study (not simply a palette variant)

**Composition:** black horizontal stripes form the main data marks on pale paper, with one restrained red accent and optional ochre / linework. Whitespace, stripe length and spacing form the graphic rhythm; typography is part of the poster, not a standard chart title.

**Honest data encoding**
- One observation (or an explicitly labelled group of parallel strokes) per row.
- **Stripe length = original non-negative value / maximum displayed value × max available stripe width**; clear shared origin (zero) and constant width-scale across rows.
- Stripe thickness is constant unless the user *explicitly maps a second field* in a future release. Number of sub-stripes must not quietly imply another measure.
- Colour (black vs red) may highlight the maximum, a user-selected record or an explicitly mapped category; decorate with fine-line circles only if unambiguously ornamental.
- Rows may be sorted high–low, low–high or kept in source order. Label/Value/Both/Index and tap inspection remain supported.
- Encourage filtered selections of ~8–24 observations; disclose first-64 cut-off if triggered. Avoid pretending dense 64-row posters are legible.

### P3 — New engine: Circle Study

**Composition:** dominant circle, smaller discs and fine concentric outlines integrated with large editorial type. This is a *new* measured circle layout, not the existing evenly spaced circle grid or old orbit mode.

**Honest data encoding**
- Default: **filled disc area ∝ value** (`radius ∝ sqrt(value/max)`), not radius proportional to value. Use a fixed maximum circle area so discs never run into headlines/footer.
- Composition should emphasise the actual maximum (or total if clearly labelled), with supporting discs for the other selected rows. Position and rotation are **decorative** unless an explicit mapping is added.
- Optional alternate **arc study** can encode `arc sweep ∝ value/max` with constant radius and line width. Label this as proportional sweep, **not circle area**.
- Do not mix angular sweep and area scaling without an on-poster legend. No fabricated categories, no ambiguous density encoding.
- Tap marks to inspect exact source values. Show optional labels only where collision and reserved-band tests pass.
- Add a compact explanatory line chosen from the active encoding (e.g., “Disc area represents duration” or “Arc sweep relative to the maximum”).

## Controls and UX

- Gallery Paper, Colour Study, Ink Study and Studio Original remain **finishes**. Do not present a finish as a new numeric chart type.
- Data Mosaic, Typographic Broadside, **Stripe Study**, **Circle Study** are **different poster compositions**. Make their selection primary and finishes secondary.
- Render changes immediately on layout/finish/category selection. Keep CSV upload and pinned/public GitHub URLs intact; category changes continue to re-filter live.
- Keep editable headline, explanation and source; include a **Restore automatic text** action. Auto captions must name the *actual* encoding currently used.
- Print-square PNG should use the full 960 × 960 output and preserve margins. No image generation, external assets, proprietary fonts or Gallerix artwork is required for the live renderer.

## Verification / release gates

1. **Real data:** use the existing official GitHub Bowie track CSV, plus a short UK-total-type dataset with near-equal numbers. Keep exact source values; no fabricated analytical claims.
2. **Visual differentiation:** the *same data* should produce four recognisably different posters. Compare 960 × 960 PNGs side by side and verify the graphic hierarchy and lack of template-like slabs.
3. **Math:** verify stripe lengths and arc sweeps against original values, disc **areas** against proportions, Mosaic original tile bounding-box areas against value shares. Include zero, equal, tiny, outlier and tied maxima cases.
4. **Readability:** 1, 8, 14, 24 and 64 observations; all 4 label-content options; label hiding; short and long source names; safe margins and no clipped content.
5. **Regression:** current free-play Cutout / Hidden Miles, existing Patchwork/Orbit/Ribbon, CSV/GitHub links, category auto-redraw, value inspection and PNG export unchanged.
6. **Device:** actual Safari on iPhone to validate dropdowns, touch inspection, layout, PNG saving and preview visibility. Do not equate simulated Canvas tests with this.
7. **Approval:** keep changes on a branch, show finished square posters for visual review and get explicit approval before merging.

## Suggested release split

- **PR #179 revision:** ship P0 (Paper copy-fit) and P1 (Ink redesign); retain the existing three gallery palettes.
- **Follow-up Poster Composer PR:** ship P2 Stripe Study + P3 Circle Study as separately tested data encodings. This keeps a purely stylistic fix from becoming an unchecked feature expansion.

**Definition of done:** poster looks deliberate enough to frame, claims match the data, and no text or geometry clips in final export.
