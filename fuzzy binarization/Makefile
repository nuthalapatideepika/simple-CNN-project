# Makefile
PY := python

.PHONY: fmt lint test train

fmt:
    ruff format .

lint:
    ruff check .

test:
    pytest -q

train:
    $(PY) src/train.py --epochs 1