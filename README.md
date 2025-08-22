
<h1 align="center" style="font-size:42px; font-weight:bold;">
ImageLearner — CNN for Image Understanding
</h1>

<p align="center" style="font-size:18px;">
A beginner-friendly PyTorch project that trains a compact Convolutional Neural Network (CNN) on MNIST and easily extends to CIFAR-10.<br>
This README also doubles as a <b>Git & GitHub mini-handbook</b>, helping you learn modern collaboration while building a real ML project.
</p>

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white">
  <img alt="PyTorch" src="https://img.shields.io/badge/PyTorch-2.x-EE4C2C?logo=pytorch&logoColor=white">
  <a href="https://github.com/nuthalapatideepika/simple-CNN-project/actions">
    <img alt="CI" src="https://github.com/nuthalapatideepika/simple-CNN-project/actions/workflows/ci.yml/badge.svg">
  </a>
  <img alt="License" src="https://img.shields.io/badge/License-MIT-green">
</p>

<hr>

<h2 style="font-size:28px;">Table of Contents</h2>

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
[Beginner efficiency checklist](#beginner-efficiency-checklist)
[Quality gates (CI, lint, tests)](#quality-gates-ci-lint-tests)
[Docker usage](#docker-usage)
[Performance tips](#performance-tips)
[FAQ](#faq)
[Troubleshooting](#troubleshooting)
[Roadmap](#roadmap)
[Contributing](#contributing)
[License](#license)
[Appendix — Git commands](#appendix--git-commands)

<hr>

<h2 style="font-size:28px;">Why this project</h2>

Clear folder layout (great for learning & interviews)  
Built-in automation: formatting, linting, tests, CI  
Practical <b>Git/GitHub</b> guide included

<hr>

<h2 style="font-size:28px;">Key features</h2>

 <b>PyTorch</b> training loop with CLI flags (`--epochs`, `--lr`, `--batch_size`, `--seed`)  
 <b>SimpleCNN</b> baseline you can easily extend  
 <b>Ruff</b> (format + lint) and <b>PyTest</b> (smoke tests)  
 <b>GitHub Actions</b> CI on every push/PR  
 <b>Dockerfile</b> for reproducible runs anywhere  
 <b>Makefile</b> shortcuts for speed  

<hr>

<h2 style="font-size:28px;">Project structure</h2>

```text
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
````

<hr>

<h2 style="font-size:28px;">Quickstart</h2>

> Requires <b>Python 3.10+</b>. On Windows, use `.\.venv\Scripts\activate` instead of `source`.

```bash
# Clone and enter the project
git clone https://github.com/nuthalapatideepika/simple-CNN-project.git
cd simple-CNN-project

# Create virtual env & install dependencies
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# Smoke test + quick 1-epoch train
pytest -q
python src/train.py --epochs 1
```

<b>Makefile shortcuts</b>

```bash
make fmt     # auto-format with Ruff
make lint    # run linter
make test    # run tests
make train   # quick training run
```

<hr>

<h2 style="font-size:28px;">Training & evaluation</h2>

```bash
python src/train.py --epochs 5 --lr 0.001 --batch_size 128 --seed 42
```

**Example output**

```text
[Epoch 1] train_loss=... train_acc=... val_loss=... val_acc=...
...
Best accuracy: 0.99xx
Saved: outputs/best.pt
```

<hr>

<h2 style="font-size:28px;">Reproducibility</h2>

* Seeds for `random`, `numpy`, and `torch` are fixed
* CuDNN deterministic settings reduce randomness
* Ensures consistent results across machines

<hr>

<h2 style="font-size:28px;">Extend to CIFAR-10</h2>

1. In `src/data.py`, replace `datasets.MNIST` with `datasets.CIFAR10`
2. Update transforms:

   ```python
   transforms.Normalize((0.4914, 0.4822, 0.4465),
                        (0.2470, 0.2435, 0.2616))
   ```
3. In `models/simple_cnn.py`, change input channels **1 → 3**
4. Add augmentations (e.g., `RandomCrop`, `RandomHorizontalFlip`)

<hr>

<h2 style="font-size:28px;">Git & GitHub — Crash Course</h2>

<h3>Core concepts</h3>

* <b>Repository</b> → project + history
* <b>Commit</b> → snapshot with message
* <b>Branch</b> → safe space for new work
* <b>Remote</b> → GitHub copy of repo
* <b>Push / Pull</b> → upload / download changes
* <b>Pull Request (PR)</b> → propose merging a branch into `main`

<h3>Daily workflow</h3>

```bash
git checkout -b feature/cifar10-dataloaders
make fmt && make lint && make test
git add -A
git commit -m "feat(data): add CIFAR-10 loaders and transforms"
git push -u origin feature/cifar10-dataloaders
# Open PR → CI runs → review → squash & merge
```

<h3>Commit messages</h3>

Use <b>Conventional Commits</b>:

* `feat(model): add dropout for regularization`
* `fix(train): correct accuracy calculation`
* `docs(readme): add CIFAR-10 guide`

<h3>Pull Requests (PRs)</h3>

* Keep PRs small & focused
* CI must pass
* Provide description + linked issue (e.g., `Closes #12`)
* <b>Squash & merge</b> after review

<h3>Issues, labels, milestones</h3>

* <b>Issues</b> → track bugs/features
* <b>Labels</b> → categorize (e.g., `bug`, `enhancement`)
* <b>Milestones</b> → group tasks for releases

<h3>Releases & tags</h3>

* <b>Tag</b> → mark a commit (e.g., `v0.1.0`)
* <b>Release</b> → bundle a tag with notes/assets

<h3>Branch protection & CODEOWNERS</h3>

* Protect `main`: require PR, review, and CI checks
* Use <b>CODEOWNERS</b> to auto-request reviewers for paths

<h3>Beginner efficiency checklist</h3>

* Enable Issues (and Discussions if needed)
* Enable <b>Squash merge</b>; disable merge commits
* Auto-delete merged branches
* Enable Dependabot + security scanning (CodeQL, secrets)
* Restrict direct pushes to `main`

<hr>

<h2 style="font-size:28px;">Quality gates (CI, lint, tests)</h2>

* <b>Ruff</b> → formatting + lint
* <b>PyTest</b> → correctness checks
* <b>GitHub Actions</b> → runs on every push/PR

<hr>

<h2 style="font-size:28px;">Docker usage</h2>

```bash
docker build -t imagelearner .
docker run --rm imagelearner python src/train.py --epochs 1
```

<hr>

<h2 style="font-size:28px;">Performance tips</h2>

* Use the largest `batch_size` your GPU allows
* Try `AdamW` + `OneCycleLR`
* Add augmentation for CIFAR-10
* Use mixed precision (`torch.cuda.amp`)
* Profile with `torch.profiler`

<hr>

<h2 style="font-size:28px;">FAQ</h2>

<b>I’m new to Git. How do I start?</b>
Install Git → clone repo → create branch → commit → push → open PR.

<b>Why can’t I push directly to `main`?</b>
Branch protection keeps `main` stable. Use PRs.

<b>CI fails on “lint”. What now?</b>
Run `make fmt` locally → commit → push again.

<b>Where is the model saved?</b>
`outputs/best.pt` after validation accuracy improves.

<hr>

<h2 style="font-size:28px;">Troubleshooting</h2>

* <b>CUDA not found</b> → install CUDA-enabled PyTorch; check `torch.cuda.is_available()`
* <b>Permission denied</b> → on Unix, `chmod +x`; ensure virtualenv is active
* <b>Dataset blocked</b> → edit dataset path in `data.py` or pre-download

<hr>

<h2 style="font-size:28px;">Roadmap</h2>

* [ ] Add CIFAR-10 example with augmentations
* [ ] Mixed precision training (`--amp`)
* [ ] Training curves in README
* [ ] CODEOWNERS + PR/Issue templates
* [ ] Pre-commit hook for Ruff

<hr>

<h2 style="font-size:28px;">Contributing</h2>

1. Open an Issue to discuss
2. Create a branch: `git checkout -b feat/your-feature`
3. Run `make fmt && make lint && make test`
4. Push branch → open PR → request review
5. Squash & merge after approval

<hr>

<h2 style="font-size:28px;">License</h2>

<b>MIT</b> — free to use/modify with attribution. No warranty.

<hr>

<h2 style="font-size:28px;">Appendix — Git commands</h2>

```bash
# Clone repo
git clone https://github.com/nuthalapatideepika/simple-CNN-project.git
cd simple-CNN-project

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
