# Project manifest — Superhero colour code

- **Slug:** 2026-11-superhero-colour-code
- **Started:** 2026-11-07
- **Category:** Culture
- **Project intent:** new DC/Marvel heroes-vs-villains comic costume analysis inspired by the 2025 *Shades of Heroism* Tableau work.
- **Current status:** Research / provisional pilot data for editorial review; NOT production ready.
- **Main dataset:** `data/character_palette_seed.csv` (24 observational records, six per cohort; requires artwork QA)
- **Derived views:** `data/chart_01_colour_frequency.csv`, `data/chart_02_primary_by_publisher.csv`, `data/chart_03_exceptions.csv`
- **Build:** `scripts/build_chart_views.py`
- **Editorial:** `content/story_discovery.md` and `content/pilot_findings.md`
- **Method/risks/sources:** `METHODOLOGY.md`
- **Rendering:** pending config/renderer and phone-image QA
- **Publishing:** not authorised; no site files or site assets touched

- **Evidence audit:** `data/source_evidence_audit.csv` (all 24 have publisher reference, 11 with relevant explicit colour text; **none pass exact comic-art review**)
- **Sensitivity input/output:** `data/colour_coding_alternatives.csv` and `data/chart_coding_sensitivity.csv`
- **Six-hue diverging chart 1:** `data/chart_01_hue_skew.csv` (replaces the more cramped 12-label bar concept, while preserving the original frequency view)
- **Current review state:** Source references strengthened, sensitivity tested; **no final visual verification, chart config, render or publication**
- **GitHub social_square render:** three `config/chart_*.py` files, three 1600px `output/superhero_*.png` exports, six `output/qa/*_320.png` and `*_390.png` phone previews.
- **QA:** `scripts/qa_phone.py` and `content/render_qa_notes.md`; layout inspected and passed, source-art verification not completed.
- **Editorial:** `content/blog_draft.md` for review only, no Jekyll files modified.
