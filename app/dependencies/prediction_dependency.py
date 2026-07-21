from app.services.prediction_service import PredictionService


def get_prediction_service():
    """
    Dependency that returns a PredictionService instance.
    """
    return PredictionService()