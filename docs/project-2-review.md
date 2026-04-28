# Project 2 Final Review: Cloud API + CI/CD Lab

Review date: 2026-04-28

Reviewer stance: strict senior reviewer for a junior Cloud/Application Support portfolio project.

## Executive Verdict

Complete v1.

Project 2 is complete as a junior portfolio project. It proves the intended basics for moving from B2B SaaS/Application Support toward Cloud/Application/Integration support:

- local API operation
- environment-based configuration
- health and readiness checks
- safe config exposure
- Docker build and run basics
- GitHub Actions test and Docker build checks
- deployment/redeploy/rollback documentation
- secrets-handling awareness
- support cases and runbook writing

It should not keep expanding. More Project 2 features would blur the purpose and make the project less focused.

## What The Project Proves

- I can build and run a small FastAPI service locally.
- I understand the difference between process health and readiness.
- I can use environment variables to change runtime behavior.
- I can expose safe diagnostic config without exposing internal dependency values.
- I can write pytest coverage for default config and endpoint behavior.
- I can build and run the app in Docker.
- I can use GitHub Actions to run tests and build a Docker image.
- I can document deployment-readiness, rollback/redeploy thinking, secrets handling, support cases, and runbooks.

## What The Project Does Not Prove

- It is not production experience.
- It is not deployed to a real cloud provider.
- It does not prove production monitoring, alerting, autoscaling, or incident response.
- It does not prove production-grade secret management.
- It does not prove senior DevOps, SRE, or platform engineering skills.
- It does not include Kubernetes, frontend work, authentication, database work, or a SaaS ticket system.

These limits are acceptable for v1.

## Verification Summary

Verified:

```text
pytest: 13 passed
local app runs through scripts/run-dev.sh
GET /health: 200
GET /config: 200 with safe non-secret values only
GET /ready without REQUIRED_DEPENDENCY_URL: 503
GET /ready with REQUIRED_DEPENDENCY_URL: 200
Docker build: passed
Docker run: passed
GitHub Actions pytest job: passed
GitHub Actions Docker build job: passed
no committed real secrets found
```

## Endpoint Behavior Summary

### `/health`

Purpose:

```text
Shows that the FastAPI process is alive and can answer a request.
```

Expected result:

```text
HTTP 200
```

It does not check external dependencies.

### `/config`

Purpose:

```text
Shows safe, non-secret runtime configuration.
```

Exposes:

- `app_name`
- `app_env`
- `app_version`
- `feature_flag_demo`

Does not expose:

- `REQUIRED_DEPENDENCY_URL`
- raw environment dumps
- secrets
- tokens
- passwords

### `/ready`

Purpose:

```text
Shows whether required configuration is present.
```

Expected behavior:

- returns `200` when `REQUIRED_DEPENDENCY_URL` is present and not blank
- returns `503` when `REQUIRED_DEPENDENCY_URL` is missing or blank
- does not call the external URL

Support meaning:

```text
The app can be alive but not ready.
```

## Docker Verification Summary

Docker verifies that the app can be packaged and run in a container.

Verified:

- Docker image builds successfully.
- Container starts.
- Host-to-container port mapping works.
- Environment variables can be passed into the container.
- `/ready` returns `503` without required config.
- `/ready` returns `200` when `REQUIRED_DEPENDENCY_URL` is provided.

Docker does not prove production deployment.

## GitHub Actions Verification Summary

GitHub Actions verifies two checks:

- Python test job runs `pytest`.
- Docker build job builds the Docker image.

Both jobs have passed on GitHub.

CI does not mean:

- the app is deployed
- the app is production-ready
- the app is monitored
- every possible bug is impossible

## Secrets And Config Safety Summary

Safe:

- `.env.example` contains fake values only.
- `.env` is ignored by git.
- `/config` returns safe values only.
- `REQUIRED_DEPENDENCY_URL` is used for readiness but is not exposed by `/config`.
- docs use `example.invalid` placeholders.

No committed real secrets were found during review.

## Known Limitations

- No real cloud deployment.
- No production secrets manager.
- No production monitoring or alerting.
- No structured application logging in this project.
- No real dependency network check.
- No database.
- No authentication.
- No frontend.
- No Kubernetes.

These are intentional v1 limits.

## Why The Project Should Stop At v1

Project 2 has reached its purpose. It proves practical cloud/application support readiness without pretending to be production infrastructure.

Adding more features now would reduce focus. The next skill area should be a new project, not a larger Project 2.

Stop Project 2 here.

## Recommended Next Project

Project 3: Observability + Incident Response Lab.

High-level direction:

- structured logs
- metrics or uptime checks
- incident scenarios
- runbook updates
- postmortem writeups

Project 3 should be planned and reviewed before implementation.
