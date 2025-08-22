<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>ImageLearner — CNN for Image Understanding</title>

  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;800&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">

  <style>
    /* =========================
       Theme tokens
    ========================== */
    :root {
      --bg: #0b0d12;
      --panel: #0f1219;
      --text: #e9edf5;
      --muted: #a9b3c8;
      --brand: #7c5cff;
      --brand-2: #14b8a6;
      --line: #1d2533;
      --code-bg: #0f1320;
      --kbd-bg: #141a25;
      --link: #9ab0ff;
      --shadow: 0 10px 30px rgba(0,0,0,.35);
    }
    @media (prefers-color-scheme: light) {
      :root {
        --bg: #ffffff;
        --panel: #ffffff;
        --text: #0b0d12;
        --muted: #475168;
        --brand: #5b3df6;
        --brand-2: #0ea5a4;
        --line: #e6e8ee;
        --code-bg: #0f172a;
        --kbd-bg: #f3f4f6;
        --link: #3b69ff;
        --shadow: 0 8px 18px rgba(0,0,0,.08);
      }
    }

    /* =========================
       Base layout
    ========================== */
    * { box-sizing: border-box; }
    html { scroll-behavior: smooth; }
    body {
      margin: 0;
      background: radial-gradient(1200px 700px at 80% -10%, rgba(124,92,255,.09), transparent 55%),
                  radial-gradient(1200px 700px at 10% -20%, rgba(20,184,166,.08), transparent 55%),
                  var(--bg);
      color: var(--text);
      font-family: Inter, system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      line-height: 1.6;
    }
    a { color: var(--link); text-decoration: none; }
    a:hover { text-decoration: underline; }
    .container {
      max-width: 1060px;
      margin: 0 auto;
      padding: 28px 18px 60px;
    }

    /* =========================
       Header (hero)
    ========================== */
    .hero {
      text-align: center;
      padding: 56px 0 28px;
    }
    .title {
      margin: 0 0 10px;
      font-size: clamp(28px, 5vw, 48px);
      font-weight: 800;
      letter-spacing: -0.02em;
      line-height: 1.1;
    }
    .lead {
      color: var(--muted);
      max-width: 820px;
      margin: 0 auto 18px;
      font-size: 18px;
    }
    .badges {
      display: flex; gap: 8px; flex-wrap: wrap; justify-content: center;
      margin: 14px 0 0;
    }
    .badges img { height: 22px; }

    /* =========================
       Content layout
    ========================== */
    .content {
      display: grid;
      grid-template-columns: 260px 1fr;
      gap: 24px;
      margin-top: 22px;
    }
    @media (max-width: 980px) {
      .content { grid-template-columns: 1fr; }
    }

    /* =========================
       Sidebar (TOC)
    ========================== */
    .toc {
      position: sticky;
      top: 18px;
      border: 1px solid var(--line);
      background: linear-gradient(180deg, var(--panel), rgba(255,255,255,.02));
      border-radius: 14px;
      padding: 14px;
    }
    .toc h3 {
      margin: 4px 6px 10px;
      font-size: 14px;
      font-weight: 700;
      letter-spacing: .02em;
      color: var(--muted);
      text-transform: uppercase;
    }
    .toc a {
      display: block;
      padding: 8px 10px;
      border-radius: 10px;
      color: var(--text);
      border: 1px solid transparent;
    }
    .toc a:hover {
      border-color: var(--line);
      background: rgba(255,255,255,.02);
      text-decoration: none;
    }
    .toc .sub { padding-left: 14px; font-size: 14px; color: var(--muted); }

    /* =========================
       Article body
    ========================== */
    article {
      border: 1px solid var(--line);
      background: linear-gradient(180deg, var(--panel), rgba(255,255,255,.02));
      border-radius: 16px;
      padding: 24px;
      box-shadow: var(--shadow);
    }
    article h2 {
      margin-top: 26px;
      font-size: 26px;
      line-height: 1.25;
    }
    article h3 {
      margin-top: 22px;
      font-size: 20px;
    }
    article p, article ul, article ol { margin: 10px 0; }
    hr {
      border: 0; border-top: 1px solid var(--line);
      margin: 24px 0;
    }

    /* Code blocks */
    pre, code, kbd {
      font-family: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
    }
    pre {
      background: var(--code-bg);
      color: #e7eaf2;
      border: 1px solid var(--line);
      border-radius: 12px;
      padding: 14px 16px;
      overflow: auto;
    }
    code {
      background: rgba(124,92,255,.14);
      border: 1px solid rgba(124,92,255,.25);
      border-radius: 6px;
      padding: 2px 6px;
      font-size: 90%;
    }
    pre code {
      background: transparent;
      border: 0;
      padding: 0;
      font-size: 90%;
    }
    kbd {
      background: var(--kbd-bg);
      border: 1px solid var(--line);
      border-bottom-width: 2px;
      border-radius: 6px;
      padding: 2px 6px;
      font-size: 85%;
    }

    /* Callouts */
    .note {
      border-left: 4px solid var(--brand);
      background: rgba(124,92,255,.08);
      padding: 10px 12px;
      border-radius: 8px;
      margin: 12px 0;
      color: var(--muted);
    }

    /* Footer */
    .foot {
      text-align: center;
      color: var(--muted);
      margin: 34px 0 8px;
      font-size: 14px;
    }

    /* Small utility spacing for lists under headings */
    .tight-list li { margin: 4px 0; }
  </style>
</head>
<body>
  <header class="hero container">
    <h1 class="title">ImageLearner — CNN for Image Understanding</h1>
    <p class="lead">
      A beginner-friendly PyTorch project that trains a compact Convolutional Neural Network (CNN) on MNIST and easily extends to CIFAR-10.
      This README also doubles as a <strong>Git &amp; GitHub mini-handbook</strong>, helping you learn modern collaboration while building a real ML project.
    </p>
    <div class="badges">
      <img alt="Python" src="https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white">
      <img alt="PyTorch" src="https://img.shields.io/badge/PyTorch-2.x-EE4C2C?logo=pytorch&logoColor=white">
      <a href="https://github.com/nuthalapatideepika/simple-CNN-project/actions">
        <img alt="CI" src="https://github.com/nuthalapatideepika/simple-CNN-project/actions/workflows/ci.yml/badge.svg">
      </a>
      <img alt="License" src="https://img.shields.io/badge/License-MIT-green">
    </div>
  </header>

  <div class="container content">
    <!-- Sidebar TOC -->
    <nav class="toc">
      <h3>Contents</h3>
      <a href="#why-this-project">Why this project</a>
      <a href="#key-features">Key features</a>
      <a href="#project-structure">Project structure</a>
      <a href="#quickstart">Quickstart</a>
      <a href="#training--evaluation">Training &amp; evaluation</a>
      <a href="#reproducibility">Reproducibility</a>
      <a href="#extend-to-cifar-10">Extend to CIFAR-10</a>
      <a href="#git--github--crash-course">Git &amp; GitHub — Crash Course</a>
      <a class="sub" href="#core-concepts">• Core concepts</a>
      <a class="sub" href="#daily-workflow">• Daily workflow</a>
      <a class="sub" href="#commit-messages">• Commit messages</a>
      <a class="sub" href="#pull-requests-prs">• Pull Requests (PRs)</a>
      <a class="sub" href="#issues-labels-milestones">• Issues, labels, milestones</a>
      <a class="sub" href="#releases--tags">• Releases &amp; tags</a>
      <a class="sub" href="#branch-protection--codeowners">• Branch protection &amp; CODEOWNERS</a>
      <a class="sub" href="#beginner-efficiency-checklist">• Beginner checklist</a>
      <a href="#quality-gates-ci-lint-tests">Quality gates</a>
      <a href="#docker-usage">Docker usage</a>
      <a href="#performance-tips">Performance tips</a>
      <a href="#faq">FAQ</a>
      <a href="#troubleshooting">Troubleshooting</a>
      <a href="#roadmap">Roadmap</a>
      <a href="#contributing">Contributing</a>
      <a href="#license">License</a>
      <a href="#appendix--git-commands">Appendix — Git commands</a>
    </nav>

    <!-- Main Article -->
    <article>
      <section id="why-this-project">
        <h2>Why this project</h2>
        <ul class="tight-list">
          <li>Clear folder layout (great for learning &amp; interviews)</li>
          <li>Built-in automation: formatting, linting, tests, CI</li>
          <li>Practical <strong>Git/GitHub</strong> guide included</li>
        </ul>
      </section>

      <section id="key-features">
        <h2>Key features</h2>
        <ul class="tight-list">
          <li><strong>PyTorch</strong> training loop with CLI flags (<code>--epochs</code>, <code>--lr</code>, <code>--batch_size</code>, <code>--seed</code>)</li>
          <li><strong>SimpleCNN</strong> baseline you can easily extend</li>
          <li><strong>Ruff</strong> (format + lint) and <strong>PyTest</strong> (smoke tests)</li>
          <li><strong>GitHub Actions</strong> CI on every push/PR</li>
          <li><strong>Dockerfile</strong> for reproducible runs anywhere</li>
          <li><strong>Makefile</strong> shortcuts for speed</li>
        </ul>
      </section>

      <section id="project-structure">
        <h2>Project structure</h2>
        <pre><code>ImageLearner/
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
</code></pre>
      </section>

      <section id="quickstart">
        <h2>Quickstart</h2>
        <div class="note">Requires <strong>Python 3.10+</strong>. On Windows, use <kbd>.\.venv\Scripts\activate</kbd> instead of <code>source</code>.</div>
        <pre><code># Clone and enter the project
git clone https://github.com/nuthalapatideepika/simple-CNN-project.git
cd simple-CNN-project

# Create virtual env & install dependencies
python -m venv .venv &amp;&amp; source .venv/bin/activate
pip install -r requirements.txt

# Smoke test + quick 1-epoch train
pytest -q
python src/train.py --epochs 1
</code></pre>
        <pre><code># Handy Makefile commands
make fmt     # auto-format with Ruff
make lint    # run linter
make test    # run tests
make train   # quick training run
</code></pre>
      </section>

      <section id="training--evaluation">
        <h2>Training &amp; evaluation</h2>
        <pre><code>python src/train.py --epochs 5 --lr 0.001 --batch_size 128 --seed 42
</code></pre>
        <pre><code>[Epoch 1] train_loss=... train_acc=... val_loss=... val_acc=...
...
Best accuracy: 0.99xx
Saved: outputs/best.pt
</code></pre>
      </section>

      <section id="reproducibility">
        <h2>Reproducibility</h2>
        <ul class="tight-list">
          <li>Seeds for <code>random</code>, <code>numpy</code>, and <code>torch</code> are fixed</li>
          <li>CuDNN deterministic settings reduce randomness</li>
          <li>Ensures consistent results across machines</li>
        </ul>
      </section>

      <section id="extend-to-cifar-10">
        <h2>Extend to CIFAR-10</h2>
        <ol>
          <li>In <code>src/data.py</code>, replace <code>datasets.MNIST</code> with <code>datasets.CIFAR10</code></li>
          <li>Update transforms:</li>
        </ol>
        <pre><code>transforms.Normalize((0.4914, 0.4822, 0.4465),
                     (0.2470, 0.2435, 0.2616))
</code></pre>
        <ol start="3">
          <li>In <code>models/simple_cnn.py</code>, change input channels <strong>1 → 3</strong></li>
          <li>Add augmentations (e.g., <code>RandomCrop</code>, <code>RandomHorizontalFlip</code>)</li>
        </ol>
      </section>

      <section id="git--github--crash-course">
        <h2>Git &amp; GitHub — Crash Course</h2>

        <h3 id="core-concepts">Core concepts</h3>
        <ul class="tight-list">
          <li><strong>Repository</strong> → project + history</li>
          <li><strong>Commit</strong> → snapshot with message</li>
          <li><strong>Branch</strong> → safe space for new work</li>
          <li><strong>Remote</strong> → GitHub copy of repo</li>
          <li><strong>Push / Pull</strong> → upload / download changes</li>
          <li><strong>Pull Request (PR)</strong> → propose merging a branch into <code>main</code></li>
        </ul>

        <h3 id="daily-workflow">Daily workflow</h3>
        <pre><code>git checkout -b feature/cifar10-dataloaders
make fmt && make lint && make test
git add -A
git commit -m "feat(data): add CIFAR-10 loaders and transforms"
git push -u origin feature/cifar10-dataloaders
# Open PR → CI runs → review → squash &amp; merge
</code></pre>

        <h3 id="commit-messages">Commit messages</h3>
        <p>Use <strong>Conventional Commits</strong>:</p>
        <ul class="tight-list">
          <li><code>feat(model): add dropout for regularization</code></li>
          <li><code>fix(train): correct accuracy calculation</code></li>
          <li><code>docs(readme): add CIFAR-10 guide</code></li>
        </ul>

        <h3 id="pull-requests-prs">Pull Requests (PRs)</h3>
        <ul class="tight-list">
          <li>Keep PRs small &amp; focused</li>
          <li>CI must pass</li>
          <li>Provide description + linked issue (e.g., <code>Closes #12</code>)</li>
          <li><strong>Squash &amp; merge</strong> after review</li>
        </ul>

        <h3 id="issues-labels-milestones">Issues, labels, milestones</h3>
        <ul class="tight-list">
          <li><strong>Issues</strong> → track bugs/features</li>
          <li><strong>Labels</strong> → categorize (e.g., <code>bug</code>, <code>enhancement</code>)</li>
          <li><strong>Milestones</strong> → group tasks for releases</li>
        </ul>

        <h3 id="releases--tags">Releases &amp; tags</h3>
        <ul class="tight-list">
          <li><strong>Tag</strong> → mark a commit (e.g., <code>v0.1.0</code>)</li>
          <li><strong>Release</strong> → bundle a tag with notes/assets</li>
        </ul>

        <h3 id="branch-protection--codeowners">Branch protection &amp; CODEOWNERS</h3>
        <ul class="tight-list">
          <li>Protect <code>main</code>: require PR, review, and CI checks</li>
          <li>Use <strong>CODEOWNERS</strong> to auto-request reviewers for paths</li>
        </ul>

        <h3 id="beginner-efficiency-checklist">Beginner efficiency checklist</h3>
        <ul class="tight-list">
          <li>Enable Issues (and Discussions if needed)</li>
          <li>Enable <strong>Squash merge</strong>; disable merge commits</li>
          <li>Auto-delete merged branches</li>
          <li>Enable Dependabot + security scanning (CodeQL, secrets)</li>
          <li>Restrict direct pushes to <code>main</code></li>
        </ul>
      </section>

      <section id="quality-gates-ci-lint-tests">
        <h2>Quality gates (CI, lint, tests)</h2>
        <ul class="tight-list">
          <li><strong>Ruff</strong> → formatting + lint</li>
          <li><strong>PyTest</strong> → correctness checks</li>
          <li><strong>GitHub Actions</strong> → runs on every push/PR</li>
        </ul>
      </section>

      <section id="docker-usage">
        <h2>Docker usage</h2>
        <pre><code>docker build -t imagelearner .
docker run --rm imagelearner python src/train.py --epochs 1
</code></pre>
      </section>

      <section id="performance-tips">
        <h2>Performance tips</h2>
        <ul class="tight-list">
          <li>Use the largest <code>batch_size</code> your GPU allows</li>
          <li>Try <code>AdamW</code> + <code>OneCycleLR</code></li>
          <li>Add augmentation for CIFAR-10</li>
          <li>Use mixed precision (<code>torch.cuda.amp</code>)</li>
          <li>Profile with <code>torch.profiler</code></li>
        </ul>
      </section>

      <section id="faq">
        <h2>FAQ</h2>
        <p><strong>I’m new to Git. How do I start?</strong><br>Install Git → clone repo → create branch → commit → push → open PR.</p>
        <p><strong>Why can’t I push directly to <code>main</code>?</strong><br>Branch protection keeps <code>main</code> stable. Use PRs.</p>
        <p><strong>CI fails on “lint”. What now?</strong><br>Run <code>make fmt</code> locally → commit → push again.</p>
        <p><strong>Where is the model saved?</strong><br><code>outputs/best.pt</code> after validation accuracy improves.</p>
      </section>

      <section id="troubleshooting">
        <h2>Troubleshooting</h2>
        <ul class="tight-list">
          <li><strong>CUDA not found</strong> → install CUDA-enabled PyTorch; check <code>torch.cuda.is_available()</code></li>
          <li><strong>Permission denied</strong> → on Unix, <code>chmod +x</code>; ensure virtualenv is active</li>
          <li><strong>Dataset blocked</strong> → edit dataset path in <code>data.py</code> or pre-download</li>
        </ul>
      </section>

      <section id="roadmap">
        <h2>Roadmap</h2>
        <ul class="tight-list">
          <li>[ ] Add CIFAR-10 example with augmentations</li>
          <li>[ ] Mixed precision training (<code>--amp</code>)</li>
          <li>[ ] Training curves in README</li>
          <li>[ ] CODEOWNERS + PR/Issue templates</li>
          <li>[ ] Pre-commit hook for Ruff</li>
        </ul>
      </section>

      <section id="contributing">
        <h2>Contributing</h2>
        <ol>
          <li>Open an Issue to discuss</li>
          <li>Create a branch: <code>git checkout -b feat/your-feature</code></li>
          <li>Run <code>make fmt &amp;&amp; make lint &amp;&amp; make test</code></li>
          <li>Push branch → open PR → request review</li>
          <li>Squash &amp; merge after approval</li>
        </ol>
      </section>

      <section id="license">
        <h2>License</h2>
        <p><strong>MIT</strong> — free to use/modify with attribution. No warranty.</p>
      </section>

      <section id="appendix--git-commands">
        <h2>Appendix — Git commands</h2>
        <pre><code># Clone repo
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
</code></pre>
      </section>
    </article>
  </div>

  <p class="foot container">© ImageLearner • MIT License</p>

  <script>
    // Optional: highlight active TOC item on scroll (simple approach)
    (function() {
      const links = [...document.querySelectorAll('.toc a')].filter(a => a.getAttribute('href')?.startsWith('#'));
      const sections = links.map(a => document.querySelector(a.getAttribute('href'))).filter(Boolean);

      function onScroll() {
        const y = window.scrollY + 100;
        let activeIdx = -1;
        sections.forEach((sec, i) => {
          const top = sec.getBoundingClientRect().top + window.scrollY;
          if (y >= top) activeIdx = i;
        });
        links.forEach((a, i) => {
          a.style.background = (i === activeIdx) ? 'rgba(124,92,255,.12)' : '';
          a.style.borderColor = (i === activeIdx) ? 'rgba(124,92,255,.35)' : 'transparent';
        });
      }
      window.addEventListener('scroll', onScroll, { passive: true });
      onScroll();
    })();
  </script>
</body>
</html>
