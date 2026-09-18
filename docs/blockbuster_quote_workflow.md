# Today’s Blockbuster Quote workflow

## One recurring process

The enabled ChatGPT task is the only daily trigger. GitHub does not run a second research task and there is no separate image-only automation.

```text
ChatGPT scheduled task
  → verify date, film, quote and context
  → render deterministic square card
  → create dated GitHub branch
  → commit edition Markdown + PNG
  → open draft pull request
  → stop

Adam reviews and merges
  → GitHub validates and deploys
  → edition becomes live
```

## Ownership

- `spec/series/blockbuster-quote.md` is the canonical prompt and publishing contract.
- The ChatGPT automation executes the prompt and opens the draft pull request.
- GitHub Actions validates and builds; it does not research or invent content.
- Adam is the publishing approval. No automation may merge.

## Expected daily files

Each draft pull request contains exactly:

```text
site/_blockbuster_quotes/YYYY-MM-DD-film-slug.md
site/assets/blockbuster-quote/YYYY-MM-DD-film-slug.png
```

Routine daily runs must not change the canonical prompt, renderer, layouts, CSS, workflows or earlier editions.

## Failure behaviour

The run fails closed when evidence, rendering or GitHub delivery is uncertain. It must not:

- substitute another date;
- publish an unverified quote;
- create duplicate branches or editions;
- push to `main`;
- merge a pull request;
- fall back to a standalone image that bypasses repository review.

After a failure, fix the cause and rerun deliberately. Do not create a second recurring task.

## Review from iPhone

1. Open the draft pull-request link from the ChatGPT task notification.
2. Confirm the card, copy, sources and green validation check.
3. Mark the pull request ready if desired.
4. Merge only when satisfied.
5. Allow GitHub Pages a few minutes to deploy.
