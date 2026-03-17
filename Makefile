PYTHON ?= python3

validate:
	$(PYTHON) scripts/validate-skills.py

check-pack:
	bash scripts/check-pack.sh .

test:
	PYTHONPATH=src pytest -q

cli-help:
	PYTHONPATH=src $(PYTHON) -m skill_engine.cli --help
