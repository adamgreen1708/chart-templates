# Gallery-inspired poster finishes — Bauhaus Art Studio

## Source and design boundary

Inspiration: Gallerix's Bauhaus search and collection, particularly their **Bauhaus Art No1** (orange circular motif and black lines on beige), **Bauhaus No11** (restrained red geometry on beige), **Bauhaus Art No17** (tonal blue circles and typography) and **Bauhaus Art No20** (a single red circle and black graphic linework).

- Reference collection: https://gallerix.co.uk/poster-prints/42-bauhaus
- This work borrows **general visual principles** (negative space, restrained palettes, one bold motif, linework, print-paper colours), not the composition or reproduction of an individual Gallerix artwork.
- There are **no external images, logos or Gallerix assets** in the live studio or its generated outputs.

## Art direction

Three originally designed gallery finishes available for the two Poster Composer v3 engines:

| Finish | Background | Palette | Graphic treatment |
|---|---|---|---|
| Gallery Paper | Warm ivory `#F4EFE3` | Brick red, ochre, blue, ink | Small masthead circle and construction line, delicate arcs inside some Mosaic tiles or a circular line study in Broadside's hero |
| Colour Study | Cream `#F2EADB` | Coral, ochre, teal, midnight blue | Same original graphic system with a brighter, balanced modern palette |
| Ink Study | Pale stone `#EFEDE4` | Black, red, stone, dark ink | Strong graphic typography and predominantly neutral marks; red accent |
| Studio Original | Existing palette | Existing studio swatches | Prior render behaviour preserved |

Gallery finishes apply **only** to the new Data Mosaic and Typographic Broadside poster compositions. Existing free-play drawing, Hidden Miles and older data-art modes render as before. Choosing one of the standard swatches while in a gallery finish visibly switches to **Studio Original**, so the palette controls are never misleading.

## Non-negotiable data encodings

- **Data Mosaic:** the *outer, ungapped rectangle bounds* of each tile encode positive value / sum of positive values. Insets are purely visual and not a second data series. Decorative concentric arcs are low-contrast and confined to larger tiles; they represent no measurement.
- **Typographic Broadside:** bar lengths start at zero and remain proportional to source values; the hero names the actual largest value. Decorative arcs and registration shapes are not data.
- All other controls continue to apply as before: local/GitHub CSVs, source metadata, category filtering, labels, sorting, editorial copy edits, 960×960 PNG export.
- The gallery selection must **not** mutate input rows, mapped columns, source values or calculations.

## Verified data, design previews and release gate

The original SVG comparison previews use the public verified 14-track Bowie debut album subset, using **duration_seconds** for 14 tracks (total 2,353 seconds; longest `Silly Boy Blue` 234 seconds = 3:54).

- [Gallery Paper Data Mosaic](previews/bauhaus-gallery-paper-mosaic.svg)
- [Ink Study Typographic Broadside](previews/bauhaus-gallery-ink-broadside.svg)

These are **deterministic design previews** created from the same source values, not screenshots of the hosted studio. Compare them to the existing v3 previews and test the live gallery finishes before merging.

Completed checks: JavaScript compile and simulated UI/canvas controls for Mosaic and Broadside across Paper, Colour Study, Ink Study and Studio Original. Real Bowie CSV filtered to the 14-track debut, 14 tiles / 14 bars and labels/PNG action remain functional.

**To do before production:** inspect final PNG pixel output on desktop and mobile Safari; ensure colours and text have adequate contrast, arc linework is clipped to tile bounds, masthead stays in safe margins, source text wraps cleanly, and the 64-row case remains legible. Confirm original free-play controls and studio swatches still work.
