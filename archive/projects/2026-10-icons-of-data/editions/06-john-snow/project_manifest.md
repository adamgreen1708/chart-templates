# Icons of Data — Edition 06: John Snow

**Started:** 12 October 2026
**Proposed headline:** The map that put a pump on trial
**Historic object:** John Snow, map of deaths from cholera around Broad Street and Golden Square, **1855 book edition** of *On the Mode of Communication of Cholera*, based on **1854 outbreak**. Specific image: **Wellcome L0063431**, CC BY 4.0 photographic reproduction.
**Status:** both modern charts approved and exact image files staged for full website review. Jekyll/Chrome desktop and mobile QA passed. No merge or Pages publication approval.

## Artefacts
- `content/snow_06_draft.md` — working manuscript with story and separately scoped method note.
- `content/snow_06_visual_plan.md` — historical original; data-true geographical reconstruction; four-part decoder.
- `research/snow_06_sources.md` — exact 1855 image rights/date, variant-map distinctions, pump-handle myth, dataset provenance.
- `data/Snow.deaths.csv` — source-preserving HistData 578 observations (local plot coords, NOT GPS).
- `data/Snow.pumps.csv` — 13 pump locations.
- `data/Snow.streets.csv` — 1241 vertex rows (528 separate street segments).
- `data/validation_summary.json` — independent row counts, schema and source SHAs; no statistical mortality-rate inference.
- `project_manifest.md` — approval gates.

## Visual rules
Stay in 1:1 square house typography, `#F3F4F6` background, black marks from Snow's historical style, restrained teal and red modern annotations, thin dividers, safe margins, documented source and alt text. Historical source must be authentic and explicitly licensed; no AI-generated fake original. Map uses appropriate cartographic equal-aspect coordinates and no fabricated geographic precision. No mortality rates or causal proof from density.

## Next
1. Author approves or edits concept, title and draft article.
2. Deterministically render original historical image (licensed), digitised map and distinct decoder; QA geometry, original-vs-reconstruction, typography and phone previews. Show actual graphics directly before any website publication.
3. On visual approval, stage the article plus Resources #06 on GitHub draft PR; Jekyll/build/desktop/mobile QA.
4. Explicit separate OK required to merge and deploy to GitHub Pages. Manual series, not scheduled.


## Visual review production — 12 October 2026
The author explicitly **approved the headline, working article and visual storyboard** and requested production of the three graphics. A verified authentic **Wellcome L0063431 1855 map** plus two **1920×1920** modern Coffeetableviz house-style figures are now staged strictly under the archive `qa/visuals/` for review, along with 600/390/320px thumbnails and SHA-256 manifests. Modern graphics use data-true map coordinates, 578 marks, 13 pumps and 528 street segments, and clearly distinguish counts from rates and illustration from source data. Original photo SHA-1 and CC BY 4.0 verified. See `content/snow_06_visual_review.md`. Successful render/QA: https://github.com/adamgreen1708/chart-templates/actions/runs/38303582365. Temporary workflow removed. **Nothing staged under `site/`; no image approval, website PR readiness, or merge authorisation.**


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
