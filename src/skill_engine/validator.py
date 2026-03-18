from dataclasses import dataclass, field

REQUIRED_TOP_LEVEL_FIELDS = ["id", "version", "title", "purpose", "inputs", "outputs"]

@dataclass
class SkillValidationResult:
    valid: bool
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

def _check_name_type_items(items, list_name, errors):
    seen_names = set()
    for idx, item in enumerate(items):
        if not isinstance(item, dict):
            errors.append(f"{list_name}[{idx}] must be an object.")
            continue
        name = item.get("name")
        type_ = item.get("type")
        if name is None:
            errors.append(f"{list_name}[{idx}] missing 'name'.")
        elif not isinstance(name, str) or not name.strip():
            errors.append(f"{list_name}[{idx}] field 'name' must be a non-empty string.")
        elif name in seen_names:
            errors.append(f"{list_name}[{idx}] duplicate name: {name}")
        else:
            seen_names.add(name)
        if type_ is None:
            errors.append(f"{list_name}[{idx}] missing 'type'.")
        elif not isinstance(type_, str) or not type_.strip():
            errors.append(f"{list_name}[{idx}] field 'type' must be a non-empty string.")

def validate_skill_dict(data):
    errors, warnings = [], []
    if not isinstance(data, dict):
        return SkillValidationResult(valid=False, errors=["Skill payload must be a dictionary."])
    for field_name in REQUIRED_TOP_LEVEL_FIELDS:
        if field_name not in data:
            errors.append(f"Missing required field: {field_name}")
    if errors:
        return SkillValidationResult(valid=False, errors=errors, warnings=warnings)
    for field_name in ("id", "version", "title", "purpose"):
        value = data.get(field_name)
        if not isinstance(value, str) or not value.strip():
            errors.append(f"Field '{field_name}' must be a non-empty string.")
    if not isinstance(data["inputs"], list):
        errors.append("Field 'inputs' must be a list.")
    if not isinstance(data["outputs"], list):
        errors.append("Field 'outputs' must be a list.")
    if isinstance(data.get("inputs"), list):
        _check_name_type_items(data["inputs"], "inputs", errors)
    if isinstance(data.get("outputs"), list):
        _check_name_type_items(data["outputs"], "outputs", errors)
    compatibility = data.get("compatibility", [])
    if compatibility and not isinstance(compatibility, list):
        errors.append("Field 'compatibility' must be a list when present.")
    elif isinstance(compatibility, list):
        for idx, item in enumerate(compatibility):
            if not isinstance(item, str) or not item.strip():
                errors.append(f"compatibility[{idx}] must be a non-empty string.")
    constraints = data.get("constraints", [])
    if constraints and not isinstance(constraints, list):
        errors.append("Field 'constraints' must be a list when present.")
    trust = data.get("trust", {})
    if trust and not isinstance(trust, dict):
        errors.append("Field 'trust' must be an object when present.")
    if not errors:
        if not compatibility:
            warnings.append("No compatibility targets declared.")
        if not constraints:
            warnings.append("No constraints declared.")
        if data.get("trust", {}).get("evidence_required", False) is False:
            warnings.append("Evidence is not required for this skill.")
    return SkillValidationResult(valid=len(errors) == 0, errors=errors, warnings=warnings)
