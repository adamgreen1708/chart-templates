# 538 Workflow

## Source of truth

The file `spec/538_template_rules.md` is the master definition of the 538 chart template.

## Current implementation

The reusable Python chart styling and rendering system lives in:

- `src/chart_538.py`
- `src/render_538.py`
- `src/chart_config_template.py`
- `docs/chart_config_prompt.txt`

The editorial planning step before config generation is defined in:

- `docs/story_discovery_and_3_chart_flow.md`

## Implementation rules

- Follow `spec/538_template_rules.md` exactly.
- Do not introduce white plot backgrounds.
- Preserve the square 8.0 x 8.0 production canvas unless explicitly changed.
- Preserve padding rules and safe margins.
- Keep title/subtitle inside safe bounds.
- Use explicit axis labels when they reduce ambiguity.
- Add axis breathing room where labels, markers, or annotations risk clipping.
- Only add vertical gridlines when explicitly requested or clearly useful.
- For blog/data-story work, do not jump straight from dataset inspection to chart config.
- First find the story and present a recommended 3-chart editorial plan unless the request is explicitly config-only.

## Project lesson rule

When a live project exposes a reusable renderer/config/editorial lesson, update the template system rather than leaving the fix trapped in one chart config.

Examples:

- axis labels needed for interpretability;
- wider plot margins needed to prevent clipping;
- annotation offset patterns that avoid edge collisions;
- output naming rules;
- recurring chart type patterns;
- recurring story-discovery or 3-chart planning patterns.

## Change control

Any reusable change should update all relevant files in one PR:

1. `spec/538_template_rules.md`
2. `src/chart_config_template.py`
3. `docs/chart_config_prompt.txt`
4. `docs/story_discovery_and_3_chart_flow.md` if the editorial planning behaviour changes
5. `AGENTS.md` if agent behaviour changes
6. tests where applicable

If implementation conflicts with the spec, resolve the conflict immediately. The repo should not knowingly hold stale template rules.
