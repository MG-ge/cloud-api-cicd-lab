# Cloud API + CI/CD Lab

A junior-friendly portfolio lab for cloud support, application support, SaaS technical support, product support, and junior integration-adjacent roles.

This project builds on Project 1, `b2b-saas-support-lab`. Project 1 proved API, SQLite, logs, tests, support cases, and runbooks. Project 2 focuses on cloud/application support readiness: environment variables, health/readiness checks, Docker, CI, deployment documentation, secrets handling, and rollback/redeploy notes.

This is not production experience. It is a local learning and portfolio project.

## Current State

Project 2 v1 is complete.

Implemented:

- FastAPI app
- `GET /health`
- `GET /config`
- `GET /ready`
- environment-based configuration
- pytest coverage for config, health, and readiness behavior
- Dockerfile for local container runs
- GitHub Actions workflow for running tests in CI
- GitHub Actions Docker image build check
- deployment-readiness documentation
- secrets-handling notes
- rollback/redeploy notes
- support cases and runbook
- career package
- interview practice guide

Real cloud deployment is not added yet.

## Target Roles

- Junior Technical Support Engineer
- SaaS Technical Support Specialist
- Application Support Specialist
- Product Support Engineer
- Cloud Support Engineer, junior or associate level
- API Support Engineer
- Junior Integration Specialist

## Tech Stack

- Python
- FastAPI
- pytest
- Docker
- GitHub Actions
- shell scripts
- curl

## Configuration

Supported environment variables:

```text
APP_NAME                  default: Cloud API CI/CD Lab
APP_ENV                   default: local
APP_VERSION               default: 0.1.0
FEATURE_FLAG_DEMO         default: false
REQUIRED_DEPENDENCY_URL   default: missing
```

`REQUIRED_DEPENDENCY_URL` is used only as a configuration-readiness check. The app does not call this URL.

Do not commit real secrets. `.env.example` contains only safe fake values.

## Run Locally

From the project folder:

```bash
cd <project-folder>
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
PORT=8020 scripts/run-dev.sh
```

In another terminal:

```bash
curl -s http://127.0.0.1:8020/health | python -m json.tool
curl -s http://127.0.0.1:8020/config | python -m json.tool
curl -s http://127.0.0.1:8020/ready | python -m json.tool
```

By default, `/ready` returns `503` because `REQUIRED_DEPENDENCY_URL` is missing.

Run with readiness configured:

```bash
REQUIRED_DEPENDENCY_URL=https://example.invalid/dependency PORT=8020 scripts/run-dev.sh
```

Then check:

```bash
curl -s http://127.0.0.1:8020/ready | python -m json.tool
```

## Run With Docker

Build the image:

```bash
docker build -t cloud-api-cicd-lab:local .
```

Run without readiness config:

```bash
docker run --rm --name cloud-api-cicd-lab -p 8020:8020 cloud-api-cicd-lab:local
```

In another terminal:

```bash
curl -s http://127.0.0.1:8020/health | python -m json.tool
curl -s -i http://127.0.0.1:8020/ready
```

`/ready` should return `503` because `REQUIRED_DEPENDENCY_URL` was not passed.

Run with readiness config:

```bash
docker run --rm --name cloud-api-cicd-lab \
  -p 8020:8020 \
  -e REQUIRED_DEPENDENCY_URL=https://example.invalid/dependency \
  cloud-api-cicd-lab:local
```

Then:

```bash
curl -s -i http://127.0.0.1:8020/ready
```

`/ready` should return `200`.

Inspect container logs:

```bash
docker logs cloud-api-cicd-lab
```

Stop the container from another terminal:

```bash
docker stop cloud-api-cicd-lab
```

## CI

GitHub Actions runs the test suite with Python 3.12.

Workflow file:

```text
.github/workflows/ci.yml
```

The CI workflow does:

1. Check out the repository.
2. Set up Python.
3. Install dependencies from `requirements.txt`.
4. Run `pytest`.
5. Build the Docker image.

CI does not deploy the app or push a Docker image to a registry. It proves the automated tests pass and the Docker image can build in GitHub's runner environment.

## Support Documentation

- [Deployment readiness notes](docs/deployment-readiness.md)
- [Secrets handling notes](docs/secrets-handling.md)
- [Rollback and redeploy notes](docs/rollback-redeploy.md)
- [Known limitations](docs/known-limitations.md)
- [Cloud API support runbook](runbooks/cloud-api-support-runbook.md)
- [Support cases](support-cases/README.md)
- [Career package](docs/career-package-project-2.md)
- [Interview practice](docs/project-2-interview-practice.md)

## Endpoints

### `GET /health`

Returns `200` if the FastAPI process is alive.

It does not check external dependencies.

### `GET /config`

Returns safe non-secret config values:

- `app_name`
- `app_env`
- `app_version`
- `feature_flag_demo`

It does not expose `REQUIRED_DEPENDENCY_URL`.

### `GET /ready`

Returns `200` when `REQUIRED_DEPENDENCY_URL` is present and not blank.

Returns `503` when `REQUIRED_DEPENDENCY_URL` is missing or blank.

It does not call the external URL.

## Known Limitations

This is a local cloud/API-readiness lab, not a production service. Current limitations are documented in [docs/known-limitations.md](docs/known-limitations.md).

## Out Of Scope

This version does not include:

- Kubernetes
- microservices
- frontend UI
- database
- authentication
- paid cloud deployment
- real production secrets
- production monitoring
- senior platform engineering claims
- real cloud deployment

## AI Usage

AI may be used as a mentor and coding assistant.

The project owner is still responsible for running the project, reading the code, understanding the commands, verifying behavior, and explaining limitations honestly.
