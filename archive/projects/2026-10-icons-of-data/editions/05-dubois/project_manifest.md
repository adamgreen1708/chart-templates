# Icons of Data — Edition 05: W. E. B. Du Bois

**Working title:** The spiral that tells a bigger story
**Started:** 12 October 2026
**Historical artefact:** W. E. B. Du Bois (with Atlanta University collaboration within the exhibit), *The Georgia Negro: City and Rural Population. 1890*, drawn circa 1900, Library of Congress **LCCN 2013650430**, LOT 11931 no. 11, digital ID ppmsca.33873.
**Status:** author approved original-inspired four-colour figures. Full site Jekyll article, original Library of Congress plate, two modern diagrams and fifth Resources entry staged in PR #114; desktop/mobile QA passed. **No merge or publication approval yet.**

## Files
- `content/dubois_05_draft.md` — ~350–400 word working narrative and deliberate three-visual placeholders.
- `content/dubois_05_visual_plan.md` — original/modern ranked comparison/encoding decoder storyboard.
- `research/dubois_05_sources.md` — institutional source and provenance audit including *disputed historical numeral transcriptions* and LoC rights.
- `data/provisional_population_1890.csv` — candidates research audit preserved (conflicting secondary captions); **superseded** by verified data.
- `data/validation_summary.json` — explicit reconciliation to authoritative 1890 Census Georgia population of 858,815; reconciles verified individual original-plate labels with Census total.
- `project_manifest.md` — gates and status.
- Catalogue and parent project manifest updated to indicate Edition 05 drafting only.

## Next stage
1. Author reviews title/angle/editorial draft.
2. **Completed (LoC original JPEG + Yale independent table):** verified four individual printed counts and reconciled Census total; exact LoC image licence still to be confirmed at publication review.
3. **Completed for visual review:** produced modern zero-based bar comparison and a distinct four-panel spiral decoder; preserve code, checksum manifest and phone thumbnails; show originals before any website asset commit.
4. On approval, integrate with current GitHub Pages Jekyll site and Resources; run desktop+mobile QA.
5. Merge/publish only after explicit author approval. Never treat staging or chart approval as merge approval.

## Visual review status — 12 October 2026
The user approved the headline and editorial direction, **not** image publication. Historical LoC original link: https://www.loc.gov/item/2013650430/; verified data: `data/verified_population_1890.csv`. Original images and two modern 1920px figures supplied in ChatGPT for visual approval; locally generated scripts and screenshot-size checks not yet committed to GitHub. Stage exact images in GitHub only **after** user reviews and approves them. No Pages publication approval.


## Complete Jekyll staging and browser QA — 12 October 2026
**State:** article + full three-figure website package staged in draft PR #114, with fifth Resources entry. All Jekyll/Chrome QA passed. **This is not permission to merge or publish.** The final website build awaits explicit user approval.

- Jekyll post: `site/_posts/2026-10-12-the-spiral-that-tells-a-bigger-story.md`; permalink `/icons-of-data/dubois-spiral/`.
- Original historical source: `site/assets/icons-of-data/dubois/01_city_and_rural_population_1890_loc.jpg`, **the authentic unmodified Library of Congress JPEG** from https://tile.loc.gov/storage-services/service/pnp/ppmsca/33800/33873v.jpg, original **815×1024**. Source SHA-256 `0514df1942f088543ff26f9bdad9eea0eff8798528f55c0efdb1efb6663f10a7`. Record LC-DIG-ppmsca-33873 and exact rights advisory **No known restrictions on publication**; this is not a CC grant.
- Modern site Chart 02: `site/assets/icons-of-data/dubois/02_the_spiral_unwound_historic_palette.png`, 1920×1920. Original author-approved review SHA-256 `d46ab51831777fd0564f2919bd215ce0d0d6162b54d7e08d1fe619209e09514c`. GitHub runner SHA-256 `ce40606de7c40e675355ea8337fc3d6a32556269ae0f47c9d308deacecccf185` (**DIFFERENT BYTES; final screenshot visual approval required**).
- Modern site Chart 03: `site/assets/icons-of-data/dubois/03_decode_the_spiral_historic_palette.png`, 1920×1920. Original author-approved review SHA-256 `ff60147eaadccad344c6b3dc1235007c36b47c43024d89fd84f993692ac50c7c`. GitHub runner SHA-256 `171694a15c3c5c9ebd1b549e24d9f596037be1d0120b7a41227ea0aa34fb7b98` (**DIFFERENT BYTES; final screenshot visual approval required**).
- Both production-rendered images use `scripts/render_historic_palette.py` and source-verified `data/verified_population_1890.csv`. Styles are per-project, matching `spec/538_template_rules.md` and previously approved Icons of Data grammar with historically inspired coloured categories. **They are not rendered by the general-purpose `src/render_538.py` engine**. Do not claim otherwise.
- Original categories sum to **858,815**, consistent with Census 1890 Georgia Black-population table. Rural group = **734,952 = 85.6%**; no data substitutions.
- Browser QA via [GitHub Actions run 38300582492](https://github.com/adamgreen1708/chart-templates/actions/runs/38300582492), Jekyll and Chrome/Playwright validated at **1365px desktop, 390px mobile, 320px narrow phone**. All 3 images decoded, original rights and research links present, no overflow/title clipping, source method displayed; all **five** Resources links work. Screenshots in `qa/site/dubois-article-desktop.png`, `dubois-article-mobile.png`, `dubois-article-narrow.png`, `dubois-resources-mobile.png`.
- Temporary QA GitHub workflow removed after completion; no global renderer/config/workflow changes survive.
- **Approval sequence:** user approved the manuscript/title and the colour-restored modern images; final site screenshots require author acceptance before PR #114 becomes mergeable by editorial policy. No live site/Pages publication yet.

