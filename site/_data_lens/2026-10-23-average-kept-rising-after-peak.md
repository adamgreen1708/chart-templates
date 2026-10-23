---
date: 2026-10-23
header: "TODAY’S DATA LENS"
title: "The average kept rising six days after the peak."
observation: "Daily values peak at 100 on Day 6, then fall every day. But the trailing 7-day average keeps rising until Day 12, because earlier low values are still dropping out of the window. Smoothing can make a turning point arrive late."
kicker: "Smoother often means slower."
hero_image: "/assets/data-lens/daily/2026-10-23-average-kept-rising-after-peak.png"
hero_alt: "Square Today’s Data Lens card showing a grey daily-value line peaking at 100 on Day 6 and then declining, while a red trailing 7-day average continues rising to its peak of 70 on Day 12. A shaded band marks the six-day lag between the raw peak and rolling-average peak."
sources:
  - title: "Datawrapper — The COVID-19 chart I wish I didn’t have to make"
    url: "https://www.datawrapper.de/blog/covid19-corona-berlin-second-wave"
qa:
  run_date_verified: true
  claim_verified: true
  sources_verified: true
  copy_deck_frozen: true
  render_checked: true
  page_copy_checked: true
---
Rolling averages are useful when daily data is noisy — website visits, service demand or operational volumes, for example — because they make the underlying direction easier to see. The trade-off is timing: a trailing average still contains earlier observations, so a sharp turn in the raw data may take several periods to appear clearly in the smoothed line.

That matters if you are using the chart to identify peaks, recoveries or the effect of an intervention. Show the raw values as context where possible, and always state the rolling window being used.
