# Superhero costume evidence review · 8 November 2026

**Status: INCOMPLETE — not authorised as a publication-grade, independently verified costume dataset.** This review strengthens the source trail and clarifies variant risk. It does **not** verify dominance for all 24 costumes.

## What was completed

- Reviewed publisher material for **all 24 names** and recorded the most relevant publisher article, comic reading list, issue, or profile in `data/publication_source_review_2026-11-08.csv`.
- 11 records have an explicit **publisher statement describing the character's costume palette**; others have comic-history or issue context but **not** a definitive costume-colour description.
- Independently confirmed Tim Leong's original claim from his 2013 [Wired excerpt](https://www.wired.com/gallery/excerpt-visual-guide-to-the-comic-book-universe/): traditional primary hues as a heroic convention and green/purple/orange as villainous convention. The new sample explores exceptions; it is not a reproduction of his original charts.
- 14 of 24 rows are flagged **high risk** for era differences, accessory colours, main-hue ambiguity, or character-role changes. This is a deliberately conservative risk assessment, not a completeness score.
- Rechecked the codebook: **traditional red/yellow/blue artist primaries**, not RGB. Accent and supporting swatches are qualitative, ordered descriptors, **not proportions**.

## What is NOT verified

- **0 / 24** records have independently approved full-body *selected-issue* art with a separately adjudicated leading costume hue in this review.
- No measured percentage-of-fabric data exists. There is no defensible way to turn these categorical swatches into area ratios without a defined image collection and pixel/region segmentation method.
- Several of the most shareable showdowns depend on artist/era interpretation: **Sinestro's yellow-vs-black suit, Thanos's blue-vs-gold armour, and Magneto's red-vs-purple outfit**, plus Green Goblin's purple apparel versus green mask/body. These need explicit selected-art confirmation, not just entity pages.
- The orange accent assigned to Joker and the black supporting hue assigned to classic Daredevil are not independently backed by the source prose; these must be checked or revised before publishing.
- The 24 are a balanced **purposive editorial sample** (six heroes and six villains per publisher), not a census or random sample. No publisher-level population inference or hypothesis-test p-value is justified.

## Publication decision

**DO NOT MERGE THE PUBLICATION PR YET.** Build it in draft form with `published: false`, exact approved V3 PNGs, a source-transparent 24-character table, an honest method note and this review attached. The visuals stay unchanged while any costume codes remain unverified. Once the selected-issue art has been inspected and classification discrepancies resolved, rerender from CSV if necessary, recheck the blog and phone images, and only then flip `published: true` and seek Adam's final explicit approval.

## Reviewer checklist
- [ ] Pin one official comic-issue cover or full-body panel for each selected costume version.
- [ ] Record main / supporting / accent hues with issue/artist/edition and whether the classification is editorial or measured.
- [ ] Reconcile high-risk examples and all five matched-colour pairs, then regenerate all derived datasets and check whether 8/12 and 3/12 remain true.
- [ ] Reinspect exact chart PNGs at full resolution and 390px/320px for any changed data.
- [ ] Validate source links and mobile reference table on the Jekyll site preview.
- [ ] Set `published: true` only after these gates, and request final approval for publication.

## Additional issue-art leads (8 November 2026)

See [`content/high_impact_art_review.md`](high_impact_art_review.md) for targeted cover/reference checks of Sinestro, Magneto, Thanos and Green Goblin. **Important:** DC's 2007 Sinestro Corps Special cover is a credible **black-and-yellow** costume reference, but its crop does not settle which hue dominates. Resolving it as black rather than yellow would remove the Wolverine–Sinestro yellow pairing and alter the chart-2 villain count, so the current approved story cannot be released without addressing this case.
