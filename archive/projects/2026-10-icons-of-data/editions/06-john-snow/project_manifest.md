# Icons of Data — Edition 06: John Snow

**Started:** 12 October 2026
**Proposed headline:** The map that put a pump on trial
**Historic object:** John Snow, map of deaths from cholera around Broad Street and Golden Square, **1855 book edition** of *On the Mode of Communication of Cholera*, based on **1854 outbreak**. Specific image: **Wellcome L0063431**, CC BY 4.0 photographic reproduction.
**Status:** manuscript and storyboard approved; original 1855 historical map and two 1920px graphics rendered and stored in the archive for **image review**; no site post, Resources edits or publication approval.

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
