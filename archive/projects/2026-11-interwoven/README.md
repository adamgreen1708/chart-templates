# Interwoven — Form and Flow V3

Exhibit 001. Approved static artwork and 23-second continuous gallery video; approved interactive mobile selection behaviour. Draft PR #241, do not merge until exact binary assets are present and browser/build QA passes.

## Provenance
Source CSV: data/matches_2526.csv, copied by Git blob identity from archive/projects/2026-11-epl-2526-unfolded/data/matches_2526.csv. Blob ef64fe7c32a9cc6a146f1f156abbf7902bbdda3a. 380 unique fixtures, 20 clubs, 760 spheres, 104 draws, 276 winner halos, 1,045 goals. Each club 19 home/19 away. Six maximal winning streaks >=5: Villa 8, City 6, Liverpool 5, Arsenal three times 5. Fixture order by date, source row order for same date. Final rank order points/GD/GF.

## Render spec
6000 x 2000 px, chronological fixture index x, final rank y. Home centre y-12; away y+12. Sphere radius 4.8 sqrt(1+1.25 goals). Winner ring radius 16; brighter clean-sheet rim. Fixture links RGB 48+8 min(total goals,7), width 2 or 3 for >=5, dashed for draws. Horizontal team threads RGB 35 width 1. Streak ribbon spans first to last win, glow scales with run count. Month labels and home/away wins, points visible. Approved static art remains separate from browser gradients. Gallery scene is simulated and uses original artwork, with seamless 23-second 30 fps continuous camera motion.

## Release files
Exact assets belong in site/assets/gallery/interwoven/. See ASSETS.sha256. Renderer and its inputs are archived here. Run python render_interwoven.py in this directory with Pillow, NumPy, Lato Regular/Medium and DejaVu Sans Mono installed. The CSV copy in data/ is the same Git blob; the renderer uses that path. The locally verified original PNG is the release source, not a browser redraw. Gallery video is the approved export (H.264 1600x900). No substitute video is acceptable.

## Recovery delivery
The original approval manifest remains unchanged. A recovery render uses the same original data and camera spline, a compressed copy of the approved gallery backdrop, and checks the static artwork against approved RGB pixel hashes. Recovered video and gallery JPEGs are not byte-identical to the original exports. The separate recovery manifest is validated before publication. The original high-resolution files remain the preferred archival versions. The one-time repair workflow committed outputs to its dedicated branch and was removed after successful recovery.
