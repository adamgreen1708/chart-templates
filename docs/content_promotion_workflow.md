# Coffeetableviz — content promotion workflow

**Status:** proposed editorial workflow for review; **no automatic publishing**.
**Audit baseline:** 20 October 2026 (Europe/London). **Site of record:** https://coffeetableviz.com, built from this GitHub repository.

## Purpose

Coffeetableviz is an enduring library of data stories, not a publication that needs today's news to remain interesting. LinkedIn is a discovery channel. A single article may have many genuinely different angles for different readers; the underlying analysis stays the same.

The goal is qualified discovery and repeat readership, not indiscriminate impressions or new posts for their own sake.

## Audited starting point

Repository inventory on main as at 20 October 2026:

- **40** files in site/_posts (six of these are also entries in Icons of Data).
- **Two** resource collections: a 13-card Choosing the right chart guide and a six-story Icons of Data collection.
- **16** editions in site/_blockbuster_quotes, each with a documented date connection, source references and quote context.
- **17** editions in site/_data_lens, a bank of short, reusable data and design explanations.

These are **repository file counts**, not proof that each page, image or social preview renders correctly on the live website. Do not double-count the six Icons of Data articles as additional main posts.

The latest Daily Pulse examined at audit time (19 October) recorded 5 visits versus a previous seven-day daily average of 20.57 and 1 LinkedIn referral. One quiet day alone does not establish a long-term trend; GoatCounter reporting began 4 October 2026, so historical comparison is limited.

## Source files and how to use them

| File | Role |
| --- | --- |
| data/promotion/content_index.csv | Starting catalogue of all 40 main posts, two resource collections and 17 archived Data Lens editions; P1/P2/P3 are **editorial** priorities, not measured performance |
| data/promotion/blockbuster_events.csv | Archived Blockbuster date connections and conservative proposed article matches; date refers to the **original** edition |
| data/promotion/pilot_queue.csv | Eight candidates over four weeks, starting Monday 26 October 2026; none is approved or scheduled |
| data/promotion/promotion_log.csv | Empty human-maintained posting and measurement log; fill only with observed LinkedIn metrics and site traffic |
| docs/content_promotion_run_commands.md | Copyable ChatGPT + GitHub commands for manual preparation and review |

The index contains **59 source paths, not guessed public links**. At draft time, open the current article front matter / Jekyll routing and resolve the canonical coffeetableviz.com URL. Never publish GitHub blob links or legacy WordPress URLs as the article destination. Confirm mobile loading, imagery, alt text and social previews first.

Content index class meanings:

- **evergreen:** enduring argument; check sources and rights but no routine data refresh merely due to age.
- **snapshot:** analysis tied to a source extract, data vintage, ranking or projection; retain the original dates and units.
- **seasonal:** useful again around a recurring sporting or cultural season; never imply historic results are current.
- **sensitive:** controversial or rapidly changing data/interpretation; require a fresh evidence and headline review before promoting.

Priority P1 = start here, P2 = additional evergreen/seasonal opportunities, P3 = hold pending stronger accuracy or freshness checks.


## Automatically register newly merged content (proposed integration)

The separate \`.github/workflows/promotion-library-sync.yml\` runs on a **push to main** affecting source content, after the ordinary site publishing approval. It does not run the daily series and does not publish to any social network.

1. \`scripts/sync_promotion_library.py --write\` scans \`site/_posts/*.md\`, \`site/_data_lens/*.md\`, \`site/resources/*/index.html\` and \`site/_blockbuster_quotes/*.md\`.
2. It compares each file's **source path** to the corresponding CSV index. New sources are appended only once; existing rows, assigned hooks, priorities, links and editorial notes are preserved byte-for-byte.
3. New articles, Resources and Data Lens cards enter \`content_index.csv\` with **priority REVIEW**, **evergreen class unclassified** and no hook.
4. New Blockbusters enter \`blockbuster_events.csv\` with their **original run date**, documented film, performer and connection type. Their article match stays empty until an editor establishes a real link. The recorded date is not independently reverified by the sync script.
5. The workflow runs small unit tests, then **opens/updates a draft PR** for those proposed CSV additions. It does not commit to \`main\` or block the original content's publication.
6. Review and merge that follow-up PR after enriching the new entries; only then can the weekly manual promotion selection consider them editorially ready.

Run locally on a checkout of the branch with:

\`\`\`bash
python -m unittest discover -s tests -p test_promotion_library_sync.py -v
python scripts/sync_promotion_library.py --check
# --check exits 1 if content is newly discovered and not yet indexed
python scripts/sync_promotion_library.py --write
\`\`\`

**Limitations:** The sync detects *new file paths*, not content revisions or deleted/renamed source paths. Treat edits to previously published articles, new sources, updated dataset vintages and changes of publication rights as separate editorial review triggers. The draft-PR workflow needs the repository setting that permits GitHub Actions to create pull requests with its token; if disabled, enable that setting or use the script in a manually opened PR. Until the first post-merge action run succeeds, the proposed automation is **not proven operational**.

## Editorial lanes and cadence

Test **two personal LinkedIn posts per week for four weeks**. This is a planning cadence, not a GitHub Action or a scheduled ChatGPT task.

1. **Useful/curious data thinking:** Resources, Icons of Data, design essays or an archived Data Lens.
2. **An intriguing finding:** film, music, sport, society or another long-form story.

Avoid reposting the same opening or simply announcing that an article exists. A strong post normally has: a curiosity-led first line, one self-contained fact or observation, the relevant chart uploaded natively when rights permit, one honest limitation, and a quiet invitation to the article or resource. UK English, conversational and mildly dry; no artificial engagement bait.

**Resources first:** promote Choosing the right chart as a document carousel using the original 13 cards (check export order, rights, tiny labels and mobile legibility). Introduce Icons of Data as a collection, then tell individual Minard, Beck, Braille, Nightingale, Du Bois and Snow stories. Braille is a tactile reading and writing system, **not** a visualisation.

**Data Lens:** treat a previously dated card as an archival extract. A new LinkedIn caption is not a new Daily Lens edition. Do not regenerate or redress date-specific cards as though issued today.

## Blockbuster as an editorial calendar, not an automatic promotion trigger

The Blockbuster series already verifies exact date connections. Preserve its existing standards; do not make changes to the Blockbuster creation or publishing instructions to improve promotional convenience.

For an older Blockbuster edition:

1. Read its source Markdown, exact original date, person/film relationship and source links.
2. Find candidate long-form articles using this conservative order: **same actor/creator**, **same film/franchise**, **genuine thematic connection** (clearly labelled as a pivot), then **no match**.
3. A film quote alone does not establish a fact about a different article. The suggested actor match is a *promotion connection*, not new analytical evidence.
4. Independently recheck the birthday, release territory, anniversary wording and any new assertions as of the **new LinkedIn posting date**. A 2026 Blockbuster RUN_DATE never becomes a new 2027 RUN_DATE merely because the source edition is reused.
5. If there is no real relationship, promote the standalone Blockbuster (subject to its rights and context) or skip. **Never force a link.**

Early examples from source records:
- Se7en's 22 September 1995 US release edition features Brad Pitt; it offers an actor-led invitation to the existing Brad Pitt IMDb ratings and quotes analyses.
- Roger Moore's 14 October birthday edition of The Spy Who Loved Me can provide a **Bond-franchise** bridge to the villain-age article, not a claim that the quote or that film proves the chart's finding.
- The Scream edition could be revisited around Halloween as a **seasonal** film conversation; Halloween is not the original date connection.

Additional date candidates from the audit (verify anew before use): Taron Egerton 10 November; Brad Pitt 18 December; Mel Gibson 3 January; David Bowie 8 January; Simon Pegg 14 February; Tom Hanks 9 July. Such future occasions should rotate across distinct posts rather than dumping a person's whole archive on the same day.

## Editorial production and approval gate

For each candidate:

1. Read the latest source article **and** current repository editorial/visual rules. Confirm category, original dataset, image and source citations.
2. Check that the landing page is live, usable on mobile, relevant and honestly described. Verify licensing for *every* image or archival reproduction used externally. A website-embedded image does **not** automatically grant unrestricted re-upload rights.
3. Write **two differentiated LinkedIn hook options**; choose one after review. Keep an explicit distinction between dated facts, projections and current statements.
4. Draft a finished LinkedIn caption and identify the actual existing chart/card resource. Create no new image unless separately requested and QA'd.
5. Display the caption, image path or preview, exact source, proposed destination link, intended trigger and accuracy caveat for **explicit approval**.
6. **Do not post to LinkedIn**, schedule distribution, or modify the site, daily-series content or renderers without separate authorisation.
7. Once the user **confirms** a LinkedIn post was published, record its URL, date, hook and observed metrics in the promotion log through a separately reviewed GitHub change; never invent outcome figures.

For externally linked posts, trial a clear, stable campaign tag such as:
https://coffeetableviz.com/resources/choosing-the-right-chart/?utm_source=linkedin&utm_medium=organic_social&utm_campaign=ctv_resource_pilot&utm_content=chart_question_hook

Only use the tagged link after confirming it opens and the site's analytics actually captures the parameters as intended. GoatCounter referrers are not necessarily a direct measure of UTM campaign attribution.

## Four-week pilot and learning loop

Candidate weeks are in pilot_queue.csv:

| Week starting | Practical/resource slot | Story/culture slot |
| --- | --- | --- |
| 26 Oct 2026 | 13-card chart-choice resource | Missing is not zero — archived Data Lens |
| 2 Nov 2026 | Minard / Icons of Data | Tables vs visualisations |
| 9 Nov 2026 | Taron Egerton birthday connection (10 Nov; **reverify**) | Braille / Icons of Data |
| 16 Nov 2026 | UK age profile and projections | Bowie's style-reset measure |

Use LinkedIn-native impressions, reactions, comments, saves and link clicks if available; record the exact reporting period and the post URL. Compare measured site traffic and referrals using GoatCounter/Daily Pulse with care. Do not attribute all referrals to a specific post on the basis of a daily total. Review **four weeks of results**, not one quiet day.

Success is learning which combination of audience, hook, visual and resource leads to genuine visits or worthwhile conversation. Keep the two strongest formats, refine the weakest, and only then consider greater cadence.

## Known review items

- The **Icons of Data** series spec still describes a pre-publication state, whereas six edition files and a resource landing page appear on main. Confirm actual Pages deployment and reconciled editorial approval **before changing that spec**. This PR deliberately leaves the daily series specifications unchanged.
- Some older articles contain legacy WordPress metadata or dated external links. Canonical destinations are now GitHub Pages at coffeetableviz.com.
- The content index is a **seed list**, not a claim that external rights, current numbers or live link checks have passed.
- Keep all article creation, QA, repo writes and LinkedIn publication **approval-first**. No scheduled or background social-posting has been enabled.
