---
date: 2026-10-29
header: "TODAY’S DATA LENS"
title: "100% can tell you less than 95%."
observation: "A Wilson interval is a 95% confidence interval for a proportion. Site A scores 100% from 10 responses, but its interval is wide: 72.2%–100%. Site B scores 95% from 1,000 responses and its interval is much narrower: 93.5%–96.2%. Narrower means a more precise estimate."
kicker: "The rate is the headline. The interval shows the uncertainty."
hero_image: "/assets/data-lens/daily/2026-10-29-100-can-tell-you-less-than-95.png"
hero_alt: "Square Today’s Data Lens card comparing customer satisfaction at two sites. Site A reports 100% from 10 responses with a wide 95% Wilson confidence interval of 72.2% to 100%. Site B reports 95% from 1,000 responses with a narrow interval of 93.5% to 96.2%. A three-step strip explains the rate, Wilson confidence interval, and that wider intervals are less precise."
sources:
  - title: "OHID — Proportions and odds (Wilson score intervals)"
    url: "https://fingertips.phe.org.uk/static-reports/public-health-technical-guidance/Basic_statistics/Proportions.html"
  - title: "NIST — confidence interval"
    url: "https://csrc.nist.gov/glossary/term/confidence_interval"
qa:
  run_date_verified: true
  claim_verified: true
  sources_verified: true
  copy_deck_frozen: true
  render_checked: true
  page_copy_checked: true
---
A Wilson interval is a **confidence interval for a proportion**. It starts with the observed rate — successes divided by responses — then adjusts the centre and width using the sample size and the chosen confidence level. For a 95% interval, the calculation uses a standard-normal value of 1.96.

The important bit is how to read it. A wide interval means the estimate is relatively imprecise; a narrow one means much more evidence sits behind the headline percentage. It does **not** mean there is a 95% probability that the true rate lies inside this particular interval.

That is why showing the denominator alongside a rate can materially change how convincing the KPI feels.
