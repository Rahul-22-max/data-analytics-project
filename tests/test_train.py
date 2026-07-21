import os
import sys
import joblib

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from config.config import MODEL_PATH, DATA_PATH
from models.chrun_model.data_loader import load_data


def test_model_exists():
    assert os.path.exists(MODEL_PATH)


def test_model_loads():
    model = joblib.load(MODEL_PATH)
    assert model is not None


def test_prediction():
    model = joblib.load(MODEL_PATH)

    # Load the dataset using the project's loader
    df = load_data(DATA_PATH)

    # Match the preprocessing used during training
    X = df.drop(["Churn", "TenureGroup"], axis=1)

    prediction = model.predict(X.iloc[:1])

    assert prediction[0] in [0, 1]