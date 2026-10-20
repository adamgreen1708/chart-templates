# Coffeetableviz Editorial Radar — planning protocol

**Status:** Proposed / review only. No automatic publication, no scheduled researcher and no change to the approved daily-series process.

## Why this exists

The promotion library answers **"what can we resurface?"**. The Editorial Radar answers **"what should we research next so an article is ready before a relevant occasion?"**

Keep these as two distinct datasets:

- `data/promotion/editorial_radar_events.csv`: *prospective* story occasions and research ideas, including ideas with no article yet.
- `data/promotion/content_index.csv`: *published* editorial content automatically discovered after its site PR merges.
- `data/promotion/blockbuster_events.csv`: *published* and separately verified Blockbuster editions. The Radar does not silently create dates, quotes or matching editions.

The **monthly snapshots** are in `docs/editorial_radar/YYYY-MM.md`. These are reviewable planning documents, not live pages under `site/`.

## Each month's article table

Each opportunity identifies:

- **An exact date**, or explicitly month-only evidence (the first of a month in the CSV is a sorting anchor, *not* a release date).
- **Type**: actor/musician birthday; death anniversary; film release; album release.
- **Historical event, territory and source links** for research verification.
- **What the next article might answer**, with a *question*, not a pretended discovery.
- **Data needed and feasible research route** (official IMDb non-commercial files when relevant, verified album track metadata, official charts where appropriate).
- **Mode**: resurface, new analysis, or a new article plus archive resurfacing.
- **Priority A/B/C** and a production status.
- **Whether an independent Blockbuster edition could connect**, without ever guaranteeing or requiring one.

The year count is arithmetical. Album month-only entries are never promoted as an exact date unless a reliable release source establishes one and the date type and territory are recorded.

## Suggested editorial preparation gates

| Gate | Meaning |
| --- | --- |
| candidate | Calendar idea; source date provisionally checked, no data analysis conducted |
| researching | Event scope and dataset access being investigated |
| data_verified | Real dataset inspected for source, missingness, comparability and reproducibility |
| chart_ready | Story discovery and proposed charts passed chart/visual QA |
| copy_ready | Article and optional LinkedIn angle written, source notes and images reviewed |
| approved | Explicit approval of the relevant finished outputs |
| published | GitHub Pages article verified live after approved PR; promotion library discovery follows |
| parked | Not viable or a stronger story was selected |

Do **not** advance a gate merely because the event date is approaching. Film release timing must identify the market and premiere vs general release; death anniversaries require an especially respectful, non-exploitative tone. One source in this candidate list does not satisfy the two-source Blockbuster production rule.

A practical target is **four weeks before the opportunity** to have the dataset scoped, **two weeks before** for chart editorial selection, and **one week before** for finished article/visual review. These are planning targets, not promises or scheduled tasks. Entries currently inside the four-week window are immediate research priorities, not overdue obligations.

Limit new analysis to roughly one substantial project per fortnight to avoid making 19 tentative dates into 19 artificial deadlines. A resurface can require far less work.

## Coordinating a main article with Blockbuster

**Example: a film-anniversary story**

- In advance: use verified IMDb non-commercial data to test whether a compelling three-chart story exists.
- Draft and QA the full chart/article as usual in a dedicated project, on a branch/PR.
- If the anniversary-date Blockbuster research finds a real film/performer connection and a reliable quote, create and QA its **separate daily edition** by following `spec/series/blockbuster-quote.md`.
- Only after both are independently approved and published: link the Blockbuster and article through a suitable caption, collection link or LinkedIn post.
- If no valid quote, do **not** manufacture one. The film anniversary can still support a site article and LinkedIn post.
- Never force the article to assert a result the data does not support.

**Example: David Bowie, January 2027**: the 80th birthday on 8 January and the 50th anniversary of *Low* on 14 January make a natural two-part editorial opportunity. One could be an accessible retrospective using existing Bowie work; the other a new, reproducible small-multiple analysis of *Low* against the verified neighbouring albums. Keep the actual release dates and current data scopes in view.

For **actor/death** dates, archive resurfacing is often enough. Do not create a new IMDb analysis just to fill a calendar slot.

## Discovery and monthly refresh — human researcher required

A deterministic script can **render and validate known events**; it cannot autonomously discover reliable new birthdays or release dates. The CSV is a **curated shortlist, not an exhaustive event calendar**. A new research pass at the beginning of each month must find, compare and verify relevant occasions from film authorities (BFI/studios/AFI/IMDb release info) and primary artist, label and chart sources, without inventing a release day for records documented only at month level.

Manual commands on an up-to-date repo checkout:

```bash
python scripts/render_editorial_radar.py --start-month 2026-11 --months 3 --check
python scripts/render_editorial_radar.py --start-month 2026-11 --months 3 --write
```

The first command catches stale snapshot tables; the second writes all three tables directly from the CSV **on the working branch**, which can then be proposed via PR. Omit `--start-month` to default to the next **Europe/London** month at execution. For future months first **research and append new source-backed CSV rows**, then rerender; an empty future monthly page only means no opportunities have been researched and entered, not that there are none.

Recommended editorial routine (manual unless separately scheduled):

1. At the **start of every month**, look two or three months ahead.
2. Gather 10–20 relevant occasions and independently confirm historical dates and precision; **choose roughly 3–5** good editorial opportunities worth exploring rather than writing all of them.
3. Audit the actual GitHub back catalogue to find resurface or collaborative links.
4. For new story candidates, produce an analysis brief (sample in `docs/editorial_radar/priority_briefs.md`) and check source data feasibility.
5. Update CSV and rerender the forward monthly tables in a **new PR** for review. Changes to seed facts should preserve source links and any contradictory evidence in notes.
6. Once an article is approved, standard site publication and the existing promotion indexer handle adding the *published* content to the evergreen library.

## Safeguards

- Nothing in this PR publishes or auto-schedules articles, Blockbuster, Data Lens or LinkedIn content.
- All recommended claims and dates are **editorial candidates**, not already-approved scripts or finished charts.
- Do not treat research ideas, tentative anniversaries or analyses that have not been completed as confirmed findings.
- Publishing to GitHub Pages remains governed by the repository's existing PR and validator process.
- Original chart data and any intended promotional image must be checked for consistent units, sample scope, licences and accuracy.
