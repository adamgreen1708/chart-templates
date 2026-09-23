# Publication package: David Bowie reinvention

## Editorial recommendation

Lead with the measurement problem, not the mythology. David Bowie gives us 26 lifetime solo studio albums across six named calendar decades, but the strongest data-story moment comes when a transparent style-reset score produces an awkward result. The charts show repeated movement through the catalogue while also showing why a genre taxonomy cannot stand in for artistic reinvention.

## Published headline

**How do you measure a chameleon?**

## Standfirst / excerpt

David Bowie released 26 lifetime solo studio albums across six named decades. A simple style-reset score shows repeated change — and the limits of trying to measure reinvention.

## Story sequence

1. **Six decades. Twenty-six albums.**  
   The lifetime solo studio chronology from 1967 to *Blackstar* in 2016.

2. **The labels rarely sit still.**  
   Distinctive AllMusic style tags appear, disappear and return across the album sequence.

3. **A reinvention score gets awkward.**  
   Twenty-six albums create 25 album-to-album moves. Twenty-three can be scored consistently; the two moves touching *The Next Day* remain explicit missing-data rows.

## Site post

`site/_posts/2026-09-23-how-do-you-measure-a-chameleon.md`

## Site assets

- `site/assets/migrated/david-bowie-reinvention/feature.svg`
- `site/assets/migrated/david-bowie-reinvention/six-decades.png`
- `site/assets/migrated/david-bowie-reinvention/style-matrix.png`
- `site/assets/migrated/david-bowie-reinvention/reinvention-score.png`

## Blog excerpt

David Bowie released 26 lifetime solo studio albums across six named decades. The catalogue plainly moves, but trying to reduce “reinvention” to one number quickly gets awkward — which turns out to be the most interesting part.

## LinkedIn

David Bowie.  
26 solo studio albums.  
Six named decades.

The easy story would be: look how often he reinvented himself.

So I tried to measure it.

I tracked album-level style labels through the catalogue, then calculated a simple reset score for each album-to-album move based on how much the labels changed.

It works. Mostly.

The largest measured reset is the 1967 debut → *Space Oddity* at 89%.

But *Station to Station* → *Low* lands at only 33%.

That is where the chart gets more interesting than the ranking.

Broad labels survive across very different records, so a tidy taxonomy can flatten a messy artistic shift. The data still shows movement — it just cannot become the art.

Three charts, one slightly awkward metric, and a David Bowie catalogue that remains difficult to pin down.

Full story on **coffeetableviz.com**.

## Instagram

How do you measure a chameleon?

David Bowie released 26 lifetime solo studio albums across six named decades.

I mapped the style labels through the catalogue and then tried a simple album-to-album “reset score”.

23 of 25 moves can be measured consistently.

The surprise? Some of the shifts you expect to leap off the chart do not.

Which is the useful bit: classification can show change, but it cannot fully capture artistry.

Full story on **coffeetableviz.com**.

## X / short social

David Bowie: 26 solo studio albums, six named decades, 25 album-to-album moves.

I tried to measure “reinvention” with a simple style-reset score.

It works — until the taxonomy starts flattening the interesting bits.

New on coffeetableviz.com.

## Chart captions and alt text

### Chart 1 — Six decades. Twenty-six albums.

**Caption:** Bowie's lifetime solo studio catalogue runs from 1967 to *Blackstar* in 2016, with a ten-year gap between *Reality* and *The Next Day*.

**Alt text:** Chronological dot plot of David Bowie's 26 lifetime solo studio albums from 1967 to 2016, with every album labelled and the ten-year gap between Reality and The Next Day highlighted.

### Chart 2 — The labels rarely sit still

**Caption:** Distinctive AllMusic style tags appear, disappear and return across the catalogue; the three near-universal umbrella labels are omitted from the display only.

**Alt text:** Album-by-style dot matrix showing distinctive AllMusic style tags across David Bowie's solo studio albums. Labels such as Glam Rock, Blue-Eyed Soul, Dance-Rock, Post-Punk and Alternative/Indie Rock appear in different parts of the chronology.

### Chart 3 — A reinvention score gets awkward

**Caption:** Twenty-six albums create 25 transitions. Twenty-three have comparable style data; the two moves involving *The Next Day* are shown as grey missing-data rows rather than zero scores.

**Alt text:** Dot plot showing style-reset scores for 25 album-to-album moves in David Bowie's solo studio catalogue. Twenty-three transitions have measured scores; The Next Day and Blackstar are retained as grey missing-data rows because The Next Day lacks comparable AllMusic Styles metadata. Space Oddity has the largest measured reset at 89%, while Low is highlighted at 33%.

## Feature-image metaphor

**A chameleon stretched across a ruler.**

The chameleon represents Bowie's repeated reinvention; the ruler represents our attempt to quantify it. Its body is broken into shifting black-and-charcoal segments while one muted-red measurement mark breaks the ruler's regular rhythm. The image expresses the actual editorial tension: change is visible, measurement is useful, but the scale never quite captures the whole animal.

## Feature-image prompt / construction brief

Use case: illustration-story. Asset type: square coffeetableviz editorial feature image. Follow `spec/feature_image_rules.md`.

Create a square stencil / screen-print editorial illustration on the house light-grey `#F3F4F6` background. Show a stylised, anonymous chameleon stretched horizontally across a large black measuring ruler. Build the chameleon from strong black and charcoal shapes, with subtle segmented shifts across its body to suggest repeated reinvention. Let its curled tail and feet interact with the ruler so the two ideas read as one composition. Add one restrained muted-red `#C44E52` measurement mark that breaks the otherwise regular scale. Strong negative space, crop-safe, readable at thumbnail size. No text, David Bowie likeness, lightning-bolt face paint, logos, album artwork, watermarks or copyrighted character imagery.

## Feature alt text

Black-and-charcoal stencil chameleon stretched across a measuring ruler on a light-grey background, with segmented body tones suggesting change and one muted-red measurement mark breaking the regular scale.

## QA checklist

- [x] Final chart set visually approved by Adam.
- [x] 26-album lifetime solo studio scope retained.
- [x] Chart 3 shows all 25 possible transitions: 23 measured plus two explicit missing-data rows.
- [x] First album is correctly treated as the baseline rather than given a fake reset score.
- [x] Site chart assets are byte-for-byte copies of the approved project PNGs.
- [x] Feature concept expresses the approved “measure a chameleon” tension rather than generic Bowie/music imagery.
- [x] Feature asset uses the locked `#F3F4F6` background and one muted-red accent.
- [x] No Bowie likeness, logos or album artwork are used.
- [ ] GitHub Pages PR build passes after publication staging.
- [ ] Adam reviews the exact feature asset and site post before merge.
