# Beck Edition 02 — rendered Jekyll layout QA
Browser test: https://github.com/adamgreen1708/chart-templates/actions/runs/37970512954

These five PNG screenshots are **review-only previews** of the unpublished Edition 02 branch, not published site artwork. They were captured automatically with Playwright Chromium/Google Chrome after a successful Jekyll build.

| Screenshot | Viewport |
|---|---|
| `beck-article-desktop.png` | 1365 × 960 desktop |
| `beck-article-mobile.png` | 390 × 844 mobile |
| `beck-article-small-mobile.png` | 320 × 680 narrow mobile |
| `beck-resource-mobile.png` | 390 × 844 Resources collection |
| `beck-home-mobile.png` | 390 × 844 homepage/latest story |

Automated assertions passed:
- Both approved 1920-pixel images load and decode in browser (lazy image loading explicitly accounted for).
- No horizontal page overflow or clipped headline at 1365, 390 and 320 px.
- The original 1933 artwork is linked to London Transport Museum, **not copied** into the post.
- Series eyebrow displays with original small-site font size; not enlarged by post first-paragraph styling.
- Resources collection contains both the Minard and Beck article links.
- Homepage's latest story and feature art correctly resolve to approved Beck images.
- Jekyll built successfully; final live deployment intentionally not performed.

Screenshots are transient QA evidence, not copies of Beck's 1933 historical map. Do not infer website is live from these pictures.
