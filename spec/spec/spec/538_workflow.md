# 538 Workflow

## Source of truth
The file `spec/538_template_rules.md` is the master definition of the 538 chart template.

## Intended implementation
A reusable Python chart styling system should eventually live in:

- `src/chart_538.py`
- `src/render_538.py`

## Rules for implementation
- Follow `spec/538_template_rules.md` exactly
- Do not introduce white plot backgrounds
- Preserve locked canvas ratio
- Preserve padding rules
- Keep title/subtitle inside safe bounds
- Only add vertical gridlines when explicitly requested

## Change control
Any change to the 538 template must be made in `spec/538_template_rules.md` first before implementation is updated.