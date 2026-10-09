# Edition 03 — Braille visual storyboard
**Status:** Design plan for approval. Do not produce or publish a historical object image without source/rights checks.

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
- Show uncontracted English examples `a` = dot **1**, `b` = dots **1,2**, `c` = dots **1,4**.
- Illustrate the context effect: the number indicator (dots **3,4,5,6**) + `a` (dot **1**) means **1**.
- Footnote: 2^6 = 64 possible states *including the empty cell*, hence 63 non-empty dot patterns. Mathematical combinatorics is not a claim about 64 entire written meanings or all 64 symbols being available for simple letters.
- **Accessibility:** Braille characters must be accompanied by print text and spelled-out dot positions in nearby visible text, caption and alt text; ensure contrast without suggesting colour encodes actual Braille.
- If using Unicode Braille glyphs, verify the correct UEB mapping. Favour data-driven circle positions over dependency on a specific Unicode Braille font.

## Visual 3 — Decode the Icon (four panels)
1. **Positions** — six-dot cell, fixed two-column, three-row geometry, correct dot numbers.
2. **Patterns** — selecting different raised-dot combinations generates different signs; show verified examples.
3. **Context** — prefix indicators (number sign) change interpretation of a subsequent cell; not every cell stands alone.
4. **Touch, not ink** — diagrammatic image on a screen versus *actual embossed material*; explicitly identify why paper/screen image cannot replace tactile access.
- Reuse the four-panel *Decode the Icon* editorial format established for Minard and Beck, not photographic simulation.
- See also modern **Unified English Braille** in UK (adopted during 2011–2015 transition). Specify code/version when explaining symbols. Don't imply today's code exactly matches the first 1829 publication.

## Publication integrity and QA
- Historical chronology & attribution: Louis Braille began development 1824; first major publication 1829; credited influence of Charles Barbier.
- Do not assume Braille is universal language or simply a substitution alphabet; identify language/code and distinction between uncontracted and contracted forms.
- No invented claim about blind people's reading experiences, speeds or personal preferences.
- Images must be static explanations, with true HTML text equivalents. Consider a separate accessible plain-text dot-position transcript below figures.
- All image rights/permissions verified for each historic photograph, not from generic site-wide statements.
- QA at actual desktop, 390px and 320px breakpoints, especially dot numbering, labels, safe margins, figure captions and screen reader equivalents.
- Await author approval of manuscript and visual storyboard before producing final rendered assets or Jekyll publishing package.
