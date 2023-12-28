
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    LOG_LEVEL: str = "INFO"
    SERVICE_VERSION: str = "0.1.0"
    PREFIX: str = ""

settings = Settings()
