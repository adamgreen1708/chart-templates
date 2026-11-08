# Pixel Universe — creative prototype review (after PR #197)

**Stage:** two original 16×16 editable **review-only prototypes**. Nothing is live, merged or ready for article publication.

Source for hue categories: `archive/projects/2026-11-superhero-colour-code/data/character_palette_seed.csv` (published, curated qualitative 24-character set). In the published study the colours are **judgements**, not digitally measured fabric-area proportions.

| Prototype | Main | Supporting | Accent | Additional creative pixels |
|---|---|---|---|---|
| Superman | blue | red | yellow | sand-coloured face, black silhouette |
| Joker | purple | green | orange | silver/grey face, black outline |

Shapes and skin/outline colours are **creative decisions**, not data inputs. There are no official insignia, traced artwork or copied panels. Neither prototype demonstrates statistically measured colour area or audience recognition.

**Review previews:** `output/prototypes/superman.svg` and `output/prototypes/joker.svg`. Source editable codes: `data/pixel_universe_prototypes.csv`.

**How to try in the live Pixel Art Studio:** take the 256-character `pixel_code` for either character and append it after `https://coffeetableviz.com/resources/8x8-pixel-art-builder/#size=16&art=`. This uses only the backwards-compatible `0–f` palette now on `main` after merged PR #197. No changes to the Studio or Tiny Pixel Zoo are needed for these previews.

## Next editorial checkpoint

- Inspect both 16×16 symbols at native/large preview and thumbnail size.
- Decide whether the visual language is sufficiently recognisable and consistent.
- Once approved, expand to the other ten selected heroes/villains, build two 1:1 mosaics, then a proper Jekyll-based Pixel Universe gallery.
- Keep the eventual article/gallery in a separate publication PR and protect all existing published superhero pages.
