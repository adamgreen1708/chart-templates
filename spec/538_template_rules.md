# 538 Chart Template (LOCKED)

This is the source of truth for the coffeetableviz 538-style renderer.

The current production standard is the square coffeetableviz renderer used by `src/render_538.py` and the CHART_CONFIG template.

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

"title_x": 0.10
"title_y": 0.92
"subtitle_x": 0.10
"subtitle_y": 0.86

"footer_left_x": 0.10
"footer_right_x": 0.90
"footer_y": 0.08

"plot_top": 0.75
"plot_bottom": 0.14
"plot_left": 0.12
"plot_right": 0.90
```

## Typography defaults

```python
"title_fontsize": 22
"subtitle_fontsize": 12
"tick_label_fontsize": 10
"axis_label_fontsize": 10
"footer_fontsize": 10

"title_wrap_width": 40
"subtitle_wrap_width": 74
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
