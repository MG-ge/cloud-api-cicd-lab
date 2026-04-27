import pytest
from fastapi.testclient import TestClient

from src.config import read_settings
from src.main import app

CONFIG_ENV_VARS = [
    "APP_NAME",
    "APP_ENV",
    "APP_VERSION",
    "FEATURE_FLAG_DEMO",
    "REQUIRED_DEPENDENCY_URL",
]


def clear_config_env(monkeypatch) -> None:
    for name in CONFIG_ENV_VARS:
        monkeypatch.delenv(name, raising=False)


def test_config_defaults_work_as_expected(monkeypatch) -> None:
    clear_config_env(monkeypatch)

    settings = read_settings()

    assert settings.app_name == "Cloud API CI/CD Lab"
    assert settings.app_env == "local"
    assert settings.app_version == "0.1.0"
    assert settings.feature_flag_demo is False
    assert settings.required_dependency_url is None


@pytest.mark.parametrize(
    ("raw_value", "expected"),
    [
        ("true", True),
        ("1", True),
        ("yes", True),
        ("false", False),
        ("0", False),
        ("no", False),
    ],
)
def test_feature_flag_demo_parses_common_boolean_values(
    monkeypatch,
    raw_value: str,
    expected: bool,
) -> None:
    clear_config_env(monkeypatch)
    monkeypatch.setenv("FEATURE_FLAG_DEMO", raw_value)

    settings = read_settings()

    assert settings.feature_flag_demo is expected


def test_health_check_returns_service_status(monkeypatch) -> None:
    clear_config_env(monkeypatch)
    client = TestClient(app)

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "service": "Cloud API CI/CD Lab",
        "version": "0.1.0",
    }


def test_config_returns_safe_config_values(monkeypatch) -> None:
    clear_config_env(monkeypatch)
    monkeypatch.setenv("APP_NAME", "Demo Cloud API")
    monkeypatch.setenv("APP_ENV", "test")
    monkeypatch.setenv("APP_VERSION", "1.2.3")
    monkeypatch.setenv("FEATURE_FLAG_DEMO", "yes")
    monkeypatch.setenv("REQUIRED_DEPENDENCY_URL", "https://example.invalid/service")
    client = TestClient(app)

    response = client.get("/config")

    assert response.status_code == 200
    assert response.json() == {
        "app_name": "Demo Cloud API",
        "app_env": "test",
        "app_version": "1.2.3",
        "feature_flag_demo": True,
    }


def test_config_does_not_expose_required_dependency_url(monkeypatch) -> None:
    clear_config_env(monkeypatch)
    monkeypatch.setenv("REQUIRED_DEPENDENCY_URL", "https://example.invalid/service")
    client = TestClient(app)

    response = client.get("/config")

    assert response.status_code == 200
    assert "required_dependency_url" not in response.json()
    assert "REQUIRED_DEPENDENCY_URL" not in response.text
    assert "https://example.invalid/service" not in response.text


def test_ready_returns_200_when_required_dependency_url_is_set(monkeypatch) -> None:
    clear_config_env(monkeypatch)
    monkeypatch.setenv("REQUIRED_DEPENDENCY_URL", "https://example.invalid/service")
    client = TestClient(app)

    response = client.get("/ready")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ready",
        "service": "Cloud API CI/CD Lab",
        "checks": {
            "required_dependency_url_present": True,
        },
    }


def test_ready_returns_503_when_required_dependency_url_is_missing(monkeypatch) -> None:
    clear_config_env(monkeypatch)
    client = TestClient(app)

    response = client.get("/ready")

    assert response.status_code == 503
    assert response.json() == {
        "status": "not_ready",
        "service": "Cloud API CI/CD Lab",
        "checks": {
            "required_dependency_url_present": False,
        },
    }


def test_ready_returns_503_when_required_dependency_url_is_blank(monkeypatch) -> None:
    clear_config_env(monkeypatch)
    monkeypatch.setenv("REQUIRED_DEPENDENCY_URL", "   ")
    client = TestClient(app)

    response = client.get("/ready")

    assert response.status_code == 503
    assert response.json()["checks"]["required_dependency_url_present"] is False
