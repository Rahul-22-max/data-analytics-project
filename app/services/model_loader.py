import joblib
import os

MODEL_PATH = "models/churn_model.pkl"


def load_model():
    if os.path.exists(MODEL_PATH):
        print("✅ ML model loaded successfully.")
        return joblib.load(MODEL_PATH)

    print("⚠ ML model not found.")
    return None


model = load_model()