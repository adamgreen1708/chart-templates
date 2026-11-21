# Editorial reset — A-Team, 21 November 2026

## Status: HOLD / REJECT FIRST RENDERS
User feedback: "These are really underwhelming". Treat all three existing charts as failed *editorial* QA regardless of passing technical render QA. The existing images must not be presented as approved, copied into site/assets or merged.

## Research from pinned ONS-derived source (1996–2024)
All figures here use exact boys' names in England and Wales; chart_02_annual.csv is pinned to Git blob 2d2c3837eb1d3c82601bdf5539e95ffab15d0579.

- **Alex vs Adrian in 2002:** Alex 1,707; Adrian 89. Ratio **19.18:1**. Among just those two names, Alex 95.04%, Adrian 4.96%.
- **Alex vs Adrian in 2024:** Alex 295; Adrian 200. Ratio **1.475:1**. Among just those two names, Alex 59.60%, Adrian 40.40%.
- Alex's lead over Adrian did **not vanish**, but its ratio contracted markedly. This two-name share has its own two-name denominator, NOT all newborn boys; show absolute counts with shares.
- **Adrian's second act:** 2002 89 births (within 1996–2024 series low), 2013 273 (highest in that series), 2024 200. This is a hump, NOT a smooth 1996-to-2024 increase.
- **Adam / Adrian ratio:** 2002 3,527 / 89 = 39.63:1; 2024 1,410 / 200 = 7.05:1.
- Published-name share (NOT all boys): Adrian 1996 = 155 / 318,517; 2024 = 200 / 277,788, a +47.95% change in this proxy. The previous official 1996/2024 male-birth two-endpoint normalisation gives approx +41.1%; do not substitute proxy for all-boy rate without labelling it.

## Three competing editorial hypotheses
1. **The sibling upset / Alex's shrinking advantage** (PREFERRED): comparative counts of Alex and Adrian went from nineteen-to-one to less than three-to-two. Strong natural human hook; denominators cancel for the same-year ratio. Weakness: other brother Adam needs deliberate inclusion in the prose or a separate chart.
2. **Adrian's peculiar comeback:** the underdog bottomed out in 2002, trebled by 2013 and stayed above his 2002 level in 2024. Strong actual non-monotonic finding; should show full curve with real years and underlying denominator. Weakness: raw births are affected by cohort size and a single-name chart is narrowly focused.
3. **Three different eras:** Adrian early popular (observed 1964 No. 30), Adam high 1994 (No. 11), Alex best observed 2002–2003 (No. 42). Charming context but one-decadal historical rankings cannot support a continuous timeline or exact peak claim. Probably prose/sidebar rather than a full data chart.
**REJECTED:** A vs J. True but detached from three brothers. 1996-to-2024 three-item percentage dot plot is a table in disguise. Connecting sparse historic ranks offers little discovery and implies continuity we did not observe.

## Proposed NEW visual arc — must pass senior-editorial gate before configs
1. **Set-up: "Three A's. Three different glory years."** Data-driven milestone strip with 1964 Adrian No. 30, 1994 Adam No. 11 and 2002–2003 Alex No. 42; **explicitly** say best *observed* ranking when decade-only sampling applies. Consider replacing with prose if merely decorative.
2. **Tension: "Adrian's spectacularly badly timed comeback"** Annual index / rate-per-10,000 trend showing 2002 low, 2013 rebound, 2024 position. For a *true share of boys born*, obtain and verify male live birth counts for every annual denominator first; otherwise use explicitly labelled published-name share as proxy, NOT total-birth share.
3. **Reveal: "Alex's 19-to-1 lead becomes 3-to-2"** High-impact paired composition: 2002 and 2024 equal-footprint grids of 20 discrete marks each, representing 5 percentage points of Alex+Adrian name registrations in that year. Count labels must show the exact 1,707/89 and 295/200 numbers. 2002 19 red Alex dots vs 1 grey Adrian dot, 2024 12 vs 8 (nearest 5 pp). Denominator must be plainly stated, and do not suggest 20 marks represent equal numbers of births across years. Alternative: honest paired 100% stacked bars with counts.
A two-chart story is preferable if the historical strip does not earn its space.

## Hard production constraints
No fabricated data, no image-generated charts. New quantitative visuals must be built from stored CSVs by an approved deterministic GitHub renderer/specialist, with actual 1600px and 390px/320px QA. A 20-dot icon grid needs a specialist repo-based renderer, not a ChatGPT illustration. Each chart must show something non-obvious and each source/denominator explicitly.
Leave PR in draft; seek editorial review and explicit approval before changing the live site.
