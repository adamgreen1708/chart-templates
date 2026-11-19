# Chart QA checklist

Use this before saying a chart config or render is ready.

## Hard editorial rejection gate — before any technical QA

- Does this chart reveal a non-obvious fact, contradiction or human connection, or just summarise rows?
- Did we inspect **competing** source-supported story routes and reject the weak ones? Would this chart still deserve to exist if there were no obligation to supply three?
- Does its title state a claim the chosen snapshot, grain and method support? Have we independently calculated and checked every displayed number?
- Are comparable groups calculated with the same statistic? Say **mean** for arithmetic average, not median; state denominator, subset, source dates and exclusions.
- Can every highlighted label answer **why this one?** Show the consistent quantitative rule (max/min/group leader) or make the case for a clearly marked editorial exception.
- Is the reader seeing *actual relationships* rather than a count inflated by repeated edges or joins?
- Would a different chart form make the distinction more obvious? Is Chart 3 a genuine reveal rather than repetition?
- Does every colour mean one thing, and does neutral metadata avoid borrowing another category's semantic colour? Are size, axes, tick scale and any truncation explained in plain English?
- Would we still find this interesting and defensible if a sceptical reader asked for the actual source rows? If not, **do not render**; return to discovery.
- **GitHub-only image source:** even exploratory charts are repo-rendered from documented real data; never generate statistical diagrams in ChatGPT or adjust chart pixels for a PDF.
- A green CI check does not equal a good story. Visually inspect source, full-size, 390px and 320px pixels; verify internal explanatory captions and footer spacing, not just outer margins.

See `docs/editorial_judgement_standard.md` and `docs/lessons/2026-11-19-pattinson-editorial-retrospective.md`.

## Post-render editorial peer review — actual published Pattinson case

- **Match headline to observable variable.** A chart of film-level ratings over release year does **not directly measure** a creative reinvention, career strategy or reputation. Distinguish an interpretative story title from a data-tested claim.
- **Show distributions when they matter.** A mean across 28 other films can conceal the overlap/range that would make a contrast meaningful. Consider a group strip/distribution before settling on one comparator triangle.
- **Interrogate sample-defined prominence.** A 24.8% share of *summed title-votes within an editorially selected 33-film sample* is not share of viewers, ticket sales or platform audience. Put limitations where readers might otherwise overgeneralise.
- **Maxima can be dull.** The highest-rated title and most-voted title may be objectively chosen yet still fail an intrigue test; the chart must justify their storytelling role, not merely selection integrity.
- **Clarify directional links.** Film → shared actor → Bond-role arrows are relation indicators, not a chronological or causal path. Verify role chronology and avoid implying co-stars caused casting.
- **Edit the hook as carefully as the figures.** If the strongest human connection appears in Chart 3, consider a teaser near the opening while preserving the full payoff.
- **Run an independent second pass after GitHub rendering** rather than relying on source-data/script validation alone. Only then invite Adam's review.
- Preserve already approved article/chart files unchanged; make process improvements on their own review PR.

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


## Standard mobile and social QA (active vNext for new charts)

- Render in GitHub from verified data + CHART_CONFIG; never retype/redraw charts in PDF tools.
- For new production charts use the shared vNext house profile; do not overwrite previously published legacy assets without approval. Use separate comparison outputs during migration.
- Inspect the actual final export at 390px and 320px (alongside full resolution), not just bounding boxes.
- Read every subtitle, legend, important annotation, axis/tick, source/date and caveat at phone size.
- Check clipping, plot overlap, collisions, safe margins, marker contrast and semantic colours.
- Prefer less copy, fewer annotations and better layouts rather than smaller essential text.
- Use shared canonical footer; do not allow individual projects to drift without documented approval.
- No overwriting previously approved chart PNGs without Adam explicitly signing off on the replacement render.


### Four-edge padding and plot-background checks (mandatory for social-square)

- Target a consistent ~8.5% reference safe frame on **top, left, right and bottom**; title and footer anchors should be visually aligned.
- The automated render QA must fail when significant foreground pixels enter the outer 7% of **any** side; do not let charts bleed to edges.
- Do not allow a separate white axes card: all plot and figure background pixels should use the matching light grey `#F3F4F6` unless an explicitly documented meaningful encoding requires otherwise.
- Stack title, subheader and explainer using measured glyph boxes; no excessive vertical gaps and no overlap with data marks.
- Reinspect the exported source PNG and phone previews after every typography, margin or plot-geometry change.

- Enforce a visible gap between x-axis title and footer credits in the shared renderer; outer margins passing does **not** prove interior elements are separated. Inspect this at 320px as well.
