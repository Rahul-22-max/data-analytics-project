from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "Customer Churn Prediction API"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True

    MODEL_PATH: str = "models/churn_model.pkl"

    API_PREFIX: str = "/api/v1"

    HOST: str = "127.0.0.1"
    PORT: int = 8000

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )


settings = Settings()