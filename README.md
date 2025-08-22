

# 📸 ImageLearner — CNN for Image Understanding

*A clean, beginner-friendly PyTorch project that trains a compact Convolutional Neural Network (CNN) on MNIST and easily extends to CIFAR-10.*  
This README also doubles as a **Git & GitHub mini-handbook**, helping you learn modern collaboration while building a real ML project.

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white">
  <img alt="PyTorch" src="https://img.shields.io/badge/PyTorch-2.x-EE4C2C?logo=pytorch&logoColor=white">
  <a href="https://github.com/YOUR_USERNAME/simple-CNN-project-/actions">
    <img alt="CI" src="https://github.com/YOUR_USERNAME/simple-CNN-project-/actions/workflows/ci.yml/badge.svg">
  </a>
  <img alt="License" src="https://img.shields.io/badge/License-MIT-green">
</p>

---

## Table of Contents

- [Why this project](#-why-this-project)
- [Key features](#-key-features)
- [Project structure](#-project-structure)
- [Quickstart](#-quickstart)
- [Training & evaluation](#-training--evaluation)
- [Reproducibility](#-reproducibility)
- [Extend to CIFAR-10](#-extend-to-cifar-10)
- [Git & GitHub — Crash Course](#-git--github--crash-course)
  - [Core concepts](#core-concepts)
  - [Daily workflow](#daily-workflow)
  - [Commit messages](#commit-messages)
  - [Pull Requests (PRs)](#pull-requests-prs)
  - [Issues, labels, milestones](#issues-labels-milestones)
  - [Releases & tags](#releases--tags)
  - [Branch protection & CODEOWNERS](#branch-protection--codeowners)
  - [Beginner efficiency checklist](#beginner-efficiency-checklist)
- [Quality gates (CI, lint, tests)](#-quality-gates-ci-lint-tests)
- [Docker usage](#-docker-usage)
- [Performance tips](#-performance-tips)
- [FAQ](#-faq)
- [Troubleshooting](#-troubleshooting)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)
- [License](#-license)
- [Appendix — Git commands](#-appendix--git-commands)

---

##  Why this project

**ImageLearner** is a **minimal but production-minded** ML starter:

  Clear folder layout (great for learning & interviews)  
  Built-in automation: formatting, linting, tests, CI  
  Practical **Git/GitHub guide** included  

---

##  Key features

- **PyTorch** training loop with CLI (`--epochs`, `--lr`, `--batch_size`, `--seed`)  
- **SimpleCNN** model you can easily extend  
- **Ruff** (format + lint) and **PyTest** (smoke tests)  
- **GitHub Actions** CI (runs on every push/PR)  
- **Dockerfile** for reproducible runs anywhere  
- **Makefile** shortcuts for speed  

---

##  Project structure

```

ImageLearner/
├─ README.md
├─ requirements.txt
├─ .gitignore
├─ Makefile
├─ Dockerfile
├─ pyproject.toml            # Ruff config
├─ .github/
│  └─ workflows/
│     └─ ci.yml              # CI: lint + tests
└─ src/
├─ train.py               # CLI + train/eval loop
├─ data.py                # dataloaders (MNIST)
└─ models/
└─ simple\_cnn.py       # baseline CNN
└─ tests/
└─ test\_smoke.py          # shape/forward test

````

---

##  Quickstart

Requires **Python 3.10+**. On Windows, use `.venv\Scripts\activate` instead of `source`.

```bash
# Clone and enter the project
git clone https://github.com/YOUR_USERNAME/simple-CNN-project-.git
cd simple-CNN-project-

# Create virtual env & install deps
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# Run tests + quick train
pytest -q
python src/train.py --epochs 1
````

### Handy commands (via Makefile)

```bash
make fmt     # auto-format with Ruff
make lint    # run linter
make test    # run tests
make train   # quick training run
```

---

##  Training & evaluation

```bash
python src/train.py --epochs 5 --lr 0.001 --batch_size 128 --seed 42
```

Example output:

```
[Epoch 1] train_loss=... train_acc=... val_loss=... val_acc=...
...
Best accuracy: 0.99xx
Saved: outputs/best.pt
```

---

##  Reproducibility

* Seeds for `random`, `numpy`, and `torch` are fixed
* CuDNN deterministic settings reduce randomness
* Ensures consistent results across machines

---

##  Extend to CIFAR-10

1. In `src/data.py`, replace `datasets.MNIST` with `datasets.CIFAR10`
2. Update transforms:

```python
transforms.Normalize((0.4914, 0.4822, 0.4465),
                     (0.2470, 0.2435, 0.2616))
```

3. In `models/simple_cnn.py`, change input channels **1 → 3**
4. Add augmentations (random crop, horizontal flip, etc.)

---

##  Git & GitHub — Crash Course

### Core concepts

* **Repository** → Project database with history
* **Commit** → Snapshot with message
* **Branch** → Safe place for new work
* **Remote** → GitHub copy of repo
* **Push / Pull** → Upload / download changes
* **Pull Request (PR)** → Proposal to merge work into `main`

---

### Daily workflow

```bash
git checkout -b feature/cifar10-dataloaders
make fmt && make lint && make test
git add -A
git commit -m "feat(data): add CIFAR-10 loaders and transforms"
git push -u origin feature/cifar10-dataloaders
```

➡ Open PR → CI runs → Review → Merge

---

### Commit messages

Follow **Conventional Commits**:

* `feat(model): add dropout for regularization`
* `fix(train): correct accuracy calculation`
* `docs(readme): add CIFAR-10 guide`

---

### Pull Requests (PRs)

* Keep PRs **small & focused**
* CI must pass
* Provide description + link issue (e.g., *Closes #12*)
* **Squash & merge** after review

---

### Issues, labels, milestones

* **Issues** → track bugs/features
* **Labels** → categorize (`bug`, `enhancement`)
* **Milestones** → group tasks for releases

---

### Releases & tags

* **Tag** → Mark commit (`v0.1.0`)
* **Release** → Bundle tag + notes/assets

---

### Branch protection & CODEOWNERS

* Protect `main`: require PR, review, CI
* Use **CODEOWNERS** to auto-request reviewers

---

### Beginner efficiency checklist

✅ Enable Issues & Discussions
✅ Enable squash merge, disable merge commits
✅ Auto-delete merged branches
✅ Enable Dependabot + security scanning
✅ Restrict direct pushes to `main`

---

## ✅ Quality gates (CI, lint, tests)

* **Ruff** → style & lint
* **PyTest** → correctness tests
* **GitHub Actions** → CI on push/PR

---

##  Docker usage

Run anywhere, no “works on my machine”:

```bash
docker build -t imagelearner .
docker run --rm imagelearner python src/train.py --epochs 1
```

---

##  Performance tips

* Use largest `batch_size` your GPU can handle
* Try **AdamW + OneCycleLR**
* Add augmentation (CIFAR-10)
* Use **mixed precision** (`torch.cuda.amp`)
* Profile with `torch.profiler`

---

##  FAQ

**Q: I’m new to Git. How do I start?**
A: Install Git → clone repo → create branch → commit → push → open PR.

**Q: Why can’t I push directly to `main`?**
A: Branch protection keeps `main` stable. Use PRs.

**Q: CI fails on “lint”. What now?**
A: Run `make fmt` locally → commit → push.

**Q: Where is the model saved?**
A: In `outputs/best.pt` after accuracy improves.

---

##  Troubleshooting

* **CUDA not found** → Install CUDA-enabled PyTorch, check `torch.cuda.is_available()`
* **Permission denied** → On Unix: `chmod +x`; ensure venv active
* **Dataset blocked** → Edit path in `data.py` or pre-download

---

##  Roadmap

* [ ] Add CIFAR-10 example with augmentations
* [ ] Mixed precision training (`--amp`)
* [ ] Training curves in README
* [ ] Add CODEOWNERS + PR/Issue templates
* [ ] Pre-commit hook for Ruff

---

##  Contributing

1. Open Issue to discuss
2. Create branch: `git checkout -b feat/your-feature`
3. Run `make fmt && make lint && make test`
4. Push branch → Open PR → Request review
5. Squash & merge after approval

---

##  License

**MIT** — Free to use/modify with attribution. No warranty.

---

##  Appendix — Git commands

```bash
# Clone repo
git clone https://github.com/YOUR_USERNAME/simple-CNN-project-.git
cd simple-CNN-project-

# New feature branch
git checkout -b feat/cifar10

# Stage + commit
git add -A
git commit -m "feat(data): add CIFAR-10 loaders and transforms"

# Push branch
git push -u origin feat/cifar10
# Open PR on GitHub

# Sync later
git checkout main && git pull
git checkout feat/cifar10
git rebase main   # or: git merge main
```

```

---

