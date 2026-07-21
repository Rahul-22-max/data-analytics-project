import joblib
import shap


def load_model(model_path):
    return joblib.load(model_path)


def create_explainer(model):
    return shap.Explainer(model)


def generate_shap_values(explainer, data):
    return explainer(data)