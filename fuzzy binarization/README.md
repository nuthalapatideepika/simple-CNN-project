# README.md
# FuzzyBinarization — CNN for Fuzzy Image Binarization

A PyTorch project for fuzzy binarization using a compact CNN.

## Quickstart

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -q
python src/train.py --epochs 1
```

## Features

- FuzzyCNN model
- Data loaders for binarization tasks (MNIST as example)
- Training CLI
- Docker & CI support

## License

MIT