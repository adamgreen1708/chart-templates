# Pilot findings — **exploratory, not publication-approved**

These figures are mechanically derived from the provisional 24-character costume dataset, not from a random or exhaustive population. **Colour coding still needs independent source-art verification.**

## The first visual contrast
- **8 of 12 heroes (66.7%)** have a dominant costume hue in the strict `red / blue / yellow` primary group.
- **3 of 12 villains (25.0%)** do.
- Red is the most frequently coded hero dominant hue: **5/12**; green leads the villain sample: **6/12**.
- Neutral hues are not disguised as green or purple: **Batman and Black Panther** were coded grey/black; **Black Manta and Venom** black.

## Publisher split
| Publisher | Hero primary-dominant | Villain primary-dominant |
|:--|--:|--:|
| Marvel | 5/6 (83.3%) | 2/6 (33.3%) |
| DC | 3/6 (50.0%) | 1/6 (16.7%) |
| **Pilot combined** | **8/12 (66.7%)** | **3/12 (25.0%)** |

These differences are **not** representative estimates of publisher-wide costume choices; the characters were purposively curated and there are only six per subgroup.

## Notable exceptions in the pilot
- Heroes without a primary dominant colour: Batman (grey), Green Lantern (green), Aquaman (orange), Black Panther (black).
- Villains with a primary dominant colour: Sinestro (yellow), Thanos (blue), Magneto (red).
- Thanos' blue-dominant and Wonder Woman's red-dominant classifications are particularly sensitive to costume illustration; the dataset marks these as requiring review.

## What this is **not**
- No measurement of `% of costume covered by a hue` and no authoritative hex values.
- Not an analysis of 23,272 FiveThirtyEight characters; that historical dataset provides alignment but **no costume colours**.
- Not a claim that costume palette predicts good or evil outside this deliberately curated illustrative sample.
- Not yet rendered through GitHub or inspected at phone size.

**Next production gate:** find and review specific full-body comic-costume references for all 24 characters; agree the dominant coding and the 3-chart story; then create configs and render through the repo's `social_square` renderer.

## Publisher reference audit and alternate-coding check (7 November 2026)
Of the 24 pilot records, **10 publisher pages or articles directly describe the relevant colour combination**; the other 14 are only character/era context. No exact full-body art review has been passed for any record; all are provisional. See `data/source_evidence_audit.csv`.

**The six-colour contrast in this pilot** (hero share minus villain share, **percentage points**, not fabric-area ratios):
- Red **+33.3 pp** (5/12 heroes vs 1/12 villains)
- Blue **+8.3 pp** (2/12 vs 1/12)
- Orange **+8.3 pp** (1/12 vs 0/12)
- Yellow **0 pp** (1/12 vs 1/12)
- Purple **−8.3 pp** (0/12 vs 1/12)
- Green **−41.7 pp** (1/12 vs 6/12)

The orange result is a warning against asserting that all three secondary hues are villainous.

**Five disputed hue assignments stress test:** heroes **7–9/12** could be strict RYB-primary dominant (baseline 8/12); villains **0–3/12** (baseline 3/12). The directional comparison is resilient *within this non-random sample only*. See `data/colour_coding_alternatives.csv` and `data/chart_coding_sensitivity.csv`.

Method note: 'Primary' refers to the **traditional red-yellow-blue art model**, not RGB display colour theory.
