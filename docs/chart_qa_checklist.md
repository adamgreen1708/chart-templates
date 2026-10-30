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

## Editorial clarity and cross-chart consistency (25 October 2026)

These are reusable QA checks, not a mandatory colour scheme for every story.

- **Every colour needs a job.** State what each accent encodes; never group unrelated categories solely to add visual variety. Neutral context can stay grey but all text must remain legible.
- **Keep semantics consistent.** In a multi-chart story the same colour must mean the same category or editorial role across charts. Use a legend when the colour distinction is not self-evident.
- **Make label-to-mark relationships unambiguous.** Use thin leader lines when labels could be matched to the wrong dot, verifying that lines do not cross text or unrelated marks. Leaders should be subordinate to the data, not decorative arrows.
- **Provide identification without assumed expertise.** Names that are not universally recognisable need context, such as an athlete's sport in brackets. Specify the measured unit, category and the achievement used to select each subject.
- **Document the comparison contract.** Check metric, population, definition, temporal basis and title format before comparing. Distinguish season-wide results from one-off events, and conditional future achievements from confirmed records.
- **Inspect final pixels at full resolution *and* phone-reading size.** Check title/subtitle, every long name and qualifier, leader line, marker, colour key, tick, group header and source/footer for clipping, collisions and safe-margin clearance. A valid config alone does not pass the visual QA gate.
- **Check headline against evidence.** A curated set of examples cannot support claims about the absolute youngest across all sports, nor averages about which sport produces younger champions without an exhaustive comparable population.

Project-specific example: youngest season champions uses red for Formula 1, blue for other motorsport, grey for all other sports. The reusable rule is semantic colour, not those exact assignments.


## Social and mobile QA (proposed vNext)

- Render in GitHub from verified data + CHART_CONFIG; never retype/redraw charts in PDF tools.
- Keep original chart assets unchanged; write proposed social output to distinct files and attach artifacts.
- Inspect the actual final export at 390px and 320px (alongside full resolution), not just bounding boxes.
- Read every subtitle, legend, important annotation, axis/tick, source/date and caveat at phone size.
- Check clipping, plot overlap, collisions, safe margins, marker contrast and semantic colours.
- Prefer less copy, fewer annotations and better layouts rather than smaller essential text.
- Use shared canonical footer; do not allow individual projects to drift without documented approval.
- No publish, replacing originals or merging profile changes before Adam explicitly signs off.
