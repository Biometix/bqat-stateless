from pydantic_settings import BaseSettings


class CommonSettings(BaseSettings):
    APP_NAME: str = "BQAT - Stateless"
    DEBUG_MODE: bool = False


class ServerSettings(BaseSettings):
    HOST: str = "0.0.0.0"
    PORT: int = 8848


class Settings(CommonSettings, ServerSettings):
    pass
