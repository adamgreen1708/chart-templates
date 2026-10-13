# Shorts in Sports × coffeetableviz — Verstappen (2015–2025)

This project supports the article **The grid is a guide, not a verdict** on coffeetableviz.com.

- Community dataset: [The Data Taylor — Shorts in Sports](https://github.com/TheDataTaylor/shorts-in-sports/blob/main/SIS-%20Max%20Verstappen.xlsx)
- Original workbook: maintained by The Data Taylor; not redistributed here.
- Article: `site/_posts/2026-10-13-max-verstappen-grid-comebacks.md`
- Chart assets: `site/assets/charts/shortsinsports-verstappen-*`
- Supporting files: `data/` and `QA_AND_METHOD.md`; the site also hosts a downloadable methodology zip.
- Chart render scripts: `scripts/revise_chart12.py` and `scripts/render_chart3.py`.

**Scope:** completed 2015–2025 Grand Prix seasons. The original workbook has 250 rows, of which 233 belong to the completed-season scope. There are 199 eligible classified, normal-grid race results for Chart 2; seven meet the Chart 3 threshold (net gains of 13+ places).

**Story:** Russia 2021 has the biggest net gain (P20 to P2; +18). São Paulo 2024 has the biggest gain **ending in victory** (P17 to P1; +16), with Belgium 2022 another victory (P14 to P1; +13).

**Interpretation:** net positions gained means final classification minus grid position, not recorded overtakes. Official FIA/F1 results corroborate the selected examples; the complete source spreadsheet remains community-curated.

**Visual style:** independent Matplotlib renders using the coffeetableviz palette and square canvas, not the locked GitHub 538 renderer. No renderer core files were changed.
