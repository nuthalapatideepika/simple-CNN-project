# AI Projects Template

A high-quality, production-ready PyTorch template for building, training, and deploying compact Convolutional Neural Networks (CNNs) on image datasets.  
Designed for rapid prototyping, reproducibility, and seamless integration with modern ML tooling.

This repository contains two AI projects:
1. **ImageLearner** - CNN for Image Understanding (MNIST/CIFAR-10)
2. **fuzzy binarization** - FuzzyCNN for binary image classification

---

## Quick Start

### Run All Projects
```bash
# Clone the repository
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>

# Install dependencies
pip install torch torchvision tqdm pytest ruff numpy pandas matplotlib

# Run all projects at once
./run_projects.sh
```

### Run Individual Projects

#### ImageLearner
```bash
cd ImageLearner
make train
# or
python src/train.py --epochs 5 --lr 0.001 --batch_size 128 --seed 42
```

#### Fuzzy Binarization
```bash
cd "fuzzy binarization"
make train
# or
python src/train.py --epochs 1
```

---

## Project Structure

```
├── src/
│   ├── models/
│   │   └── simple_cnn.py
│   ├── data.py
│   └── train.py
├── tests/
│   └── test_smoke.py
├── requirements.txt
├── Makefile
├── Dockerfile
├── pyproject.toml
├── .gitignore
├── LICENSE
├── README.md
└── .github/
    └── workflows/
        └── ci.yml
```

---

## Best Practices

- **Reproducibility:** Set random seeds for all libraries.
- **Code Quality:** Use Ruff for linting and formatting.
- **Testing:** Validate model forward passes and data loaders.
- **Documentation:** Keep README and docstrings up to date.
- **Version Control:** Commit often and use descriptive messages.

---

## License

This project is licensed under the MIT License.

---

## Contributing

Pull requests and issues are welcome!  
Please follow the code style and add tests for new features.

---

## Acknowledgements

Built with [PyTorch](https://pytorch.org/), [TorchVision](https://pytorch.org/vision/), and inspired by best practices in open-
