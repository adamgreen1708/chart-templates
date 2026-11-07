# Superhero colour code — dataset and method (research draft)

**Status:** provisional manual costume coding, NOT approved chart or blog evidence. **No publishing.**
**Original Tableau concept:** https://public.tableau.com/app/profile/adam.green4310/viz/Shadesofheroism/shadesofheroism
**Existing Coffeetableviz write-up:** /2025/01/17/shades-of-heroism/

## Question
Do classic comic-book heroes predominantly use **red, yellow and blue** while villains predominantly use **orange, green and purple**? Does this differ between Marvel and DC? Where does it fail?

## Pilot design
- 24 recognisable characters: six classic heroes and six classic villains per publisher (a **purposive, balanced editorial sample**).
- One defined, classic **comic-book** costume/era per character; do not mix MCU/DCEU films, games, reboots or civilian clothes.
- Heroes/villains label is tied to the costume portrayal, not a timeless claim about the character. Loki and Magneto's antagonist eras and Sinestro's yellow suit are declared explicitly.
- A visually most prominent **costume hue** is coded by editorial judgement, not extracted scientifically. Where multiple main colours compete, see `coding_notes` and `coding_confidence`.
- Skin and hair are **excluded**. Accents are recorded but **do not count** towards the dominant-colour metric. Hence Black Manta's red eyes and Batman's yellow belt do not make their costumes red/yellow.
- Raw colour words are preserved: gold, silver, grey, etc. The strict primary **dominant** group is only `red`, `blue`, `yellow`; secondary is `orange`, `green`, `purple`. Gold is NOT silently treated as yellow; neither are black, white or grey forced into primary/secondary groups.
- Source URLs provide publisher or official comic character context, not measured costume percentages. Some URLs lead to an index/series; before approval, a curator must inspect a dated, specific reference comic panel or full-body character artwork and preserve its citation.
- Every seed row is marked `provisional_visual_QA_required`. No statistical population claims, hypothesis-test p-values or percentage-of-fabric claims are warranted.
- This pilot should be expanded or systematically sampled before broad language such as “Marvel heroes generally wear…” is used.

## Source inventory
1. [Tim Leong, *Super Graphic*](https://www.wired.com/2013/07/excerpt-visual-guide-to-the-comic-book-universe/) — inspiration/hypothesis only, no copied colour ratios.
2. [ACMI on superhero costume colour conventions](https://www.acmi.net.au/stories-and-ideas/primary-colours-adapting-superhero-costumes-from-page-to-screen/) — historical explanatory context.
3. [DC character directory](https://www.dc.com/characters) and individual official character profiles — identity/colour visual references.
4. [Marvel character directory](https://www.marvel.com/characters) and comic profiles/reading lists — identity/colour visual references.
5. [FiveThirtyEight comic-character data](https://github.com/fivethirtyeight/data/tree/master/comic-characters) — potential future scale-up for an objective 2014 appearance-based sampling frame; **not joined to this pilot**. Its alignment and appearance counts do **not** provide costume colours.

## Reproducibility
`scripts/build_chart_views.py` reads `data/character_palette_seed.csv`, verifies 24 unique rows and six per cohort, and regenerates the three numeric chart CSVs. No values in those views are hand-entered.

## QA release gates
1. Verify the concrete comic costume variant against artwork, attach an exact edition/issue/page or visual URL, independently code dominant hue, and reconcile ambiguous cases.
2. Re-run derived views and read the denominators. The sample is small (n=6 per publisher/role subgroup).
3. Agree the editorial story and render all three via `src/render_538.py` with `render_profile: social_square`.
4. Check exported pixels at native resolution, 390px and 320px, including semantic colours, safe margins and chart captions.
5. Prepare archive/blog content and any site asset mapping only after editorial and visual approval, then use a separate publication PR. This research PR does not publish or change `main`.

## Evidence audit (7 November 2026)
- `data/source_evidence_audit.csv` links all 24 pilot records to current Marvel/DC pages or editorial articles. **10 of the 24 references explicitly describe a relevant costume colour or colour combination in publisher prose**; the other 14 provide identity, era or contextual evidence only.
- Even the ten textual colour descriptions **do not establish the most extensive fabric/armour colour**. No one has assessed full-resolution publisher art for every row; `exact_image_reviewed=no` for all 24. Thus all `review_status` values remain `provisional_comic_art_review_required` and no record has final high confidence.
- `data/colour_coding_alternatives.csv` records five plausible *alternative hue/variant* assignments (Batman, Iron Man, Sinestro, Thanos, Magneto) for a conservative sensitivity test. Batman's blue-grey outfit is another documented comic era, **not** evidence that his selected grey-black outfit is blue.
- Publisher sources explicitly distinguish costume eras: DC describes Aquaman's iconic orange and green outfit and his costume changes; Marvel describes Wolverine's yellow/blue suit as well as alternate brown, black and other costumes.
- This is a **RYB/traditional art classification**: red, yellow and blue are treated as primaries; orange, green and purple as secondaries. It is not digital additive RGB, under which green is a primary.
- Numerical `share_percent` represents **share of characters coded with a given dominant hue** (e.g. 5 out of 12), NEVER percentage of garment area, and **all shares are descriptive of this purposive sample**.

## Coding sensitivity analysis
The five explicitly documented alternatives are switched independently, and a possible min/max is calculated for strict primary-dominant characters:
- Heroes: **7–9 out of 12** (58.3%–75.0%), versus 8/12 baseline.
- Villains: **0–3 out of 12** (0%–25.0%), versus 3/12 baseline.
In this specific curated sample, the directional hero-villain contrast survives these five alternatives. **This is not inferential or representative evidence**. New artwork or a wider sample could overturn the result.

See `data/chart_coding_sensitivity.csv`. Both it and `data/chart_01_hue_skew.csv` are reproducibly regenerated by `scripts/build_chart_views.py`. The diverging hue view uses **raw frequency differences before rounding**, avoiding subtraction artifacts such as 33.4 instead of 33.3 percentage points.

## Release status / uncompleted gate
The `source_evidence_audit.csv` and publisher editorials strengthen contextual source quality, but full comic-art verification and a clearly documented selection frame remain incomplete. **Do not describe these rows as independently visually verified**, do not turn provisional results into factual population claims, and do not publish them.
