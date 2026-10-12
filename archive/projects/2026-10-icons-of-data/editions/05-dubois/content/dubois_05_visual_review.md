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
