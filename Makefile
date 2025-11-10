.PHONY: test lint fmt bootstrap security-scan

bootstrap:
python -m venv .venv
. .venv/bin/activate && pip install -e .[cli] pytest ruff

test:
pytest

lint:
ruff check src tests

fmt:
ruff check --select I --fix src tests
ruff format src tests

security-scan:
pip install pip-audit
pip-audit
