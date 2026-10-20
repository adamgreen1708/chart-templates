# Edition 07 — visual storyboard (GITHUB-RENDERED; EXACT IMAGE APPROVAL PENDING)

## Figure 01 — The authentic original, *not* a Coffeetableviz render
- Historical original: Ed Hawkins, University of Reading Art Collection, *Climate Stripes: Warming Stripes, Global 2020*, digital edition 2021 (UAC/11018), one annual stripe from 1850 through 2020.
- Display **exact original 1200×675 JPEG** `qa/visuals/01_reading_global_2020_original_unmodified.jpg`, as the first visual by itself, with title/source in the external HTML caption. No 1920×1920 Coffeetableviz framing, border, overlay, crop, recolouring or reproduction by renderer. A previously framed image was deleted following author feedback.
- Link historical origin to Hay-on-Wye 2017 data design shown in 2018; **do not claim Hawkins was first ever to encode warming as coloured textile/stripes**. The collection explicitly acknowledges knitting precedents.
- Rights: University of Reading Art Collection documents CC reuse; source byte provenance and SHA-256 in `content/hawkins_07_visual_review.md`. Article caption must provide creator, collection ID UAC/11018 and canonical source link. Artist's 2020 edition precedes the later 2023 baseline change.

## Figure 02 — The century shifts colour
- Modern, clearly labelled independently sourced reconstruction: Met Office HadCRUT.5.2.0.0 annual analysis global mean 1850 through last **completed** year available.
- Top: one uniform-width band per valid annual observation; historic cool→warm blue/red palette is a deliberate source-faithful exception to site accents.
- Bottom: restrained line/scatter trace of the **same values** with unit, zero/reference line, years and explicit baseline; the extra axis reveals quantities and variability that stripes hide.
- Data gate: obtain official annual CSV, inspect missingness and time period, calculate a single documented scaling method (diverging palette), preserve order and year count.
- Native Met Office anomalies relative to 1961–1990; if an alternate baseline 1961–2010 is used, derive it from this series and label. Do not claim exact colour identity with Reading / Berkeley Earth official stripes.
- One fixed blue/red range, explicit colour scale, no fake values, no truncated year endpoints.

## Figure 03 — Decode the Icon (four panels)
A. **One band = one year:** show four real adjacent completed years, in chronological order.
B. **Colour carries temperature:** same annual values in marks with a labelled colour scale and a reference centre.
C. **What has gone missing?** same excerpt with axis, unit, variation and uncertainty source note where available; no invented error bar.
D. **Same record, different reference choice:** explain rebasing shifts the numerical zero without changing the underlying temperatures. Distinguish source series from Hawkins' source data and preserve the dataset identity.

## House/QA
- **Only figures 02 and 03** are square 1920×1920 Coffeetableviz renders: #F3F4F6 base, black editorial headings, generous safe margins, thin dividers/footer. **Figure 01 is original 1200×675 landscape** with no template applied.
- Differentiate original, sourced reconstructed figure and schematic decoder.
- Include concise source + baseline + colour palette note in every graphic; 390/320px small-screen readability.
- No work under site/_posts, site/assets, or site/resources until figure and editorial approval.


Final GitHub render references and provenances: `content/hawkins_07_visual_review.md`; Actions final https://github.com/adamgreen1708/chart-templates/actions/runs/39505109952 .
