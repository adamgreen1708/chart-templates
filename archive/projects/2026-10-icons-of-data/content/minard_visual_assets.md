# Minard publication asset register

Status: **both reviewed PNGs approved editorially; binary upload to GitHub outstanding.** No site publication approval given.

## Exact reviewed PNG files
| Jekyll static path | Pixel dimensions | SHA-256 |
|---|---:|---|
| `site/assets/icons-of-data/minard/02_shrinking_army.png` | 1920 × 1920 | `d773841188e51026f423060214daf98daa06197d9733028732d652a563b078bb` |
| `site/assets/icons-of-data/minard/03_decode_the_icon.png` | 1920 × 1920 | `e6505c2326f3ba431d59ee698adc47bcc95ca71e22ac0fbeb78cadbfed5efca6` |

These were approved in the Icons of Data visual review on 8 October 2026.
The exact PNGs and their rendering script/data are bundled in the **Icons of Data Minard site-ready assets ZIP**, delivered in the same ChatGPT conversation. Keep them unchanged; do not recreate/recompress without a new visual QA.

The current GitHub connector only supports UTF-8 text file writes or encoded blob content, and cannot consume local binary source files directly. Therefore the exact binary PNGs are **not in this PR yet**. This is a real publication blocker.

## Historical original
`https://commons.wikimedia.org/wiki/File:Minard.png`

Current site draft hotlinks the stable Commons file image `https://upload.wikimedia.org/wikipedia/commons/2/29/Minard.png`, with explicit public-domain credit and links to source metadata. Do not substitute a modern redraw without attribution/permission checks.

## How the site handles incomplete assets
The staged Minard Jekyll article uses `site.static_files` tests. Its two modern figures are displayed only when their expected PNG files exist, otherwise it displays honest review placeholders. This avoids invisible broken images but **does not constitute publication QA**.

## Before any merge
1. Upload the two exact PNGs to the paths above and confirm hashes.
2. Supply story-specific approved card/hero artwork consistent with `spec/feature_image_rules.md`; the historical original currently carries the page's introductory visual.
3. Run the Jekyll build and check output URLs/assets, metadata, mobile layout, captions, alt text and keyboard filtering.
4. Compare PR against current main (no unrelated changes).
5. Request explicit authorisation before merging or publishing to GitHub Pages.
6. After merge, verify Pages deploy and live URLs.

**Do not merge PR #107 in its present incomplete form.**
