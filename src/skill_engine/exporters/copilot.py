from ..models import Skill

def export_skill_to_copilot(skill: Skill) -> dict:
    return {
        "id": skill.id,
        "version": skill.version,
        "title": skill.title,
        "purpose": skill.purpose,
        "inputs": [{"name": i.name, "type": i.type, "required": i.required, "description": i.description} for i in skill.inputs],
        "outputs": [{"name": i.name, "type": i.type, "description": i.description} for i in skill.outputs],
        "constraints": skill.constraints,
        "compatibility": ["copilot"],
        "source_architecture": "andyai-skill-engine",
    }
