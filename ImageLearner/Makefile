# Makefile

# Makefile for ImageLearner project

.PHONY: fmt lint test train performance

fmt:
	ruff format . && ruff check . --fix

lint:
	ruff check .

test:
	PYTHONPATH=/home/runner/work/AI-projects/AI-projects/ImageLearner pytest

train:
	PYTHONPATH=/home/runner/work/AI-projects/AI-projects/ImageLearner python src/train_synthetic.py --epochs 5 --lr 0.001 --batch_size 128 --seed 42

performance:
	PYTHONPATH=/home/runner/work/AI-projects/AI-projects/ImageLearner python src/performance.py