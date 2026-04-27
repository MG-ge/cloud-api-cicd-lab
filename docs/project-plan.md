# Project Plan

## Project Name

Cloud API + CI/CD Lab

## Portfolio Purpose

This is Project 2 in the career lab.

It builds on Project 1, `b2b-saas-support-lab`, but it should not repeat the same database-heavy ticket system.

Project 1 proved:

- REST API basics
- SQLite data investigation
- HTTP status-code reasoning
- structured logs
- pytest tests
- support cases
- runbooks

Project 2 should prove:

- basic cloud-readiness
- Docker basics
- GitHub Actions CI
- environment configuration
- health and readiness checks
- safe secrets handling
- deployment documentation
- rollback and redeploy thinking

The project should be easy to explain:

```text
I built a small FastAPI service, tested it locally, configured it with environment variables, packaged it with Docker, ran tests in GitHub Actions, and documented deployment, secrets, rollback, and support troubleshooting notes.
```

This must be described as a portfolio lab, not production experience.

## Target Roles

Good target roles:

- Junior Technical Support Engineer
- SaaS Technical Support Specialist
- Application Support Specialist
- Product Support Engineer
- Cloud Support Engineer
- API Support Engineer
- Junior Integration Specialist
- Sovellusasiantuntija

## Success Criteria For v1

Version 1 is successful when a reviewer can see:

- a small API that runs locally
- `GET /health`
- environment-variable configuration
- a safe config endpoint that does not expose secrets
- a readiness endpoint that can fail for a clear reason
- pytest tests
- a Dockerfile
- documented Docker run commands
- GitHub Actions running tests
- deployment notes
- secrets-handling notes
- rollback and redeploy notes
- at least two support cases
- at least one runbook
- known limitations
- AI usage note

## Technical Stack

Use a simple backend stack:

- Python
- FastAPI
- pytest
- Docker
- GitHub Actions
- shell scripts
- curl

Do not add a database in v1 unless there is a clear support reason. Project 1 already covered SQLite and SQL investigation.

## Planned API Surface

### `GET /health`

Purpose:

```text
Shows that the API process is running.
```

Example response:

```json
{
  "status": "ok",
  "service": "cloud-api-cicd-lab"
}
```

Support meaning:

`/health` proves the process can answer a request. It does not prove the app is fully configured or ready for real work.

### `GET /config`

Purpose:

```text
Shows safe, non-secret runtime configuration.
```

Allowed output:

- app name
- environment name
- feature flag value
- whether required config is present

Never output:

- API keys
- passwords
- tokens
- raw secret values

### `GET /ready`

Purpose:

```text
Shows whether the app has required configuration to handle work.
```

Example support scenario:

```text
/health returns 200, but /ready returns 503 because a required environment variable is missing.
```

This is useful for cloud/application support because a process can be alive but misconfigured.

## Environment Variables

Planned safe variables:

```text
APP_NAME
APP_ENV
PORT
FEATURE_FLAG_DEMO
REQUIRED_DEPENDENCY_URL
```

Secrets rule:

```text
.env.example may contain variable names and fake values only.
Real secrets must never be committed.
GitHub Actions should reference secret names only, not secret values.
```

## Docker Plan

Docker should be added after local config and tests work.

Docker v1 should prove:

- build an image
- run the API in a container
- pass a port mapping
- pass environment variables
- inspect container logs
- stop and rerun the container

Do not add Docker Compose unless one container is no longer enough.

## GitHub Actions Plan

CI should be added after local tests are stable.

The first workflow should:

- check out the repo
- set up Python
- install dependencies
- run pytest

CI should not deploy anything in v1.

The goal is to prove that tests run automatically and that the owner can read pass/fail output.

## Deployment Documentation Plan

Deployment docs should be documentation-only in v1 unless explicit deployment is approved later.

Deployment notes should explain:

- required environment variables
- startup command
- health check URL
- readiness check URL
- how to inspect logs
- what to check after a redeploy

Do not claim real cloud deployment unless it actually exists.

## Secrets Handling Plan

Document:

- use `.env.example` for names and fake values
- use local `.env` only on the developer machine
- keep `.env` in `.gitignore`
- use GitHub Actions secrets for real CI secrets if needed later
- never print secret values in logs, docs, tests, or support cases

## Rollback And Redeploy Plan

Rollback/redeploy notes should stay beginner-friendly.

Planned documentation should explain:

- how to identify the last known good commit
- how to rerun tests before redeploying
- how to rebuild a Docker image from a known commit
- how to redeploy the same version if config was wrong
- how to verify `/health` and `/ready` after rollback or redeploy
- how to document what changed

No real production rollback is claimed.

## Support Case Ideas

Planned support cases:

- `/health` works but `/ready` fails because required config is missing.
- Docker container runs but the port mapping is wrong.
- CI fails because a test catches a broken health response.
- A fake secret is accidentally placed in `.env.example` and removed before commit.

## Runbook Ideas

Planned runbooks:

- API does not start locally.
- Health check fails.
- Readiness check fails.
- Docker container does not respond.
- GitHub Actions test job fails.
- Redeploy or rollback checklist.

## Simple Roadmap

### Phase 0: Plan Review

- Review this plan.
- Confirm scope.
- Do not add more application code before acceptance.

### Phase 1: Local API And Config

- Keep `/health` working.
- Add environment config.
- Add `/config`.
- Add tests.

### Phase 2: Readiness

- Add `/ready`.
- Make readiness fail when required config is missing.
- Add tests and support notes.

### Phase 3: Docker

- Add Dockerfile.
- Document build and run commands.
- Add Docker troubleshooting notes.

### Phase 4: CI

- Add GitHub Actions.
- Run pytest in CI.
- Document how to read CI output.

### Phase 5: Deployment Documentation

- Add deployment checklist.
- Add secrets-handling notes.
- Add rollback and redeploy notes.

### Phase 6: Portfolio Packaging

- Polish README.
- Add support cases.
- Add runbooks.
- Add known limitations.
- Add CV and LinkedIn package.

## Scope Boundaries

Do not add:

- Kubernetes
- microservices
- complex authentication
- paid cloud services
- frontend UI
- production monitoring
- infrastructure-as-code
- senior platform engineering claims

Those can be future projects only after this v1 is explainable.
