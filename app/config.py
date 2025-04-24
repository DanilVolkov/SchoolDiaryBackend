import secrets
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    SECRET_KEY: str = secrets.token_urlsafe(32)
    HASH_ALGORITHM: str = 'HS256'
    ACCESS_TOKEN_EXPIRES_DAYS: int = 30

settings = Settings()
