import os
import sys

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from config.config import (
    DATA_PATH,
    MODEL_PATH,
    REPORTS_DIR,
    VERSION_DIR,
    LOG_DIR
)


def test_dataset_exists():
    assert os.path.exists(DATA_PATH)


def test_reports_directory():
    assert os.path.isdir(REPORTS_DIR)


def test_version_directory():
    assert os.path.isdir(VERSION_DIR)


def test_logs_directory():
    assert os.path.isdir(LOG_DIR)


def test_model_path():
    assert MODEL_PATH.endswith(".pkl")