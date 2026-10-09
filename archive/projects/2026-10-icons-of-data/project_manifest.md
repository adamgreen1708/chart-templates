# Project manifest — Icons of Data
**Project:** `2026-10-icons-of-data`
**Created:** 2026-10-08
**Status:** approved modern visuals committed to draft PR #107 with exact SHA-256 checks; site build/mobile QA and publication approval pending
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
- Exact modern PNGs committed under `site/assets/icons-of-data/minard/`, with verified reference SHA-256 hashes: `content/minard_visual_assets.md`.
- Primary original (public-domain Minard scan): Wikimedia Commons, credited in site source.
- A one-off GitHub Actions job rendered the approved images with pinned dependencies and verified both original SHA-256 checksums before committing. The temporary workflow has since been removed; reproducible renderer: `scripts/render_minard.py`.
- No changes to protected reusable renderers, global CSS or active GitHub workflows remain.
- PR: https://github.com/adamgreen1708/chart-templates/pull/107 (draft, not merged).
- Card/social preview uses the approved Minard reconstruction; original historical scan appears within the article. Publication blocked pending latest Jekyll/mobile QA, explicit approval and Pages deployment verification.


## Edition 02: Beck — 9 October 2026
A separately reviewable research package has been started under `editions/02-beck/`:
- Draft: `content/beck_02_draft.md`
- Historical claim / image reuse audit: `research/beck_02_sources.md`
- Three-visual editorial plan: `content/beck_02_visual_plan.md`
- Edition manifest: `project_manifest.md`

**State:** editorial kickoff only. No published post, site Resources updates, original 1933 map copy, new graphic assets or general renderer changes. Historical image reuse rights require separate review; the drafted comparison requires verified network source data.
