import json
from pathlib import Path
from skill_engine.models import Skill
from skill_engine.validator import validate_skill_dict

def test_minimal_skill_is_valid() -> None:
    data = json.loads(Path('examples/skills/minimal_skill.json').read_text(encoding='utf-8'))
    result = validate_skill_dict(data)
    assert result.valid is True
    assert result.errors == []
    assert 'Evidence is not required for this skill.' in result.warnings

def test_skill_can_be_loaded_into_model() -> None:
    data = json.loads(Path('examples/skills/minimal_skill.json').read_text(encoding='utf-8'))
    skill = Skill.from_dict(data)
    assert skill.id == 'andyai.minimal.status'
    assert skill.version == '1.0.0'
    assert len(skill.inputs) == 2
    assert len(skill.outputs) == 2
