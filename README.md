<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-blue?logo=python" alt="Python" />
  <img src="https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter" alt="Jupyter" />
  <img src="https://img.shields.io/badge/OS-macOS-lightgrey?logo=apple" alt="macOS" />
  <img src="https://img.shields.io/badge/License-Educational-green" alt="License" />
  <img src="https://img.shields.io/badge/Status-Active-success" alt="Status" />
</p>

<h1 align="center">LearningLab AI</h1>
<p align="center"><em>A hands-on pathway through AI fundamentals — Math, Python, ML, DL, Transformers, RL.</em></p>

Explore a curated collection of runnable notebooks to learn core AI fundamentals: Python, data structures & algorithms, linear algebra, machine learning, deep learning, transformers, and reinforcement learning.

---

## Highlights
- **Modular Notebooks**: Organized by topic for focused study.
- **Runnable Examples**: Each section includes code you can execute.
- **Math + Code**: Blend of intuition, equations, and implementation.

> Tip: Open notebooks in Jupyter Lab for the best UX.

---

## Quick Start

1. Create/activate your environment (conda recommended):
```zsh
conda create -n aienv python=3.11 -y
conda activate aienv
```
2. Install dependencies:
```zsh
pip install -r requirements.txt
```
3. Launch Jupyter Lab/Notebook:
```zsh
jupyter lab
# or
jupyter notebook
```

---

## Repository Map

### MathBasics
- `learning_linalg.ipynb`: Linear algebra essentials (vectors, matrices, eigen, SVD).
- `learning_calculus.ipynb`: Calculus essentials (limits, derivatives, integrals, series, multivariable).

### PythonBasics
- `learning_python.ipynb`: Python foundations for AI (types, control flow, functions, OOP).
- `learning_dsa.ipynb`: Data structures & algorithms (lists, stacks, queues, trees, graphs, complexity).

### ModelBasics
- `learning_ml.ipynb`: Classic ML (regression, classification, clustering, model evaluation).
- `learning_dl.ipynb`: Deep learning (ANNs, MLPs, RNNs, LSTMs, VAEs).
- `learning_transformers.ipynb`: Transformer architecture, attention, positional encodings, training tips, interpretability.

### Root
- `learning_rl.ipynb`: Reinforcement learning foundations (MDP, policy/value, Q-learning, actor-critic).

---

## Suggested Learning Path
- **Start with MathBasics** → linear algebra, calculus.
- **Move to PythonBasics** → solidify coding fundamentals + DSA.
- **Study ModelBasics** → ML → DL → Transformers.
- **Finish with RL** → apply learning to sequential decision-making.

---

## Working With Notebooks
- **Kernel**: Ensure your environment is selected in Jupyter.
- **Requirements**: If a notebook needs extra libs, add them to `requirements.txt`.
- **Reproducibility**: Run cells top-to-bottom; use seed setting when provided.

### Recommended Extensions
- `jupyterlab` for rich notebook UX
- `black` or `ruff` for code formatting
- `matplotlib` inline and interactive backends

---

## Conventions
- Minimal external dependencies; focus on clarity and pedagogy.
- Images stored under `images/` and referenced relative to notebook locations.
- Math rendered via Markdown with KaTeX-compatible notation.

---

## Troubleshooting
- If imports fail, confirm `conda activate aienv` and `pip install -r requirements.txt`.
- For plotting issues on macOS, try:
```zsh
export MPLBACKEND=TkAgg
```
- If Jupyter can't see the env, re-install kernel:
```zsh
python -m ipykernel install --user --name aienv --display-name "Python (aienv)"
```

- If you see font warnings, clear Jupyter cache:
```zsh
jupyter lab clean
```

---

## Roadmap
- Add differential equations primer.
- Expand RL with policy gradients and modern algorithms.
- Include lightweight datasets and utilities for experimentation.

---

<p align="center">Crafted with curiosity. 🚀</p>

---

## License
Educational content and examples for personal learning and teaching.
