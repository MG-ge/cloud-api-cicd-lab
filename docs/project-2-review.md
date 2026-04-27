# Project 2 Review: Cloud API + CI/CD Lab

Review date: 2026-04-27

Updated after must-fix items: 2026-04-27

Reviewer stance: strict senior reviewer for a junior SaaS/Application Support, Cloud Support, Application Support, Integration Support, and early DevOps/SRE portfolio path.

## 1. Executive Verdict

This repo is credible for a junior cloud/application support portfolio project.

It is clearly different from Project 1. Project 1 focused on a local SaaS support API with data investigation and support cases. Project 2 focuses on runtime configuration, health/readiness behavior, Docker, GitHub Actions CI, deployment-readiness thinking, secrets handling, rollback/redeploy notes, and operational support cases.

What is strong:

- Simple FastAPI app with clear support-focused endpoints.
- Good distinction between `/health` and `/ready`.
- Safe `/config` endpoint that avoids exposing `REQUIRED_DEPENDENCY_URL`.
- Tests are isolated from the developer machine's real environment variables.
- Docker usage is simple and explainable.
- GitHub Actions CI exists and has passed on GitHub.
- Documentation is honest about not being production experience.
- Support cases and runbook are relevant to real junior support work.

What is weak:

- Docker is only verified manually, not in CI.
- CI is intentionally basic and does not run linting, type checks, or Docker build checks.
- There is no real deployment, which is acceptable, but the owner must explain that clearly.
- The owner still needs to practice explaining the project without reading from the docs.

What a recruiter or hiring manager should understand in 60 seconds:

```text
This is a junior portfolio lab showing that I can build and support a small API, configure it with environment variables, understand health versus readiness checks, package it with Docker, run tests in GitHub Actions, avoid exposing secrets, and document support workflows such as CI failure, readiness failure, rollback, and redeploy.
```

## 2. Completion Check

| Item | Status | Notes |
| --- | --- | --- |
| README | Present | Clear and junior-appropriate. |
| Setup instructions | Present | Local, Docker, and endpoint verification commands exist. |
| `.env.example` | Present | Uses safe fake values. |
| Tests | Present | 13 pytest tests. |
| Run script | Present | `scripts/run-dev.sh`. |
| Dockerfile | Present | Simple Python 3.12 image. |
| `.dockerignore` | Present | Excludes local/cache files. |
| GitHub Actions CI | Present | Runs pytest on push and pull request. |
| Health endpoint | Present | `GET /health`. |
| Config endpoint | Present | `GET /config`, safe values only. |
| Readiness endpoint | Present | `GET /ready`, returns 503 when required config is missing. |
| Deployment-readiness docs | Present | `docs/deployment-readiness.md`. |
| Secrets-handling docs | Present | `docs/secrets-handling.md`. |
| Rollback/redeploy docs | Present | `docs/rollback-redeploy.md`. |
| Support cases | Present | 3 cases. |
| Runbook | Present | Cloud API support runbook. |
| Known limitations | Present | Honest and useful. |
| AI usage note | Present | Honest and junior-credible. |
| Local verification evidence | Present | `STATUS.md` records test/API/Docker/CI checks. |
| Career package | Present | `docs/career-package-project-2.md`. |
| Interview practice | Present | `docs/project-2-interview-practice.md`. |

## 3. Technical Correctness Review

### FastAPI App Structure

The app is appropriately small:

- `src/main.py` owns endpoint definitions.
- `src/config.py` owns environment parsing.
- No unnecessary routers, dependency injection layers, database, auth, or frontend were added.

This is the right level for a junior portfolio lab.

### Configuration Handling

`read_settings()` is explicit and readable. Defaults are clear:

- `APP_NAME`
- `APP_ENV`
- `APP_VERSION`
- `FEATURE_FLAG_DEMO`
- `REQUIRED_DEPENDENCY_URL`

Blank strings are handled correctly for required dependency readiness.

The boolean parser is intentionally boring and safe. Unknown values fall back to `False`, which is acceptable for a demo feature flag. In a production system, unknown boolean values might be logged or rejected, but that is not necessary here.

### Endpoint Behavior

`GET /health`:

- Returns `200` when the app process can answer.
- Does not check external dependencies.
- Correct for process-level health.

`GET /config`:

- Returns safe values only.
- Does not expose `REQUIRED_DEPENDENCY_URL`.
- Correct for demonstrating safe support diagnostics.

`GET /ready`:

- Returns `200` when required config is present.
- Returns `503` when `REQUIRED_DEPENDENCY_URL` is missing or blank.
- Does not call the external URL.
- Correct for a configuration-readiness demo.

### Error Handling

The 503 response is explicit and readable. Using `JSONResponse` is fine here.

There is no global error handler, which is acceptable. Adding one would be unnecessary for this scope.

### Logging

The app relies on Uvicorn/default runtime logs. That is acceptable for this slice.

Weakness: there are no custom structured logs. This should stay as future work unless the next portfolio step is specifically observability.

### Tests

Tests are strong for the current scope:

- Defaults are tested.
- Boolean parsing is tested.
- `/health` is tested.
- `/config` safe output is tested.
- `/ready` 200 and 503 paths are tested.
- `monkeypatch` isolates tests from real machine environment variables.

Small gap: tests do not cover uppercase boolean values like `TRUE` or whitespace around values. The implementation supports them, but tests do not prove it.

### Docker

The Dockerfile is simple and understandable:

- Python 3.12 slim base image.
- Installs `requirements.txt`.
- Copies only `src`.
- Runs Uvicorn.
- Uses `PORT` with a default of `8020`.

This is good for junior Docker practice.

Weaknesses that are acceptable for now:

- Runs as root.
- No Docker healthcheck.
- Docker build is not tested in CI.

These are not must-fix items for this portfolio stage.

### GitHub Actions CI

The workflow is correctly scoped:

- runs on `push`
- runs on `pull_request`
- checks out code
- sets up Python 3.12
- installs dependencies
- runs pytest

This is enough for a junior support/cloud-readiness portfolio project.

Nice improvement later: add dependency caching or a Docker build check, but only after the owner can explain the current CI clearly.

### Dependency Files

`requirements.txt` is small and pinned. That is good for reproducibility.

`pyproject.toml` configures pytest only. That is acceptable.

### Ignore Files

`.gitignore` and `.dockerignore` are appropriate. Local virtual environments, cache files, logs, and `.env` are excluded.

## 4. Support-Role Relevance Review

This project demonstrates:

Troubleshooting:

- Diagnosing why `/health` can pass while `/ready` fails.
- Checking Docker logs and port mappings.
- Reading CI failures and reproducing locally.

API understanding:

- Clear use of `GET` endpoints.
- JSON responses are readable.
- HTTP status codes carry support meaning.

Configuration understanding:

- Environment variables control runtime behavior.
- Missing config can make a service not ready even when it is alive.
- Safe config output helps support without exposing sensitive values.

HTTP status-code reasoning:

- `200` means the check passed.
- `503` means the service is alive but not ready.

Cloud-readiness:

- App can run locally and in Docker.
- Port mapping is documented.
- CI runs in GitHub's environment.
- Deployment-readiness checks are documented without fake production claims.

Secrets handling:

- `.env.example` uses fake values.
- `.env` is ignored.
- Docs explain why secret names and secret values are different.

Documentation:

- README explains the project quickly.
- Runbook and support cases show practical support thinking.
- Known limitations are honest.

## 5. CV Alignment

English CV bullets:

- Built a junior portfolio FastAPI service demonstrating environment-based configuration, `/health` and `/ready` checks, and safe non-secret config output.
- Packaged the API with Docker and added GitHub Actions CI to run pytest automatically on push and pull request.
- Documented cloud/application support workflows including readiness failures, Docker port issues, CI failures, secrets handling, and rollback/redeploy checks.

Finnish CV bullets:

- Toteutin junior-tason FastAPI-portfoliopalvelun, jossa harjoitellaan ympäristömuuttujia, `/health`- ja `/ready`-tarkistuksia sekä turvallista konfiguraation näyttämistä.
- Paketoin API:n Dockerilla ja lisäsin GitHub Actions -CI:n, joka ajaa pytest-testit automaattisesti push- ja pull request -tilanteissa.
- Dokumentoin sovellus- ja pilvitukitilanteita, kuten readiness-virheitä, Docker-porttiongelmia, CI-virheitä, salaisuuksien käsittelyä sekä rollback/redeploy-tarkistuksia.

Do not call this production experience.

## 6. Interview Preparation

### 5 Interview Questions And Model Answers

1. What is the difference between `/health` and `/ready`?

Model answer:

`/health` only proves the FastAPI process can respond. `/ready` checks whether required configuration is present. In this project, `/health` can return 200 while `/ready` returns 503 if `REQUIRED_DEPENDENCY_URL` is missing.

2. Why does `/config` not return `REQUIRED_DEPENDENCY_URL`?

Model answer:

Because support endpoints should avoid exposing sensitive or internal dependency values. `/config` returns only safe values like app name, environment, version, and feature flag state.

3. What does Docker prove in this project?

Model answer:

Docker proves I can package and run the same small API in a container, pass environment variables, map ports, inspect logs, and separate app behavior from local machine setup.

4. What does GitHub Actions prove here?

Model answer:

It proves the tests can run automatically in GitHub after a push or pull request. It does not prove the app is deployed or production-ready.

5. What would you check if `/health` is 200 but `/ready` is 503?

Model answer:

I would check whether `REQUIRED_DEPENDENCY_URL` is set and not blank, then inspect the app's environment/configuration. I would not assume the process is down because `/health` already proves it is responding.

### 3 Things To Explain Without AI

- Why `/health` and `/ready` are intentionally different.
- How environment variables change app behavior locally and in Docker.
- What a green GitHub Actions run proves and what it does not prove.

### 2 Likely Weaknesses An Interviewer Might Notice

- There is no real cloud deployment yet.
- Docker is not built or tested inside the CI workflow.

Good response:

```text
Those are intentional limits for this stage. This repo proves local API behavior, Docker basics, CI tests, and support documentation. I would add real deployment or Docker-in-CI only after I can explain the current foundation clearly.
```

## 7. Improvement Backlog

### Must Fix Before Heavy Sharing

No open must-fix items remain after the 2026-04-27 update.

Completed must-fix items:

- Updated stale `AGENTS.md` wording.
- Added `docs/career-package-project-2.md`.
- Added `docs/project-2-interview-practice.md`.

### Nice To Improve

- Add tests for uppercase and whitespace boolean env values.
- Add a CI step that builds the Docker image.
- Add a short `docs/local-verification.md` file with the exact latest verification commands and expected results.
- Add one support case for missing secret/config value in a deployment-like environment.
- Add a short architecture diagram in Markdown or Mermaid.

### Future Project, Not Project 2 v1

- Real cloud deployment.
- Kubernetes.
- Terraform or infrastructure-as-code.
- Production monitoring/alerting.
- Real dependency checks over the network.
- Authentication.
- Database.
- Frontend.

## 8. Verification Commands

Install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run tests:

```bash
pytest
```

Run locally:

```bash
PORT=8020 scripts/run-dev.sh
```

Verify endpoints:

```bash
curl -s http://127.0.0.1:8020/health | python -m json.tool
curl -s http://127.0.0.1:8020/config | python -m json.tool
curl -s -i http://127.0.0.1:8020/ready
```

Run with readiness configured:

```bash
REQUIRED_DEPENDENCY_URL=https://example.invalid/dependency PORT=8020 scripts/run-dev.sh
curl -s -i http://127.0.0.1:8020/ready
```

Build Docker image:

```bash
docker build -t cloud-api-cicd-lab:local .
```

Run Docker container:

```bash
docker run --rm --name cloud-api-cicd-lab \
  -p 8020:8020 \
  -e REQUIRED_DEPENDENCY_URL=https://example.invalid/dependency \
  cloud-api-cicd-lab:local
```

Check GitHub Actions:

```bash
gh run list --repo MG-ge/cloud-api-cicd-lab --limit 5
```

## 9. Final Recommendation

Do not add more technical features yet.

Next best step:

1. Practice explaining Project 2 manually.
2. Add Project 2 to CV/LinkedIn when ready.
3. Only then decide whether to add Docker build in CI or a no-cost deployment simulation.

The repo is already a credible junior portfolio project. The next gains come from presentation, explanation, and small verification polish, not more architecture.

## 10. Second Review After Must-Fixes

Verdict after must-fix cleanup:

```text
Project 2 is ready to use as a junior portfolio repo, assuming the owner can explain it clearly and honestly.
```

The repo now has:

- accurate project instructions
- career package
- interview practice material
- support cases
- runbook
- known limitations
- AI usage note
- local and GitHub CI verification

Do not add more features until the owner can answer the interview questions without AI.
