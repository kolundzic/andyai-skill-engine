import json
import subprocess
import sys

def test_cli_help_runs() -> None:
    result = subprocess.run(
        [sys.executable, '-m', 'skill_engine.cli', '--help'],
        capture_output=True,
        text=True,
        env={'PYTHONPATH': 'src'}
    )
    assert result.returncode == 0
    assert 'skill-engine' in result.stdout

def test_cli_export_copilot_runs() -> None:
    result = subprocess.run(
        [sys.executable, '-m', 'skill_engine.cli', 'export-copilot', 'examples/skills/minimal_skill.json'],
        capture_output=True,
        text=True,
        env={'PYTHONPATH': 'src'}
    )
    assert result.returncode == 0
    payload = json.loads(result.stdout)
    assert payload['source_architecture'] == 'andyai-skill-engine'
