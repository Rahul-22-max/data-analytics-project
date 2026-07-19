import os
import joblib

from app.core.config import settings

MODEL_PATH = settings.MODEL_PATH


def load_model():
    """
    Load the trained ML model if available.
    """

    if not os.path.exists(MODEL_PATH):
        print("⚠ ML model not found.")
        return None

    try:
        model = joblib.load(MODEL_PATH)
        print("✅ ML model loaded successfully.")
        return model

    except Exception as e:
        print(f"❌ Failed to load model: {e}")
        return None


# Load the model when the application starts
model = load_model()