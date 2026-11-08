# Pixel Universe — implementation brief v1.0

**Status:** agreed creative direction; **Phase A (palette compatibility) in a draft PR**. No publication or merge authorised.
**Repository:** `adamgreen1708/chart-templates`
**Inspiration:** the published [Who wears the hero colours?](https://coffeetableviz.com/stories/who-wears-the-hero-colours/) story and [Tim Leong's *Super Graphic*](https://www.wired.com/gallery/excerpt-visual-guide-to-the-comic-book-universe/).

## Core question

**Can you recognise a superhero from colour alone?**

Use the *existing* curated comic-costume palette dataset as a springboard for original, accessible, interactive data art. A pixel icon is an **artistic interpretation** of recorded colour categories, **not** an observed body/fabric-area proportion, objective identity-recognition experiment or artwork tracing.

## Defined v1 audience experience

- Twelve original **16×16** pixel-art **mask/bust-like** icons, six heroes and six villains.
- Two matching square artworks: a hero mosaic and a villain mosaic.
- One dedicated gallery at `/resources/pixel-universe/`, with each icon's name, record-derived main / supporting / accent hues, and an **Open & remix** link to the existing [Pixel Art Studio](/resources/8x8-pixel-art-builder/).
- A short Coffeetableviz story with a clear link to the **published superhero palette** article, and a gentle invitation to remix.
- A companion social draft. Nothing publishes before review.

### Approved character set

| Role | Publisher | Character | Coded main → supporting → accent |
|---|---|---|---|
| Hero | DC | Superman | blue → red → yellow |
| Hero | DC | Batman (Bruce Wayne) | grey → black → yellow |
| Hero | DC | Wonder Woman (Diana) | red → blue → gold |
| Hero | DC | The Flash (Barry Allen) | red → yellow |
| Hero | Marvel | Spider-Man (Peter Parker) | red → blue → black |
| Hero | Marvel | Wolverine (Logan) | yellow → blue → black |
| Villain | DC | The Joker | purple → green → orange |
| Villain | DC | Riddler (Edward Nygma) | green → purple |
| Villain | DC | Lex Luthor | green → purple |
| Villain | Marvel | Green Goblin (Norman Osborn) | green → purple |
| Villain | Marvel | Magneto (Max Eisenhardt) | red → purple |
| Villain | Marvel | Venom (Eddie Brock) | black → white |

These categories are read from `archive/projects/2026-11-superhero-colour-code/data/character_palette_seed.csv` **on current main**. Preserve selected costume versions and the published `data/publication_source_review_2026-11-08.csv` qualitative-method caveats. Do **not** silently replace the seed using unmerged PR #194 research.

## Pixel Art Studio compatibility contract

The current 13-entry JavaScript palette has white/eraser index `0` and twelve paint entries `1–12`. This phase appends **three** named colours without moving or changing the first 13 swatches:

| Index (numeric) | Pixel code | Colour | HEX |
|---:|:---:|---|---|
| 13 | d | Purple | `#6F42C1` |
| 14 | e | Gold | `#D4A017` |
| 15 | f | Silver | `#B8BDC3` |

There are now **16 total entries / 15 paint colours**, not sixteen paint colours.

One lowercase hexadecimal character per pixel (`0–f`) replaces the former base-13 character encoder. Since all previous values `0–c` have identical one-character spelling and unchanged palette indices, all old saved codes / URLs retain the **same bytes and appearance**. No migration of `localStorage` keys or old URLs is needed.

- 8×8 URL: `#art=<64 hex digits>`
- 16×16 URL: `#size=16&art=<256 hex digits>`
- Preserve `coffeetableviz.pixel-art.v1` and `coffeetableviz.pixel-art.16.v1` storage keys.
- Preserve all `site/_data/pixel_art_gallery.yml` codes, plus old heart/smile presets.
- The pixel builder JS, zoo JS, paint colour buttons and both page templates must use the same indexed colours.
- Do not change the pixel count, export size, artwork URL format, zoom/pan, undo/redo or save/share semantics.
- **No new characters/presets in Phase A**; first validate compatibility.

## Original art directions

One coherent 16×16 geometry family: simplified original graphic icons/masks/busts; consistent edge/outline weight; 1–3 story colours where possible; optional dark/white neutral pixels to maintain contrast; deliberate symmetry where it helps identification. Avoid copy-pasting protected comic panels, comic-book logos, distinctive insignia and traced official artwork. Stylise rather than reproduce exact costumes. Keep visuals clearly labelled as **inspired by** characters and their qualitative palettes, and do not imply affiliation or endorsement by Marvel/DC.

Prefer readability at **64px thumbnail** and 320px mobile display. Mosaic artwork is 1:1, with `#F3F4F6` background unless a tested contrast exception is approved, no clipped edges and a consistent six-tile composition per side.

## Proposed v1 file structure (Phase B)

```text
archive/projects/2026-11-pixel-universe/
  project_manifest.md
  implementation_brief.md
  data/
    pixel_universe_characters.csv
    pixel_universe_presets.csv
  scripts/
    build_pixel_universe.py
    validate_pixel_universe.py
  output/
    hero_mosaic.png
    villain_mosaic.png
    presets/
  content/
    editorial_draft.md
    qa_notes.md
    social_copy.md
site/_data/pixel_universe.yml
site/resources/pixel-universe/index.html
```

Generate the 12-character table from the upstream CSV and join by exact identifiers; never hand-maintain an independent source-of-truth colour dataset. Store each 16×16 drawing as a 256-character code, keyed to the source character/version. Derive both gallery thumbnails and share links from that code, and check rendered PNGs are deterministic.

### Controlled delivery

**Phase A — this draft PR:** additive colour swatches, safe hexadecimal encoding/decoding, page copy, regression tests, brief/manifest. Branch from current `main`. Do **not** publish the site or touch unrelated art data; stop for review.

**Phase B — after Phase A approval/merge:** 12 original 16×16 drawings, first prototypes Superman + Joker for creative review, two mosaics, gallery, deterministic exports and links. New branch and PR; review at phone scale and native resolution.

**Phase C — after art/gallery approval:** publish a short Culture/Design editorial sequel, feature asset, source note and understated social post in a separate PR. Follow current Jekyll/GitHub Pages publishing workflow and verify the published URL after merge. No automatic main merge.

### Tests and approval gates

1. Original `0–c` HEX mappings are byte-for-byte identical to the prior published Studio and Tiny Zoo data.
2. All legacy `#art` and `#size=16&art` links and locally saved codes still parse and render; test at least one existing 8×8 and 16×16 example.
3. New `d/e/f` colours round-trip through 8×8 and 16×16 paths, local persistence, preview and PNG export.
4. All UI swatch labels, hex strings, indices and script versioned URLs are in sync.
5. Existing Tiny Pixel Zoo thumbnails, presets and links do not change visually.
6. Full-size, 390px and 320px visual QA; no clipping or inaccessible text and preserved keyboard/touch/zoom/undo behaviours.
7. All 12 sprite records must match actual source character/version and main/support/accents; avoid fabricated area shares.
8. An approved Pixel Universe release stays separate from the already-published superhero article and from unmerged research PR #194.
9. **Never merge or publish before explicit approval.**
