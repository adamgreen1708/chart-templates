# Icons of Data — Edition 06: John Snow

**Started:** 12 October 2026
**Proposed headline:** The map that put a pump on trial
**Historic object:** John Snow, map of deaths from cholera around Broad Street and Golden Square, **1855 book edition** of *On the Mode of Communication of Cholera*, based on **1854 outbreak**. Specific image: **Wellcome L0063431**, CC BY 4.0 photographic reproduction.
**Status:** concept/research kickoff; 350–400-word conversational draft and three-visual storyboard. No renderings, no site posts, no Resources edits, no merged PR/Pages publication.

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
