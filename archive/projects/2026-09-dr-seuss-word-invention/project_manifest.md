# Project manifest: Dr Seuss word invention

## Status

- Status: Story route selected; published aggregate metrics transcribed; three chart configs staged for render/QA
- Started: 25 September 2026
- Last updated: 25 September 2026
- Owner: Adam Green
- Repo project slug: `2026-09-dr-seuss-word-invention`
- Working branch: `project/2026-09-dr-seuss-word-invention`

## Story

- Working headline/angle: **The nonsense has rules**
- Core question: what makes an invented Dr Seuss word feel distinctly Seussian rather than merely random?
- Audience: coffeetableviz readers plus language, books and data audiences.
- Current recommendation: use published linguistic analysis to move from what Seuss invented, to how sound shaped it, to the unusually heavy use of the letter Z.

## Source scope

Primary quantitative source:

- Daniel Teuber (2018), *An Analysis of the Nonce-Words of Dr. Seuss*, Journal of Osaka Sangyo University Humanities & Social Sciences 34, pp. 43–69.
- The study analyses 377 type-2 nonce words collected from 33 Dr Seuss books.
- The project's charts use only aggregate statistics published in the paper. No full book text or copyrighted corpus is stored in this repository.

Independent contextual corroboration:

- Bruce Hayes (2022), *The coinages in Seuss*, English Language & Linguistics, Cambridge University Press.
- Hayes independently analyses Seuss coinages and reports systematic phonological patterns, including frequent initial /z/.

Official contextual source:

- Seussville author timeline for the constrained-vocabulary background to *The Cat in the Hat* and *Green Eggs and Ham*.

## Key analytical findings

From Teuber's published analysis:

- Common nouns: 61% of the 377-word sample.
- Proper nouns: 27%.
- Adjectives: 5%.
- Interjections: 4%.
- Verbs: 3%.
- Common + proper nouns therefore account for 88% of the sample, using the paper's rounded percentages.
- Rhyme only: 48%.
- Rhyme + alliteration: 19%.
- Alliteration only: 17%.
- Neither: 16%.
- Rhyme and/or alliteration therefore influence roughly 84% of the sample.
- In the letter-frequency comparison, Z accounts for 4.42% of letters in the 377 Seuss nonce words (2,556 letters), compared with 1.02% in the paper's top-1,000-US-surnames list and 0.10% in its 3,000-common-English-word list.
- The Seuss-vs-common-word Z share is 44.2 times as large (4.42 / 0.10), a derived comparison from the published percentages.

Important limitation:

- This is a study of a defined subset of Seuss nonce words, not a complete census of every unusual word he wrote.
- The comparison lists have different purposes and sizes; Chart 3 compares letter shares, not raw Z counts.

## Recommended three-chart sequence

1. **Seuss mostly invented things** — parts of speech establish what kinds of words dominate the sample.
2. **The nonsense follows the sound** — rhyme/alliteration categories show that the coinages are highly structured.
3. **Z does much more work in Seuss** — the letter-frequency comparison lands the memorable fingerprint.

Full rationale and QA risks: `content/story_plan.md`.

## Files

| File | Purpose | Status |
|---|---|---|
| `content/research_plan.md` | Source method, scope and caveats | Created |
| `content/story_plan.md` | Story options and recommended three-chart route | Created |
| `data/dr_seuss_word_invention_metrics.csv` | Published aggregate metrics used by all three charts | Created |
| `config/chart_01_invented_things.py` | Part-of-speech chart config | Created |
| `config/chart_02_sound_system.py` | Rhyme/alliteration chart config | Created |
| `config/chart_03_z_signature.py` | Z-frequency comparison chart config | Created |
| `output/` | Rendered chart PNGs | Pending workflow render |
| `content/qa_report.md` | Render/data QA record | Pending render QA |

## Build decision

No renderer or reusable template change is currently required. The existing locked square 538 renderer supports the proposed horizontal bar and dot charts directly.

Live coffeetableviz.com publication is not part of this first build stage. The project should reach chart QA and Adam review before a Jekyll publication package or feature image is created.
