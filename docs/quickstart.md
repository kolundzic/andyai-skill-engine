# Quickstart v0.1

## Install

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

## First checks

```bash
make validate
make check-pack
make test
make cli-smoke
```

## First CLI run

```bash
python -m skill_engine.cli validate examples/skills
```
