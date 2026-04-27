# Project 2 Plan Review

Strict senior review for a junior Cloud API + CI/CD portfolio project.

Review date: 2026-04-27

## Executive Verdict

Project 2 is directionally strong and clearly worth building.

The plan is different enough from Project 1 because it moves away from SaaS ticket/data investigation and focuses on cloud/application support readiness: environment configuration, health versus readiness, Docker, CI tests, deployment documentation, secrets handling, and rollback/redeploy notes.

The scope is appropriate for a junior portfolio project as long as the implementation stays disciplined:

- one small FastAPI service
- no database unless a clear support reason appears
- no Kubernetes
- no paid deployment by default
- no frontend
- no complex auth
- no production claims

The existing `/health` scaffold fits the plan. It is a useful first checkpoint, but it should not grow into unrelated API features.

## 1. Is Project 2 Clearly Different From Project 1?

Yes.

Project 1 proved:

- API basics
- SQLite data checks
- users, organizations, roles, and tickets
- support cases
- SQL investigation
- structured logs
- runbooks

Project 2 should prove:

- service configuration
- health versus readiness
- Docker local repeatability
- CI test automation
- GitHub Actions output reading
- safe environment variables
- secrets handling discipline
- deployment-style documentation
- rollback and redeploy thinking

That is a good progression.

Risk to avoid:

```text
Do not rebuild another ticket system or database app in Project 2.
```

Project 2 should be about how a service is configured, tested, packaged, and checked.

## 2. Is The Scope Small Enough?

Mostly yes.

The planned v1 is reasonable if built in phases:

1. `/health`
2. environment config
3. `/config`
4. `/ready`
5. tests
6. Docker
7. GitHub Actions
8. deployment docs
9. secrets notes
10. rollback/redeploy notes
11. support cases
12. runbook

This is a lot of artifacts, but each one can stay small.

The scope becomes too large if any of these appear:

- real cloud deployment
- multiple services
- database migrations
- frontend dashboard
- auth system
- Kubernetes
- Terraform or infrastructure-as-code
- production monitoring stack

Keep v1 local and GitHub-based.

## 3. Is There Any Over-Engineering?

No major over-engineering yet.

Good restraint:

- no Kubernetes
- no microservices
- no frontend
- no paid cloud service
- no database by default
- no fake production wording

Potential over-engineering risk:

- adding Docker Compose too early
- adding real deployment too early
- adding secrets integrations before there is a real need
- adding complex settings libraries before plain environment reads are understood
- adding too many endpoints beyond `/health`, `/config`, and `/ready`

Recommendation:

```text
Use simple Python environment reads first. Add abstractions only if the code becomes confusing.
```

## 4. Is Anything Missing Before Implementation?

The plan is complete enough to begin after review.

Before implementation, decide these small details:

- What exact environment variables are required versus optional.
- What `/ready` returns when required config is missing.
- Whether `/ready` should return `200` or `503` for missing config.
- Which config values are safe to show in `/config`.
- What Docker image name will be used locally.
- Whether GitHub Actions should run only `pytest` in v1.

Recommended decisions:

```text
APP_NAME: optional, default cloud-api-cicd-lab
APP_ENV: optional, default local
FEATURE_FLAG_DEMO: optional, default false
REQUIRED_DEPENDENCY_URL: required for /ready
/ready success: 200
/ready failure: 503
/config: show only safe values and booleans, never raw secrets
CI v1: install dependencies and run pytest only
```

No blocker found.

## 5. Does The Existing `/health` Scaffold Fit The Plan?

Yes.

Current scaffold:

- `src/main.py`
- `GET /health`
- `tests/test_health.py`
- `scripts/run-dev.sh`
- `requirements.txt`
- `pyproject.toml`

This is the right starting point.

What `/health` proves:

```text
The API process is running and can respond to a request.
```

What `/health` does not prove:

```text
The app is correctly configured, connected to dependencies, safe to deploy, or ready for real work.
```

That distinction is exactly why `/ready` is useful later.

## 6. What Should The MVP Include?

MVP should include only the smallest complete cloud-support story.

### Code

- `GET /health`
- config loading from environment variables
- `GET /config`
- `GET /ready`
- tests for all three endpoints

### Docker

- one Dockerfile
- documented build command
- documented run command
- documented port mapping
- documented environment variable passing
- documented log inspection

### CI

- one GitHub Actions workflow
- install dependencies
- run pytest
- no deployment step

### Documentation

- README quickstart
- environment variable reference
- Docker run guide
- CI guide
- deployment checklist
- secrets handling note
- rollback/redeploy note
- at least two support cases
- one runbook
- known limitations
- AI usage note

### Support Cases

Minimum useful cases:

- `/health` passes but `/ready` fails because required config is missing.
- Docker container is running but the app is unreachable because of wrong port mapping.
- CI fails because a test catches a broken response.

Two cases are enough for MVP; three is stronger if kept concise.

## 7. What Should Be Explicitly Excluded?

Exclude from Project 2 v1:

- Kubernetes
- microservices
- frontend UI
- complex authentication
- real cloud deployment unless explicitly approved later
- paid services
- real production secrets
- Terraform or infrastructure-as-code
- database unless a clear support reason appears
- queues, workers, caches, or background jobs
- production monitoring stack
- alerting platform
- custom auth or RBAC
- senior platform engineering claims

These can be future projects or later phases only after this project is explainable.

## 8. What Must Be Understood Manually Before Codex Writes Code?

Before more code is written, be able to explain these in simple words.

### Health Versus Readiness

```text
/health means the process is alive.
/ready means the service is configured enough to do useful work.
```

Example:

```text
The server can return /health as OK but /ready can fail if REQUIRED_DEPENDENCY_URL is missing.
```

### Environment Variables

```text
Environment variables let the same code run with different settings in local, CI, Docker, or cloud-like environments.
```

Manual understanding:

- where variables are set
- what default values mean
- why `.env.example` has fake values
- why `.env` must stay out of Git

### Secrets Handling

```text
A secret is a value like an API key, token, password, or private credential.
```

Manual understanding:

- never commit real secrets
- never print secrets in logs
- GitHub Actions should reference secret names, not raw values
- config endpoints must not expose secret values

### Docker

```text
Docker packages the app with its runtime so it can run more consistently across machines.
```

Manual understanding:

- image versus container
- build command
- run command
- port mapping
- passing environment variables
- checking container logs
- stopping a container

### CI

```text
CI runs checks automatically after code changes.
```

Manual understanding:

- GitHub Actions workflow file
- dependency install step
- pytest step
- pass/fail logs
- CI passing does not mean production is healthy

### Rollback And Redeploy

```text
Redeploy means run the app version again. Rollback means return to a previous known-good version.
```

Manual understanding:

- identify last known good commit
- rerun tests
- rebuild known version
- verify `/health` and `/ready`
- document what changed

## Recommended Implementation Order

After this review is accepted:

1. Add config loading and tests.
2. Add `/config` with safe non-secret output.
3. Add `/ready` and tests for success/failure.
4. Update README with config and readiness examples.
5. Add Dockerfile and Docker docs.
6. Add GitHub Actions CI.
7. Add deployment, secrets, rollback/redeploy docs.
8. Add support cases and runbook.

Do not skip directly to Docker or CI before config and readiness are understood.

## Final Review Decision

Approved for implementation after the owner reviews this plan.

No application code should be changed until the plan is accepted.
