---
date: 2026-10-17
header: "TODAY’S DATA LENS"
title: "On a log scale, doubling travels the same distance."
observation: "10→20 and 50→100 are very different absolute changes: +10 and +50. But both are doublings — a 100% increase. On a logarithmic axis, equal ratios occupy equal distances, so those two changes appear the same length."
kicker: "Linear measures difference. Log measures ratio."
hero_image: "/assets/data-lens/daily/2026-10-17-log-scale-doubling-same-distance.png"
hero_alt: "Square Today’s Data Lens card titled ‘On a log scale, doubling travels the same distance.’ It compares 10→20 and 50→100 on linear and logarithmic axes. The linear scale shows different arrow lengths for +10 and +50; the log scale shows equal arrow lengths because both changes are ×2, or +100%."
sources:
  - title: "Datawrapper — How to read a log scale: Growth rate"
    url: "https://www.datawrapper.de/blog/weeklychart-logscale"
  - title: "Datawrapper — How to read a log scale: The chart that can’t start at zero"
    url: "https://www.datawrapper.de/blog/weeklychart-logscale2"
  - title: "Storytelling with Data — How axis scales distort your data’s story (and what to do instead)"
    url: "https://www.storytellingwithdata.com/blog/dont-let-your-axis-scales-distort-the-story"
  - title: "FlowingData — Coronavirus, a Visual Rundown — The Process 080"
    url: "https://flowingdata.com/2020/03/12/coronavirus-process-080/"
qa:
  run_date_verified: true
  claim_verified: true
  sources_verified: true
  copy_deck_frozen: true
  render_checked: true
  page_copy_checked: true
---
Log scales are useful when the **relative change matters more than the raw difference**, particularly when values span a very wide range. A good example is comparing growth across businesses or populations of very different sizes: moving from 10 to 20 and from 1,000 to 2,000 are both doublings, even though their absolute increases are nowhere near the same.

They’re also useful for spotting sustained percentage growth in a time series, because equal growth rates produce similar slopes. The trade-off is unfamiliarity — and zero cannot appear on a logarithmic axis. A useful check is: **am I trying to compare ratios, or actual differences?**
