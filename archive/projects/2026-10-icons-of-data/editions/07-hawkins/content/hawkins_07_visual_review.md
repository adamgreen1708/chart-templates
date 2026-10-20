# Icons of Data 07 — visual review pack (20 October 2026)

**Gate:** Source and modern render review. **No website publication or image approval.** Four editorial research files and original source CSV are staged on draft PR #138. Rendered PNGs are retained as exact review attachments in the author chat, **not committed to GitHub** pending approval.

## Figure 01: historically authentic original

- Ed Hawkins, *Climate Stripes: Warming Stripes, Global 2020*, digital edition 2021, University of Reading Art Collection UAC/11018. Original time coverage **1850–2020**.
- University collection archive: https://collections.reading.ac.uk/letter-printing-graphicdesign-collections/explore/online-exhibitions/climate-stripes/
- Exact unmodified University image link: https://collections.reading.ac.uk/letter-printing-graphicdesign-collections/wp-content/uploads/sites/7/2021/10/UAC_11018-1200px.jpg
- University art collection states the stripes may be shared/copied/remixed/repurposed for any purpose, with original creator/source credit. Preserve this exact original distinct from newer HadCRUT5 figures.
- Authentic original only **linked for review**; not copied into the repo or transformed.

## Figure 02: 'The years turn red' (not yet author approved)

- Render: 1920×1920 PNG, SHA-256 **d483622ec69878d4a1810a4aa4192f9990c6184df5a67bf8d09f4b891bcfe58e**.
- Source: Met Office HadCRUT.5.2.0.0 analysis global annual 1850–2025, 176 contiguous complete annual observations. Original CSV copied without editing into `data/HadCRUT.5.2.0.0.analysis.summary_series.global.annual.snapshot_2026-10-19.csv`; its final 2026 partial-year observation is excluded from all derived figures.
- Upstream 19 October 2026 snapshot and source SHA-256 manifest at https://github.com/climate-resource/bookshelf-global-surface-temperature/tree/74218762d2d1dda92047a234360fa1d870d0857f/inputs/2026.10 ; recorded upstream source hash `7f750b673bb34aad722736ee21f122b5ea692c99877fa0b1066df65e51f32c04`.
- Plot inputs were rounded from original annual values to **four decimal places (0.0001°C)** for local deterministic rendering, with a cross-environment FNV32 fingerprint over all 176 annual triples: **4e628c81** matched against the original CSV fetched back from GitHub. The original unrounded file remains on branch.
- Native reference **1961–1990**; fixed diverging blue–red colour scale from −1.25 to +1.25°C; this is **not** an exact replica of official Reading/Berkeley image/palette.
- The 95% intervals in the line figure are the published 2.5–97.5% HadCRUT5 intervals, not point uncertainty invented by the renderer. 2025 estimate +1.0732167°C -> displayed +1.07°C.

## Figure 03: 'What the stripes leave out' (not yet author approved)

- Render: 1920×1920 PNG, SHA-256 **354dd9d5d341dc630953d783c342f2bd7f990beb21eef0b0a73c6b67ee2a634e**.
- Four panels: 2015–2025 actual source-year slices; the chosen fixed diverging colour scale; HadCRUT5 1980–2025 line and 95% bounds; comparison of identical 2025 observation on two baselines.
- 1961–2010 mean of annual HadCRUT5 anomaly values (native reference 1961–1990) = **+0.18100777836°C**; 2025 rebased to 1961–2010 mean = **+0.89220892164°C**, displayed **+0.89°C**, compared with **+1.07°C** against native baseline.
- A different zero is a change in reference, not a change in measured temperature.

## QA gate and remaining work

- Render: both 1920 square, light grey #F3F4F6, house-like Inter fallback (Space Grotesk/IBM Plex unavailable locally), no fake original, data-true layout and metadata.
- First render had title/subtitle collision; revised and **actual final PNG pixels inspected** after rerender. Final headings, panel dividers, annotations, axes, 2025 endpoint and source lines appear non-overlapping at full resolution. Source typography/footers will need attention in browser 320/390px tests.
- Preview files and reproducible local renderer remain in the author conversation, **not in repository**. GitHub site asset copying must reproduce exact approved hash or author must reapprove differing pixels.
- Next: author reviews all 3 visuals. If approved, stage exact PNGs (and attributable original or linked artefact), render script, captions/accessible alt and site draft; run Jekyll/Chrome mobile+desktop tests. Do NOT merge/deploy until a separate explicit approval.

Data terms: https://www.metoffice.gov.uk/hadobs/hadcrut5/terms_and_conditions.html (Open Government Licence v3) and Morice et al., JGR Atmospheres, 2021, doi:10.1029/2019JD032361. Required full Met Office licence acknowledgement goes in website methodology once copy is staged.
