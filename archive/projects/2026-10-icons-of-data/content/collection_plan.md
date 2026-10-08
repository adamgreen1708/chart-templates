# Icons of Data — editorial collection plan
**Status:** Working draft · 8 October 2026
**Tagline:** The remarkable ways we turn information into understanding.
**Location after approval:** `site/resources/icons-of-data/` linked from the existing `site/resources/index.html`; individual editions as Jekyll posts.

## The two-tier model
1. **One permanent Resources feature:** an evergreen museum-style introduction, filterable catalogue and primer on different encoding channels. Lives under Resources and expands with each approved entry.
2. **A sequence of deep dives:** one article per icon, linked back to the collection. Start with Minard; later bring in Harry Beck's Tube diagram and Louis Braille's tactile writing system.

## Reader journey for the resource feature
1. Hook: information is not intrinsically a bar, chart, map or even visual.
2. Gallery: iconic originals with careful image rights/credits and accessible captions.
3. The Encoding Library: cards organised by position, width/area, colour, topology, tactile patterns, sequence and signals.
4. **Encoding fingerprints:** descriptive matrix of which channels each icon uses; no arbitrary numeric 'genius' or 'accuracy' score.
5. Timeline: dates attached to specific original artefacts or editions; no spurious 'first invented' narratives.
6. Open each object: links to the long-form editions, original sources, methods and downloadable provenance.
7. CTA: suggest an icon via a later agreed mechanism; retain handcrafted editorial validation.

## Proposed categories (overlapping)
- **Numbers into pictures:** Minard, Nightingale, Playfair, Du Bois.
- **Mapping and connections:** Snow's cholera map, Harry Beck's Tube diagram.
- **Symbols, signals and touch:** Braille, Morse code, musical notation.
- **Making the invisible visible:** warming stripes and further science-based designs.

## First-edition narrative: Minard
**Core argument:** Instead of marking points on a route, Minard made the journey itself shrink. Line width turns a map into an argument about loss.

### 3-part visual sequence
1. **The whole argument on one sheet** (set the scene): the historical original, with clearly labelled source and crop/rights. Highlight which panels and marks represent what. Do not recreate historical facts via model-generated imagery.
2. **The disappearing band** (build the tension): data-faithful graphical reconstruction of the troop route by group, keeping advancing versus retreating strands distinct. Use HistData's 51-route record dataset and city lookup. Keep historic quantities as *Minard's plotted estimates*.
3. **Why one line works so hard** (land the aha moment): small-multiple 'encoding fingerprints' separating geographic position, band width, travel direction and temperature/time annotations; descriptive matrix, not fabricated scores. Use nine sourced temperature observations with Réaumur unit QA.

### Risks to resolve before rendering
- 422,000 at the western end of the original map is not interchangeable with one group's 340,000 starting value from the HistData digitisation; verify separate branches and totals.
- Temperature unit, missing date, path order and group splits need specific checks.
- Schematic composites must never be presented as an exact original.
- No claim that cold weather alone explains losses.
- Feature image must follow `spec/feature_image_rules.md` (light-grey background, muted-red accent) and express **shrinking width across a route**, not a generic soldier/map illustration.
- Site's existing `resources/index.html` presently has only the chart-choice guide: preserve it and introduce Icons of Data as a second substantial resource after content approval.

## Next milestones
**A — Foundation (this PR):** collection spec, candidate catalogue, attributed Minard source data, draft and QA plan.
**B — Minard visual review:** inspect original, reconcile totals and unit handling, produce 3 visuals and feature artwork, display for approval.
**C — Resource launch:** implement first public collection landing page with approved originals, captions and filtering, plus the Minard Jekyll article; preview mobile and desktop, image/asset links and accessibility.
**D — Publish only after approval:** open final site PR, merge only when approved, verify Pages deployment and final URLs.
**E — Expand deliberately:** Tube diagram and Braille are preferred additions; source/rights and accessibility reviewed per edition.
