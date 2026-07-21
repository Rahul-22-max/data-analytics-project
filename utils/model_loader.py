import joblib
from pathlib import Path

# Project root directory
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Models directory
MODELS_DIR = PROJECT_ROOT / "models"


def load_model(model_path):
    if not model_path.exists():
        raise FileNotFoundError(
            f"Model file not found: {model_path}"
        )

    print(f"Loading model from: {model_path}")

    return joblib.load(model_path)


def load_churn_model():
    return load_model(MODELS_DIR / "churn_model.pkl")


def load_ltv_model():
    return load_model(MODELS_DIR / "ltv_model.pkl")


def load_linear_model():
    return load_model(MODELS_DIR / "linear_regression_ltv.pkl")


def load_xgboost():
    return load_model(MODELS_DIR / "xgboost_ltv.pkl")