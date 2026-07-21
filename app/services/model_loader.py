from pathlib import Path
import joblib

from app.core.config import settings

MODEL_PATH = Path(settings.MODEL_PATH)


def load_model():
    if MODEL_PATH.exists():
        print("✅ ML model loaded successfully.")
        return joblib.load(MODEL_PATH)

    print("⚠ ML model not found.")
    return None


model = load_model()