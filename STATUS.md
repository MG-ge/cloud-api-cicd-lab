# STATUS.md

## Current Phase

Project 2 v1 complete.

## Current State

Project 2 is complete as a junior portfolio v1 after `b2b-saas-support-lab`.

Implemented in Slice 1:

- FastAPI app
- `GET /health`
- `GET /config`
- `GET /ready`
- environment-based settings
- safe boolean parsing for `FEATURE_FLAG_DEMO`
- readiness check based on `REQUIRED_DEPENDENCY_URL`
- pytest coverage
- local run script
- pinned dependencies
- `.env.example` with safe fake values

Implemented in Slice 2:

- Dockerfile
- `.dockerignore`
- local Docker build command documentation
- local Docker run command documentation
- port mapping example
- environment variable passing example
- container log inspection notes

Implemented in Slice 3:

- GitHub Actions workflow at `.github/workflows/ci.yml`
- checkout step
- Python 3.12 setup step
- dependency install step
- pytest step

Implemented in Slice 4:

- deployment-readiness notes
- secrets-handling notes
- rollback and redeploy notes
- support runbook
- support cases

Implemented in Slice 5:

- senior review updated after must-fixes
- stale `AGENTS.md` wording corrected
- Project 2 career package
- Project 2 interview practice guide

Implemented in Slice 6:

- Docker image build check in GitHub Actions CI
- no Docker registry push
- no deployment

Not implemented yet:

- real cloud deployment
- production secret storage
- production monitoring
- alerting

Optional improvements not implemented:

- real cloud deployment
- structured application logs

## What Slice 1 Proves

- I can keep a small API running locally.
- I can distinguish `/health` from `/ready`.
- I can read config from environment variables.
- I can avoid exposing config values that should stay private.
- I can test default config and endpoint behavior.
- I can return `503` for a service that is alive but not ready.

## What Slice 2 Proves

- I can build a local Docker image for a small API.
- I can run the API in a container.
- I can map host port `8020` to container port `8020`.
- I can pass environment variables into a container.
- I can inspect container logs.
- I can distinguish app behavior from container packaging behavior.

## What Slice 3 Proves

- I can define a basic CI workflow.
- I can run tests automatically on push and pull request.
- I can separate CI from deployment.
- I can explain that CI passing means tests passed, not that production is healthy.

## What Slice 4 Proves

- I can document deployment checks without claiming a real deployment.
- I can explain safe handling of environment variables and secrets.
- I can describe rollback and redeploy decisions.
- I can write support cases from symptoms, commands, evidence, cause, and resolution.
- I can create a runbook that a junior support engineer could follow.

## What Slice 5 Proves

- I can package the project for CV, LinkedIn, GitHub, and interview use.
- I can describe the project without claiming production experience.
- I can identify what I should understand before adding more features.

## What Slice 6 Proves

- I can make CI verify both tests and Docker packaging.
- I can keep CI separate from deployment.
- I can build a container image without pushing it to a registry.

## Latest Verification

Last verified on 2026-04-27.

```text
pytest: 13 passed
GET /health: 200
GET /config: 200
GET /ready without REQUIRED_DEPENDENCY_URL: 503
GET /ready with REQUIRED_DEPENDENCY_URL: 200
docker build -t cloud-api-cicd-lab:local .: passed
docker run without REQUIRED_DEPENDENCY_URL: passed, /ready returned 503
docker run with REQUIRED_DEPENDENCY_URL: passed, /ready returned 200
local pytest after adding CI workflow: passed, 13 passed
GitHub Actions CI: passed on GitHub
local docker build -t cloud-api-cicd-lab:test .: passed
GitHub Actions Docker build: passed on GitHub
deployment-readiness docs: added
support cases: added
runbook: added
career package: added
interview practice guide: added
```

## Completion Decision

Project 2 v1 is complete.

Stop adding features to Project 2 for now. It already proves the intended junior cloud/application support readiness skills:

- environment-based configuration
- `/health`, `/config`, and `/ready`
- Docker build and run basics
- GitHub Actions pytest and Docker build checks
- secrets-handling notes
- deployment-readiness notes
- rollback/redeploy notes
- support cases and runbook

## Next Project

Project 3 should be `Observability + Incident Response Lab`.

The next project should focus on logs, metrics, alerts, incident triage, runbooks, and post-incident review.

Do not expand Project 2 into Kubernetes, frontend, auth, database, or a SaaS ticket system.

## Not In Scope For v1

- Kubernetes
- microservices
- complex authentication
- database
- paid cloud deployment
- real production secrets
- frontend UI
- production monitoring
- senior platform engineering claims
