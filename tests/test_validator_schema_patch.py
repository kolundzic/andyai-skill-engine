import json
from pathlib import Path
from skill_engine.validator import validate_skill_dict

def load_example():
    return json.loads(Path("examples/skills/minimal_skill.json").read_text(encoding="utf-8"))

def test_minimal_skill_validates():
    result = validate_skill_dict(load_example())
    assert result.valid is True
    assert result.errors == []

def test_duplicate_input_names_fail():
    data = load_example()
    data["inputs"] = [{"name": "state", "type": "string"}, {"name": "state", "type": "object"}]
    result = validate_skill_dict(data)
    assert result.valid is False
    assert any("duplicate name" in e for e in result.errors)

def test_empty_compatibility_entry_fails():
    data = load_example()
    data["compatibility"] = ["copilot-export", ""]
    result = validate_skill_dict(data)
    assert result.valid is False
    assert any("compatibility[1]" in e for e in result.errors)

def test_empty_output_name_fails():
    data = load_example()
    data["outputs"][0]["name"] = ""
    result = validate_skill_dict(data)
    assert result.valid is False
    assert any("outputs[0]" in e for e in result.errors)
