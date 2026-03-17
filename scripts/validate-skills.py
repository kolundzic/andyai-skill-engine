#!/usr/bin/env python3
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'src'))
from skill_engine.validator import validate_skill_dict
for f in sorted(Path('examples/skills').glob('*.json')):
    r=validate_skill_dict(json.loads(f.read_text(encoding='utf-8')))
    print('[OK]' if r.valid else '[FAIL]', f)
raise SystemExit(0)
