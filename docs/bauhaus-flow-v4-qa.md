# Flow Snake v4 — aligned horizontal names and seamless measured ends

**Source of truth:** Bauhaus Studio Canvas renderer at `site/resources/bauhaus-art-studio/index.html`. Unmerged review branch; no direct changes to `main`.

## User design correction

The labels **must read horizontally**. “Aligned vertically” means that the **right-hand edges of the horizontal text** form a perfectly straight vertical column. The user did **not** request rotated / vertical lettering.

The source screenshot uses David Bowie's `Never Let Me Down` album with 11 tracks. In the source-backed preview, track names now have a common right edge x=264 at each original row's y position. A 2px gap separates each label from the coloured horizontal starting ledge, which begins at x=266 **on every row** and runs to its own S curve (initial upright x≈310–368). These lead-ins are decorative: their lengths do not encode data.

The previous endpoint returned upward to the zero line and then painted a separately stroked vertical measured segment. This caused visually inconsistent joins. The new second cubic curve ends at the exact `y=342` shared zero baseline with a vertical downward tangent, and the entire row draws in **one `ctx.beginPath` / one `ctx.stroke`**, including the measured endpoint at `y=342 + 390 × actual_value / maximum`. Palette colour, opacity and width remain identical across the entire continuous stroke.

## Source data and test cases

Repository CSV: `archive/projects/2026-09-david-bowie-track-distributions/data/bowie_track_distribution_rows.csv`. Use `track_title` and `duration_seconds`, filtering `album_title`:

- `Never Let Me Down`: 11 real tracks, minimum **233s**, maximum **346s** (`Zeroes`). All 11 titles displayed horizontally at 11px in the independent SVG preview.
- `Aladdin Sane`: 10 real tracks, minimum **181s**, maximum **315s** (`Time`). Updated the old v3 preview so it no longer depicts the superseded staggered labels and split bars.

## Checks and release gates

- JavaScript compiled successfully after renderer updates.
- Geometry calculated from the **actual current source data** for both albums and synthetic counts 1, 2, 8, 14, 15, 16, 24 and 64. Every horizontal ledge begins at x=266; the geometric endpoints meet the shared zero baseline x≈655–846, y=342.
- All measured vertical heights remain precisely `390 × source_value / actual_maximum`. No source values were changed, and the geometry of the decorative curves remains independent of the metric.
- The terminal sampled curve was refined to 64 segments; the final segment's horizontal deviation before joining the vertical measured portion is at most 0.204px across tested counts, with no upward backtracking/hairpin.
- Test the single Canvas stroke per record, visibility/legibility of the x=264 label column and full-record tap hit regions.
- Verify real iPhone Safari rendering and exported 960×960 PNG before final public release. Static SVG design previews are not browser screenshots; they are source-grounded geometrical comparisons.
- Scope: **Flow Snake only**. Sun Stripe, Classic bars, Circle Study, other poster modes, source footer and CSV selector logic are not changed.

## Review imagery

- [Never Let Me Down (11 tracks), matching screenshot album](previews/bauhaus-flow-v4-never-let-me-down.svg)
- [Aladdin Sane (10 tracks), corrected comparison](previews/bauhaus-stripe-v3-flow.svg)
