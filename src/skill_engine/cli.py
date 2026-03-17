import argparse, json
from pathlib import Path
from .exporters.copilot import export_skill_to_copilot
from .models import Skill
from .validator import validate_skill_dict

def cmd_validate(path_str: str) -> int:
    path = Path(path_str)
    files = [path] if path.is_file() else sorted(path.glob('*.json'))
    failed = False
    for skill_file in files:
        payload = json.loads(skill_file.read_text(encoding='utf-8'))
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

def cmd_check_pack(root_str: str) -> int:
    root = Path(root_str)
    required = ['README.md','RELEASE_NOTES_v0.8.md','docs/testing.md','docs/project-structure.md','.gitignore','LICENSE','CONTRIBUTING.md','CHANGELOG.md']
    missing = [item for item in required if not (root / item).exists()]
    if missing:
        for item in missing:
            print(f"Missing required file: {item}")
        return 1
    print("Pack check passed.")
    return 0

def cmd_export_copilot(skill_file_str: str) -> int:
    skill_file = Path(skill_file_str)
    payload = json.loads(skill_file.read_text(encoding='utf-8'))
    result = validate_skill_dict(payload)
    if not result.valid:
        for error in result.errors:
            print(f"error: {error}")
        return 1
    print(json.dumps(export_skill_to_copilot(Skill.from_dict(payload)), indent=2))
    return 0

def main() -> int:
    parser = argparse.ArgumentParser(prog='skill-engine')
    sub = parser.add_subparsers(dest='command', required=True)
    p_validate = sub.add_parser('validate'); p_validate.add_argument('path')
    p_check = sub.add_parser('check-pack'); p_check.add_argument('root', nargs='?', default='.')
    p_export = sub.add_parser('export-copilot'); p_export.add_argument('skill_file')
    args = parser.parse_args()
    if args.command == 'validate': return cmd_validate(args.path)
    if args.command == 'check-pack': return cmd_check_pack(args.root)
    if args.command == 'export-copilot': return cmd_export_copilot(args.skill_file)
    return 1

if __name__ == '__main__':
    raise SystemExit(main())
