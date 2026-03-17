PYTHON ?= python3

validate:
	$(PYTHON) scripts/validate-skills.py

check-pack:
	bash scripts/check-pack.sh .

test:
	PYTHONPATH=src pytest -q

cli-smoke:
	PYTHONPATH=src $(PYTHON) -m skill_engine.cli --help
	PYTHONPATH=src $(PYTHON) -m skill_engine.cli check-pack .
