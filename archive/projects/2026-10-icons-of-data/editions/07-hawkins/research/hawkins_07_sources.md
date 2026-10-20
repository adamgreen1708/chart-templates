# Edition 07 — primary source audit (20 October 2026)

## Verified against institutional primary sources

| Claim / gate | Primary evidence | Status |
|---|---|---|
| Ed Hawkins / University of Reading developed climate stripes in 2018 | https://www.reading.ac.uk/planet/climate-resources/climate-stripes | Verified institutional statement |
| One vertical stripe per annual temperature, shades blue/red; CURRENT Reading baseline 1961–2010 | https://www.reading.ac.uk/planet/climate-resources/climate-stripes | Verified; **historic editions used a different period** |
| Hay-on-Wye 2017 data were designed for a 2018 literary-festival presentation | https://collections.reading.ac.uk/art-collections/explore/online-exhibitions/climate-stripes/ | Verified exhibition and accession details |
| Preserved Global 2020 artwork, temperatures 1850–2020, digitally published / collected in 2021 | https://collections.reading.ac.uk/art-collections/2021/12/20/show-your-stripes-the-artwork-that-made-climate-change-data-go-viral/ | Verified; UAC/11018 |
| Not the first *ever* to turn temperature into coloured patterns — Ed Hawkins acknowledges climate knitting precedents | https://collections.reading.ac.uk/art-collections/2021/12/20/show-your-stripes-the-artwork-that-made-climate-change-data-go-viral/ | Verified; no sole-inventor claim |
| Latest University stripes refreshed with Berkeley Earth data through 2025 | https://www.reading.ac.uk/news/2026/University-News/Cities-and-countries-warming-fast-new-climate-stripes-show | Verified; note exact download/data product required to replicate |
| Met Office HadCRUT5 is 5.2.0.0, released September 2026; anomalies native baseline 1961–1990 | https://www.metoffice.gov.uk/hadobs/hadcrut5/ and https://hadobs.metoffice.gov.uk/hadcrut5/data/HadCRUT.5.2.0.0/download.html | Verified. Original 19 Oct 2026 pinned upstream CSV now present in this GitHub draft; 176 complete annual observations 1850–2025; excludes 2026 partial. |
| Met Office terms OGL v3, attribution statement and Morice et al. required | https://www.metoffice.gov.uk/hadobs/hadcrut5/terms_and_conditions.html | Verified; credit in final caption/notes |
| Berkeley Earth source has CC BY-NC 4.0 restrictions, not interchangeable with OGL | https://berkeleyearth.org/data/ | Verified; avoid copying dataset unless permission/terms cleared |
| Historic original image reproduction use | https://collections.reading.ac.uk/art-collections/2021/12/20/show-your-stripes-the-artwork-that-made-climate-change-data-go-viral/ | University confirms Creative Commons reuse. Exact original UAC/11018 JPG is stored unmodified with SHA-256 in qa/visuals; preserve exact 1200×675 source and credit in article caption. |

## Verified design evolution — Hawkins' own explanation

- Ed Hawkins, **14 May 2024**: the 2023 stripes update changed the historical colour pivot period from **1971–2000** to **1961–2010**, expanded the palette limits, and added dark colours to cope with 2023's exceptional temperatures while staying visually similar to earlier versions. https://climatelabbook.substack.com/p/warming-stripes
- This means the archived *Global 2020* artwork predates the baseline update. **Never label that exact archival artefact as though it had been originally produced with the newer 1961–2010 setting.**
- The native **HadCRUT5 1961–1990** baseline is a *different* convention. Met Office explains anomalies and the benefits of averaging over a reference period: https://weather.metoffice.gov.uk/climate/science/global-temperature-records ; IPCC notes the WMO legacy 1961–1990 reference is retained for longer-term change assessment: https://www.ipcc.ch/report/ar6/wg1/chapter/atlas/
- 1961 is not a special year when warming began; it is a period boundary, and rebasing does not alter the sequence of underlying observed temperature changes.
- Final GitHub Actions correction to author review: https://github.com/adamgreen1708/chart-templates/actions/runs/39506769249 .

## Remaining editorial/publishing gates

- Author to review actual unframed historical source and two GitHub-rendered modern charts.
- Caption separately specifies creator, art edition, archive, period and rights; note modern data source and baseline separately.
- Do not merge/deliver site content before image approval, responsive site checks and separate publication approval.
