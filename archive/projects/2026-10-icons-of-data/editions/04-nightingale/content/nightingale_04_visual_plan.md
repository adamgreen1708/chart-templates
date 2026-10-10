# Icons of Data #04 — Florence Nightingale visual storyboard

**Editorial argument:** A graphic can make an important question impossible to ignore, but visual force is not the same thing as proof.

## 01 — The original 1858 plate (historical source)
Show **the actual** "Diagram of the Causes of Mortality in the Army in the East" from Florence Nightingale's 1858 `Notes on Matters Affecting the Health, Efficiency, and Hospital Administration of the British Army`, **specifically Wellcome L0041105**.

- Licensed source: https://commons.wikimedia.org/wiki/File:Diagram_of_the_causes_of_mortality_in_the_army_Wellcome_L0041105.jpg
- Original scan size 3942×2566; file CC BY 4.0, Wellcome Library, London / Wellcome Images.
- Attribution: "Florence Nightingale, 1858. Digital image: Wellcome Collection (L0041105), CC BY 4.0"; if resized/cropped for the blog declare modification. Keep original publication edition distinguished from differently arranged 1859 reproductions.
- Caption: **right** circle Apr 1854–Mar 1855; **left** circle Apr 1855–Mar 1856; blue disease, red wounds, black other causes; rates shown by area.
- Do not generate this image from a model, invent alternate labels, replace the real object with generic rose graphics, or silently confuse Wellcome L0041105 with other plates.

## 02 — What the statistics were saying (data-first, modern chart)
Question: **What happened to monthly mortality rates by cause, across the two years?**

- Use all **24 monthly** observations in the archived `data/nightingale_24_months.csv` from public HistData transcription.
- Series: annualised monthly death rates **per 1,000 soldiers**: `Disease.rate`, `Wounds.rate`, `Other.rate`. No double axes, no combining counts with rates.
- Time axis: real Apr 1854 to Mar 1856, continuous and evenly spaced months. Vertical time-context band or subtle divider at Apr 1855, with balanced layout and zero-based y-axis (or clearly labelled non-zero axis only if explicitly justified for lines; house default zero).
- Colours: Nightingale historical legend decoded in text, but modern chart may use matching blue, muted red and charcoal with accessible direct labels and source credit.
- Key quantities to compare if desired: disease 11,157 vs wounds 772 recorded deaths in the *first* period; the share 11,157 / 13,294 = **83.9%**. These counts are **separate supporting context** and not the annualised rates on the plot.
- January 1855 disease peak annualised **1,022.8 deaths per 1,000 soldiers** does NOT mean 1,023 soldiers actually died from every 1,000 that month. It is monthly rate ×12: 2,761 recorded disease deaths / 32,393 estimated troops ×12×1,000.
- Label explicitly **annualised rate from monthly counts**. Footnote: source data derived from 19th-century army returns, recompiled in modern HistData; administrative classifications/strength estimates are historical.
- Correlation/causation gate: source records do not isolate effect of sanitation versus season, population change, military action.

## 03 — Decode the Icon: HOW the argument is encoded
Question: **Why does this diagram look persuasive, and what might a reader miss?**

A four-panel editorial image, distinct from the evidence timeline in Visual 02:
1. **Time around a circle:** each of 12 months has **the same 30° angle**; direction/ordering and distinct year panels.
2. **Area, not radius:** coloured sector **area ∝ annualised mortality rate**. For fixed angle, radius ∝ square root(rate). Illustrate with simple comparable constructed magnitudes, clearly marked *schematic*, not invented historical records.
3. **Three causes / one centre:** blue = Nightingale's Victorian preventable or mitigable zymotic disease; red = wounds; black = other; the chart draws category areas from a **shared centre and overlaps them**, **not** stacked outer-band thicknesses.
4. **What comparison can't settle:** two different periods, troop populations and seasons; trend supports reform urgency but is not proof one intervention caused a decline. A compact annotated rate legend helps with the counterintuitive >1,000 annualised example.

**Integrity rules:** No claims Nightingale invented all polar diagrams or single-handedly caused reform; no fixed-percent modern diagnosis from 'zymotic'; no annualised rates labelled deaths/counts; no bogus numbers in icon decoder; original image licence note and alt text; chart widths, labels, safe margins & readability on 390px/320px phone.

**Publishing flow:** author approves editorial and storyboard; generate visuals, show for distinct visual approval; stage complete site Jekyll & Resources package; run desktop/mobile QA; explicit author approval required before GitHub merge/Pages publication.
