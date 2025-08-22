# Makefile

# Makefile for ImageLearner project

.PHONY: fmt lint test train

fmt:
    ruff . --fix

lint:
    ruff .

test:
    pytest

train:
    python src/train.py --epochs 5 --lr 0.001 --batch_size 128 --seed 42