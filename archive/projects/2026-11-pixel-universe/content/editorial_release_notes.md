# Pixel Universe — editorial sequel publication checklist

**Status:** editorial draft only. PR stacked after the *gallery* draft PR #200. No site post is enabled or published here.

## Intended publication

- Working title: **Pixel Universe: can you recognise a superhero in 256 squares?**
- Recommended subject category: **Culture** (aligning to the published superhero colour post); tags might include `superheroes`, `comics`, `pixel-art`, `colour`, `design`.
- Proposed path: `/stories/pixel-universe-256-squares/` (only after the eventual site PR is approved and merged).
- Canonical follow-on from `/stories/who-wears-the-hero-colours/`.
- Main interactive CTA: `/resources/pixel-universe/`.
- Exact editorial body: `editorial_draft.md`.
- Draft social copy: `social_copy.md`.

## Needed before an article PR can be approved

1. Gallery and artwork stack PRs #198 → #199 → #200 must be reviewed, merged in order if approved, and deployed/verified. Do not merge while any are unapproved.
2. Run reproducible gallery builder and four pytest suites (CI PR #200), plus actual 320px/390px browser QA and visual screenshot inspection.
3. Feature-art review under `spec/feature_image_rules.md`. The archived mosaics are square but contain multicolour sprites and **embedded text**; they are suitable as article figures but should not silently be promoted to the locked black/charcoal/red text-free feature style. Agree a story-specific illustration (such as one recognisable, original monochrome pixel silhouette facing an incomplete palette) before enabling the story.
4. Prepare `site/_posts/YYYY-MM-DD-pixel-universe-256-squares.md` only after selecting the publication date and reviewing final copy. Set `published: false` in the unmerged publication PR, verify content, metadata, responsive inline figures, source notes, links and feature image. Enable and merge only after explicit approval.
5. Verify the actual GitHub Pages deployment succeeded and open the final story/gallery URLs; do not call them live from a draft branch.
6. Do not change the published `site/_posts/2026-11-08-who-wears-the-hero-colours.md` or use unmerged evidence PR #194 as canonical source.

## Data-to-story checks

- **12 icon portraits**, each a **16×16** code = 256 cells, with **six heroes and six villains**.
- Colour fields pulled from the existing published 24-character qualitative set. Artwork silhouettes, outlines and decorative pixels are human-directed creative decisions, not fabric measurements.
- All twelve entries and source-exact editable codes remain in `site/_data/pixel_universe.yml`.
- Avoid phrasing that would imply tested recognition ability or representative character-colour statistics.
