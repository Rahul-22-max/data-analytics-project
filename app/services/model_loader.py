import os
import pickle

MODEL_PATH = "models/churn_model.pkl"


class ModelLoader:
    _model = None

    @classmethod
    def load_model(cls):

        if cls._model is None:

            if os.path.exists(MODEL_PATH):

                with open(MODEL_PATH, "rb") as file:
                    cls._model = pickle.load(file)

                print("✅ ML Model Loaded Successfully")

            else:

                print("⚠ Model file not found. Using dummy prediction.")

        return cls._model