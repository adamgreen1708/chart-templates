# Project manifest — Icons of Data
**Project:** `2026-10-icons-of-data`
**Created:** 2026-10-08
**Status:** foundation draft, awaiting editorial/art approval
**Project scope:** evergreen Resources collection plus independently authored long-form editions about influential systems for encoding information.

## Files in this foundation
- `content/collection_plan.md` — collection model, editorial strategy, site location and staged milestones.
- `content/minard_01_draft.md` — first-article working manuscript with figure placeholders.
- `data/icons_catalogue.csv` — sourced seed entries; unverified candidates are explicitly marked.
- `data/minard_troops.csv` — 51 route observations, column names preserved.
- `data/minard_cities.csv` — 20 places, column names preserved.
- `data/minard_temperature.csv` — 9 temperature observations, one missing date preserved.
- `spec/series/icons-of-data.md` — series-wide standards (kept outside archive for reuse).

## Source data provenance
The three Minard CSV files copy the corresponding tables from the public `vincentarelbundock/Rdatasets` GitHub repository, `HistData` package, at:
- https://github.com/vincentarelbundock/Rdatasets/blob/master/csv/HistData/Minard.troops.csv
- https://github.com/vincentarelbundock/Rdatasets/blob/master/csv/HistData/Minard.cities.csv
- https://github.com/vincentarelbundock/Rdatasets/blob/master/csv/HistData/Minard.temp.csv

Dataset documentation: https://friendly.github.io/HistData/reference/Minard.html
Original map provenance: https://catalogue.bnf.fr/ark:/12148/cb40650878p

**Source caution:** the `HistData` documentation mislabels the campaign as 1815. It was 1812–1813. The CSVs are transcription/digitisation for reproduction, not new first-hand evidence; dates and temperature units must be audited against the original diagram before plotting.

## Scope of foundation delivery
No Jekyll post, resources page, renderer/config changes, visual output or site image is included. No change is published to GitHub Pages. Work remains in a draft branch/PR pending approval.
