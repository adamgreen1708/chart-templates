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
