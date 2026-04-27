# Deployment Readiness Notes

This project is not deployed to a cloud provider yet.

These notes document what should be checked before and after a simple deployment later.

## Deployment Goal

Run the FastAPI app in a predictable environment where:

- required environment variables are set
- the app starts successfully
- `/health` returns `200`
- `/ready` returns `200` when required config is present
- logs can be inspected when something fails

## Required Runtime Values

```text
APP_NAME
APP_ENV
APP_VERSION
FEATURE_FLAG_DEMO
REQUIRED_DEPENDENCY_URL
PORT
```

Required for readiness:

```text
REQUIRED_DEPENDENCY_URL
```

If `REQUIRED_DEPENDENCY_URL` is missing or blank, the app can still be alive, but `/ready` returns `503`.

## Startup Command

Local shell:

```bash
PORT=8020 scripts/run-dev.sh
```

Docker:

```bash
docker run --rm --name cloud-api-cicd-lab \
  -p 8020:8020 \
  -e REQUIRED_DEPENDENCY_URL=https://example.invalid/dependency \
  cloud-api-cicd-lab:local
```

## Pre-Deployment Checklist

- Confirm the latest commit has passing tests.
- Confirm GitHub Actions CI is green.
- Confirm `.env.example` has fake values only.
- Confirm real secrets are not committed.
- Confirm the target environment has the required environment variables.
- Confirm the expected port is configured.
- Confirm the health and readiness URLs are known.

## Post-Deployment Checks

Use the deployed base URL instead of `127.0.0.1`.

```bash
curl -s <base-url>/health | python -m json.tool
curl -s -i <base-url>/ready
curl -s <base-url>/config | python -m json.tool
```

Expected results:

- `/health` returns `200`
- `/ready` returns `200` when `REQUIRED_DEPENDENCY_URL` is configured
- `/config` does not expose `REQUIRED_DEPENDENCY_URL`

## Log Checks

If the app does not respond:

- check whether the process or container started
- check the configured port
- check startup logs
- check whether the service crashed during import
- check whether the platform has the correct start command

For Docker:

```bash
docker logs cloud-api-cicd-lab
```

## What This Does Not Prove

These notes do not prove production readiness.

They only show that the project owner understands the basic deployment checks a support engineer should perform around a small API service.
