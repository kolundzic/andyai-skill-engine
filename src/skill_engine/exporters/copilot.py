from __future__ import annotations

from typing import Any

from ..models import Skill


def export_skill_to_copilot(skill: Skill) -> dict[str, Any]:
    """
    Minimal compatibility export for Copilot-oriented packaging.

    AndyAI Skill Engine remains the master architecture,
    while Copilot is treated as an export target.
    """
    return {
        "id": skill.id,
        "version": skill.version,
        "title": skill.title,
        "purpose": skill.purpose,
        "inputs": [
            {
                "name": item.name,
                "type": item.type,
                "required": item.required,
                "description": item.description,
            }
            for item in skill.inputs
        ],
        "outputs": [
            {
                "name": item.name,
                "type": item.type,
                "description": item.description,
            }
            for item in skill.outputs
        ],
        "constraints": skill.constraints,
        "compatibility": ["copilot"],
        "source_architecture": "andyai-skill-engine",
    }
