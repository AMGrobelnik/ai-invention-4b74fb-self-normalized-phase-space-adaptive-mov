# Self-Normalized Phase-Space Adaptive Moving Average Forecasting for Short Noisy Time Series

<div align="center">

<a href="https://cdn.jsdelivr.net/gh/AMGrobelnik/ai-invention-4b74fb-self-normalized-phase-space-adaptive-mov@main/workflow.svg">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="workflow-dark.svg">
  <img alt="Artifact workflow — how every artifact in this repo was built" src="workflow.svg">
</picture>
</a>

<sub>🖱️ <b><a href="https://cdn.jsdelivr.net/gh/AMGrobelnik/ai-invention-4b74fb-self-normalized-phase-space-adaptive-mov@main/workflow.svg">Open the interactive diagram</a></b> — every card links to its artifact folder.</sub>

</div>

> **TL;DR** — We presented Self-Normalized Phase-Space Adaptive Moving Average (PSAMA) forecasting, incorporating rolling MAD normalization to stabilize dynamic window sizing across short noisy time series. Evaluations across 1,000 trajectories and 5,880 trials validate its robustness and statistical significance.

<details>
<summary>Full hypothesis</summary>

In high-noise time series governed by stochastic dynamics, a locally adaptive sliding-window moving average whose window size dynamically scales with self-normalized local gradient volatility (via rolling median absolute deviation) provides precise local noise suppression and inflection tracking, though aggregate global error metrics depend heavily on stochastic transition regimes compared to naive persistence.

</details>

[![Download PDF](https://img.shields.io/badge/Download-PDF-red)](https://cdn.jsdelivr.net/gh/AMGrobelnik/ai-invention-4b74fb-self-normalized-phase-space-adaptive-mov@main/paper.pdf) [![LaTeX Source](https://img.shields.io/badge/LaTeX-Source-orange)](https://github.com/AMGrobelnik/ai-invention-4b74fb-self-normalized-phase-space-adaptive-mov/tree/main/paper_latex)

This repository contains all **6 artifacts** produced across **2 rounds** of an autonomous AI research run — round by round, exactly in the order they were invented.

## Round 1

| Artifact | Type | Demo | Source | Builds on |
|----------|------|------|--------|-----------|
| **[Synthetic Time Series Dataset for Adaptive Moving Average](https://github.com/AMGrobelnik/ai-invention-4b74fb-self-normalized-phase-space-adaptive-mov/tree/main/round-1/dataset-1)** | [![dataset](https://img.shields.io/badge/dataset-f59e0b)](https://github.com/AMGrobelnik/ai-invention-4b74fb-self-normalized-phase-space-adaptive-mov/tree/main/round-1/dataset-1) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AMGrobelnik/ai-invention-4b74fb-self-normalized-phase-space-adaptive-mov/blob/main/round-1/dataset-1/demo/data_code_demo.ipynb) | [![Source Code](https://img.shields.io/badge/Source_Code-2962FF)](https://github.com/AMGrobelnik/ai-invention-4b74fb-self-normalized-phase-space-adaptive-mov/tree/main/round-1/dataset-1/src) | — |
| **[Adaptive Moving Average Forecasting](https://github.com/AMGrobelnik/ai-invention-4b74fb-self-normalized-phase-space-adaptive-mov/tree/main/round-1/experiment-1)** | [![experiment](https://img.shields.io/badge/experiment-8b5cf6)](https://github.com/AMGrobelnik/ai-invention-4b74fb-self-normalized-phase-space-adaptive-mov/tree/main/round-1/experiment-1) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AMGrobelnik/ai-invention-4b74fb-self-normalized-phase-space-adaptive-mov/blob/main/round-1/experiment-1/demo/method_code_demo.ipynb) | [![Source Code](https://img.shields.io/badge/Source_Code-2962FF)](https://github.com/AMGrobelnik/ai-invention-4b74fb-self-normalized-phase-space-adaptive-mov/tree/main/round-1/experiment-1/src) | — |
| **[Phase-Space Adaptive MA Evaluation](https://github.com/AMGrobelnik/ai-invention-4b74fb-self-normalized-phase-space-adaptive-mov/tree/main/round-1/evaluation-1)** | [![evaluation](https://img.shields.io/badge/evaluation-10b981)](https://github.com/AMGrobelnik/ai-invention-4b74fb-self-normalized-phase-space-adaptive-mov/tree/main/round-1/evaluation-1) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AMGrobelnik/ai-invention-4b74fb-self-normalized-phase-space-adaptive-mov/blob/main/round-1/evaluation-1/demo/eval_code_demo.ipynb) | [![Source Code](https://img.shields.io/badge/Source_Code-2962FF)](https://github.com/AMGrobelnik/ai-invention-4b74fb-self-normalized-phase-space-adaptive-mov/tree/main/round-1/evaluation-1/src) | — |

## Round 2

| Artifact | Type | Demo | Source | Builds on |
|----------|------|------|--------|-----------|
| **[Phase-Space Adaptive Moving Average Dataset](https://github.com/AMGrobelnik/ai-invention-4b74fb-self-normalized-phase-space-adaptive-mov/tree/main/round-2/dataset-1)** | [![dataset](https://img.shields.io/badge/dataset-f59e0b)](https://github.com/AMGrobelnik/ai-invention-4b74fb-self-normalized-phase-space-adaptive-mov/tree/main/round-2/dataset-1) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AMGrobelnik/ai-invention-4b74fb-self-normalized-phase-space-adaptive-mov/blob/main/round-2/dataset-1/demo/data_code_demo.ipynb) | [![Source Code](https://img.shields.io/badge/Source_Code-2962FF)](https://github.com/AMGrobelnik/ai-invention-4b74fb-self-normalized-phase-space-adaptive-mov/tree/main/round-2/dataset-1/src) | — |
| **[Self-Normalized Phase-Space Adaptive Moving Average](https://github.com/AMGrobelnik/ai-invention-4b74fb-self-normalized-phase-space-adaptive-mov/tree/main/round-2/experiment-1)** | [![experiment](https://img.shields.io/badge/experiment-8b5cf6)](https://github.com/AMGrobelnik/ai-invention-4b74fb-self-normalized-phase-space-adaptive-mov/tree/main/round-2/experiment-1) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AMGrobelnik/ai-invention-4b74fb-self-normalized-phase-space-adaptive-mov/blob/main/round-2/experiment-1/demo/method_code_demo.ipynb) | [![Source Code](https://img.shields.io/badge/Source_Code-2962FF)](https://github.com/AMGrobelnik/ai-invention-4b74fb-self-normalized-phase-space-adaptive-mov/tree/main/round-2/experiment-1/src) | <sub><i>uses:</i><br/>[dataset‑1&nbsp;(R1)](https://github.com/AMGrobelnik/ai-invention-4b74fb-self-normalized-phase-space-adaptive-mov/tree/main/round-1/dataset-1)</sub> |
| **[Normalized PSAMA Statistical Rigor and Error Analysis](https://github.com/AMGrobelnik/ai-invention-4b74fb-self-normalized-phase-space-adaptive-mov/tree/main/round-2/evaluation-1)** | [![evaluation](https://img.shields.io/badge/evaluation-10b981)](https://github.com/AMGrobelnik/ai-invention-4b74fb-self-normalized-phase-space-adaptive-mov/tree/main/round-2/evaluation-1) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AMGrobelnik/ai-invention-4b74fb-self-normalized-phase-space-adaptive-mov/blob/main/round-2/evaluation-1/demo/eval_code_demo.ipynb) | [![Source Code](https://img.shields.io/badge/Source_Code-2962FF)](https://github.com/AMGrobelnik/ai-invention-4b74fb-self-normalized-phase-space-adaptive-mov/tree/main/round-2/evaluation-1/src) | <sub><i>similarities:</i><br/>[experiment‑1&nbsp;(R1)](https://github.com/AMGrobelnik/ai-invention-4b74fb-self-normalized-phase-space-adaptive-mov/tree/main/round-1/experiment-1)</sub> |

## Repository Structure

Artifacts are grouped by the round of invention that produced them. Each
artifact has its own folder with source code and a self-contained demo:

```
.
├── round-1/                         # One folder per round of invention
│   ├── experiment-1/
│   │   ├── README.md                # What this artifact is + dependencies
│   │   ├── src/                     # Full workspace from execution
│   │   │   ├── method.py            # Main implementation
│   │   │   ├── method_out.json      # Full output data
│   │   │   └── ...                  # All execution artifacts
│   │   └── demo/                    # Self-contained demo
│   │       └── method_code_demo.ipynb # Colab-ready notebook (code + data inlined)
│   ├── dataset-1/
│   │   ├── src/
│   │   └── demo/
│   └── evaluation-1/
│       ├── src/
│       └── demo/
├── round-2/                         # Later rounds build on earlier artifacts
├── paper.pdf                        # Research paper
├── paper_latex/                     # LaTeX source files
├── workflow.svg                     # Artifact dependency diagram (this page's header)
└── README.md
```

## Running Notebooks

### Option 1: Google Colab (Recommended)

Click the "Open in Colab" badges above to run notebooks directly in your browser.
No installation required!

### Option 2: Local Jupyter

```bash
# Clone the repo
git clone https://github.com/AMGrobelnik/ai-invention-4b74fb-self-normalized-phase-space-adaptive-mov
cd ai-invention-4b74fb-self-normalized-phase-space-adaptive-mov

# Install dependencies
pip install jupyter

# Run any artifact's demo notebook
jupyter notebook <artifact_folder>/demo/
```

## Source Code

The original source files are in each artifact's `src/` folder.
These files may have external dependencies - use the demo notebooks for a self-contained experience.

---
*Generated by AI Inventor Pipeline - Automated Research Generation*
