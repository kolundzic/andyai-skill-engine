# AndyAI Skill Engine

[![CI](https://img.shields.io/badge/CI-validate-ready-brightgreen)](#)
[![Version](https://img.shields.io/badge/version-v1.4-blue)](#)
[![License](https://img.shields.io/badge/license-Apache--2.0-lightgrey)](#)
[![Public Core](https://img.shields.io/badge/model-public--core-orange)](#)

**AndyAI Skill Engine** is a public Apache-2.0 core for reusable, verifiable AI skill orchestration.

Copilot compatibility is an export path.  
**AndyAI Skill Engine remains the master architecture.**

## Why it matters

This repo focuses on **execution structure**:
- reusable skill definitions
- validator-first discipline
- compatibility exports
- trust-aware packaging
- public baseline for future enterprise layers

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

## Main commands

```bash
python -m skill_engine.cli validate examples/skills
python -m skill_engine.cli check-pack .
python -m skill_engine.cli export-copilot examples/skills/minimal_skill.json
```

## Public core policy

Commercial differentiation should be built above this public core through:
- enterprise governance packs
- hosted trust tooling
- advanced exporters
- premium adapters
- support / SLA layers
