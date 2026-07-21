import os
import sys
import pandas as pd

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from config.config import DATA_PATH


def test_dataset_loads():
    df = pd.read_csv(DATA_PATH, sep="\t")

    assert not df.empty


def test_target_column():
    df = pd.read_csv(DATA_PATH, sep="\t")

    assert "Churn" in df.columns


def test_dataset_rows():
    df = pd.read_csv(DATA_PATH, sep="\t")

    assert len(df) > 7000
    