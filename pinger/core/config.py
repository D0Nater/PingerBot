"""Global application configuration."""

import logging
from os import environ
from typing import Any, Self

from pydantic_settings import BaseSettings, SettingsConfigDict


logger = logging.getLogger(__name__)


class BaseConfig(BaseSettings):
    """Base configuration."""

    model_config = SettingsConfigDict(env_file_encoding="utf-8", env_nested_delimiter="__", extra="ignore")

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize config."""
        super().__init__(*args, **kwargs)
        logger.debug(f"Config initialized: {self.model_dump()}")

    @classmethod
    def from_env(cls) -> Self:
        """Create config from environment variables."""
        return cls(_env_file=environ.get("ENV_FILE", ".env"), _secrets_dir=environ.get("SECRETS_DIR"))


class TgBotConfig(BaseConfig):
    """Telegram bot configuration."""

    token: str


class AppConfig(BaseConfig):
    """Global application configuration."""

    tgbot: TgBotConfig
