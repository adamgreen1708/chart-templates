# Project manifest — Simon Reeve / Tropic of Capricorn

## Status

- Status: charts approved; live-site publication package staged on draft PR #87; awaiting Pages validation and Adam final approval
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
- `site/_posts/2026-10-01-one-invisible-line-23000-miles-of-detours.md`
- `site/assets/migrated/simon-reeve-tropic-of-capricorn/feature.svg`
- `site/assets/migrated/simon-reeve-tropic-of-capricorn/route-zigzag.png`
- `site/assets/migrated/simon-reeve-tropic-of-capricorn/route-longitude.png`
- `site/assets/migrated/simon-reeve-tropic-of-capricorn/transport-modes.png`

## Reusable renderer change

This project adds `src/editorial_schematics.py` and a guarded dispatch in `src/render_538.py`. Existing dot/bar/scatter/line rendering remains unchanged.

New chart types:

- `route_zigzag`
- `route_longitude`
- `mode_clusters`

## Gate

Adam approved the final chart set on 1 October 2026. Site post, feature artwork and exact approved chart assets are now staged on draft PR #87. Do not merge until the pull-request Pages build passes and Adam gives final approval.
