# Coffeetableviz social vNext: October 2026 retrospective and review

**Status: draft, opt-in; existing 538 standard remains locked.**

## Root cause and evidence

The October seven-chart carousel exposed upstream branding differences:
- Conventional 538 configs: UK age profile and Messi, with per-project subtitle, annotation and footer sizes.
- Shared bespoke route geometry: Simon Reeve, with its own editorial header/footer geometry.
- Independent Matplotlib figures: Ed Hawkins, Minard, Nightingale and Verstappen, sharing some colours but not a consistent typography/spacing contract.

The PDF did not introduce those different chart styles; they existed in the PNGs.

## Mandatory delivery contract

1. The source of truth for data, CHART_CONFIG, renderer and accepted PNG is GitHub.
2. Charts of ordinary types use src/render_538.py; specialised graphics must be registered as a shared, deterministic CHART_CONFIG-backed renderer type with a central header/footer.
3. All approved output uses light grey #F3F4F6 and defined semantic use of primary #1F8FA8 / accent #C44E52. Historical colours need documented meaning, not arbitrary replacement.
4. Social is an **opt-in** profile; do not change previous standard output, published assets or existing default configs.
5. QA of chart content, source/version, units and data claims is required independently from visual QA.
6. Inspect 390px and 320px **actual PNG previews** plus full-size; shortening or selectively decluttering captions is preferable to tiny labels.
7. Existing approved assets must not be replaced or the PR merged without explicit approval.

## Three evidence-based preview cases

- 04A UK population: a normal line chart with annotations.
- 01B Simon Reeve: a labelled map-like editorial schematic.
- 03C Verstappen: a dense start/finish chart newly migrated to shared `position_shift` via CHART_CONFIG.

Workflow `.github/workflows/qa-social-profile.yml` renders the three configs, runs tests and uploads original-size output plus 390px and 320px QA images. The workflow **does not** publish to the site or commit generated images.

## Design review

Trial sizes: title 26pt, subtitle 16pt, axis/tick 12pt, annotations at least 11.5pt, footer 10.5pt. These are starting sizes, not a blanket rule; label density may require redesign.

Manual checks before promotion:
- original and social versions side-by-side at phone size;
- margins, source and subtitle readable;
- no overlap or ungrounded data transformations;
- project captions short and natural;
- footer and alignment consistent across the three types;
- no degraded original SVG/PNG and no change to main.

**Do not classify the workflow as passing visual QA solely because files exist or are resized.** A human must inspect the actual rendered pixels.

## Later migration backlog

Legacy scripts for Minard, Nightingale, Ed Hawkins and other editorial series need gradual, chart-by-chart migration. Do not rewrite them in bulk or weaken their distinctive encodings. Record remaining exceptions and the exact source PNG hash at migration time.

## Trial finding from actual 390px/320px previews

The first Simon Reeve social render visibly collided with the explainer and had unreadable dense stop/country labels. The review branch now moves the map below the larger heading and displays selected country names, preserving all ten numbered positions while directing readers to the full route. This is a social **editorial reduction**, not a replacement for the full website chart. Compare the updated pixels before approving. Verify the subtitle and country labels still clear the plot; automated tests alone cannot certify this.

## October review correction — layout and canvas (30 October)

The first mobile prototypes repeated three problems identified by Adam: unequal whitespace/padding on the four edges, a disconnected Simon Reeve subtitle/explainer stack, and a default white Matplotlib plot patch on Verstappen. All are upstream rendering defects, not PDF defects. The updated social profile uses a shared 8.5% reference safe frame with figure text aligned near 9%/91% and the plot inset further for axis labels. The rendered-pixel QA job enforces at least **7% clear margin** on all four edges and rejects white plot panels. This minimum allows for antialiasing and modest label width but never authorises edge bleed.

For editorial schematics the social heading is now stacked based on the text's rendered bounding boxes rather than hard-coded gap guesses. The mobile Simon Reeve variant shortens its wording and tightens the bracket/tick panel while retaining the exact source geometry and ten numbered country markers. Never apply the social simplification to the approved web image without explicit review.

A clean CI run is necessary but not enough: final decision still depends on Adam seeing the actual 390px and 320px previews and confirming visual consistency.
