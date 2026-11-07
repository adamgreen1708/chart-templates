# Story discovery — superhero colour code

**Stage:** pilot dataset, three rendered review charts, phone-size layout QA complete; source-art verification and site publication still blocked.

## Ranked routes

1. **Colour is a clue, not a rule (recommended).** Revisit Tim Leong's contrast between heroic primaries and villainous secondaries; show the pattern, publisher split, and famous exceptions. **Strength:** visual and testable. **Risk:** only a purposive n=24 pilot; colour assignment is observational.
2. **Marvel vs DC: two houses, one palette?** Is one universe more loyal to primary colours? **Strength:** clear comparison. **Risk:** six characters per cohort too few to represent a publisher, particularly with variant costumes.
3. **The wardrobe rebels.** Green-clad heroes and primary-coloured villains. **Strength:** memorable and shareable. **Risk:** anecdote-only unless backed by the comparison.
4. **Colour proportions and IMDb movie scores.** **Rejected for this comic-book research:** film imagery and ratings would recreate the weaker 2025 methodology and require unreliable fabric-area estimates.

## Recommended 3-chart editorial sequence

### 1 — Is there a colour code for good and evil?
Compare **dominant costume hue**, by hero and villain: red, blue, yellow, green, purple, orange (plus explicit neutral-colour caveat). Source: `data/chart_01_hue_skew.csv` (built from `data/chart_01_colour_frequency.csv`).
Recommended form: six-row diverging horizontal bar comparison of **hero share minus villain share, in percentage points** (positive = more frequent among heroes). State that grey, black and other hues are omitted from these six rows but still included in both denominators. The six-row form is deliberately chosen for phone readability.

### 2 — Does Marvel follow DC's rules?
Compare the **share of characters whose dominant hue is a strict primary** for the four publisher × hero/villain groups. Source: `data/chart_02_primary_by_publisher.csv`. Recommended form: four labelled horizontal bars (all denominators six), visually pair the two roles within publisher.

### 3 — The colour code has some famous rebels
Show **heroes without a primary dominant hue** and **villains with a primary dominant hue**, with actual hue names and a visible key. Source: `data/chart_03_exceptions.csv`. Recommended form: compact dot/table with exact names, publisher, dominant-hue swatch. If current shared renderer cannot colour points accurately, propose a limited documented renderer extension after reviewing charts 1–2 rather than silently changing the whole house template.

**Working takeaway (not a publication-ready quantitative claim):** classic costume colour conventions are a helpful visual trope, but notable costumes break the rule.

## Publication blockers
- Actual art/colour verification of all 24 observations not complete.
- Sampling is editorial, not random or exhaustive; avoid population generalisations.
- No PNG render/phone-sized QA yet. Keep this branch research-only until validated.

## Updated phone-first chart-1 decision (7 November 2026)
Twelve separate tiny hero/villain bars for six colours are likely to be cramped at 320px. The **recommended production chart 1** is now a **six-row diverging horizontal bar**:
- `data/chart_01_hue_skew.csv` stores each colour's hero and villain counts, shares, plus the signed difference in **percentage points** (positive = more frequent among heroes).
- Use a zero reference line and clear `More common among heroes` / `More common among villains` axis captions. Keep actual hue as an unambiguous row label; use documented semantic highlights rather than decorative multicolour bars when a shared chart colour is also being used for role.
- Actual sample result from the provisional dataset: **red +33.3 percentage points** towards heroes, **green −41.7 pp** towards villains; six family rows fit the square canvas more easily than 12 category labels. Black and grey are still counted in both denominators.
- Note orange is **more common among heroes (one Aquaman vs zero villains)** in this deliberately curated sample, a useful counterexample to a simplistic 'secondaries mean evil' headline.
- The story plan remains **1. Hue skew by role; 2. Four publisher/role primary shares; 3. Seven named exceptions**.
- Do not describe any percentage-point difference as percentage of costume coverage, or test significance from the purposive sample.
