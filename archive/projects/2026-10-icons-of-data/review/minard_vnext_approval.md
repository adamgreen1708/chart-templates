# Minard chart 02 — approved house-vNext migration

**Author approval:** 30 October 2026, in the ChatGPT chart review conversation.

The author approved the 1600 × 1600 chart and 390px/320px previews displayed inline in the review. The replacement PNG was copied byte-for-byte from the previously successful GitHub Actions render, [run 41140184070](https://github.com/adamgreen1708/chart-templates/actions/runs/41140184070), artifact `minard-vnext-phone-review`. **It was not regenerated for publication.**

- Approved PNG SHA-256: `970985bd18cead8727057a8b7d85fb83876890b4170fe8fa34eec3ed7306e22c`
- Approved Git blob: `2c1af63849164e734716d62a05ef4773321cfb2d`
- Site asset: `site/assets/icons-of-data/minard/02_shrinking_army.png`
- Previous original preserved exactly at `archive/projects/2026-10-icons-of-data/legacy/02_shrinking_army_2026-10_original.png`
- Previous original Git blob: `404cd6665f4fb1e558dd1280daf4c5ab9c63b12b`

The original 51 troop-route records, 20 cities and nine temperature records remain in GitHub unchanged. The migration preserves line-width proportionality to estimated troop strength, three outward/retreat route groups, historic degrees Réaumur, missing-date uncertainty and approximate plotted map positions. It does **not** interpret route width as a death toll.

The new renderer is `src/editorial_minard.py`, registered as `minard_campaign` through the shared renderer. Its review config and data integrity tests are preserved in GitHub. The temporary one-off staging workflow was removed after successfully committing the exact approved image on PR #166.
