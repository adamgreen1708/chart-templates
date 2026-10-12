# Icons of Data #05 — W. E. B. Du Bois visual review
**Status:** Two original visual aids delivered for author approval; nothing staged as site images or published. Historical original itself must be linked directly, never recreated.

## Three figures
1. **Historical original**: original c.1900 ink and watercolour *City and Rural Population. 1890*, LoC item 2013650430, digital ID ppmsca.33873, [LoC view](https://www.loc.gov/item/2013650430/), [readable medium source JPEG](https://tile.loc.gov/storage-services/service/pnp/ppmsca/33800/33873v.jpg); item-level advisory: **No known restrictions on publication**. Specific archival credit/rights assessment still required for eventual website edition.
2. **The spiral, unwound**: original Coffeetableviz chart, 1920×1920, review PNG SHA-256 **7d8bba520e0d6b943f9380cd14e6e74031e840a9631309a98d4b0467597458fb**; zero-based four-category ranking in high-to-low order and 85.6% countryside-and-villages share. Bar widths not inflated; numbers verified.
3. **A striking shape. A tricky comparison.**: original four-panel schematic decoder, 1920×1920, review PNG SHA-256 **2941945b3fe7adbac479119b31e5dfd2f7cb83bd481790be62e25d96c27c9f2d**. Panels: compact coiling, original category colours, numerical label accuracy, historical settlement boundaries. The coil is an explanatory schematic, never a proportional reconstruction.

**Exact accepted bytes rule:** These two sha256 hashes are the review baseline; commit the exact files only after the user's visual approval. If GitHub-runner drawing changes pixels, explicitly re-review the website rendition before publication. Review ZIP in current ChatGPT turn includes source `render_dubois.py`, `population_1890_verified.csv`, screenshots in `qa/`, `visual_manifest.json`, captions and QA notes. No images or script bytes have yet been committed to GitHub.

## Original-source audit now passed
- LoC original shows the four printed values (original category labels quoted only in archive as needed): **78,139 / 8,025 / 37,699 / 734,952**.
- These are corroborated [independently by Yale National Initiative unit 26.01.04 (2026)](https://teachers.yale.edu/curriculum/units/2026/1/4/8), and their sum **858,815** agrees with US Census Georgia historical Table 25 (1890 Black population).
- Secondary reproductions incorrectly/ambiguously print **70,839** or **37,899**; maintain the record of those disagreements in source audit rather than substitute these values.
- Correct interpretation: 1890 Georgia, not all US, 1890 data but c.1900 artwork, `Country and villages` rather than a definition-equivalent modern `rural` series.
- 734,952/858,815 = 85.577%; **85.6%** on Chart 2.

## Rendering QA
- Both charts 1920×1920, explicit titles, legible and unclipped safe margins.
- Chart 2 common zero-based scale 0–800k, sorted high to low, correct count labels, no second axis or fabricated percentages.
- Chart 3 qualitative, distinctly not a second ranking. No claim the spiral path is precisely proportional to all drawn segment lengths.
- 600px/390px/320px reduced-size reviews included in ZIP; meaningful source citation, alt text and direct data description required in Jekyll captions.
- No historic facsimile generated, no historic image licence asserted beyond precise LoC notice.
- Await author visual approval before GitHub site assets or any PR merge.


## CORRECTION — existing visual designs superseded, 12 October 2026
The user **approved the chart concepts and data only**, but specifically **rejected the first visual styling** as a deviation from the locked coffeetableviz render system. **Do not use the two earlier PNG hashes from the preceding section as accepted final image assets.**

The replacement review graphics (not yet committed to GitHub) follow `spec/538_template_rules.md` and the approved #04 Nightingale visual grammar, using 8×8 square / 1920×1920 PNG, background `#F3F4F6`, teal `#1F8FA8` and limited red `#C44E52`, black titles, light dividers, safe margins and a slim source footer. Reject the earlier custom red series banner, large grey footer band, four-colour bars and rounded cards.

- Revised **02 The spiral, unwound** PNG review SHA-256: `56c9106a77554d11fb693a8f1975eba7ba403d140a6a7ee5f3ad456eda797731`.
- Revised **03 Decode the Icon** PNG review SHA-256: `aa94fa221bf642a56e7553ac42ad0646244ef8eb9e750751b33dbcbad9c843b8`.
- Revised review pack delivered through ChatGPT as `icons_of_data_05_house_style_revision.zip`: includes 2 PNGs, 600/390/320px QA thumbnails, documented Matplotlib review source, `chart_config_dubois_02.py` (full repo-compatible **CHART_CONFIG** for `src/render_538.py`), verified CSV and sha manifest.
- **Important:** the local PNG preview imitates the standard renderer style, but **has not itself been produced by `src/render_538.py`**. After the user visually approves this review, run the actual repository renderer using the saved config, compare its output and QA labels/margins, then stage final assets separately. Decoder #03 remains a deterministic editorial composition in the established series style rather than an unsupported core chart type.
- **Approval gate:** author must approve these revised renders before committing image assets or initiating publication. PR remains a draft; no Jekyll or Resources files changed.


## Author approval — original-inspired historic palette, 12 October 2026
The user **explicitly approved** the *third*, historically coloured revision of Charts 02 and 03. This **supersedes** both the initial decorative designs and the later teal/red-only revised versions. Keep the locked editorial square typography, grey `#F3F4F6` canvas, horizontal presentation, thin frame rules and safe margins, but use the four historical **category-specific colour cues**.

**Exact author-approved review image files** (local ChatGPT review archive) SHA-256:
- Chart 02 `02_the_spiral_unwound_historic_palette.png`: `d46ab51831777fd0564f2919bd215ce0d0d6162b54d7e08d1fe619209e09514c`.
- Chart 03 `03_decode_the_spiral_historic_palette.png`: `ff60147eaadccad344c6b3dc1235007c36b47c43024d89fd84f993692ac50c7c`.

**Historical colour mapping (near visual interpretations, not sampled exact values):** country and villages RED `#C44E52`; cities over 10,000 GREEN `#43855A`; cities 5,000–10,000 BLUE `#2A83A6`; cities 2,500–5,000 YELLOW `#D1A53A`. Core house teal `#1F8FA8` remains used for contextual 1890 cue. All groups are identified by text as well as hue.

Production-source staging:
- `scripts/render_historic_palette.py`: deterministic Python script derived from approved review source; it reads `data/verified_population_1890.csv` and uses the same two figure designs. Global `src/render_538.py`, `src/chart_config.py` and locked renderer defaults are untouched. The historical palette is a project-specific exception, not a new default.
- `site/_posts/2026-10-12-the-spiral-that-tells-a-bigger-story.md` and `site/resources/icons-of-data/index.html` staged, not published.
- Source archival photograph will be fetched *unaltered* from the specific Library of Congress `LC-DIG-ppmsca-33873` digital record, with explicit item's 'No known restrictions on publication' advisory. Do not label this as a Creative Commons licence.
- GitHub runner renders may differ in exact PNG bytes from the author-reviewed files due to backend/font differences. Compare approved SHA-256 against actual generated SHA and **show final site screenshot for visual acceptance**. Never claim exact identity when hashes differ.

**Approval scope:** Figure concepts, house styling and Du Bois colour mapping are approved. This is **not** author approval to merge PR #114 or publish to GitHub Pages. Complete browser/site and final visual review still required.
