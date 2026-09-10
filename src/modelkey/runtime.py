from __future__ import annotations

import logging
import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    log_level: str = "INFO"
    environment: str = "development"

    @classmethod
    def from_env(cls) -> "Settings":
        return cls(
            log_level=os.getenv("MODELKEY_LOG_LEVEL", "INFO").upper(),
            environment=os.getenv("MODELKEY_ENV", "development"),
        )


def configure_logging(settings: Settings | None = None) -> None:
    settings = settings or Settings.from_env()
    level = getattr(logging, settings.log_level, logging.INFO)
    logging.basicConfig(
        level=level,
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
    )
