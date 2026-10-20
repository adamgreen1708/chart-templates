# Icons of Data #07 — GitHub Actions visual review (corrected 20 October 2026)

**State:** author identified Figure 01 was wrongly presented in a Coffeetableviz frame. Correction completed exclusively in the GitHub draft process, no website changes, no merge or publication. The original artefact is shown as-is. Author approved this corrected original plus the two GitHub-rendered modern figures on 20 October 2026, authorising website staging and QA **only**. Final merge and publication approval remain pending.

## Figure 01 — authentic historical original, no Coffeetableviz frame

- **Only original artwork file:** `qa/visuals/01_reading_global_2020_original_unmodified.jpg`.
- Ed Hawkins, *Climate Stripes: Warming Stripes, Global 2020*, digital 2021, University of Reading Art Collection UAC/11018; 1850–2020.
- **Original dimensions 1200 × 675**, downloaded intact on a GitHub Actions runner from https://collections.reading.ac.uk/art-collections/wp-content/uploads/sites/2/2021/10/UAC_11018-1200px.jpg .
- SHA-256 `64ac4a7b3ed36fc7448b107caa4b6c222005013862ecf017947e24ad4d16f07f`. Source byte identity checked against known checksum.
- Credit and date belong **outside the image**, in the eventual article caption. No rendered title, banner, label, recrop or typography should be introduced.
- University collection provenance and permissive Creative Commons terms: https://collections.reading.ac.uk/art-collections/2021/12/20/show-your-stripes-the-artwork-that-made-climate-change-data-go-viral/ .
- Previous `01_the_original_warming_stripes.png` and its preview derivatives **deleted** from the GitHub branch after author correction. Do not stage or display the framed version.

## Figures 02–03 — Coffeetableviz explanatory graphics only

- **02 — The years turn red:** `qa/visuals/02_the_century_shifts_colour.png` (1920 × 1920), SHA-256 `cc74466aa9d4bb80f8b9fda6b7f2aeec44a2577d09b67105da5994d87bc42a97`.
- **03 — Decode the Icon:** `qa/visuals/03_decode_the_icon.png` (1920 × 1920), SHA-256 `b5eaac606edd53251cc86468a78da17658e16ae855b7be535f56dd7789ca0959`.
- Pinned original data: HadCRUT5 v5.2.0.0 Met Office global annual series, 176 completed years 1850–2025, native baseline **1961–1990**, incomplete 2026 excluded. Original source checksum `7f750b673bb34aad722736ee21f122b5ea692c99877fa0b1066df65e51f32c04`.
- 2025 native anomaly **+1.0732167°C**; rebased to 1961–2010 anomaly **+0.89220892164°C**, from original-row baseline offset +0.18100777836°C. This is a teaching comparison, not a claim these figures match the Reading original's colours.

## Important distinction: three different reference periods

1. The **historical pre-2023 Warming Stripes** used **1971–2000**.
2. Hawkins changed the stripes reference period to **1961–2010** for the 2023 update, and broadened the colour limits because 2023 was so extreme. He explains this first-hand in his 14 May 2024 article https://climatelabbook.substack.com/p/warming-stripes .
3. The underlying **Met Office HadCRUT5** data file in this project uses **1961–1990**. The World Meteorological Organization retains this older baseline for long-term comparison; there is nothing climatically unique about 1961 as an individual year.

This distinction MUST be explained in article/captions, not implied that Hawkins always used 1961–2010, or that the 2020 and 2025 figures have matching baselines.

## QA and approvals

- **Corrective GitHub Actions run:** https://github.com/adamgreen1708/chart-templates/actions/runs/39506769249 — success; independent sha256/original dimensions check; both modern PNGs rerendered and verified, stale framed source image removed.
- Renderer `scripts/render_hawkins_review.py` now treats Figure 01 as an unaltered historical file (1200 × 675); it generates only Figures 02 and 03 as square Coffeetableviz graphics.
- All files remain within the edition's `archive/**` tree on draft PR #138. The temporary GH Actions workflow may be removed once verified; don't make site or shared renderer changes.
- The author has approved the exact corrected original and two modern PNGs. Their site copies were verified byte-for-byte, and Jekyll/browser QA passed. Separate explicit approval is still required before merge and publication.

## Website staging and browser QA — 20 October 2026

- Author explicitly approved the corrected three-image set and authorised the next step of staging the website. This approval does **not** authorise GitHub merge or live deployment.
- Staged Jekyll article: `site/_posts/2026-10-20-how-the-world-changed-colour.md`, proposed permalink `/icons-of-data/ed-hawkins-warming-stripes/`. Art attribution in the caption, not inside Figure 01; full Met Office method/licence acknowledgement; 1971–2000 / 1961–2010 / 1961–1990 periods distinguished.
- Staged original and exact approved modern image bytes in `site/assets/icons-of-data/ed-hawkins/`; 3 source/output SHA-256 pairs match exactly.
- Updated `site/resources/icons-of-data/index.html` to **seven** editions; entry #07, encoding fingerprint, primary source and baseline references included.
- GitHub Actions website staging and QA: https://github.com/adamgreen1708/chart-templates/actions/runs/39508118680 — **success**. Jekyll build passed; headless Chrome screenshots and checks at **1365, 390, 320px**; all 3 images had correct natural dimensions and descriptive alt; 7 Resources entries; **no horizontal overflow, no page JavaScript errors**, required article text/attribution present.
- Exact screenshots: `qa/site/hawkins-article-desktop.png`, `hawkins-article-mobile.png`, `hawkins-article-narrow.png`, and matching Resources page captures; `qa/site/browser_qa.json` records machine-readable results. Desktop and mobile previews have been visually inspected.
- PR #138 **remains draft**. No changes merged to main and no Pages deployment. Next: author reviews staged website article/screenshots and gives a separate explicit OK before merge.
