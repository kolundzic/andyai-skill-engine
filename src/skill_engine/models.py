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

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Skill":
        inputs = [SkillInput(name=i["name"], type=i["type"], required=i.get("required", True), description=i.get("description","")) for i in data.get("inputs", [])]
        outputs = [SkillOutput(name=i["name"], type=i["type"], description=i.get("description","")) for i in data.get("outputs", [])]
        trust_data = data.get("trust", {})
        trust = TrustMetadata(
            evidence_required=trust_data.get("evidence_required", False),
            safe_for_preview=trust_data.get("safe_for_preview", True),
            notes=trust_data.get("notes", []),
        )
        reserved = {"id","version","title","purpose","inputs","outputs","constraints","compatibility","trust"}
        metadata = {k: v for k, v in data.items() if k not in reserved}
        return cls(
            id=data["id"], version=data["version"], title=data["title"], purpose=data["purpose"],
            inputs=inputs, outputs=outputs,
            constraints=data.get("constraints", []),
            compatibility=data.get("compatibility", []),
            trust=trust, metadata=metadata
        )
