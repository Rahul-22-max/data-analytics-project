import os
import sys
import pandas as pd

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from config.config import VERSION_DIR


def test_registry_exists():
    registry = os.path.join(
        VERSION_DIR,
        "model_registry.csv"
    )

    assert os.path.exists(registry)


def test_registry_not_empty():
    registry = os.path.join(
        VERSION_DIR,
        "model_registry.csv"
    )

    df = pd.read_csv(registry)

    assert not df.empty


def test_saved_models():
    files = [
        f for f in os.listdir(VERSION_DIR)
        if f.endswith(".pkl")
    ]

    assert len(files) >= 1