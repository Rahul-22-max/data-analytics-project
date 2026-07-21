import os
import sys

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from config.config import REPORTS_DIR


def test_metrics_csv():
    path = os.path.join(
        REPORTS_DIR,
        "model_metrics.csv"
    )

    assert os.path.exists(path)


def test_classification_report():
    path = os.path.join(
        REPORTS_DIR,
        "classification_report.txt"
    )

    assert os.path.exists(path)


def test_feature_importance():
    path = os.path.join(
        REPORTS_DIR,
        "logistic_feature_importance.csv"
    )

    assert os.path.exists(path)