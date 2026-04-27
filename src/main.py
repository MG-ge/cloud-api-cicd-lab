from typing import Any

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from src.config import read_settings

app = FastAPI(title="Cloud API + CI/CD Lab")


@app.get("/health")
def health_check() -> dict[str, str]:
    settings = read_settings()

    return {
        "status": "ok",
        "service": settings.app_name,
        "version": settings.app_version,
    }


@app.get("/config")
def get_config() -> dict[str, Any]:
    settings = read_settings()

    return {
        "app_name": settings.app_name,
        "app_env": settings.app_env,
        "app_version": settings.app_version,
        "feature_flag_demo": settings.feature_flag_demo,
    }


@app.get("/ready")
def readiness_check() -> JSONResponse:
    settings = read_settings()

    if not settings.required_dependency_configured:
        return JSONResponse(
            status_code=503,
            content={
                "status": "not_ready",
                "service": settings.app_name,
                "checks": {
                    "required_dependency_url_present": False,
                },
            },
        )

    return JSONResponse(
        status_code=200,
        content={
            "status": "ready",
            "service": settings.app_name,
            "checks": {
                "required_dependency_url_present": True,
            },
        },
    )
