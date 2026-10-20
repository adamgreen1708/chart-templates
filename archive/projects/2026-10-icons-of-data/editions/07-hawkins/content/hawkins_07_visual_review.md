# Icons of Data #07 — GitHub Actions visual review

**Status:** Three actual GitHub-rendered 1920×1920 square author-review graphics produced and pixel-inspected. The previous local renders are *superseded*, and their SHA-256 references are no longer candidates for publication. **Author's approval of these exact GitHub image bytes is outstanding. No site changes or merge/publish authorisation.**

## Author-review files (all on draft PR #138)

Historical edition retained separately:
- `qa/visuals/01_reading_global_2020_original_unmodified.jpg` — 1200×675 untouched University of Reading UAC/11018 artwork, 1850–2020. SHA-256 `64ac4a7b3ed36fc7448b107caa4b6c222005013862ecf017947e24ad4d16f07f`. Acquired on GitHub runner from https://collections.reading.ac.uk/art-collections/wp-content/uploads/sites/2/2021/10/UAC_11018-1200px.jpg. University history/rights: https://collections.reading.ac.uk/art-collections/2021/12/20/show-your-stripes-the-artwork-that-made-climate-change-data-go-viral/ (CC licence and creator attribution).
- `qa/visuals/01_the_original_warming_stripes.png` — editorial 1920×1920 frame containing unaltered source artwork without cropping/recolouring, attributed; SHA-256 `11d7328cbda28a87a1fe43a1e6e99a286454d99d01b78db4d58baea518f3f480`.
- `qa/visuals/02_the_century_shifts_colour.png` — independent Met Office-derived 1850–2025 reconstruction with same-source annual time-series and published 95% range; SHA-256 `cc74466aa9d4bb80f8b9fda6b7f2aeec44a2577d09b67105da5994d87bc42a97`.
- `qa/visuals/03_decode_the_icon.png` — four genuinely populated panels on annual slots, diverging temperature colour, actual anomaly/uncertainty and reference-period changes; SHA-256 `b5eaac606edd53251cc86468a78da17658e16ae855b7be535f56dd7789ca0959`.
- All three have 600/390/320px actual-downsampled QA previews. Machine-generated `qa/render_manifest.json` retains full hashes, numeric assertions and source details.

## Reproducibility / verification

- **GitHub Actions final successful renderer/QA run:** https://github.com/adamgreen1708/chart-templates/actions/runs/39505109952 . Two preliminary runners caught or addressed a Figure 03 panel-background occlusion, Figure 02 2025 endpoint label collision, and lower-right Figure 03 edge clearance; **only the final run's hashes above are the approved-candidate baseline**.
- Reproducible repo script: `scripts/render_hawkins_review.py` (numpy 2.1.3, matplotlib 3.9.2, Pillow 11.0.0; DejaVu Sans on Ubuntu GitHub runner). These are GitHub Actions-generated images, **not local substitutes**.
- Dataset: original `data/HadCRUT.5.2.0.0.analysis.summary_series.global.annual.snapshot_2026-10-19.csv`, SHA-256 `7f750b673bb34aad722736ee21f122b5ea692c99877fa0b1066df65e51f32c04`. Source vintage HadCRUT.5.2.0.0, Met Office native baseline 1961–1990; 176 complete years 1850–2025, no partial-year 2026. Annual 2025 anomaly **+1.0732167°C**. 1961–2010 offset computed from the same source **+0.18100777836°C**. Modern colours use an explicitly fixed −1.25 to +1.25°C palette and are **not** a replica of the historical Reading/Berkeley palette.
- Verified final PNG SHA-256, 1920×1920 and 320/390/600 thumbnails on runner; downloaded the actual Actions archive and independently reproduced those hashes in the reviewer runtime. Actual three rendered pixels visually inspected: all four Figure 03 panels show data, text no longer overlaps or clips, Figure 02 2025 label clears its point, source notes/dividers/footers safe at full size. At 320px thumbnail the smallest methodological notes are very small: provide full accessible HTML captions/alt and tap-to-enlarge functionality on website; this is **still a site QA gate**, not a passed browser test.
- Met Office OGL v3.0 + Morice et al. (2021) full attribution required when the article is staged.

## Pending explicit approval

1. Author review **these exact three GitHub-generated graphics**; fix and GitHub-rerender any requested changes.
2. Only after image approval, draft Jekyll/Resources changes on PR and run actual browser/390px/320px checks with informative HTML captions, alt and image lightboxes. Do not silently rerender between approval and site staging.
3. Separate explicit approval to merge/deploy and verify live Pages.
