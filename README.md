# AndyAI Skill Engine

[![CI](https://img.shields.io/badge/CI-validate-ready-brightgreen)](#)
[![Version](https://img.shields.io/badge/version-v0.9-blue)](#)
[![License](https://img.shields.io/badge/license-MIT-lightgrey)](#)

**AndyAI Skill Engine** is a skill-based orchestration architecture for reusable, verifiable AI execution.

Copilot compatibility is an export path.  
**AndyAI Skill Engine remains the master architecture.**

## What this repo now includes

- skill schema + examples
- validation core
- Copilot export adapter
- trust + packaging discipline
- CLI entrypoint
- dev setup and CI validation
- repo hardening basics
- public-facing quickstart and FAQ

## Version line

- `v0.3` — base packaging
- `v0.4` — operational skeleton
- `v0.5` — trust + packaging discipline
- `v0.6` — CLI + dev entry
- `v0.7` — repo hardening + quality
- `v0.8` — CI + test hardening
- `v0.9` — release polish + public-facing pack

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

## Main CLI commands

```bash
python -m skill_engine.cli validate examples/skills
python -m skill_engine.cli check-pack .
python -m skill_engine.cli export-copilot examples/skills/minimal_skill.json
```

## Public positioning

AndyAI Skill Engine is the reusable execution-structure layer between:
- raw model capability
- vendor-specific tool surfaces
- future operational agent systems

It is designed to stabilize skills above one-off prompts and below final business UX.
