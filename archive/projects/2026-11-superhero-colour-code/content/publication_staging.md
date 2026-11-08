# Publication staging notes — 8 November 2026

**Status:** site-ready *draft structure* only. `published: false` is deliberate; **not authorised for site release**.

- Jekyll post: `site/_posts/2026-11-08-who-wears-the-hero-colours.md` (subject category `Culture`).
- Feature/card image: **approved V3 chart 1**; reused as the header illustration so it is not duplicated in the body. Images 2 and 3 appear as centred responsive `figure.story-chart` blocks with descriptive alt text and captions.
- Reference table under colour wheels is the **same 24-character, 12-row Markdown table** checked into `content/blog_draft_v3.md`, generated from the GitHub colour-wheel dataset. Existing site CSS makes tables horizontally scrollable on phones.
- Three website PNGs must be copied as **identical binary blobs** from `archive/projects/2026-11-superhero-colour-code/output/superhero_v3_*.png`. Do not re-render or regenerate approved visuals for publication staging.
- Editorial text keeps all three approved hooks: line-up → colour wheels → five matched hue pairs. Number claims apply only to this selected 24-character pilot. The method note explicitly discloses incomplete comic-art verification.
- Detailed evidence: `data/publication_source_review_2026-11-08.csv` and `content/publication_readiness.md`; zero issue-specific image approvals, high-risk rows unresolved.
- Jekyll publication PR must stay **draft** until art checks are finished and Adam explicitly approves changing `published: false` to `published: true`.
- No data recoding or V3 chart replacement was made in the publication package. No direct main merge or Pages deployment.

## Actual GitHub QA outcomes (8 November 2026)

- [Standard Jekyll Pages PR build](https://github.com/adamgreen1708/chart-templates/actions/runs/42482331546): passed; deploy correctly skipped for PR.
- [Source-driven publication-package test](https://github.com/adamgreen1708/chart-templates/actions/runs/42482466222): passed (approved PNG binary equality, 24 row/twelve table-line mapping, unpublished flag, `Culture` category and source-review status).
- [Full disposable Jekyll article build](https://github.com/adamgreen1708/chart-templates/actions/runs/42482709147): passed **after** adding accessible figure captions with the literal approved chart 2 and 3 titles. This test temporarily changes the article copy to `published: true` **only inside the GitHub runner**, builds the Jekyll site, checks that actual HTML contains all three images and the cast table, and discards the test workspace. **The PR post remains `published: false`.**
- The one-off workflow files were removed after their successful runs; the reproducible `tests/test_superhero_publication_staging.py` remains committed to the project.
- **New high-impact art finding:** `content/high_impact_art_review.md` pinpoints Sinestro Corps Special #1 and issue candidates for Magneto/Thanos. Yellow-dominant Sinestro is *not validated*. Reclassifying it as black would change the villain count and remove one currently charted paired match.

**Editorial decision: ready as a technical publication draft, *not* ready to merge as a factual publication.**
