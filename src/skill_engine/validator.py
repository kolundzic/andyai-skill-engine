from dataclasses import dataclass, field

@dataclass
class SkillValidationResult:
    valid: bool
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

def validate_skill_dict(data):
    errors=[]; warnings=[]
    for k in ['id','version','title','purpose','inputs','outputs']:
        if k not in data: errors.append(f'Missing required field: {k}')
    if not errors and data.get('trust',{}).get('evidence_required', False) is False:
        warnings.append('Evidence is not required for this skill.')
    return SkillValidationResult(valid=len(errors)==0, errors=errors, warnings=warnings)
