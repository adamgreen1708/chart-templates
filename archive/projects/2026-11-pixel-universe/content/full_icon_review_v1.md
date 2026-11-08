# Pixel Universe v1 — full icon set for creative review

**Status:** 12 editable original **16×16** icons completed for review, including the **unchanged, previously approved Superman and Joker**. This research-art PR is stacked after prototype PR #198, not on the live site. No merge or publication.

## Data and design

- **Primary source:** `archive/projects/2026-11-superhero-colour-code/data/character_palette_seed.csv` already published in the repository.
- **Manual art codes:** `data/pixel_universe_art_v1.csv` (12×256 exact hexadecimal indices, source-named character and original geometric art description).
- **Deterministic generation:** `scripts/build_pixel_universe_v1.py` joins each art code to source data, checks publisher/role and required colour tags, parses the current Studio palette, and regenerates individual SVGs and two 1:1 square mosaics.
- **Mosaic previews:** `output/v1/hero_mosaic.svg`, `output/v1/villain_mosaic.svg`.
- **The two approved prototypes:** Superman and Joker pixel codes compared byte-for-byte against `data/pixel_universe_prototypes.csv` from PR #198; unchanged.
- **Ten new creations:** Batman, Wonder Woman, Flash, Spider-Man, Wolverine, Riddler, Lex Luthor, Green Goblin, Magneto and Venom.

### Visual rule

Consistent blocky, original simplified busts or mask silhouettes. Contrast-led black outlines; source main/support/accent colours present but **not** deliberately sized to represent measured clothing areas. Other face/eye/outline shades are design choices. No official emblems or copied art. These are standalone, unofficial fan-inspired illustrations.

### Editing in Pixel Art Studio

For a row in `data/pixel_universe_art_v1.csv`, append its exact 256-character `pixel_code` after `https://coffeetableviz.com/resources/8x8-pixel-art-builder/#size=16&art=`. The resulting link opens an editable design using the 16-entry palette merged in PR #197. This preview phase intentionally does **not** add a public gallery or alter the Zoo.

### QA gates

- All 12 artwork codes are exact 16×16 lowercase hex encodings, unique, and use the original 16-slot palette.
- All required colour categories come from the published *qualitative* costume dataset. No percentages, pixels of garment area, or objectively measured recognition performance are claimed.
- Generator and test scripts are stdlib-only; tests check row counts, the two unaltered prototypes, palette colour presence, and exact deterministic SVG mosaic regeneration.
- Image composition: 1200×1200 light grey `#F3F4F6`, six 16×16 previews arranged 3×2 per mosaic, names under each icon and an editorial method footer.
- **Remaining:** run tests in GitHub CI, inspect at 320px/390px and phone scale; fix any crowding, then review creative direction before gallery/article development.

**Not published**: Jekyll story, Pixel Universe resource/gallery and live Studio are untouched. PR #194 is also unchanged.
