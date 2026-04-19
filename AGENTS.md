# AGENTS.md

This repository contains locked chart template systems.

## 538 template rules
- The source of truth is `spec/538_template_rules.md`
- Workflow guidance is in `spec/538_workflow.md`
- Implementation must follow the spec exactly
- Do not introduce a white plot area
- Preserve the locked canvas ratio
- Preserve padding and title/subtitle spacing rules
- Only add vertical gridlines when explicitly requested

## Development rules
- Prefer simple, reusable matplotlib code
- Keep implementation modular
- Do not change spec files unless explicitly instructed
- If implementation conflicts with spec, the spec wins