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


## Edition 04 — site staging after author approved visuals (10 October 2026)
Florence Nightingale's three-visual edition (Wellcome 1858 L0041105, modern 24-month mortality trend and polar-area explanatory diagram) is now staged on draft PR #113, along with Resources entry #04. Exact source references, archival reproduction CC BY 4.0, modern renderer and rate-validation data are included. Jekyll/browser QA at 1365/390/320px passed on run 38072120585. Github runner image rasterisation differs from the original user-approved PNGs; await final visual approval before merging or publishing.

## Edition 05 — W. E. B. Du Bois (12 October 2026)
Started a draft editorial research package under `editions/05-dubois/` for the specific LoC item 2013650430, *City and Rural Population. 1890*, drawn circa 1900 for the Paris Exposition. Includes ~360-word article draft, three purposeful visual specs (authentic poster → source-data zero-based ranked view → spatial-encoding decoder), institution-based research and **provisional** chart counts reconciled to Census 1890 Georgia Black population 858,815. Two source reproductions disagree on individual category labels, so exact transcription is a **hard rendering gate**. No images or site files created. Author editorial approval and figure rights remain outstanding.


## Edition 05 — website staging after visual approval (12 October 2026)
Du Bois's historic four-colour visual revision approved. Full blog edition (authentic LoC 815×1024 JPEG, two 1920px custom house-style graphic images, captions, archival numerical checks, Resources entry #05) staged in PR #114. Jekyll/Playwright desktop 1365px, mobile 390px and narrow 320px QA passed in run 38300582492; screenshots in edition `qa/site/`. Note site runner PNG pixels differ from approved local review PNGs; final author visual review/merge permission still pending. No changes to global 538 renderer or publishing system.



## Edition 06 — John Snow (12 October 2026)
New focused research kickoff under `editions/06-john-snow/`: 363-word editorial manuscript **“The map that put a pump on trial”**, three separate visual treatments (specific authentic **1855** book map, accurate 578-mark/13-pump/528-street-segment reconstruction, four-panel decode), historical/source/image-rights research, and unchanged public HistData source tables with independent schema/geometry checks. Chosen historical original is Wellcome **L0063431**, an image reproduction labelled **CC BY 4.0**; distinguish from the public-domain-marked book scan and the 1855 parish inquiry map. Historical outbreak was **1854**; no claim the map discovered contaminated water or that pump handle removal ended an already declining outbreak.
**State:** concept/working draft only. No images rendered, Jekyll/site/Resources content changed, or publication approved. Await author editorial direction; preserve separate image and merge approval gates.


## Edition 06 — first three visuals for author review (12 October 2026)
Original **1855** Wellcome L0063431 source image and two house-style 1920px modern visuals now rendered and staged for *review only* on PR #115 in `editions/06-john-snow/qa/visuals/`. Pinned data: 578 digitised map marks, 13 pump positions, 528 street segments. Exact original/photo hashes, CC BY 4.0, small-screen thumbnails and manuscript QA specified in `editions/06-john-snow/content/snow_06_visual_review.md`. Runner https://github.com/adamgreen1708/chart-templates/actions/runs/38303582365 passed; temporary workflow removed. **No `site/**` modifications. Await author visual approval before website integration, with a separate final merge/publish gate.**
