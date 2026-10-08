# Project manifest — Icons of Data
**Project:** `2026-10-icons-of-data`
**Created:** 2026-10-08
**Status:** drafted Jekyll Resources hub and Minard article; modern visuals approved; binary upload, full Jekyll QA and final publication approval pending
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

## 8 October delivery update
- Draft Jekyll article: `site/_posts/2026-10-08-a-line-that-disappears.md`, following the approved ~400-word version.
- New Resources collection: `site/resources/icons-of-data/index.html`, introducing Minard, Beck's Tube map and Braille with a filterable encoding gallery, encoding matrix and verified timeline.
- Draft Resources navigation: `site/resources/index.html`, with the original 13-card guide preserved.
- Exact modern PNGs approved and delivered separately in an asset ZIP; hashes and expected site paths: `content/minard_visual_assets.md`.
- Primary original (public-domain Minard scan): Wikimedia Commons, credited in site source.
- The modern binary PNGs are NOT yet in GitHub: GitHub connector cannot read local binary files directly; never claim the site package is complete until uploaded and verified.
- No changes to renderer, global CSS, GitHub workflow or protected core files.
- PR: https://github.com/adamgreen1708/chart-templates/pull/107 (draft, not merged).
- Publication blocked pending image upload, card/hero artwork, Jekyll and mobile QA, explicit approval, Pages deployment verification.
