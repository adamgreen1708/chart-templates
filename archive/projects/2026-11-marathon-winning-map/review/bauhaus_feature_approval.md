# Bauhaus feature — publication handoff

**Status: user-uploaded original PNG integrated and verified, publication PR awaiting explicit approval.**

- Image submitted: `IMG_8958.png`, 960×960 RGBA PNG, 111508 bytes, SHA-256 `6c3224a95d787e955c814154eac90837c4b388deb4b77d81146cdcfffd51812d`.
- User supplied a dark charcoal poster with cream lines and restrained gold accent, titled `Major Marathons | Wins by Nationality (Women)`. It is an *explicit owner-approved exception* to the default light-grey feature-art house palette. Preserve the uploaded pixels rather than generating a different illustration.
- Data source: `data/marathon-majors/marathon_major_wins_by_nationality_women.csv` at commit `7fd9a2e6fea602dab07f802bac95254c69357e9c`. Counts sum to **149**, including Kenya **68**, Ethiopia **43**, Japan **9**, United Kingdom **7**, Russia **6**, Germany **5**, United States **4**, Latvia **2**, Netherlands **2**, China **1**, Israel **1**, Romania **1**. Combined Kenya/Ethiopia **111/149 (74.5%)**.
- Image depicts the six *historic* big-city marathons across **2000–26**; the article's statistical comparisons intentionally cover two complete decades **2000–09** and **2010–19** only. This is noted in the revised article.
- Verified exact asset path: `site/assets/features/marathon-nationalities-bauhaus-2026.png`.
- Implemented frontmatter changes: set `hero_image`, `card_image` and `social_image` all to that PNG path. Suggested alt: `Dark Bauhaus-style graphic of women's total wins by nationality across six major city marathons, 2000–26. Kenya leads with 68, Ethiopia has 43, and the next country is Japan with nine.`
- **Important:** The user-supplied PNG is attached as an exact Git blob, verified against Git SHA-1 `1e460cb4f7e6c7d3dc43cadaff56180d404a78b4` and SHA-256 above. All three Jekyll hero/card/social paths now point at it. This preview remains unmerged until editor approval and successful PR build.

## Final gate

Exact original PNG is now in the Git tree. Confirm the SHA-1 and SVG/PNG metadata, check Jekyll article HTML and three new site chart assets, run production build, compare diff, obtain final editorial approval, then merge and verify Pages deployment.
