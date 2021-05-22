from pydantic import BaseSettings, AnyHttpUrl


class Settings(BaseSettings):
    """ Base Class to Access Enviroment Variables. Can be overwritten programatically.
    """
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "FastAPI-Template"
    PROJECT_DESC: str = "A basic template for creating Fast-API applications"
    PROJECT_VERSION: str = "1.0.0"
    BACKEND_CORS_ORIGINS: list[AnyHttpUrl] = []

    # Mongo Variables 
    MONGO_URL: str = "mongodb://localhost:27017"
    DB_NAME: str = "test_db"

settings = Settings()
