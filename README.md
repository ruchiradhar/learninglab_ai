<div align="center">

<!-- Dark mode banner -->
<img src="images/banner_dark.svg#gh-dark-mode-only" alt="LearningLab AI Dark Banner" width="100%" />
<!-- Light mode banner -->
<img src="images/banner_light.svg#gh-light-mode-only" alt="LearningLab AI Light Banner" width="100%" />

<br/>

<img src="https://img.shields.io/badge/Python-3.11-000000?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/Jupyter-NOTEBOOK-000000?style=for-the-badge&logo=jupyter&logoColor=F37626" alt="Jupyter" />
<img src="https://img.shields.io/badge/macOS-000000?style=for-the-badge&logo=apple&logoColor=white" alt="macOS" />
<img src="https://img.shields.io/badge/Status-ACTIVE-111111?style=for-the-badge&logo=github" alt="Status" />
<img src="https://img.shields.io/badge/Focus-Education-111111?style=for-the-badge&logo=bookstack&logoColor=white" alt="Educational" />

</div>

<br/>

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

### MLBasics
- `learning_ml.ipynb`: Classic ML (regression, classification, clustering, model evaluation).
- `learning_dl.ipynb`: Deep learning (ANNs, MLPs, RNNs, LSTMs, VAEs).

### LLMBasics
- `learning_embeddings.ipynb`: On the tokenization and embeddings (mainly from the Hands on LLM Book) 
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
- TBD

---

<p align="center">Crafted for personal learning. 🚀</p>

---

## License
Educational content and examples for personal learning and teaching.

---
