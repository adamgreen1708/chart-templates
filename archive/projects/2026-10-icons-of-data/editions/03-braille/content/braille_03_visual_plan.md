# Edition 03 — Braille visual storyboard
**Status:** Design plan for approval. Do not produce or publish a historical object image without source/rights checks.

## UK encoding standard (locked for Edition 03)
Use **UK Unified English Braille (UEB)** throughout. UKAAF is the UK standards authority; RNIB is the primary UK explainer and publication source; the internationally agreed ICEB UEB rulebook (2024) defines the actual shared code. The UK adopted UEB in 2011 and completed transition from the older UK Standard English Braille by 2015. American English Braille (EBAE) is historical US terminology and **not** our reference code. UEB signs are shared internationally, so UK and US users of UEB generally use the same basic alphabet and numeric indicator; do not invent a UK-only alphabet difference. Label charts, dot tables, alt text and methods **“UK Unified English Braille (UEB) — uncontracted examples”**. Historical Louis Braille context is separate from modern UEB.

Encoding source hierarchy: [RNIB facts](https://shop.rnib.org.uk/blogs/news/eight-essential-braille-facts) → [UKAAF UEB standard](https://www.ukaaf.org/standards/ueb/) → [ICEB UEB rules (2024)](https://iceb.org/publications/ueb/). No American-only transcriber guide as sole authority for a symbol.

## Editorial intention
Our first **tactile information-encoding** episode. Don't call Braille a data visualisation, or imply an on-screen graphic recreates the lived experience of reading Braille. The goal is to make the mechanics of a six-dot cell understandable while respecting that the native medium is **touch**.

## Visual 1 — The original idea: a cell you can feel
**Lead question:** What does a tactile writing system actually look and feel like?

- One institutionally sourced photograph of genuinely **embossed** Braille, with visible raised marks and descriptive alt text (use suitable lighting, no fake digitally printed dots passed off as relief).
- Pair with **1829 original publication** archival reference from Perkins School for the Blind; avoid claiming the photographed physical page was made in 1829 unless confirmed for that exact item.
- Possible original artefact: Perkins's copy of Louis Braille's 1829 book *Procédé pour écrire les paroles, la musique et le plain-chant au moyen de points*; photo rights to be resolved before embedding.
- Sources: https://www.perkins.org/brailles-most-famous-book/ and https://www.perkins.org/history-of-braille/.
- If reuse rights cannot be established, provide original reader-created tactile reference only when a real embossed sample exists, and link externally to the archival photographs. Never pretend an illustration is physical raised Braille.
- Caption must distinguish developed **1824** vs published **1829**.

## Visual 2 — Six places. Many patterns.
**Lead question:** How can six positions carry so much information?

- Original deterministic square, light-grey, house fonts/colour.
- A large *numbered* six-dot cell: top-to-bottom left is 1–2–3, top-to-bottom right is 4–5–6.
- Show **UK UEB uncontracted** examples `a` = dot **1**, `b` = dots **1,2**, `c` = dots **1,4**, verified from RNIB and ICEB UEB rules endorsed by UKAAF.
- Illustrate the UK UEB context effect: numeric indicator (dots **3,4,5,6**, `⠼`) + `a` (dot **1**, `⠁`) means digit **1** (`⠼⠁`), per RNIB and ICEB. Include the words “in this code and context”.
- Footnote: 2^6 = 64 possible states *including the empty cell*, hence 63 non-empty dot patterns. Mathematical combinatorics is not a claim about 64 entire written meanings or all 64 symbols being available for simple letters.
- **Accessibility:** Braille characters must be accompanied by print text and spelled-out dot positions in nearby visible text, caption and alt text; ensure contrast without suggesting colour encodes actual Braille.
- If using Unicode Braille glyphs, verify the correct UEB mapping. Favour data-driven circle positions over dependency on a specific Unicode Braille font.

## Visual 3 — Why Braille was a breakthrough (revised; approved)
**Editorial question:** Why did six dots make such a difference beyond simply encoding letters?

The original four-panel `Decode the Icon` plan was too similar to Chart 2. It has been superseded by the **approved 9 October revision** `03_why_braille_mattered.png`.

1. **The fingertip test:** contrast Barbier's earlier 12-dot cell and Braille's compact six-dot arrangement, labelled a historical comparison, not reproduced originals.
2. **Read AND write:** original schematic slate, stylus and paper illustrations explain independent writing alongside reading; no artefact photo is claimed.
3. **Context matters:** one UEB dot-1 cell represents *a* as a letter or *1* after the numeric indicator; Chapter 2 contains the detailed indicator mechanics.
4. **Designed for touch:** contrast flat screen diagrams and raised marks on paper. Neither cartoon is usable tactile Braille.

**Distinct roles:** Chart 2 = technical six-dot encoding; Chart 3 = significance, agency and tactile medium. Keep these stories different in captions and article placement. Use modern UK UEB conventions (RNIB, UKAAF/ICEB), and historical background from Perkins. The approved author review requires preserving Chart 2.

**Delivery:** GitHub-runner reproduction uses unchanged drawing code and visually matches the approved layouts, but PNG/pixel hashes differ slightly because of font rasterisation on the runner. Keep the differing raster output identified as the site-review rendition and request final visual approval before merging; do not claim binary identity.

## Publication integrity and QA
- Historical chronology & attribution: Louis Braille began development 1824; first major publication 1829; credited influence of Charles Barbier.
- Do not assume Braille is universal language or simply a substitution alphabet; identify language/code and distinction between uncontracted and contracted forms.
- No invented claim about blind people's reading experiences, speeds or personal preferences.
- Images must be static explanations, with true HTML text equivalents. Consider a separate accessible plain-text dot-position transcript below figures.
- All image rights/permissions verified for each historic photograph, not from generic site-wide statements.
- QA at actual desktop, 390px and 320px breakpoints, especially dot numbering, labels, safe margins, figure captions and screen reader equivalents.
- Await author approval of manuscript and visual storyboard before producing final rendered assets or Jekyll publishing package.
