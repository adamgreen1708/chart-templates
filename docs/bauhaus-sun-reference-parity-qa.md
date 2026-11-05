# Sun Stripe — reference SVG versus live Canvas parity (November 2026)

## Issue

The approved [PR #186 Sun Stripe SVG](previews/bauhaus-stripe-v3-sun.svg) was **hand-built as a static design preview**, not exported from the interactive Canvas. It was presented as a design reference but was *not* a test of the visible default Studio experience. A successful merge/deployment did not guarantee the same data, labels or editorial wording on-screen.

Two verified causes of mismatch:

- The Studio starts with **illustrative Jan–Dec values**. When the existing Bowie GitHub preset is used, its `filterDefaultFirst` selection is **David Bowie**, the **first** of 26 source albums, **not Aladdin Sane** (sixth category, zero-based index 5), which is the 10-track source fixture behind the approved SVG.
- The SVG uses the exact headline **“Track duration / 10 stripes”** and short deck **“10 observations · stripe height scales with duration; min/max shown by circle area”**. Until this correction, the interactive renderer auto-generated **“Duration seconds / 10 stripes”** and used “Duration seconds” in the deck, even with identical Bowie data.

## Correction

- Added an explicit **opt-in reference link**:
  `https://coffeetableviz.com/resources/bauhaus-art-studio/?example=aladdin-sun`
- It loads the **real repository CSV** via the Studio's existing public GitHub importer, selects label `track_title`, numeric value `duration_seconds`, filter `album_title = Aladdin Sane`, 10 valid rows in source order, **Stripe + Sun**, Gallery Paper finish, and turns on original track-name labels.
- Only the Sun/Duration-seconds automatic editorial title/deck is changed to match the approved SVG text. It does **not** change metric values, circle areas, bar height, colour palette, user-edited headline/deck, or the copy for Flow Snake, Classic or other poster families.
- The URL query is accepted only when exactly `example=aladdin-sun`. A plain URL starts normally and is **not** silently switched to Bowie data. No dataset content is inserted into a share URL; the browser fetches a public CSV.
- Changed the GitHub importer to resolve a named existing category with an explicit `filterValue` preference. Other curated presets keep their previous `filterDefaultFirst` behaviour. The `loadGithub` helper now reports success to the one-shot reference loader.
- The preset draws through the **actual live `renderPosterV3` → `renderStripeSun`** path, not a separate special-purpose visual renderer. It does not add another artistically authored SVG to the app.

## Verification and known limitations

- JavaScript compiles and the exact reference URL path was simulated with the full Studio event handlers and a Canvas mock using the official source CSV. It made **one GitHub CSV request**, selected category index **5 = Aladdin Sane**, the `duration_seconds` metric and **10 rows**; `Show labels` was on.
- Rendered editorial content matched the approved SVG: **“Track duration / 10 stripes”** and the exact short deck; the source footer identified `bowie_track_distribution_rows.csv` and `album_title = Aladdin Sane`. 10 source-aligned bar columns and one vertical label per track were emitted in Canvas drawing operations. The data-driven min/max circle continues to obey the source values: 181 seconds and 315 seconds.
- `applyImported()` itself refreshes Canvas, so the reference loader deliberately avoids a second redundant render.
- The source footer contains the Studio's truthful extra chart-family suffix (`· stripe study`) which the static SVG omits. The static SVG also includes an additional design-preview disclaimer line. These are small copy differences, and the preview must not be misrepresented as an actual exported Canvas image.
- Browser/network limitations prevented a pixel-perfect comparison of a deployed Safari/Chromium PNG. After merge, test the reference URL on iPhone Safari and export its 960 × 960 PNG, compare with SVG for visual safety, labels, text, colours and circle position.

**Do not merge until reviewed.** This is a parity and testability improvement, not a replacement of the main Stripe Study data-art workflow.
