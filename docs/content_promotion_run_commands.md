# Coffeetableviz — promotion run commands

The repository source of truth for this workflow is docs/content_promotion_workflow.md. This is a **manual, approval-first** process. The website is on GitHub Pages, not WordPress. Neither of the commands below publishes a LinkedIn post, creates a new daily series edition, or commits a site change.

## One-click command: build this week's LinkedIn drafts

Use @GitHub and prepare this week's Coffeetableviz LinkedIn promotion candidates.

Before proposing anything, read docs/content_promotion_workflow.md and data/promotion/content_index.csv, data/promotion/pilot_queue.csv, and data/promotion/blockbuster_events.csv from the current main branch of adamgreen1708/chart-templates. Treat those as the working promotion seed and re-read the current source pages or series files for every proposed item. Check relevant dates, data snapshots, originality and image rights. Resolve the current public site URLs from front matter and verify mobile-readable imagery.

Present **two** candidates for the week (one practical/resource and one culture/story), each with a distinct LinkedIn opening hook, finished UK-English post copy, source article, specific approved visual or asset path, intended link and any material verification required. Do not present unverifiable claims as facts; do not silently substitute a different dataset or regenerate daily cards. Show for approval **without** posting to LinkedIn, modifying GitHub, scheduling tasks or claiming the drafts are published. If a candidate is unsuitable, propose a grounded replacement from the existing library.

## One-click command: find a date-led resurface

Use @GitHub to find a relevant date-led opportunity for Coffeetableviz.

Read the current Blockbuster source records from site/_blockbuster_quotes and data/promotion/blockbuster_events.csv alongside docs/content_promotion_workflow.md and the main article catalogue. Resolve the current date in Europe/London. Look for a verifiable upcoming birthday, exact film-release anniversary with territory, or clearly identified seasonal opportunity that honestly connects to an *existing* article. Prefer exact actor or franchise connections to loose associations. Recheck the date source; never imply the source Blockbuster card was created today if it was not. Produce one optional LinkedIn draft plus a grounded rationale and article URL for review. If nothing is genuinely relevant, say so and offer an evergreen resource instead. Do not change any GitHub files, render new daily editions or post automatically.


## One-click command: review newly indexed material

Use @GitHub to review the newest Coffeetableviz promotion-library entries.

Read docs/content_promotion_workflow.md and the current data/promotion/content_index.csv and data/promotion/blockbuster_events.csv on main. Identify new entries marked priority REVIEW or evergreen_class unclassified, and any Blockbuster additions with an empty article match. Read their actual source pages and source evidence; assess an appropriate evergreen/freshness class, promotion priority, two differentiated hook ideas, relevant calendar links (if any) and material preflight risks. **Do not fabricate related films, birthdays or audience reach.** Show the editorial decisions for approval. Only after explicit approval should you make a branch/commit/PR to enrich the CSV; do not write to main directly or publish to LinkedIn.

## After publication — voluntary measurement update

Only after the user confirms the LinkedIn publication, request the actual LinkedIn post URL and any available impressions, clicks, saves and engagement counts. Update data/promotion/promotion_log.csv **via a reviewable PR**, with measured values and clear reporting dates. Do not backfill or estimate missing metrics.

At the end of the four-week pilot, compare which formats and hooks reached meaningful audiences and generated attributable traffic. Refine the library and queue on a proposed PR, not on main without review.
