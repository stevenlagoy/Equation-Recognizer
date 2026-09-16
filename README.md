# Handwritten Mathematical Expression Recognition

CS 59300: Application of Deep Learning, Fall 2026

## Team

- Steven LaGoy, lagosm01@pfw.edu
- Dalton Lybarger, lybads01@pfw.edu
- Pranav Rao, raops01@pfw.edu
- Om Singhal, singo01@pfw.edu

## Overview

A deep learning application that recognizes handwritten mathematical
expressions (digits, letter variables, and operators) and converts
them into a machine-readable format, including plain text and LaTeX.
The intended use case is helping instructors turn handwritten notation
from digital whiteboards into content that can be copied, edited,
stored, or used in accessibility-oriented workflows.

## Pipeline

1. Input a handwritten expression (image upload or in-app drawing).
2. Preprocess the image (grayscale, resize, normalize, denoise).
3. Segment the image into individual characters.
4. Classify each character with a CNN.
5. Determine character ordering.
6. Reconstruct the full expression.
7. Display the result as plain text and LaTeX.

## Project Structure

```
Equation-Recognizer/
├── src/equation_recognizer/
│   ├── data/            # Dataset loading and vocabulary definitions
│   ├── preprocessing/   # Image preprocessing and segmentation
│   ├── models/          # CNN architectures
│   ├── inference/       # Expression reconstruction and LaTeX output
│   └── utils/           # Shared helpers
├── scripts/
│   └── train.py         # Baseline training entry point
├── tests/               # Unit tests
├── notebooks/           # Exploratory notebooks
├── data/
│   ├── raw/             # Untracked raw datasets
│   └── processed/       # Untracked processed datasets
├── pyproject.toml
├── requirements.txt
└── .gitignore
```

## Setup

```bash
python -m venv .venv
source .venv/bin/activate # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pip install -e .
```

Run tests:

```bash
pytest
```

Run the baseline training script (not yet implemented):

```bash
python scripts/train.py
```

## Status

Initial project scaffolding. Character vocabulary, dataset selection, and the training pipeline are still to be finalized during requirements gathering (see project proposal).
