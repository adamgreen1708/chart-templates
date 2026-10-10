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

## Edition 02 approval and site staging — 9 October 2026
Harry Beck's two original explanatory diagrams were approved and committed exactly, with verified SHA-256 hashes, by GitHub Actions run 37969690244. Files: `site/assets/icons-of-data/beck/02_geography_vs_connections.png` and `03_decode_the_icon.png`. The Jekyll article and Edition 02 link in Resources are staged on draft PR #109; Beck's 1933 original remains a museum link due unresolved reproduction rights. Work awaits site/mobile QA and **explicit merge/publish authorisation**.

## Edition 03: Braille — 9 October 2026
Editorial kickoff: `editions/03-braille/`, including the ~350-word manuscript, verified historical and UK/English Braille code references, accessible three-visual storyboard, and exact dot-position examples for deterministic diagrams.

**State:** draft for editorial review. No visual or historical photograph has been generated/republished, no Jekyll post or live Resources change, and no Pages merge/publish authorisation. Distinguish six-dot cell drawings on a screen from tactile Braille. Development 1824; book published 1829; historical image rights remain a gate.


## Edition 04: Florence Nightingale — 10 October 2026
An editorial concept package was started under `editions/04-nightingale/`: conversational manuscript, three-visual plan, exact **1858** Wellcome L0041105 plate reference and CC BY 4.0 licence, critical historical-claim research, a 24-month HistData mortality transcription and independently derived QA summary. The original historical plates' two-period orientation, **annualised rate vs death counts**, area vs radius, and cautious interpretation are mandatory.

**State:** concept/manuscript only, submitted for author review. No images generated, Jekyll post, Resources page edit or publishing approval. The historical source plate may be reused only with its specific licence credit. No claims Nightingale invented polar-area graphics or proved causal effect of sanitation from the diagram alone.
