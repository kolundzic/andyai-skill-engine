from dataclasses import dataclass, field
from typing import Any

@dataclass
class SkillInput:
    name: str
    type: str
    required: bool = True
    description: str = ""

@dataclass
class SkillOutput:
    name: str
    type: str
    description: str = ""

@dataclass
class TrustMetadata:
    evidence_required: bool = False
    safe_for_preview: bool = True
    notes: list[str] = field(default_factory=list)

@dataclass
class Skill:
    id: str
    version: str
    title: str
    purpose: str
    inputs: list[SkillInput]
    outputs: list[SkillOutput]
    constraints: list[str] = field(default_factory=list)
    compatibility: list[str] = field(default_factory=list)
    trust: TrustMetadata = field(default_factory=TrustMetadata)
    metadata: dict[str, Any] = field(default_factory=dict)
