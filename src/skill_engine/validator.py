from dataclasses import dataclass, field
from typing import Any
from .models import Skill

REQUIRED_TOP_LEVEL_FIELDS = ["id", "version", "title", "purpose", "inputs", "outputs"]

@dataclass
class SkillValidationResult:
    valid: bool
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

def validate_skill_dict(data: dict[str, Any]) -> SkillValidationResult:
    errors, warnings = [], []
    if not isinstance(data, dict):
        return SkillValidationResult(valid=False, errors=["Skill payload must be a dictionary."])
    for field_name in REQUIRED_TOP_LEVEL_FIELDS:
        if field_name not in data:
            errors.append(f"Missing required field: {field_name}")
    if errors:
        return SkillValidationResult(valid=False, errors=errors, warnings=warnings)
    if not isinstance(data["inputs"], list):
        errors.append("Field 'inputs' must be a list.")
    if not isinstance(data["outputs"], list):
        errors.append("Field 'outputs' must be a list.")
    for list_name in ("inputs", "outputs"):
        items = data.get(list_name, [])
        if isinstance(items, list):
            for idx, item in enumerate(items):
                if not isinstance(item, dict):
                    errors.append(f"{list_name}[{idx}] must be an object.")
                    continue
                if "name" not in item:
                    errors.append(f"{list_name}[{idx}] missing 'name'.")
                if "type" not in item:
                    errors.append(f"{list_name}[{idx}] missing 'type'.")
    if not errors:
        skill = Skill.from_dict(data)
        if not skill.compatibility:
            warnings.append("No compatibility targets declared.")
        if not skill.constraints:
            warnings.append("No constraints declared.")
        if skill.trust.evidence_required is False:
            warnings.append("Evidence is not required for this skill.")
    return SkillValidationResult(valid=len(errors) == 0, errors=errors, warnings=warnings)
