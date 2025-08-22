# ImageLearner — CNN for Image Understanding

*A clean, beginner-friendly PyTorch project that trains a compact Convolutional Neural Network (CNN) on MNIST and easily extends to CIFAR-10.*  
This README also serves as a **Git & GitHub mini-handbook**, helping you learn modern collaboration while building a real ML project.

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.10+-3776AB">
  <img alt="PyTorch" src="https://img.shields.io/badge/PyTorch-2.x-EE4C2C">
  <a href="https://github.com/YOUR_USERNAME/simple-CNN-project-/actions">
    <img alt="CI" src="https://github.com/YOUR_USERNAME/simple-CNN-project-/actions/workflows/ci.yml/badge.svg">
  </a>
  <img alt="License" src="https://img.shields.io/badge/License-MIT-green">
</p>

---

## Table of Contents
[Why this project](#why-this-project)
  [Key features](#key-features)
  [Project structure](#project-structure)
  [Quickstart](#quickstart)
  [Training & evaluation](#training--evaluation)
  [Reproducibility](#reproducibility)
  [Extend to CIFAR-10](#extend-to-cifar-10)
  [Git & GitHub — Crash Course](#git--github--crash-course)
  [Core concepts](#core-concepts)
    [Daily workflow](#daily-workflow)
    [Commit messages](#commit-messages)
    [Pull Requests (PRs)](#pull-requests-prs)
   [Issues, labels, milestones](#issues-labels-milestones)
   [Releases & tags](#releases--tags)
   [Branch protection & CODEOWNERS](#branch-protection--codeowners)
   [Make your repo efficient (beginner checklist)](#make-your-repo-efficient-beginner-checklist)
 [Quality gates (CI, lint, tests)](#quality-gates-ci-lint-tests)
 [Docker usage](#docker-usage)
 [Performance tips](#performance-tips)
  [FAQ](#faq)
 [Troubleshooting](#troubleshooting)
 [Roadmap](#roadmap)
 [Contributing](#contributing)
 [License](#license)
 [Appendix — Git commands](#appendix--git-commands)

---

## Why this project
ImageLearner is a **minimal but production-minded** ML starter:
 📂 Clear folder layout (great for learning & interviews)  
 ⚙️ Built-in automation: formatting, linting, tests, CI  
 📖 Practical **Git/GitHub guide** included  

---

## Key features
 **PyTorch** training loop with sensible CLI (`--epochs`, `--lr`, `--batch_size`, `--seed`)
 **SimpleCNN** model you can easily extend
 **Ruff** (format + lint) and **PyTest** (smoke tests)
 **GitHub Actions** CI (runs on every push/PR)
 **Dockerfile** for reproducible runs anywhere
 **Makefile** shortcuts for speed

---

## Project structure
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
      └─ simple_cnn.py       # baseline CNN
└─ tests/
   └─ test_smoke.py          # shape/forward test
---
## Quickstart
Requires Python 3.10+. On Windows, use .venv\Scripts\activate instead of source.
# Clone and enter the project
git clone https://github.com/YOUR_USERNAME/simple-CNN-project-.git
cd simple-CNN-project-

# Create a virtual environment & install deps
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# Run tests and a quick 1-epoch train
pytest -q
python src/train.py --epochs 1
# Handy commands (Makefile):
make fmt     # auto-format code with Ruff
make lint    # run linter
make test    # run tests
make train   # quick training run
## Training & evaluation
python src/train.py --epochs 5 --lr 0.001 --batch_size 128 --seed 42
Example output:
[Epoch 1] train_loss=... train_acc=... val_loss=... val_acc=...
...
Best accuracy: 0.99xx
Saved: outputs/best.pt
---
## Reproducibility
Seeds for random, numpy, and torch are fixed
CuDNN deterministic settings reduce randomness
Ensures consistent results across machines
----
## Extend to CIFAR-10
In src/data.py, replace datasets.MNIST with datasets.CIFAR10
Update transforms:
transforms.Normalize((0.4914, 0.4822, 0.4465),
                     (0.2470, 0.2435, 0.2616))
In models/simple_cnn.py, change input channels from 1 → 3
Add augmentations: random crop, horizontal flip, etc.
----
## Git & GitHub — Crash Course
#Core concepts
Repository: Project database with history
Commit: Snapshot with a message
Branch: Safe place for new work
Remote: GitHub copy of repo
Push / Pull: Upload / download changes
Pull Request (PR): Proposal to merge branch into main
---
## Daily workflow
git checkout -b feature/cifar10-dataloaders   # new branch
make fmt && make lint && make test            # check locally
git add -A
git commit -m "feat(data): add CIFAR-10 loaders and transforms"
git push -u origin feature/cifar10-dataloaders
# Open PR on GitHub → run CI → get review → squash & merge
--
## Commit messages
Use Conventional Commits (feat, fix, docs, refactor, test, chore, perf, ci).
Examples:
feat(model): add dropout for regularization
fix(train): correct accuracy calculation
docs(readme): add CIFAR-10 extension guide
--
## Pull Requests (PRs)
Keep them small & focused
CI must pass
Good description + linked issue (e.g., Closes #12)
Squash & merge after review
---
## Issues, labels, milestones
Issues: Track tasks/bugs/ideas
Labels: Tag issues (bug, enhancement)
Milestones: Group issues for releases
---
## Releases & tags
Tag: Mark a commit (e.g., v0.1.0)
Release: Package a tag with notes/assets
---
## Branch protection & CODEOWNERS
Protect main: require PRs, 1 approval, CI checks, conversation resolution
Use CODEOWNERS to auto-request reviewers
----
## Make your repo efficient (beginner checklist)
Enable Issues (and Discussions if needed)
Enable Squash merge, disable merge commits
Enable Auto-delete merged branches
Enable Dependabot, Secret scanning, CodeQL
Restrict direct pushes to main
-----
## Quality gates (CI, lint, tests)
Ruff: consistent formatting + lint
PyTest: basic correctness tests
GitHub Actions: runs on every push/PR
___
## Docker usage
Run anywhere, no "works on my machine":
docker build -t imagelearner .
docker run --rm imagelearner python src/train.py --epochs 1

____
## Performance tips
Use largest batch_size your GPU can handle
Try AdamW + OneCycleLR
Add augmentation for CIFAR-10
Use mixed precision (torch.cuda.amp)
Profile with torch.profiler
----
## FAQ
Q: I’m new to Git. How do I start?
A: Install Git → clone repo → create branch → commit → push → open PR.
Q: Why can’t I push directly to main?
A: Branch protection keeps main stable. Always use PRs.
Q: CI fails on “lint”. What now?
A: Run make fmt locally → commit → push again.
Q: Where is the model saved?
A: In outputs/best.pt after accuracy improves.
___
## Troubleshooting
CUDA not found: Install CUDA-enabled PyTorch, check torch.cuda.is_available()
Permission denied: On Unix, run chmod +x; use virtualenv
Dataset blocked: Edit dataset path in data.py or pre-download
_______
## Roadmap
 Add CIFAR-10 example with augmentations
 Mixed precision training (--amp)
 Training curves in README
 Add CODEOWNERS + PR/Issue templates
 Pre-commit hook for Ruff
_______
## Contributing
Open an Issue to discuss
Create a branch: git checkout -b feat/your-feature
Run make fmt && make lint && make test
Push branch → open PR → request review
Squash & merge after approval
________
## License
MIT — Free to use/modify with attribution. No warranty.
_____
## Appendix — Git commands
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


