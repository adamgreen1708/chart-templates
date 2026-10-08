# Icons of Data — series specification (draft)
Status: editorial proposal for approval. Not live or scheduled.
Repository: `adamgreen1708/chart-templates`
Started: 2026-10-08

## Editorial promise
**Icons of Data — The remarkable ways we turn information into understanding.**

Explore historically important, distinctive and influential systems for encoding information. This is broader than statistical charts: it includes cartography, network diagrams, notation, tactile writing systems and more. Braille belongs here, but must never be described as a visualisation or reduced to a sighted-only exercise.

## Editorial selection gate
- A real, identifiable work, system or edition, with a credible provenance.
- A concrete explanation of **what information** is represented and **which channel(s)** carry it.
- Significance is supported by authoritative sources, not popularity guesses.
- Show the cost/trade-off of the encoding, not just praise for attractive design.
- Historical dates distinguish conception, issue, publication and later adoption.
- Do not claim an inventor invented a general encoding technique without verification.

## Per-edition package
1. Original work, with creator/date/edition, image provenance and reuse rights verified.
2. Editorial hook, under 40 words.
3. Decode the Icon: an annotated, source-faithful decomposition of the encoding.
4. Rebuild or experimental counterpart, where underlying real data can be verified. Mark schematics prominently.
5. What it makes easier to understand; what gets hidden, simplified or distorted.
6. Brief historical context and accessible alt text/captions.
7. Methods and source notes; clear difference between historical estimates and modern observations.
8. Links to the evergreen Resources collection and related editions.

## Reusable encoding vocabulary (non-exhaustive)
- **Position** (including geographic position)
- **Length, width and area** (distinguish visually)
- **Colour** (hue versus ordered intensity)
- **Shape and orientation**
- **Time / sequence**
- **Topology / connectivity**
- **Tactile patterns and positional dot codes**
- **Signal duration / rhythm**
Record primary and secondary channels separately. Categories are descriptive tags, not numerical effectiveness scores.

## Minard first-edition integrity gates
- Original: Charles Joseph Minard, `Carte figurative ... campagne de Russie 1812-1813`, printed 1869 (BnF).
- The map uses **width proportional to an estimated number of men**; the legend gives 1 mm per 10,000 men. Dark retreat band, warm-toned advance band.
- Do not present the shrinking band as deaths alone: changes include multiple causes and unit movement; Minard explicitly gives a simplification concerning detached corps.
- Original French temperature values are **degrees Réaumur**; verify units before any Celsius conversion and label conversions.
- The HistData description incorrectly says the campaign was in **1815**. Use the BnF/original title's **1812–1813**, not that typo.
- HistData's 51 troop path records include multiple **groups** and advance/retreat directions; never treat the first record as the total army or collapse groups by accident.
- One of the nine temperature rows has a missing `date` value. Retain missingness rather than inventing a date.
- Ensure derived renderers use the right data and display clear source notes, generous safe margins and descriptive, accurate alt text.
- Never publish a historical source image before checking its specific digital reproduction's reuse terms.

## Publishing and approval
Work in a focused branch/PR; no merge, Pages publication, site resource link, social post, or approved finished image substitution before explicit editorial approval. This series is manual, not scheduled. Use existing GitHub Pages/Jekyll publishing path, not WordPress/Jetpack.
