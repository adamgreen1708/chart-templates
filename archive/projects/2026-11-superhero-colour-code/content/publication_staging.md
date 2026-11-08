# Publication staging notes — 8 November 2026

**Status:** Route 2 qualitative publication ready for final PR review. Jekyll `published: true` is staged **on the PR branch only**; nothing is live until the PR is explicitly approved and merged.

- Jekyll post: `site/_posts/2026-11-08-who-wears-the-hero-colours.md` (subject category `Culture`).
- Feature/card image: **approved V3 chart 1**; reused as the header illustration so it is not duplicated in the body. Images 2 and 3 appear as centred responsive `figure.story-chart` blocks with descriptive alt text and captions.
- Reference table under colour wheels is the **same 24-character, 12-row Markdown table** checked into `content/blog_draft_v3.md`, generated from the GitHub colour-wheel dataset. Existing site CSS makes tables horizontally scrollable on phones.
- Three website PNGs must be copied as **identical binary blobs** from `archive/projects/2026-11-superhero-colour-code/output/superhero_v3_*.png`. Do not re-render or regenerate approved visuals for publication staging.
- Editorial text keeps all three approved hooks: line-up → colour wheels → five matched hue pairs. Number claims apply only to this selected 24-character pilot. The method note explicitly discloses incomplete comic-art verification.
- Detailed evidence: `data/publication_source_review_2026-11-08.csv` and `content/publication_readiness.md`; zero issue-specific image approvals, high-risk rows still open **and disclosed** under the qualitative-publication approach.
- Jekyll publication PR must remain unmerged until Adam explicitly approves the final publication. **Route 2 allows qualitative release despite outstanding art checks because the limitations are plainly stated in the article.**
- No data recoding or V3 chart replacement was made in the publication package. No direct main merge or Pages deployment.

## Actual GitHub QA outcomes (8 November 2026)

- [Standard Jekyll Pages PR build](https://github.com/adamgreen1708/chart-templates/actions/runs/42482331546): passed; deploy correctly skipped for PR.
- [Source-driven publication-package test](https://github.com/adamgreen1708/chart-templates/actions/runs/42482466222): passed (approved PNG binary equality, 24 row/twelve table-line mapping, unpublished flag, `Culture` category and source-review status).
- [Full disposable Jekyll article build](https://github.com/adamgreen1708/chart-templates/actions/runs/42482709147): passed **after** adding accessible figure captions with the literal approved chart 2 and 3 titles. This test temporarily changes the article copy to `published: true` **only inside the GitHub runner**, builds the Jekyll site, checks that actual HTML contains all three images and the cast table, and discards the test workspace. **At the time of this earlier test the PR post remained `published: false`; Route 2 has since set it to `published: true` on the branch.**
- The one-off workflow files were removed after their successful runs; the reproducible `tests/test_superhero_publication_staging.py` remains committed to the project.
- **New high-impact art finding:** `content/high_impact_art_review.md` pinpoints Sinestro Corps Special #1 and issue candidates for Magneto/Thanos. Yellow-dominant Sinestro is *not validated*. Reclassifying it as black would change the villain count and remove one currently charted paired match.

**Updated editorial decision: prepared for qualitative publication under Route 2. No merge without final explicit Adam approval.**

## Route 2 editorial approval — 8 November 2026

- Adam selected publishing as a **curated qualitative exploration** rather than insisting on 24 individually image-verified colour measurements. Counts describe **manually coded selected costume versions only**, not a random Marvel/DC sample.
- The live-site Jekyll flag is set to `published: true` **only in PR #196**. No main branch merge or GitHub Pages deployment is authorised by this preparation.
- The source image art-validation flags and confidence remain candidly incomplete; they are separate from accepting an exploratory article. Sinestro's leading yellow versus black stays low-confidence.
- Existing charts and the table are untouched. Re-run the publication-package tests and GitHub Pages build before asking for merge approval.

## Route 2 final technical QA — 8 November 2026

- [Publication-ready qualitative article QA](https://github.com/adamgreen1708/chart-templates/actions/runs/42484846910) — **passed**. Tests verified the `published: true` Jekyll flag in PR branch, `Culture` category, all three approved PNGs as binary-identical to the archive assets, the 24-source/12-table-row sequence, and honest caveats. A real Jekyll site build rendered the final article with its three chart images and character table.
- [Regular coffeetableviz Pages PR build](https://github.com/adamgreen1708/chart-templates/actions/runs/42484802857) — **passed**. PR build only; no deployment.
- The 24-character dataset remains manually coded and not independently verified as an exact-area measurement. Fourteen rows retain high-risk audit flags, and Sinestro stays editorially yellow-dominant at low confidence. Route 2 explicitly accepts these documented limitations for a qualitative story.
- **No approval to merge has been given in this preparation step.** Publish only after Adam explicitly approves the reviewed PR.
