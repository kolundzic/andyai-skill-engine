# AndyAI Skill Engine

AndyAI Skill Engine is a skill-based orchestration architecture for reusable, verifiable AI execution.

## Current line

- v0.3 base packaging
- v0.4 operational skeleton
- v0.5 trust + packaging discipline
- v0.6 CLI + dev entry
- v0.7 repo hardening + quality
- v0.8 CI + test hardening

## Quick start

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
make validate
make check-pack
make test
make cli-smoke
```

Copilot compatibility is an export path. AndyAI Skill Engine remains the master architecture.
