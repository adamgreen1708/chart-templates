# Today’s Data Lens

Status: live recurring-series specification.

## Purpose

Publish one concise, accurate and visually useful observation about charts, data, visualisation, communication, numbers or analytical thinking. Each edition should be readable in under one minute and make one idea—not a bundle of tips.

## Publishing contract

Each daily edition lives in `site/_data_lens/` and contains:

- the exact Europe/London run date;
- one verified title, observation and closing line;
- direct source links for factual or research-based claims;
- explicit QA sign-off flags;
- one finished square image;
- accessible HTML text matching the image.

The repository validator must pass before Jekyll builds the site. If a factual, logical, arithmetic, comparison, chart or rendering gate fails, no edition is committed.

## Review model

1. The enabled ChatGPT task reads this specification from `main` and checks for an existing edition for the run date.
2. ChatGPT researches several candidate ideas and selects one with a strong, supportable observation.
3. Claims, comparisons, units, scales, labels, arithmetic and sources are checked before copy is frozen.
4. The final card is rendered and inspected at full size.
5. The task commits only the dated edition Markdown and PNG to `automation/data-lens-YYYY-MM-DD`.
6. The task opens a draft pull request and stops.
7. GitHub validates and builds the site.
8. Adam reviews; only Adam’s merge publishes the edition.

## Edition front matter

```yaml
---
date: 2026-09-19
header: "TODAY’S DATA LENS"
title: "One clear observation."
observation: "Two or three concise sentences containing only verified claims."
kicker: "A short closing line containing no new factual claim."
hero_image: "/assets/data-lens/daily/2026-09-19-edition-slug.png"
hero_alt: "Accessible description of the complete editorial card."
sources:
  - title: "Primary or authoritative source title"
    url: "https://example.com/source"
qa:
  run_date_verified: true
  claim_verified: true
  sources_verified: true
  copy_deck_frozen: true
  render_checked: true
---
```

## Daily-run rules

- Resolve and freeze the current date from Europe/London before research.
- Research fresh candidates; do not reuse stale copy or an old render.
- Prefer primary sources, official datasets and original research.
- Keep source definitions, time periods, geographies and units comparable.
- Reproduce arithmetic and inspect chart axes, labels, baselines and encodings.
- Use deterministic typography and layout for all factual text.
- Render exactly one square publication image.
- Read every visible word, date, number and source line after rendering.
- Reject clipping, overlap, malformed text, inconsistent scales or changed copy.
- Never push to `main`, merge, or bypass repository review with a standalone image.

## Expected daily delivery

Create exactly two files:

```text
site/_data_lens/YYYY-MM-DD-slug.md
site/assets/data-lens/daily/YYYY-MM-DD-slug.png
```

Open one draft pull request titled `Add Data Lens — TITLE (YYYY-MM-DD)` and return its link. No routine daily run may modify the specification, validator, layouts, CSS, workflow files, resource pages or an earlier edition.
