import os
import joblib

MODEL_PATH = "models/churn_model.pkl"


class ModelLoader:
    _model = None

    @classmethod
    def load_model(cls):
        if cls._model is None:
            if os.path.exists(MODEL_PATH):
                cls._model = joblib.load(MODEL_PATH)
                print("✅ ML Model Loaded Successfully")
            else:
                print("⚠ ML model not found. Using fallback prediction.")
        return cls._model