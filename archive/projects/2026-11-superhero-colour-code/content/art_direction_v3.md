# Comic-art direction — chart review V3 (not for publication)

**Purpose:** Explore a more recognisably comic-book treatment for the approved three-chart narrative, without replacing v2 charts, revising source measurements, or implying statistical representativeness.

The experimental branch is `draft/2026-11-superhero-art-direction`, branched from PR #193's v2 version. It is **not a replacement or approval request for PRs #192/#193**.

## V3 outputs

| Order | Editorial hook | Data | Chart encoding |
|---|---|---|---|
| 01 | Can you spot the villain? | `data/chart_v2_01_costume_gallery.csv` (12 characters) | Two opposing comic-panel line-ups; three equal chips are categorical main/second/accent hues, never garment proportions |
| 02 | Good colours. Bad intentions. | `data/chart_v2_02_role_scorecard.csv` (24 characters) | Two wheels of 12 **equal** 30-degree sectors, one sector per selected character, colour = dominant coded hue; centre 8/12 vs 3/12; cohorts are first DC then Marvel clockwise |
| 03 | Same paint. Different morals. | `data/chart_v2_03_colour_twins.csv` (5 pairs) | Five paired comic-card showdowns, shared leading hue as centre badge, left/right secondary hue identified explicitly |

- All three read the pre-existing v2 derived CSVs (re-generated from `data/character_palette_seed.csv` by `scripts/build_chart_views.py`).
- Code is a new opt-in `src/editorial_palette_art.py` module connected through `src/editorial_palette.py`, and the ordinary `src/render_538.py` path. Does not use generated character imagery, commercial logos or comic panels.
- New configs `config/chart_v3_0*.py`, output `output/superhero_v3_0*.png`, native 1600×1600, square house background `#F3F4F6`.
- **Presentation still subject to editorial judgement:** the wheels make relative role palettes attractive but make individual wedge names invisible. Chart 1 and the source CSV provide character identities; chart 3 supplies matched exceptions.
- **Research limitations have not changed:** purposive 24-character pilot, all exact costume-art classifications provisional, no measured fabric coverage and no claims representing all Marvel/DC characters. Source audits and ambiguity notes are in `METHODOLOGY.md` and `data/source_evidence_audit.csv`.
- Do not merge this experiment into #193 without specific approval. Do not modify any Jekyll post, site asset or production output.
