# Icons of Data #06 — John Snow visual review

**Edition:** 06 · *The map that put a pump on trial*
**Status:** author approved both modern visuals. Exactly approved JPG/PNG bytes, full Jekyll article and Resources #06 entry now staged on PR #115; browser QA passed. **No merge or Pages publication approval yet.**

## Review figures

1. **Authentic original — John Snow, 1855 book edition**
   - `qa/visuals/01_snow_original_wellcome_L0063431_review.jpg` (1600 × 1534 pixels).
   - Exact digitised photographic object: Wellcome Collection **L0063431**, original full image 5064 × 4856, SHA-1 `3cb5210cd4b7fd3c1cc4426ca01bf9b96b6cf7c8`.
   - **CC BY 4.0** for this particular digital photograph, credited Wellcome Collection; metadata source: https://commons.wikimedia.org/wiki/File:Map_showing_deaths_from_Cholera_in_Broad_Street..._Wellcome_L0063431.jpg
   - Review image SHA-256 `025cfcef1e21220ca82eb0b703d65494bd8670962934b3514c173764e172d166`. Downsampled proportionally, no crop or colour edit. Link the original work, specific image licence and any changes in website caption.

2. **Chart 02 — The pattern, mapped**
   - `qa/visuals/02_the_pattern_mapped.png` **1920 × 1920**, SHA-256 `d1add220b9e69e44b2392e7b0f23ea1af5bff1dbecebd1180f41c0e5fd4f16bd`.
   - Deterministic source: `scripts/render_snow_review.py` and three pinned, unchanged `HistData` CSVs. Includes 578 digitised **fatal attack display marks**, 13 water pumps, 528 street polyline groups from 1241 vertices; Broad St pump position explicitly source-verified.
   - Houses are symbolised by dark square marks instead of imitating the orientations of Snow's historical black bars. Broad Street pump uses a modern red diamond and other water pumps teal crosses (not source colours). Streets are plotted in the original map-relative x/y units with **equal aspect**, not GPS.
   - The bottom note explicitly warns: no at-risk-population denominators, no mortality rates and **578 is not the full outbreak death toll**.

3. **Chart 03 — Decode the Icon**
   - `qa/visuals/03_decode_the_icon.png` **1920 × 1920**, SHA-256 `458087d1fb8072e51963c67c5868c5baad0bc3dcc86b9edda1d55aea21bf8edb`.
   - Four genuinely distinct teaching panels: bars for fatal attacks; geographical proximity is not water use; counts vs rates with missing denominators; lack of individual dates plus the **8 September 1854** pump-handle removal after the outbreak was already declining.
   - Panel 01 and panel 03 numbers are explicitly **schematic examples**, not newly invented historical observations. No fictional curve or fabricated household census counts.

## Styling
Reuses author-approved Icons of Data house style (#04 Nightingale, #05 Du Bois): square 1920px output, **#F3F4F6** canvas, bold black claim-based titles, restrained #1F8FA8 / #C44E52 accents, thin dividers, original source footer, safe margins and label legibility. No new site CSS or shared renderer overrides.

## QA provenance
- Temporary GitHub Actions runner `https://github.com/adamgreen1708/chart-templates/actions/runs/38303582365` rendered final corrected version and independently validated output dimensions, SHA-256, table counts, image width and historical original SHA-1.
- Smaller **600/390/320px** thumbnails are also saved alongside each modern figure for mobile visual inspection; exact previews correspond to above PNGs.
- Renderer is edition-specific: correct for a historical *map with no data axes*, not a claim that generic `src/render_538.py` can produce a faithful map from line-segment vertices.
- These preview images are stored **only inside the edition archive** on the draft PR for author inspection. **Do not add to `site/assets` or publish yet.**

## Before publication
1. Author approve or request edits to these actual three images.
2. Stage exactly approved artwork and article/Jekyll Resources entry with proper image reuse metadata; do not substitute changed rasterisation without author re-check.
3. Perform Jekyll + Playwright screenshots at 1365px, 390px and 320px and verify alt text and captions.
4. Obtain **separate explicit permission** before merging to `main` and verifying Pages deployment.


## Exact visual approval and website staging — 12 October 2026
The user explicitly approved both modern **Chart 02** and **Chart 03**, after approving the editorial manuscript and title. Website article and Resources content are now staged **only on PR #115**. The historical original is source-verified Wellcome Collection **L0063431**, CC BY 4.0 and proportionally resized without crop/recolour. The original review image and both modern PNGs are **copied byte-for-byte** into `site/assets/icons-of-data/john-snow/`, **not rerendered**.

Image baselines (author-reviewed SHA-256, separately verified for source files and staged website copies):
- Historical review JPG: `025cfcef1e21220ca82eb0b703d65494bd8670962934b3514c173764e172d166`, 1600×1534, source image Wellcome L0063431 originally 5064×4856, source SHA-1 `3cb5210cd4b7fd3c1cc4426ca01bf9b96b6cf7c8`.
- Chart 02 `02_the_pattern_mapped.png`: `d1add220b9e69e44b2392e7b0f23ea1af5bff1dbecebd1180f41c0e5fd4f16bd`, 1920×1920.
- Chart 03 `03_decode_the_icon.png`: `458087d1fb8072e51963c67c5868c5baad0bc3dcc86b9edda1d55aea21bf8edb`, 1920×1920.

**Website files staged**
- `site/_posts/2026-10-12-the-map-that-put-a-pump-on-trial.md`; proposed permalink `/icons-of-data/john-snow-cholera-map/`. Includes all three figures, informative alt descriptions and fair historical licence/method notes.
- `site/assets/icons-of-data/john-snow/`: exactly approved three image bytes.
- `site/resources/icons-of-data/index.html`: **sixth story**, encoding fingerprint row, and a primary source note. Existing site CSS and all shared renderers left unchanged.
- QA screenshots: `qa/site/snow-article-desktop.png`, `snow-article-mobile.png`, `snow-article-narrow.png`, `snow-resources-mobile.png`, `snow-home-mobile.png`.

**Actual QA:** Jekyll/Chrome in [GitHub Actions run 38304702761](https://github.com/adamgreen1708/chart-templates/actions/runs/38304702761) passed for 1365px desktop, 390px mobile and 320px narrow mobile. All three images loaded at their original dimensions, descriptive alt text and Wellcome source/CC BY 4.0 link present, no horizontal overflow or title clipping, six Icons of Data story links verified, and home/latest card includes Snow article. Full-page mobile previews visually inspected; no obvious clipping or layout issue.

Temporary site QA workflow removed, no workflow/render/spec mutations remain. **PR #115 must not merge/publish until author sees and explicitly approves this complete website rendition**; user approval of Charts 02/03 does not authorise GitHub Pages deployment.
