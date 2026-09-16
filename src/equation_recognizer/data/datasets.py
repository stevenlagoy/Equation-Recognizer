"""
Dataset loading and vocabulary definitions

Will hold PyTorch Dataset classes for character vocabulary (digits, variables,
operators) and dataset-merging logic, TBD after requirements gathering.
"""

from pathlib import Path

# Root directory for raw and processed data
DATA_DIR = Path(__file__).resolve().parents[3] / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"

# Placeholder vocab
CHARACTER_VOCAB = [
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
    "a", "b", "c", "x", "y", "z",
    "+", "-", "*", "/",
    "(", ")",
    "=", "lt", "gt", "leq", "geq"
]