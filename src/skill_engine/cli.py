import argparse, json
from pathlib import Path
from .validator import validate_skill_dict

def main():
    p=argparse.ArgumentParser(prog='skill-engine'); s=p.add_subparsers(dest='cmd', required=True)
    a=s.add_parser('validate'); a.add_argument('path')
    b=s.add_parser('check-pack'); b.add_argument('root', nargs='?', default='.')
    c=s.add_parser('export-copilot'); c.add_argument('skill_file')
    args=p.parse_args()
    if args.cmd=='validate':
        path=Path(args.path); files=[path] if path.is_file() else sorted(path.glob('*.json'))
        bad=False
        for f in files:
            r=validate_skill_dict(json.loads(f.read_text(encoding='utf-8')))
            print('[OK]' if r.valid else '[FAIL]', f)
            bad = bad or (not r.valid)
        raise SystemExit(1 if bad else 0)
    if args.cmd=='check-pack':
        root=Path(args.root)
        req=['README.md','RELEASE_NOTES_v0.7.md','docs/testing.md','docs/project-structure.md','.gitignore','LICENSE','CONTRIBUTING.md','CHANGELOG.md']
        miss=[x for x in req if not (root/x).exists()]
        [print(f'Missing required file: {m}') for m in miss]
        print('Pack check passed.' if not miss else '')
        raise SystemExit(1 if miss else 0)
    if args.cmd=='export-copilot':
        print(json.dumps({'status':'stub','source':'andyai-skill-engine'}, indent=2))
        raise SystemExit(0)

if __name__=='__main__':
    main()
