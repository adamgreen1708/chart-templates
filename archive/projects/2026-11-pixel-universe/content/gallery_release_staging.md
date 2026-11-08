# Pixel Universe gallery — Phase B release staging

**Status:** draft for preview and review, **not published**. This is a separate PR stacked on the 12-icon creative PR #199 (itself stacked on #198). Neither this page nor the studio is merged into main in this step.

## What ships when approved

- Jekyll resource page at `site/resources/pixel-universe/index.html`, permalink `/resources/pixel-universe/`.
- Single generated Jekyll dataset `site/_data/pixel_universe.yml`: **12 original 16×16 characters**, DC/Marvel and Hero/Villain labels, unchanged 256-character pixel codes, version-specific published qualitative colour records, precise HEX values from current Pixel Art Studio.
- 12 source-faithful static SVG previews under `site/assets/pixel-universe/icons/` and two 1200×1200 mosaic assets copied exactly from their verified, archived SVG generator outputs.
- No additional JS renderer: previews are **static generated SVG**, and each **Open & remix** link opens the exact same 256-character code using Pixel Art Studio's `#size=16&art=...` format. No new storage keys, alternate URL format or Zoo interference.
- Responsive 3-column desktop / 2-column tablet / 1-column narrow-phone card gallery, with explicit `320px/390px` inspection still required.
- Resources directory card linking the gallery, plus correction of the already-stale old "Twelve colours" reference to the currently live 15 paint colours.
- Source/qualitative caveats, unofficial fan-inspired art disclaimer, explicit link to published *Who wears the hero colours?* article.

## Deterministic generation and tests

Generator: `archive/projects/2026-11-pixel-universe/scripts/build_pixel_universe_gallery.py`

```sh
python archive/projects/2026-11-pixel-universe/scripts/build_pixel_universe_gallery.py --check
python -m pytest tests/test_pixel_universe_gallery.py -q
```

The generator reads the **published 24-row superhero seed and source review**, **12-row original artwork CSV**, two approved prototype codes, and current `site/assets/js/pixel-art-builder.js` palette. It derives YAML, previews and mosaic site assets with explicit equality checks against the archived approved mosaics.

## Important release protocol

- Publication of the gallery has not been authorised merely by generating this preview branch. Do not merge to `main` before Adam approves.
- Keep PR #194's unmerged research completely separate.
- Validate the actual GitHub Pages Jekyll build, mobile layout and user-facing edit links before merge.
- The feature/editorial sequel is a distinct follow-on PR after gallery approval; do not silently publish an article.
- The original qualitative dataset provides **colour names**, not fabric-colour coverage, image mask ratios, audience-recognition accuracy or actual measurements of comic costumes.
