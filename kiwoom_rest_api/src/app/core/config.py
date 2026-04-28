"""Application settings for FastAPI runtime."""

from dataclasses import dataclass
import os


@dataclass(slots=True)
class Settings:
    app_name: str = "Kiwoom REST API"
    app_version: str = "0.1.0"
    env: str = "dev"
    debug: bool = True
    api_prefix: str = "/api/v1"



def load_settings() -> Settings:
    env = os.getenv("APP_ENV", "dev").strip().lower() or "dev"
    debug_raw = os.getenv("APP_DEBUG", "true").strip().lower()
    debug = debug_raw in {"1", "true", "yes", "on"}

    return Settings(
        app_name=os.getenv("APP_NAME", "Kiwoom REST API"),
        app_version=os.getenv("APP_VERSION", "0.1.0"),
        env=env,
        debug=debug,
        api_prefix=os.getenv("API_PREFIX", "/api/v1"),
    )
