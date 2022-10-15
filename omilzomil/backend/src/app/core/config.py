import os
import secrets
import urllib.parse
from typing import List, Union
from pydantic import BaseSettings, AnyHttpUrl, validator


class Settings(BaseSettings):
    SECRET_KEY: str = secrets.token_urlsafe(32)
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8

    BACKEND_CORS_ORIGINS: List[str] = ["*"]

    MYSQL_HOST: str = urllib.parse.quote_plus(os.environ["MYSQL_HOST"])
    MYSQL_USER: str = urllib.parse.quote_plus(os.environ["MYSQL_USER"])
    MYSQL_PASSWORD: str = urllib.parse.quote_plus(os.environ["MYSQL_PASSWORD"])
    MYSQL_DB: str = urllib.parse.quote_plus(os.environ["MYSQL_DATABASE"])
    SQLALCHEMY_DATABASE_URI: str = f"mysql+mysqldb://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{3306}/{MYSQL_DB}"

    class Config:
        case_sensitive = True


settings = Settings()
