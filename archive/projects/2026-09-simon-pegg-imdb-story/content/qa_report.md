# Simon Pegg chart QA

## Data

- Source dataset: 33 eligible IMDb principal-actor movie records.
- Vote floor: every analytical record has at least 1,000 votes.
- Identity: Simon Pegg `nm0670408`.
- Duplicate analytical `tconst` values: 0.
- Missing analytical years, runtimes or ratings: 0.
- Partnership groups are mutually exclusive: *Mission: Impossible* (6), *Star Trek* (3), Edgar Wright (3), other eligible movies (21).
- Reproduced group means: 7.35, 7.53, 7.50 and 6.09 respectively.
- Partnership-title vote share reproduced: 76.6%.

## Config and renderer

- All three configs compile as complete Python files.
- Dataset paths and column names match exactly.
- Sorting uses the required dictionary form.
- Output names are descriptive and project-scoped.
- Only the approved coffeetableviz palette is specified in project configs.
- The locked `src/render_538.py` completed all three renders without warnings.
- No renderer, template or workflow files were changed.

## Visual inspection

- All outputs are square 1600 × 1600 PNG files at 200 DPI.
- First pass identified over-wide chart 2 and chart 3 headlines plus insufficient axis/footer separation.
- Second pass shortened both headlines and raised the plot floor from 0.14/0.16 to 0.18.
- Titles, subtitles and plot areas no longer overlap.
- Axis labels and footers are separated.
- Highlight points remain inside the plotting area.
- Annotation offsets keep labels within safe margins.
- Group sample sizes are visible in chart 2.
- The three finite partnership sequences in chart 3 are presented as film order, not as continuous time trends.

## Interpretation guardrails

- IMDb ratings describe titles, not Simon Pegg's individual performance or critical acclaim.
- `title.principals` is a principal-credit subset, not a guaranteed complete filmography.
- The two three-film groups are small samples.
- The partnership grouping is descriptive and does not establish that Simon Pegg or any collaborator caused a title's rating.
