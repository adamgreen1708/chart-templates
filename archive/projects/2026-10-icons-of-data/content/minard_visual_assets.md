# Minard publication asset register

Status: **both exact approved PNGs present on PR #107 branch and verified by SHA-256 in GitHub Actions**. No site publication approval given.

## Approved PNGs — committed to GitHub
| Site static path | Dimensions | SHA-256 |
|---|---:|---|
| `site/assets/icons-of-data/minard/02_shrinking_army.png` | 1920 × 1920 | `d773841188e51026f423060214daf98daa06197d9733028732d652a563b078bb` |
| `site/assets/icons-of-data/minard/03_decode_the_icon.png` | 1920 × 1920 | `e6505c2326f3ba431d59ee698adc47bcc95ca71e22ac0fbeb78cadbfed5efca6` |

These are the exact reviewed images from 8 October 2026, not a stylistically similar substitute.

An on-branch, **temporary GitHub Actions job** rendered the archived deterministic Python script with pinned reference package versions and compared each generated PNG's SHA-256 to the approved image before committing. The job completed successfully: https://github.com/adamgreen1708/chart-templates/actions/runs/37841911808.

The temporary workflow was then removed from the branch. The reusable rendering script remains at `archive/projects/2026-10-icons-of-data/scripts/render_minard.py`, and source data at `archive/projects/2026-10-icons-of-data/data/`.

The article references both verified assets at their permanent site paths. Its Jekyll conditionals also avoid missing-image placeholders if assets were deleted inadvertently.

## Original historical artwork
Original 1869 chart: https://commons.wikimedia.org/wiki/File:Minard.png

The original work is identified as public domain and attributed on the draft Resources and story pages. Both currently point to Wikimedia's stable hosted scan; consider a self-hosted copy in a future maintenance update to avoid hotlink dependence, with original credit retained.

## Metadata
The approved, story-specific `02_shrinking_army.png` is used as both card and social preview artwork. It conveys the shrinking band, has light-grey background and the story-specific caption and alt text. The story's hero visual is the attributed original map within the article (not a duplicated lead image).

## Still to QA before merge
1. Confirm latest Jekyll PR build succeeds after the asset commits.
2. Test mobile and desktop rendering, external original image loading, full-size modern graphics, alt text and keyboard-operated encoding filters.
3. Recompare the final branch against the latest `main` and confirm only intended changes.
4. Explicit author approval to merge PR #107 (nothing has been published yet).
5. Once approved and merged, verify Pages deployment and live URLs.
