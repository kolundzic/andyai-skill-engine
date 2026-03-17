#!/usr/bin/env python3
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
from skill_engine.validator import validate_skill_dict

def main() -> int:
    skills_dir = Path("examples/skills")
    failed = False
    for skill_file in sorted(skills_dir.glob("*.json")):
        payload = json.loads(skill_file.read_text(encoding="utf-8"))
        result = validate_skill_dict(payload)
        if result.valid:
            print(f"[OK] {skill_file}")
            for warning in result.warnings:
                print(f"  warning: {warning}")
        else:
            failed = True
            print(f"[FAIL] {skill_file}")
            for error in result.errors:
                print(f"  error: {error}")
    return 1 if failed else 0

if __name__ == "__main__":
    raise SystemExit(main())
