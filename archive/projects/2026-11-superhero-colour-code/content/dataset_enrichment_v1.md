# Superhero colour data — additive evidence and pixel-art staging (v1)

**Status:** research-only, provisional, not approved for website publication. This work is deliberately stacked **after** the existing superhero editorial redesign PR #193 and changes only four NEW project-specific files. It does not edit the seed, chart CSVs, renderer, chart configs, existing PR #193, site assets or Pixel Art Studio.

## Input and outputs

- Canonical upstream input: `data/character_palette_seed.csv` from PR #192 (inherited via PR #193). **24** curated characters, six heroes and six villains per publisher.
- `data/costume_variant_evidence_v1.csv`: a source/evidence row for **each of the 24** seed characters. Candidate comic issues and stronger direct DC/Marvel primary-source references are noted where traceable.
- `data/pixel_colour_dictionary_v1.csv`: exact colour-index/HEX lookup for the **existing** Pixel Art Studio (`site/assets/js/pixel-art-builder.js`). These are **output display colours**, never measured source artwork colours.
- `data/character_pixel_staging_v1.csv`: an all-24-character mapping of provisional category-level palettes to existing pixel colour indices, with explicit gaps.

## Evidence grading (per-record; no art measurements yet)

| Source evidence grade | Rows | Meaning |
|---|---:|---|
| `specific_issue_and_costume_colour_text` | 6 | Publisher text explicitly associates a costume colour and named comic issue/era |
| `publisher_costume_palette_text` | 5 | Publisher prose mentions costume colours but does not fix an issue/image |
| `specific_issue_identity_only` | 1 | Issue proves selected character/era, not the dominant costume area |
| `publisher_context_only` | 12 | Reference does not settle costume colours; existing seed remains provisional |

**Important:** a specific-issue text reference is **not** the same thing as checking a full-body image. No costume silhouette has been isolated; zero measured colour percentages; **24/24** remain unapproved for dominant-area claims. Sources can name colour combinations without determining which covers the largest fraction of armour or fabric.

Examples of better anchors:
- **The Flash (Barry Allen)** — DC describes red bodysuit and yellow boots and cites SHOWCASE #4 (1956): https://www.dc.com/blog/2014/10/02/catching-up-with-the-flashes
- **Riddler** — DC describes Dick Sprang's green leotard/purple belt from DETECTIVE COMICS #140: https://www.dc.com/blog/2022/08/18/the-fashion-files-riddler-edition
- **Lex Luthor** — DC names the green warsuit introduced in ACTION COMICS #544: https://www.dc.com/blog/2021/09/30/monster-of-metropolis-twelve-moments-that-defined-lex-luthor
- **Wolverine** — Marvel dates the classic yellow/blue costume to GIANT-SIZE X-MEN #1: https://www.marvel.com/articles/comics/top-10-wolverine-costumes
- **Daredevil** — Marvel dates the red costume to DAREDEVIL #7: https://www.marvel.com/amp/articles/comics/daredevil-1964-first-series-now-complete-on-marvel-unlimited
- **Venom** — Marvel anchors Eddie Brock's first Venom bonding in AMAZING SPIDER-MAN #300; additional publisher text describes the black-and-white symbiote: https://www.marvel.com/comics/discover/713/venom-eddie-brock and https://www.marvel.com/comics/collection/70328/venom_adventures_2018

## Pixel Art Studio integration analysis

- **14/24** characters have all recorded colour categories mapped to existing Studio swatches without a missing colour. The remainder have at least one unmapped colour.
- Purple, gold and silver **do not exist** as exact named swatches in the current 13-colour Studio. Purple must not be replaced silently by pink. Gold and silver must not silently become yellow/grey.
- Grey maps to the existing Slate swatch as an **approximate display mapping**, explicitly marked as such.
- All displayed HEX values come from the Studio's palette, **not** from comic art or a measurement process.
- Do not use the indices or categories to produce a 16×16 art code as if they represented fabric-area coverage. Pixel composition must be designed and labelled as an artistic interpretation until source-image masks and measured proportions exist.
- Leave `site/assets/js/pixel-art-builder.js`, gallery, presets and URL format **untouched**. The approved future integration should add a reviewed palette extension and then create a separate art deliverable.

## Next quality gates

1. Pick one dated, official comic panel/cover or full-body reference for each selected costume and record the visual URL, issue, character costume boundaries and licence/display constraints.
2. Independently classify hue against the selected artwork; adjudicate ambiguous red/blue and red/gold mixtures.
3. For any *numeric costume proportions*, define and archive the costume mask and pixel-count script, exclude hair/skin/background, quantify the uncertainty, and only then update the chart data.
4. Rebuild and QA the three editorial charts **only after** approved dataset changes; do not overwrite PR #193 images.
5. Develop a separately reviewed Pixel Universe publication package using the same approved data, with an accessible data/artist-interpretation distinction.

**No claim about all Marvel/DC comics is supported by this purposive 24-character sample.**
