# Bauhaus Stripe Study v3 — release review and QA

**Basis:** main after merged PR #185. Proposed v3 feature branch for user approval; not published.

## Requested changes covered

1. **Sun Stripe**: labels moved away from the bottom. They rotate -90° and run upwards beside the source-value vertical bars. Small type, within the drawing's y=341..788 safe region and x=201..849; labels follow the original Show labels setting, now turned on by default when entering Sun via poster selector, layout selector or Stripe-style selector. User can turn them off again. The original vertical title back bar remains.
2. **Flow Snake**: extended to fill more of the poster while retaining source-value accuracy. The connector width is 3.2px for up to 16 rows, 2.1px for 17–28, and 1.5px for 29+. Its measured segment uses the **same stroke and palette colour**. The measured right-hand straight vertical bar length is `390 × value / maximum` from the shared y=342 baseline; S curves remain unencoded artistry.
3. **Classic**: replace decorative background circle with a source-derived **MAX outer reference circle and MIN inner filled circle**. `r_max=205` and `r_min=205 × sqrt(min/max)`; hence `area_min / area_max = min/max` by construction. Both values are also printed in a compact legend above the source footer. For max=0 no numeric area is fabricated.
4. **All Stripe studies**: restore the small explanatory/deck line from the actual or edited `editorCopy().deck`. Use the existing safely wrapped text helper at x=83, top=210, width=793, height=60, size 14 down to 11, 2 lines maximum. Sun headline stays vertical; Flow and Classic headline remains above the deck.

## Data fixture and numerical verification

Repository source: `archive/projects/2026-09-david-bowie-track-distributions/data/bowie_track_distribution_rows.csv`.

- Filter: `album_title = Aladdin Sane`; label: `track_title`; metric: `duration_seconds`.
- Exactly **10 observed tracks**, source maximum **Time 315 seconds (5:15)**, source minimum **Cracked Actor 181 seconds (3:01)**.
- JavaScript compiled following edit of single-file Bauhaus Art Studio.
- In a simulated Canvas draw with the real source values: **Sun** produced 10 vertical measured bars, 10 vertically rotated track labels beside the bars, plus its vertical back-bar headline; no bottom row labels.
- **Flow** produced 10 coloured connectors and 10 measured straight right-hand segments. Both parts use the same colour, opacity and 3.2px width. Their measured heights (from the common 342px baseline) equal `390 × current_value / 315`.
- **Classic** produced 10 proportional bars, two filled circles and one outer stroke. Verified `(r_min/r_max)^2 = 181/315`, within floating-point error; source-derived MAX/MIN legend present.
- **Flow geometry** for selected counts 1, 2, 8, 10, 16, 24, 64: all line coordinates stayed within x≈266–846, y≈297–749 for multiple rows, respecting chart safe margins.
- Scoped exclusively to Bauhaus HTML, this spec/QA, and three new SVG source-data design previews. Existing other chart families remain intact.

## Remaining visual QA

- Real iPhone Safari portrait and desktop browser: vertical Sun label spacing for 10, 16, 24 rows; long mixed-case titles, angled text clipping; verify label text does not overlap other bars. Check labels are enabled on Sun entry, and user can turn Show labels off.
- Check deck is actually visible on all three charts and on both one-line and two-line custom explanatory text, without collision with header or artwork.
- Flow Snake: check enlarged S bends avoid deck and source attribution, and closely spaced segments remain legible on mobile; ensure continuous connector/measurement style even with category colouring and all palette finishes.
- Classic: assess the **source-derived min/max circles visually behind the bars**; check contrast, rare max=min and zero/min=0 cases, legend/footer clearance.
- Test CSV GitHub import, live metric/album/category selection, missing Spotify-streams values, tap inspection, and actual 960×960 PNG export. The independent SVG previews are not screenshots of this browser-rendered Canvas.

## Side-by-side SVG concepts

- [Sun Stripe with vertical track labels](previews/bauhaus-stripe-v3-sun.svg)
- [Wider and finer measured Flow Snake](previews/bauhaus-stripe-v3-flow.svg)
- [Classic Bars with accurate MIN/MAX circles](previews/bauhaus-stripe-v3-classic.svg)

**Approval gate:** do not merge into main until user reviews and confirms.
