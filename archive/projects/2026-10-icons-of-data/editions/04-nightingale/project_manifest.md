# Icons of Data — Edition 04: Florence Nightingale
**Started:** 10 October 2026
**Working title:** The chart that made disease impossible to ignore
**Artefact:** Florence Nightingale, *Diagram of the Causes of Mortality in the Army in the East*, Wellcome digitised **1858** plate L0041105.
**Status:** working article, three-visual storyboard, source/data audit. No generated images, Jekyll post, Resources update or website publication. Await author review.

## Files
- `content/nightingale_04_draft.md` — conversational UK-English article with three figure slots and data/source note.
- `content/nightingale_04_visual_plan.md` — historical original, 24-month rate timeline, polar area decoder with area-versus-radius integrity.
- `research/nightingale_04_sources.md` — published-artifact and historical/data claim audit with correct licence.
- `data/nightingale_24_months.csv` — unmodified 24-row HistData transcription (full fields incl. row numbers), upstream Git SHA referenced.
- `data/validation_summary.json` — independently checked counts, denominators, rates and key derivations.
- `project_manifest.md` — scope, QA and approval gate.

## Important comparative analysis
- Source monthly population `Army` varies; official `Disease.rate` etc. are **annualised** per-1,000 troops, not monthly dead / 1,000. Use rate series (not arbitrary counts) in modern comparison.
- First year 11,157 disease recorded deaths / 13,294 all causes = 83.9%. Prove with archive CSV; do not confuse this percentage with chart wedge areas.
- Original 1858 chart and modern visual #02 are different encodings; be explicit and fair about trade-offs, and show the real original credited CC BY 4.0.
- No invented data, no claims that Nightingale discovered disease mechanism, invented polar charts or alone caused reforms.

## Next stage
1. Author approve/rework title and draft narrative/visual storyboard.
2. Produce source-faithful figures; show historical original and two original modern diagrams for separate visual approval.
3. Prepare full site Jekyll/Resources integration in dedicated review PR after content approval, preserve source licence and alt text.
4. Browser/mobile QA at 1365, 390 and 320px, safe margins, no clipping or false rate axes.
5. Explicit author publishing approval before merging to `main` and verifying Pages.
