# Coffeetableviz house-vNext migration plan

**Decision:** Adam approved the new chart identity and phone QA on 30 October 2026. The normal **new** chart production path is `render_profile="social_square"`. There is no separate production social-rendering workflow: the shared GitHub renderer is used for both the blog and social media. Old `standard` configs survive only to keep already-published images reproducible.

## What is and is not excluded from normal rendering

- **Included:** all ordinary production `archive/projects/*/config/*.py` configs (except those prefixed `social_`), including new configs that specify the vNext house profile.
- **Excluded:** three original experimental `social_*.py` files created in October for side-by-side previews. They remain test fixtures and are rendered by `.github/workflows/qa-social-profile.yml`, never copied automatically into the public site assets.
- **Not migrated automatically:** old published charts and custom standalone Matplotlib scripts. They need explicit data checks, a centrally configured renderer and a new image review before swapping links.

## Migration order and scope

1. **Florence Nightingale** — source: `archive/projects/2026-10-icons-of-data/editions/04-nightingale/scripts/render_nightingale.py`. Preserve the verified 24-month series, units, colours and historical caveats. Move the selected `02_what_the_numbers_reveal.png` to a normal CHART_CONFIG-backed type, using central header, plot, palette semantics, safe frame and footer.
2. **Ed Hawkins** — source: `archive/projects/2026-10-icons-of-data/editions/07-hawkins/scripts/render_hawkins_review.py`. Preserve pinned HadCRUT5 dataset, anomaly reference period, uncertainty interval and the scientifically meaningful warming-stripe colour scale. Reuse the central typography/frame; treat the two-panel stripes + trend as a specialist renderer, not a simple line chart.
3. **Charles Joseph Minard** — source: `archive/projects/2026-10-icons-of-data/scripts/render_minard.py`. Preserve digitised troop routes, directional width encoding, temperature series, geographically approximate positions and source notes. Add a reusable ribbon/route chart type to the GitHub renderer rather than discarding bespoke geometry.

## Per-chart acceptance gates

- Use verified original data and pinned source references; compare data-derived values between original and new chart.
- Add regular production CHART_CONFIG and a centrally styled specialist renderer only when the standard chart types are insufficient.
- Keep canvas `#F3F4F6`, approved vNext title/subtitle/footer hierarchy and equal outer padding; do not force historic blue/beige/black colours to arbitrary brand colours when they encode data.
- Produce full-size plus 390px and 320px PNG previews through GitHub Actions, and show images **inline in ChatGPT**, not as inaccessible ZIP-only references.
- Inspect four-edge margins, white plot patches, text collisions, axes/footer clearance and source attribution.
- Get explicit approval of each replacement image. Only then change published `site/assets/icons-of-data/*` assets through branch/PR; archive and preserve original source files and references.
- Do not batch-retrofit unrelated archival projects or silently change existing published images.

## Rollout checkpoints

A. Promote the approved vNext house layout as the default of `src/chart_config_template.py` and chart-config generation guidance (this branch).

B. Migrate Nightingale, review and approve, then publish.

C. Migrate Ed Hawkins, review and approve, then publish.

D. Migrate Minard, review and approve, then publish.

E. Audit subsequent independent chart scripts; either migrate them or document a necessary scientific/technical exception while retaining the shared outer layout.

Published originals remain unchanged until their individual approval. New charts always start with the vNext house style.
