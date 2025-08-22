# ImageLearner — CNN for Image Understanding

A beginner-friendly PyTorch project that trains a compact Convolutional Neural Network (CNN) on MNIST and easily extends to CIFAR-10. This README also doubles as a **Git & GitHub mini-handbook**, helping you learn modern collaboration while building a real ML project.

## Key features

- **PyTorch** training loop with CLI flags (`--epochs`, `--lr`, `--batch_size`, `--seed`)
- **SimpleCNN** baseline you can easily extend
- **Ruff** (format + lint) and **PyTest** (smoke tests)
- **GitHub Actions** CI on every push/PR
- **Dockerfile** for reproducible runs anywhere
- **Makefile** shortcuts for speed

## Project structure

```
ImageLearner/
├─ README.md
├─ LICENSE
├─ requirements.txt
├─ .gitignore
├─ Makefile
├─ Dockerfile
├─ pyproject.toml
├─ src/
│  ├─ train.py
│  ├─ data.py
│  └─ models/
│     └─ simple_cnn.py
└─ tests/
   └─ test_smoke.py
```

## Quickstart

> Requires **Python 3.10+**. On Windows, use `.\.venv\Scripts\activate` instead of `source`.

```bash
# Clone and enter the project
git clone https://github.com/yourusername/ImageLearner.git
cd ImageLearner

# Create virtual env & install dependencies
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# Smoke test + quick 1-epoch train
pytest -q
python src/train.py --epochs 1
```

## Training & evaluation

```bash
python src/train.py --epochs 5 --lr 0.001 --batch_size 128 --seed 42
```

**Example output**

```
[Epoch 1] train_loss=... train_acc=... val_loss=... val_acc=...
...
Best accuracy: 0.99xx
Saved: outputs/best.pt
```

## Reproducibility

- Seeds for `random`, `numpy`, and `torch` are fixed
- CuDNN deterministic settings reduce randomness
- Ensures consistent results across machines

## Git & GitHub — Crash Course

### Core concepts

- **Repository** → project + history
- **Commit** → snapshot with message
- **Branch** → safe space for new work
- **Remote** → GitHub copy of repo
- **Push / Pull** → upload / download changes
- **Pull Request (PR)** → propose merging a branch into `main`

### Daily workflow

```bash
git checkout -b feature/cifar10-dataloaders
make fmt && make lint && make test
git add -A
git commit -m "feat(data): add CIFAR-10 loaders and transforms"
git push -u origin feature/cifar10-dataloaders
# Open PR → CI runs → review → squash & merge
```

### Commit messages

Use **Conventional Commits**:

- `feat(model): add dropout for regularization`
- `fix(train): correct accuracy calculation`
- `docs(readme): add CIFAR-10 guide`

### Pull Requests (PRs)

- Keep PRs small & focused
- CI must pass
- Provide description + linked issue (e.g., `Closes #12`)
- **Squash & merge** after review

### Issues, labels, milestones

- **Issues** → track bugs/features
- **Labels** → categorize (e.g., `bug`, `enhancement`)
- **Milestones** → group tasks for releases

### Releases & tags

- **Tag** → mark a commit (e.g., `v0.1.0`)
- **Release** → bundle a tag with notes/assets

### Branch protection & CODEOWNERS

- Protect `main`: require PR, review, and CI checks
- Use **CODEOWNERS** to auto-request reviewers for paths

### Beginner efficiency checklist

- Enable Issues (and Discussions if needed)
- Enable **Squash merge**; disable merge commits
- Auto-delete merged branches
- Enable Dependabot + security scanning (CodeQL, secrets)
- Restrict direct pushes to `main`

## License

This project is licensed under the MIT License. See the LICENSE file for details.