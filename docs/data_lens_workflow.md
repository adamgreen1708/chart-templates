# Data Lens workflow

## Daily series

Data Lens is the home for short visual thinking about charts, data and communication.

- **Today’s Data Lens** is the dated daily edition.
- **Resources** are a separate top-level site section for evergreen guides and reference material.

The two sections can share the same palette, accessibility expectations and repository review model, but Resources should not be presented inside the Data Lens landing page.

## Daily publishing flow

```text
ChatGPT scheduled task
  → resolve Europe/London date
  → research and verify one idea
  → freeze copy and sources
  → render and inspect one square card
  → create dated GitHub branch
  → commit edition Markdown + PNG
  → open draft pull request
  → stop

Adam reviews and merges
  → GitHub validates and deploys
  → edition appears in Data Lens
```

The daily trigger must not push to `main` or merge its own pull request.

## Expected daily files

```text
site/_data_lens/YYYY-MM-DD-slug.md
site/assets/data-lens/daily/YYYY-MM-DD-slug.png
```

Routine editions must not change the canonical specification, layouts, CSS, validators, workflows, resource pages or earlier editions.

## Resource publishing flow

Resources live under `site/resources/`. The current 13-card guide keeps its image assets under `site/assets/data-lens/resources/`; future resource assets can be organised under the Resources section when needed. Resource changes are deliberate releases, not part of the daily Data Lens automation, and use a focused pull request plus the same GitHub Pages build check.

## Review from iPhone

1. Open the draft pull-request link from the ChatGPT task notification.
2. Confirm the image, copy, sources and green validation check.
3. Mark the pull request ready if desired.
4. Merge only when satisfied.
5. Allow GitHub Pages a few minutes to deploy.
