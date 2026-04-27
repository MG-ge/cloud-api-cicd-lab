import os
from dataclasses import dataclass
from typing import Mapping

DEFAULT_APP_NAME = "Cloud API CI/CD Lab"
DEFAULT_APP_ENV = "local"
DEFAULT_APP_VERSION = "0.1.0"


@dataclass(frozen=True)
class Settings:
    app_name: str
    app_env: str
    app_version: str
    feature_flag_demo: bool
    required_dependency_url: str | None

    @property
    def required_dependency_configured(self) -> bool:
        return bool(self.required_dependency_url)


def parse_bool(value: str | None) -> bool:
    if value is None:
        return False

    normalized = value.strip().lower()

    if normalized in {"1", "true", "yes", "y", "on"}:
        return True

    if normalized in {"0", "false", "no", "n", "off", ""}:
        return False

    return False


def read_settings(environ: Mapping[str, str] | None = None) -> Settings:
    source = os.environ if environ is None else environ

    required_dependency_url = source.get("REQUIRED_DEPENDENCY_URL")
    if required_dependency_url is not None:
        required_dependency_url = required_dependency_url.strip() or None

    return Settings(
        app_name=source.get("APP_NAME", DEFAULT_APP_NAME).strip() or DEFAULT_APP_NAME,
        app_env=source.get("APP_ENV", DEFAULT_APP_ENV).strip() or DEFAULT_APP_ENV,
        app_version=source.get("APP_VERSION", DEFAULT_APP_VERSION).strip()
        or DEFAULT_APP_VERSION,
        feature_flag_demo=parse_bool(source.get("FEATURE_FLAG_DEMO")),
        required_dependency_url=required_dependency_url,
    )
