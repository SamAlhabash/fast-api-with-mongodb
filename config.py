from pydantic import BaseSettings


class Settings(BaseSettings):
    """ Base Class to Access Enviroment Variables. Can be overwritten programatically.
    """
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "FastAPI-Template"


settings = Settings()
