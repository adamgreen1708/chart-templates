# Bauhaus Circle Study — Editorial Catalogue / MIN–MAX QA

**Proposed feature PR.** This affects only the My Data → Art **Circle Study** renderer in `site/resources/bauhaus-art-studio/index.html`. It does not change the underlying Circle Area/Arc geometry calculations, source CSVs, other poster types, or the website publishing workflow.

## Design requirement from the visual review

Original user screenshot: a square Spotify-streams artwork with 11 concentric source circles, two redundant small explainer labels on the upper left and a separate `11 OF 11 RECORDS DISPLAYED` callout below. User also supplied a modernist typographic reference and requested a small editorial block listing each plotted track name and stream count.

**New layout:** preserve the established masthead, title, explanatory deck and footer. Move measured concentric geometry to the right; build an uncluttered typographic record list on the left. Remove the redundant explainer labels and displayed-count callout. Use a larger, two-column source-grounded MAX/MIN typographic summary below the artwork. All text stays within the existing 960×960 safe zones.

## Data mapping and truthfulness

- **Circle Area:** complete filled circle area remains `value/maximum`. The visible overlapping annulus is a design consequence and **must not be described as the encoded area**.
- **Circle Arcs:** angle swept remains `value/maximum × 2π` on a fixed-radius, fixed-width reference track. The catalogue is also active in arc mode.
- **Record scope:** honour the current filter and source/selected sort before taking the original first **16** records. The artwork and the catalogue both then display those selected records, arranged **largest first** to match the outer-to-inner measured geometry. No additional records may be silently added or invented.
- **Range scope:** display the real minimum and maximum only. If equal, show the truthful identical values.
- The catalogue consists of one source-grounded label and exact formatted measure per plotted circle/arc, a small ordinal, and a colour tick using the same styling as the matching measured layer. Labels may ellipsise at a constrained 11px, numbers **must never ellipsise** (hide visually if too wide; original value accessible on tap).
- A compact line below the title already describes the current mapping in plain English. No unmeasured arrows, decorative statistics, upper quartiles or medians are added.
- The two **MAX/MIN** stat blocks use larger tabular-like numbers, small 11px headings and the actual source record names. Their values and catalogue rows are tappable. With 16-of-N records the titles explicitly say `MAX / SHOWN`, `MIN / SHOWN`.
- All count/disclosure context moves into the actual source footer: `all 11 records shown`, `first 16 of 64 records shown`, or `source MIN/MAX from N valid rows`; preserve existing missing-value exclusions and CSV first-64 disclosures.

## Source-verified example — the exact screenshot case

Repository CSV: `archive/projects/2026-09-david-bowie-track-distributions/data/bowie_track_distribution_rows.csv` from `main`.

- `label=track_title`, `value=spotify_streams`
- `album_title=The Rise and Fall of Ziggy Stardust and the Spiders from Mars`
- Exactly **11 valid matching tracks**, all 11 drawn.
- **MAX:** `Starman`, **829,880,663** Spotify streams.
- **MIN:** `Hang On to Yourself`, **23,172,806** Spotify streams.
- Catalogue order: actual 11 records sorted largest to smallest for radius/arc ordering, with full source counts shown. The source values come from GitHub; no invented stream totals or inferred rankings across other albums.

Independent SVG design previews from that same checked source:

- [Concentric Area with editorial catalogue](previews/bauhaus-circle-editorial-ziggy-area.svg)
- [Concentric Arcs with editorial catalogue](previews/bauhaus-circle-editorial-ziggy-arcs.svg)

**Important:** the vector previews are source-derived *design comparisons*, not screenshots of the hosted page or of a real mobile Safari canvas.

## Test results

The embedded JavaScript compiled. Simulated DOM/Canvas checks using the actual Bowie CSV passed **17 assertions**:

1. Correct 11-track filtered Spotify dataset and updated editorial deck.
2. Previous unnecessary explainer labels and `OF 11 RECORDS DISPLAYED` callout absent.
3. Eleven record rows visible, ordered largest to smallest.
4. Actual MAX/MIN values **829,880,663 / 23,172,806**, correctly formatted.
5. Exact source labels preserved for the two stat blocks.
6. Record count included in the footer rather than as a separate art callout.
7. Measured circle centres shifted right, with the narrow list entirely to the left.
8. Tapping a catalogue row returns the complete real label and raw value.
9. Tapping the MAX stat returns the complete source value.
10. Arc mode preserves the catalogue and stat values without changing the mappings.
11. Range mode shows only the original two min/max records.
12. All-album dataset with 64 valid plotted rows only draws/list the original first 16 and discloses this in footer.
13. Extrema of this 16-record subset explicitly labelled as displayed-only.
14. PNG preview/export UI action remains connected.
15. Existing Patchwork remains available.
16. Newly imported CSV cannot silently replace an existing artwork before the first explicit Create.
17. Both existing Circle Art and Arc mathematical encodings remain untouched.

## Visual and device QA gate before merge

- Inspect the final **actual canvas-exported PNG** at 960×960 in a browser and compare it to the two independent vector previews. Verify 11px label fidelity, mobile downscaling, header/deck/footer safe margins and full number fit.
- Test **1 / 2 / 11 / 16 / 64** source values, very long labels, a numeric value wider than the allocated column, ties and a valid zero-only dataset.
- Test Gallery Paper, Ink Study, Colour Study and Studio Original contrast; swatches must match actual layer colours.
- Test tapping a record row, centre ring, arc and MIN/MAX block on a real iPhone Safari; check PNG saving.
- Confirm current sorting before the Circle first-16 cap, and verify the first-16 subset disclosure rather than implying global extrema.
- No direct merge to main without explicit approval.
