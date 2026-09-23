# Publication package: Brad Pitt quotability

## Editorial recommendation

Lead from the real trigger: Adam watching *Fury* and hearing Wardaddy’s “Ideals are peaceful. History is violent.” Use that to ask where Wardaddy sits among Brad Pitt’s most quotable film roles, then let the data overturn the expectation: Tyler Durden dominates the verified IMDb quote-entry ranking.

## Published headline

**Fury started it. Tyler Durden owns the answer.**

## Description / excerpt

Watching *Fury* sent me down a Brad Pitt quotability rabbit hole: 44 verified IMDb film-role pages, one dominant Tyler Durden, and Wardaddy in eighth.

## Story sequence

1. **Fury started it. Tyler Durden owns the answer.**  
   Ranked top-12 film-role pages. Tyler Durden leads with 105 IMDb quote entries; Wardaddy ranks eighth with 40.

2. **Ratings help. They do not explain the quotes.**  
   All 44 verified film-role pages. Pearson r = 0.54 between quote-entry count and IMDb rating. Fury sits at 40 / 7.6.

3. **Rusty did most of his talking on the first job.**  
   Rusty Ryan: Ocean’s Eleven 42, Ocean’s Twelve 13, Ocean’s Thirteen 17.

## Short verified quote examples

Use sparingly as editorial texture:

- *Fury* / Wardaddy: “Ideals are peaceful. History is violent.”
- *Fight Club* / Tyler Durden: “The things you own end up owning you.”
- *Moneyball* / Billy Beane: “How can you not be romantic about baseball?”
- *F1* / Sonny Hayes: “Hope is not a strategy.”
- *Ocean’s Eleven* / Rusty Ryan: “Been practicing that speech, haven’t you?”

The quotes support the data story; they do not explain or cause the counts.

## Site post

`site/_posts/2026-09-23-fury-started-it-tyler-durden-owns-the-answer.md`

## Site assets

- `site/assets/migrated/brad-pitt-quotability/feature.svg`
- `site/assets/migrated/brad-pitt-quotability/top-roles.png`
- `site/assets/migrated/brad-pitt-quotability/quotes-vs-rating.png`
- `site/assets/migrated/brad-pitt-quotability/oceans.png`

## LinkedIn

I was watching *Fury* when Wardaddy said:

“Ideals are peaceful. History is violent.”

Naturally, I wondered where that puts him among Brad Pitt’s most quotable film roles.

Using IMDb character-page quote counts, I could verify 44 film-role pages.

A few findings:

- Tyler Durden / *Fight Club*: **105**
- Billy Beane / *Moneyball*: **53**
- Wardaddy / *Fury*: **40** — 8th
- Rusty Ryan / *Ocean’s Eleven*: **42**, falling to 13 and 17 in the sequels

There is a moderate relationship between quote count and IMDb rating (r = 0.54), but plenty of exceptions. Which is good. Otherwise this would have been a very short blog post.

Full story and charts on **coffeetableviz.com**.

## Instagram

Watching *Fury* turned into a Brad Pitt quote-count rabbit hole.

Wardaddy: **40 IMDb quote entries**.  
Tyler Durden: **105**.

Across 44 verified film-role pages, ratings help explain some of the pattern — but not much of the fun.

And Rusty Ryan? 42 quote entries in *Ocean’s Eleven*, then 13 and 17 in the sequels.

A few actual lines are threaded through the post too, because a chart about quotes without any quotes felt a bit rude.

Full story: **coffeetableviz.com**

## X / short social

Watching *Fury* made me ask a very normal question: which Brad Pitt role is most quotable?

IMDb quote entries, n=44 verified film-role pages:
Tyler Durden 105
Wardaddy 40 (8th)

Plus ratings, outliers and Rusty Ryan’s sequel drop.

coffeetableviz.com

## Feature-image metaphor

**A tank starts the question; a plain soap bar outweighs it on quotability.**

Use a seesaw as the visual tension. One side carries a compact WWII tank silhouette representing *Fury* / Wardaddy. The other carries a plain, unlabelled soap bar representing Tyler Durden / *Fight Club*, weighted down by a cluster of quotation-mark shapes. The soap side sits visibly lower. One small muted-red quotation mark sits beside the tank as the only colour accent.

This communicates the actual story: *Fury* inspired the question, but Tyler Durden dominates the measured quote count.

## Feature-image prompt

Use case: illustration-story. Asset type: square coffeetableviz editorial feature image. Follow `spec/feature_image_rules.md`.

Create a square stencil / linocut editorial illustration on the house light-grey `#F3F4F6` background. Show a simple seesaw in strong black and charcoal silhouette. On the raised left side, place a compact WWII tank silhouette with an open commander hatch, symbolic of *Fury* but with no logos, insignia, people or recognisable actor likeness. On the lower right side, place a plain rectangular soap bar with several bold black quotation-mark shapes clustered around and above it, making that side visibly heavier. Add one small muted-red `#C44E52` quotation mark near the tank as the only colour accent. Strong negative space, crop-safe, readable at thumbnail size, screen-print/stencil texture. No text, film titles, logos, faces, watermarks or copyrighted character likenesses.

## Feature alt text

Black-and-charcoal stencil illustration on a light-grey background showing a tank and a plain soap bar on opposite ends of a seesaw, with the soap side weighed down by quotation marks and one muted-red quote mark beside the tank.

## QA checklist

- [x] 54-film source list reused rather than rebuilt.
- [x] 44 film-role quote counts verified; 10 unresolved titles excluded, not treated as zero.
- [x] Unit described as film-role page, not unique character.
- [x] Wardaddy / Fury = 40 and ranks eighth in the verified sample.
- [x] Tyler Durden / Fight Club = 105.
- [x] Pearson relationship reproduced as r = 0.54; causal language avoided.
- [x] Rusty Ryan sequence reproduced as 42, 13, 17.
- [x] Short quote wording rechecked against IMDb quote pages.
- [x] Official chart PNGs rendered and committed by GitHub Actions.
- [x] Feature concept expresses the Fury-to-Tyler editorial tension rather than generic Brad Pitt imagery.
- [x] Feature asset committed to the publication branch.
- [ ] Final publication PR reviewed before merge.
