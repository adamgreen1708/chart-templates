# Coffeetableviz 538 Chart Template — approved vNext house standard

This is the source of truth for the coffeetableviz 538-style renderer.

The production standard for **new projects** is the approved mobile-readable `social_square` house profile, configured and rendered through `src/render_538.py` and `src/chart_config_template.py`. Existing archived configs without `render_profile` are treated as legacy `standard` until their chart is deliberately migrated and reviewed. This is one future-facing house style, not two competing designs.

## Canvas

- Width: 8.0
- Height: 8.0
- Aspect ratio: 1:1 square
- Export: PNG
- DPI: 200

## Background

- Full canvas background: light grey `#F3F4F6`
- Plot area: same light grey
- Do not introduce a white plot area

## Active palette

- Primary / focus blue: `#1F8FA8`
- Accent / highlight red: `#C44E52`
- Context grey: `#D9D9D9`
- Secondary grey: `#7A7A7A`
- Text: `#111111`
- Subtitle/footer text: `#555555`

## Layout defaults

Use these defaults unless a specific chart needs more room.

```python
"fig_width": 8.0
"fig_height": 8.0

"render_profile": "social_square"

"title_x": 0.09
"title_y": 0.91
"subtitle_x": 0.09
"subtitle_y": 0.84

"footer_left_x": 0.09
"footer_right_x": 0.91
"footer_y": 0.09

"plot_top": 0.72
"plot_bottom": 0.22
"plot_left": 0.17
"plot_right": 0.87
```

## Typography defaults

```python
"title_fontsize": 26
"subtitle_fontsize": 16
"tick_label_fontsize": 12
"axis_label_fontsize": 12
"footer_fontsize": 10.5

"title_wrap_width": 32
"subtitle_wrap_width": 54
"title_max_lines": 2
"subtitle_max_lines": 2
```

## Titles and subtitles

- Left aligned.
- Must stay within chart bounds.
- Must not overlap each other.
- Must not overlap the plot area.
- Titles should be message-led, not generic.
- Subtitles should explain the takeaway in plain language.

## Axes and labels

The renderer supports explicit axis labels:

```python
"x_label": ""
"y_label": ""
```

Rules:

- Use axis labels when the measure is not obvious from the title/subtitle.
- Use short sentence-case labels.
- Keep labels clear and non-technical.
- For World Cup / Arsenal-style time or ranking charts, prefer explicit axis labels when they reduce ambiguity.
- Use `axis_label_fontsize` to control both x and y axis label size.
- Add breathing room through `x_axis.min`, `x_axis.max`, `y_axis_min`, `y_axis_max`, and `x_margin` when labels or markers risk clipping.

## Supported axis configuration

```python
"x_axis": {
    "min": None,
    "max": None,
    "tick_interval": None,
    "format": None
}

"y_axis_min": None
"y_axis_max": None
"y_tick_interval": None
"y_tick_format": None
"x_margin": 0.08
```

Supported formats include:

- `None`
- `"percent"`
- `"currency"`
- `"millions"`
- `"billions"`
- Python numeric formats such as `".0f"` and `".1f"`
- datetime formatter strings such as `"%Y"` when `x_is_datetime` is true

For scatter/matrix charts that use numeric positions for categorical axes, optional explicit tick labels are supported:

```python
"x_tick_labels": [
    {"value": 1, "label": "First"}
],
"y_tick_labels": [
    {"value": 1, "label": "Category A"}
]
```

Use these only when a numeric plotting position needs a human-readable categorical label. Keep the list compact enough to remain readable on the square canvas.

## Gridlines

- Horizontal gridlines: on by default.
- Vertical gridlines: off by default.
- Only enable vertical gridlines when they genuinely improve readability.

```python
"vertical_gridlines": False
```

## Chart types

Supported chart types:

- `line` — time trend or ordered sequence
- `bar` — category comparison
- `dot` — ranked comparison
- `scatter` — relationship between two numeric variables

Horizontal bars are supported with:

```python
"chart_type": "bar"
"orientation": "horizontal"
```

## Editorial schematic chart types

The renderer also supports three mobile-first editorial schematic types when a conventional statistical chart would obscure the story:

- `route_zigzag` — ordered stops evenly spaced around a reference line; use when sequence is more important than geographic distance.
- `route_longitude` — broken longitude panels with approximate place coordinates and an explicit latitude reference; use only with documented coordinates and a visible approximation/exaggeration caveat.
- `mode_clusters` — grouped categorical items with deterministic vector pictograms and prominent group counts.

These types use the same square canvas, background and house palette as the core renderer. They must remain deterministic: no generated text, generated icons, or image-model output may be used in the final chart PNG.

For `route_longitude`, any vertical exaggeration must be stated on-chart. For `route_zigzag`, even spacing must be stated on-chart so readers do not infer distance.

## Highlighting and annotation

Use highlights sparingly.

Supported row-matching format:

```python
"highlight_points": [
    {"Country": "United Kingdom"},
    {"Year": 2025}
]
```

Supported explicit-coordinate format:

```python
"highlight_points": [
    {"x": 1998, "y": 6}
]
```

Annotations may also match rows or use explicit x/y coordinates.

Rules:

- Keep annotations short.
- Keep annotations inside the chart area where possible.
- For right-edge labels, use negative x offsets.
- Avoid labels overlapping title, subtitle, footer, or chart edges.
- Prefer no arrow unless the point genuinely needs a pointer.

For text annotations in front of dotted reference guides, an optional Matplotlib
`bbox` dictionary can be supplied in each `annotate_points` item. Use a
background matching the canvas (normally `#F3F4F6`), no edge, and modest
padding. This masks guides behind the text without hiding the rest of the
reference line. Leave `bbox` absent for ordinary annotations.

Example: `"bbox": {"facecolor": "#F3F4F6", "edgecolor": "none", "pad": 1.2}`.

## Reference lines

Supported reference line axes:

- `"x"`
- `"y"`
- `"diagonal"`

Use diagonal reference lines for scatter charts such as actual vs benchmark or 2024 vs 2025 comparisons.

## Filters and derived views

The renderer supports simple filters in CHART_CONFIG:

```python
"filters": [
    {"column": "Country", "operator": "==", "value": "United Kingdom"}
]
```

Supported operators:

- `<=`
- `<`
- `>=`
- `>`
- `==`
- `!=`

## Output rules

- Always export PNG.
- Prefer descriptive output filenames.
- Use `output/chart.png` for the active default render.
- Use `output/descriptive_chart_name.png` when producing multiple outputs.

## Change control

When a project forces a reusable improvement, update the template system in the same conversation:

1. Update this spec.
2. Update `src/chart_config_template.py` if the config surface changes.
3. Update `docs/chart_config_prompt.txt` if prompting rules change.
4. Update tests if renderer or template assumptions change.
5. Mention the template update in the final handback.

## Semantic colour and editorial labelling QA

When a story uses multiple chart panels, colours must carry a **defined editorial meaning** consistently across the set; arbitrary alternation of category colours is not permitted. Focus/accent/context assignments should be documented per story. The locked palette specifies available colours, not a requirement to use them all.

When labels sit away from the plotted marks, use restrained leader lines if that is necessary to remove ambiguity. Test leaders for crossings and collisions on the final PNG. Add concise contextual identifiers (such as a sport in brackets after an athlete's name) when readers may not recognise the names. Source, unit and provisional status must remain explicit.

Final QA must inspect the exported image pixels at full size and mobile-readable size, including all labels, lines, legend, footers and safe margins. See `docs/chart_qa_checklist.md` for the full reusable checklist.


## Approved house-vNext profile and legacy compatibility

**Approved for new charts on 30 October 2026.** New project configs must specify `"render_profile": "social_square"`. This is the **normal** Coffeetableviz layout for publication and phone use, not a second rendering workflow. Both statistical and specialist chart geometry call the shared style and render through GitHub.

- Square 8 × 8 inches, 200 DPI, light-grey canvas and plot `#F3F4F6`.
- Title 26 pt, subtitle 16 pt, axes/ticks 12 pt, key annotations at least 11.5 pt, footer 10.5 pt.
- Title/subtitle and footer share consistent ~9% inset alignment. Minimum clear border 7% all edges; target ~8.5% safe frame.
- Use a consistent `Adam Green | coffeetableviz` left footer and source/caveat on the right, with sensible space between captions and credits.
- Review actual 390px and 320px rendered PNGs. Fail a chart for clipped labels, overlapping subtitle/explainer, white axes patches or unequal padding.
- Source-defined or historical colours retain meaningful semantics. Palette consistency does not erase historical encodings.
- `profile_overrides` may be used only when justified and reviewed. Do not silently shrink key text.

**Compatibility:** the `standard` profile is retained only for archived charts not yet migrated, to avoid unintentionally changing published image files. `social_*.py` files in October project folders are *test fixtures*, intentionally excluded from the normal publication loop. Production `config/*.py` charts with the approved profile are **not excluded** and use the regular GitHub renderer and publishing path.

**Migration:** update archived project configurations/renderer types one chart at a time, show phone previews for approval, then publish the replacements through the normal GitHub PR flow. See `spec/house-vnext-migration.md`.

