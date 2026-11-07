# Render and phone-size QA — superhero colour pilot

**Date:** 7 November 2026  
**Repository:** `adamgreen1708/chart-templates`  
**Status:** **layout review passed**, **scientific/data-source validation still open**, **not publication approved**.

## Actual workflow executions
- [Initial render](https://github.com/adamgreen1708/chart-templates/actions/runs/42418624492) passed mechanically but failed actual-pixel QA: title/subtitle overlaps; chart 2 unsafe left labels; chart 3 clipped names and all-blue dots.
- [Corrected render](https://github.com/adamgreen1708/chart-templates/actions/runs/42418816820) resolved collisions, clipping, and hue colours via per-row scatter highlights.
- [Final copy/layout render](https://github.com/adamgreen1708/chart-templates/actions/runs/42419170546) passed.
- [Latest exact phone-preview QA](https://github.com/adamgreen1708/chart-templates/actions/runs/42419236978) passed automated 1600px size, grey background and significant-ink 7% outer margin checks; the actual resized 320px and 390px PNGs were visually inspected in chat.

## Latest native-resolution outputs
- `output/superhero_01_hue_skew.png`
- `output/superhero_02_marvel_dc_primary.png`
- `output/superhero_03_costume_rebels.png`

## Final rendered phone previews
- `output/qa/superhero_01_hue_skew_320.png`, `output/qa/superhero_01_hue_skew_390.png`
- `output/qa/superhero_02_marvel_dc_primary_320.png`, `output/qa/superhero_02_marvel_dc_primary_390.png`
- `output/qa/superhero_03_costume_rebels_320.png`, `output/qa/superhero_03_costume_rebels_390.png`

## Reproducibility & renderer lessons
- Files rendered through **GitHub** `.github/workflows/render-archived-project.yml`, which regenerates the derived CSV views using `scripts/build_chart_views.py`, copies each `config/*.py` to the shared config slot and executes `src/render_538.py`.
- All three use approved **`render_profile="social_square"`**, 8x8 inches, DPI 200; source PNGs are 1600px square on `#F3F4F6` throughout.
- One-line titles are used to avoid collisions with the fixed house subtitle anchor. Titles/axis captions shortened for phone use; chart 2 has extra left margin for group labels.
- **Data-driven hue markers** in chart 3 use `scatter`, not `dot`, because the current `dot` path does not apply per-row highlight colours. This is a potential reusable renderer improvement for later, not an excuse to bypass the locked renderer. No `/src` modifications were made.
- Chart 3 uses a documented chart-specific left-margin and 15pt tick-label override to keep names and colour words legible within the square.
- `scripts/qa_phone.py` is reusable for this archive: requires Pillow. Automated margins cannot alone prove copy legibility, so we also inspected native, 390px and 320px images manually.

## Outstanding publication gates
1. **Critical:** independently visually confirm the 24 exact comic-era costume references and adjudicate ambiguous dominant hues; all 24 remain provisional in the seed CSV.
2. Strengthen sample definition or keep all comparative language explicitly limited to these 24 purposefully selected examples.
3. Adam reviews and approves the three rendered charts and editorial draft; only then prepare feature art, Jekyll files, site assets and separate publication PR.
4. Do not use `publish_asset_map.csv` here: these chart PNGs are for review only, not live site assets.
