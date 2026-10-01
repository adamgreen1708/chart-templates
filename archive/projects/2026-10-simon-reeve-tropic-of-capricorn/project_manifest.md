# Project manifest — Simon Reeve / Tropic of Capricorn

## Status

- Status: deterministic render QA round 2; waiting for the final GitHub Actions render to commit the revised PNGs
- Started: 1 October 2026
- Owner: Adam Green
- Repo project slug: `2026-10-simon-reeve-tropic-of-capricorn`

## Editorial takeaway

**One invisible line creates a very crooked journey.**

## Chart sequence

1. `route_zigzag` — ten countries in travel order, schematic/even spacing.
2. `route_longitude` — named stops by approximate longitude and latitude, split into Africa/Australia/South America panels.
3. `mode_clusters` — eight named transport modes grouped into Ground/Air/Water/Animal.

## Project files

- `data/route_countries.csv`
- `data/route_places.csv`
- `data/transport_modes.csv`
- `config/chart_01_route_zigzag.py`
- `config/chart_02_route_longitude.py`
- `config/chart_03_transport_modes.py`
- `content/story_plan.md`
- `content/source_notes.md`
- `content/qa_report.md`
- `content/publication_package.md`

## Reusable renderer change

This project adds `src/editorial_schematics.py` and a guarded dispatch in `src/render_538.py`. Existing dot/bar/scatter/line rendering remains unchanged.

New chart types:

- `route_zigzag`
- `route_longitude`
- `mode_clusters`

## Gate

Do not stage or merge live site publication until Adam has reviewed the official GitHub Actions renders.
