"""Guard the automatic chart renderer against unrelated non-chart archives.

On workflow_dispatch an invalid project remains a hard failure.
On automatic pushes, unrelated data-only and art-only archives are skipped.
"""
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
WORKFLOW=ROOT/".github/workflows/render-archived-project.yml"


def test_push_skips_archives_without_chart_config():
    content=WORKFLOW.read_text(encoding="utf-8")
    assert 'if [[ ! -d "$project_dir/config" ]]; then' in content
    assert 'if [[ "$GITHUB_EVENT_NAME" == "workflow_dispatch" ]]; then' in content
    assert 'echo "Config directory not found: $project_dir/config"' in content
    assert 'echo "Skipping non-chart project without config: $project_dir"' in content
    assert 'continue' in content.split("Skipping non-chart project without config",1)[1].split("fi",1)[0]


def test_real_config_projects_still_require_renderer_checks():
    code=WORKFLOW.read_text(encoding="utf-8")
    assert 'all_configs=("$project_dir"/config/*.py)' in code
    assert 'python src/render_538.py' in code
    assert 'Configured output must be inside output/' in code
    assert 'git checkout -- src/chart_config.py' in code
