# Today’s Data Lens

Status: live recurring-series specification.

## Purpose

Publish one concise, accurate and visually useful observation about charts, data, visualisation, communication, numbers or analytical thinking. Each edition should be readable in under one minute and make one idea—not a bundle of tips.

## Required inspiration/reference pass

Before general candidate research, read `spec/series/data-lens-reference-sources.md` from `main` and complete its required daily reference pass. The curated panel is the default inspiration layer for Today’s Data Lens: use it to seed ideas about chart craft, perception, statistical interpretation, communication, encoding and analytical thinking.

The reference panel is an **idea source, not a substitute for verification**. Any empirical claim, current statistic or historical fact in the finished edition must still be checked against a primary, official or otherwise authoritative source.


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
2. ChatGPT reads `spec/series/data-lens-reference-sources.md`, completes the required reference pass, researches several candidates and selects one with a strong, supportable observation.
3. Claims, comparisons, units, scales, labels, arithmetic and sources are checked before copy is frozen.
4. The final card is rendered, then the actual final PNG is opened and inspected at full size. The inspection must cover every text block, axis and tick label, caption, annotation, panel boundary, divider, source line, footer and outer safe margin. Any clipping, overlap, collision, truncation, unreadable text or unsafe edge clearance is a render failure and requires a rerender followed by another inspection.
5. `qa.render_checked` may be set to `true` only after that final-pixel inspection passes. Code execution, image dimensions, calculated bounding boxes or inspection of an earlier/intermediate render do not satisfy this gate.
6. The task commits only the dated edition Markdown and PNG to `automation/data-lens-YYYY-MM-DD`.
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
- Complete the required reference pass in `spec/series/data-lens-reference-sources.md` before choosing the topic; then research fresh candidates and do not reuse stale copy or an old render.
- Prefer primary sources, official datasets and original research.
- Keep source definitions, time periods, geographies and units comparable.
- Reproduce arithmetic and inspect chart axes, labels, baselines and encodings.
- Use deterministic typography and layout for all factual text.
- Render exactly one square publication image.
- Open and inspect the actual final PNG at full size after rendering. Do not treat renderer success, dimensions, geometry calculations or an earlier preview as visual QA.
- Read every visible word, date, number and source line in that final PNG.
- Check every text block, axis/tick label, caption, annotation, chart mark, panel boundary, divider, source line, footer and outer safe margin for clearance.
- Reject and rerender for any clipping, overlap, collision, truncation, malformed text, unreadable text, unsafe edge clearance, inconsistent scale, changed copy or element touching/crossing a boundary it should not touch.
- After any rerender, repeat the full final-pixel inspection from the beginning.
- Set `qa.render_checked: true` only after the actual final PNG passes this inspection. If the inspection cannot be performed, fail the run rather than presenting or publishing the edition.
- Never push to `main`, merge, or bypass repository review with a standalone image.

## Expected daily delivery

Create exactly two files:

```text
site/_data_lens/YYYY-MM-DD-slug.md
site/assets/data-lens/daily/YYYY-MM-DD-slug.png
```

Open one draft pull request titled `Add Data Lens — TITLE (YYYY-MM-DD)` and return its link. No routine daily run may modify the specification, validator, layouts, CSS, workflow files, resource pages or an earlier edition.
