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
