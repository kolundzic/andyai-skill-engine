import json
from pathlib import Path

from skill_engine.models import Skill
from skill_engine.validator import validate_skill_dict


def test_minimal_skill_is_valid() -> None:
    example_path = Path("examples/skills/minimal_skill.json")
    data = json.loads(example_path.read_text(encoding="utf-8"))

    result = validate_skill_dict(data)

    assert result.valid is True
    assert result.errors == []


def test_skill_can_be_loaded_into_model() -> None:
    example_path = Path("examples/skills/minimal_skill.json")
    data = json.loads(example_path.read_text(encoding="utf-8"))

    skill = Skill.from_dict(data)

    assert skill.id == "andyai.minimal.status"
    assert skill.version == "0.4.0"
    assert len(skill.inputs) == 2
    assert len(skill.outputs) == 2


def test_missing_required_field_fails() -> None:
    bad_payload = {
        "id": "broken.skill",
        "version": "0.1.0",
        "title": "Broken Skill",
        "inputs": [],
        "outputs": [],
    }

    result = validate_skill_dict(bad_payload)

    assert result.valid is False
    assert any("purpose" in error for error in result.errors)
