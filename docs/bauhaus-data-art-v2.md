# Bauhaus Art Studio — Data Art v2

Status: implementation on a feature branch; merge requires visual/mobile QA.

## Editorial premise

Form follows **real data**. Build lively Bauhaus-inspired square posters from a local CSV, a public GitHub CSV or a clearly labelled illustrative example. Keep creative decisions separate from data encodings, and make the poster explain its own choices.

The original free-play geometric studio remains available.

## Data-to-art grammar

| Control | Meaning | Guardrail |
|---|---|---|
| Value field | Filled area of each solid mark | Zero-based area proportional to non-negative values by default, **not** radius. |
| Shape family | Circle, square, triangle, half circle, quarter circle, or mixed | In mixed mode a category may determine shape when multiple categories are present; otherwise shapes cycle for decoration. Every family is scaled to equal area for equal values. |
| Area contrast | Optional enhanced differences | Uses 10% minimum area plus 90% min–max range; labelled **not zero-based**. Never present this as directly proportional to the original value. |
| Colour | Median, 4 equal-width bands, category, or decorative | Decorative is labelled non-data. Category colour can repeat when more than four categories exist. |
| Order | Original, ascending, descending | Sorting affects arrangement only. |
| Composition | Geometric grid, orbit, or ribbon | Artful position, not a numeric positional scale. |
| Filter | Choose a category | Category is applied before the 64-mark limit. |

Quick presets: **Patchwork**, **Orbit**, **Rhythm Ribbon**, **Minimal Blocks**. The **Surprise me** action rotates/cycles decorative marks without changing source values. Palette controls apply across creative and data-art modes.

## Editorial text

Three editable fields:
- Headline: derived from selected measure and number of marks.
- Small explanation: number of rows, mark type, area scale, colour encoding, and shape mapping when present.
- Footer: source filename, selected row count / first-64 notice, filter, composition, and sort where relevant.

Any field can be overwritten by the user. A **Restore automatic text** action resets all three. Loading a different dataset resets custom wording to avoid accidentally reusing an outdated source or metric. Text is wrapped inside safe boundaries of the square canvas and clipped only with an ellipsis if longer than the available two lines. The constant Coffeetableviz series eyebrow is not an editable headline.

## Optional labels on shapes

A **Show labels on shapes** checkbox (default off) reveals a label-content selector:
- **Label** — selected label column's original text
- **Value** — selected numeric measure's original value
- **Label + value** — two lines when there is space
- **Index / displayed order** — position in the currently sorted and filtered artwork; never imply statistical rank unless the order actually represents a ranking

**Auto-hide when cramped** defaults on. The label renderer first checks the available tile/mark size, then attempts collision-safe placement. All layouts (Grid, Ribbon, Orbit) shorten long labels with ellipses. No labels may enter the headline, deck or footer bands, clip beyond square art boundaries, or collide with another label. Orbit additionally avoids other marks. Disabling automatic hiding allows extra attempts at small font size but does **not** override collision protection.

The displayed label count and number suppressed are reported in the workspace. **Tap-to-inspect always keeps the complete source label and numeric value** regardless of truncation/omission. Labels overlay the artwork; they must never change numeric area, category colours, source order, sorting, or data contents.

PNG saving exports the actual on-canvas labels. Existing local/GitHub CSV and free-play behaviours remain unchanged.

Label QA: toggle on/off; test all four contents and three layouts; long/short labels; close-packed 64 records; different palettes and sorting; safe margins and inter-label collision; no hidden data value coercion; export PNG and mobile tap interaction.

## Data safety and export

- Keep both local CSV upload and public GitHub CSV import on \`main\`; no GitHub credentials are embedded.
- Import maximum 2 MB and 10,000 source rows. Render a maximum of 64 **matching** rows, prominently disclosing the first-64 restriction if it applies.
- Reject missing, negative, non-finite numeric values in the selected data before rendering; do not silently drop them.
- Tap a mark to inspect its actual source label and value.
- Export a 960 × 960 PNG. Preserve the creative-only design-link privacy guardrail: dataset values are never embedded in a share URL.

## Required QA before merge

- Run JS syntax and simulated UI tests for all presets, layouts, mark families, colour rules, sort and both area scale options.
- Read and chart **real repository CSVs**, including Bowie album filtering and daily site visits. Confirm exact source values when inspecting a mark.
- Verify all custom/auto text behaviours, long text wrapping, and changes of dataset.
- Verify zero and equal-valued data, invalid numeric data, over-64 first-rows disclosure, and image export.
- Check actual rendered pixels: safe margins, title/subtitle/footer wrapping, ribbon/order clarity, marker collisions (especially orbit and large datasets), legibility, colour/shape differentiation.
- Test the hosted feature on an actual iPhone Safari screen: CSV file picker, GitHub URL fetch, touch inspection, controls and image save.

No mobile-browser or final-pixel QA may be marked complete based only on a JavaScript or simulated-canvas test.

## Future design possibilities

Data-defined rotation (when meaningful), a multi-variable legend, downloadable mapping manifest, and SVG export. All require honest encoding descriptions and explicit mapping of data fields rather than pseudo-data meaning.
