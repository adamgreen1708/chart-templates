# The A-Team — Adam, Adrian and Alex
Status: DRAFT RESEARCH; NOT PUBLICATION APPROVED.
Scope: England and Wales, boys, exact first names. Historical top-100 GRO/ONS rankings are ten-year snapshots only, not annual counts; absences do not imply rank 101. The 1996–2024 ONS-derived TidyTuesday extract is version-pinned; 2025 official ONS workbook is available but not imported here. Names fewer than three births are suppressed.

Source links:
- https://www.ons.gov.uk/peoplepopulationandcommunity/birthsdeathsandmarriages/livebirths/datasets/babynamesenglandandwalestop100babynameshistoricaldata
- https://www.ons.gov.uk/peoplepopulationandcommunity/birthsdeathsandmarriages/livebirths/datasets/babynamesinenglandandwalesfrom1996
- https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2026/2026-06-16/england_wales_names.csv

Three different hypotheses:
1. Adrian arrived first; Adam overtook; Alex appeared later — historical rank chart. Evidence: 1944–1994 observed ranks, not interpolated. Risk: decennial sample only.
2. Adam persisted longer in the rankings while Alex and Adrian changed differently — annual ranked series. Risk: ranks are not numbers of babies; verify clear three-name colour encoding.
3. A grew at J's expense among published boys' name registrations — annual shares of A/J first letters. Risk: denominator excludes suppressed names, not all births; cannot prove parents' motivations.
The preferred 3-chart sequence is historical setup, annual rivalry, alphabetical reversal if the data support it. Reject any filler chart after data audit.

Colours across charts: Adam/A: #1F8FA8; Alex/J: #C44E52; Adrian: #777777. The colour keys and different subjects must be stated clearly on each chart.
Production: GitHub render-archived-project workflow only, 1600px plus real 390px and 320px PNG review, no ChartGPT visual mock data, no publication without explicit approval.
