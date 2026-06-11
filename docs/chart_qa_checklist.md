# Chart QA checklist

Use this before saying a chart config or render is ready.

## Data checks

- Dataset path exists.
- File extension is included.
- Column names exactly match the dataset.
- No invented columns.
- No mock values.
- Units are clear.
- Percent values are handled consistently.
- Date columns are parsed correctly.
- Sorting matches the story.

## Story checks

- The chart has one clear message.
- Title is punchy and message-led.
- Subtitle explains the takeaway.
- Source text is present.
- Highlights support the story.
- Labels are used sparingly.
- The chart does not try to tell three stories at once.

## Config checks

- `CHART_CONFIG` is valid Python.
- No missing commas.
- No missing quotes.
- `data_format` is correct.
- `chart_type` matches the analytical task.
- `x_col`, `y_col`, `series_col`, and `value_col` are correct.
- `sort` is a dictionary or `None`, not a string.
- `sort_descending` is included.
- Output filename is descriptive.

## Layout checks

- Title does not overlap subtitle.
- Subtitle does not run off the right edge.
- Axis labels do not clip.
- Data labels stay inside safe margins.
- Footer is visible.
- Chart is not cramped.
- No unnecessary gridlines.
- Highlight points are visible.

## Renderer checks

- The active renderer can run the config.
- Output file appears in the expected location.
- If a workflow fails, inspect logs before asking Adam to troubleshoot.
- If output is missing, check filename, output path, and workflow artifact settings.

## Adam pain-point checks

Before handing back, ask:

- Would this force Adam to copy/paste too much on mobile?
- Can this be committed directly to GitHub instead?
- Is a full replacement file better than a snippet?
- Have we avoided the common label clipping and margin problems?
- Have we reduced the chance of another config/render iteration?
