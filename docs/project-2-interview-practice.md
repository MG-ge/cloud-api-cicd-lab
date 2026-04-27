# Project 2 Interview Practice

Use this file to test whether you can explain Project 2 without AI.

The goal is not to memorize every command. The goal is to understand what each command proves.

## What You Should Have Learned

You should be able to explain:

- what a FastAPI endpoint is
- what `/health` is used for
- why `/ready` can fail while `/health` succeeds
- what environment variables are
- why `/config` must not expose secret or internal values
- what Docker changes compared with running directly on your Mac
- what port mapping means
- what GitHub Actions CI does
- why green CI does not mean the app is deployed
- why support cases and runbooks matter for support roles
- why this project avoids Kubernetes, frontend, auth, database, and real cloud deployment for now

## 60-Second Explanation

```text
Cloud API + CI/CD Lab is a junior portfolio project for cloud and application support readiness. I built a small FastAPI service with /health, /config, and /ready endpoints. The app reads configuration from environment variables, avoids exposing sensitive config, runs locally and in Docker, and uses GitHub Actions to run pytest automatically. I also documented support cases, deployment-readiness checks, secrets handling, and rollback/redeploy notes. It is not production experience, but it shows practical support troubleshooting skills.
```

## Self-Test Questions

Answer these out loud before looking at the model answers.

### 1. What is `/health`?

Model answer:

`/health` is a simple endpoint that returns `200` when the FastAPI process is alive and can answer a request. It does not check external dependencies or full readiness.

### 2. What is `/ready`?

Model answer:

`/ready` checks whether the app has required configuration. In this project, it returns `200` when `REQUIRED_DEPENDENCY_URL` is set and `503` when it is missing or blank.

### 3. Why can `/health` return `200` while `/ready` returns `503`?

Model answer:

Because the process can be running, but the app may still be missing required configuration. Alive and ready are not the same thing.

### 4. Why does `/config` not show `REQUIRED_DEPENDENCY_URL`?

Model answer:

Because support endpoints should show only safe, non-secret information. Internal dependency URLs or secret-like values should not be exposed in diagnostic output.

### 5. What does Docker prove here?

Model answer:

Docker proves the app can be packaged and run in a container with explicit port mapping and environment variables. It also lets me inspect container logs and separate app behavior from my local Python setup.

### 6. What does `-p 8020:8020` mean?

Model answer:

It maps port `8020` on my Mac to port `8020` inside the container, so I can call the API from the host machine.

### 7. What does GitHub Actions CI prove?

Model answer:

It proves GitHub can install the dependencies and run the test suite automatically after code changes. It does not prove the app is deployed, monitored, or production-ready.

### 8. What would you check if Docker is running but curl cannot reach the API?

Model answer:

I would check `docker ps`, confirm the port mapping, check `docker logs cloud-api-cicd-lab`, and verify I am curling the correct host port.

### 9. What would you check if CI fails?

Model answer:

I would open the failed GitHub Actions run, identify the failed step, read the pytest output, reproduce locally with `pytest`, fix the smallest cause, push again, and confirm CI turns green.

### 10. Why is this project not production experience?

Model answer:

It is a local portfolio lab. It does not include real customers, real cloud deployment, production secrets, monitoring, alerting, authentication, or production operations.

## Interview Weaknesses To Answer Honestly

Weakness:

```text
There is no real cloud deployment.
```

Good answer:

```text
Correct. I intentionally kept this version focused on local API behavior, Docker, CI, and support documentation. I can explain the deployment-readiness checklist, but I am not claiming production deployment experience.
```

Weakness:

```text
Docker is not built in CI.
```

Good answer:

```text
Correct. The current CI runs pytest only. A reasonable next improvement would be to add a Docker build check to CI, but I wanted the first CI workflow to stay simple and explainable.
```

## Practice Interview

Use this order:

1. Explain the project in 60 seconds.
2. Explain `/health` versus `/ready`.
3. Explain how env vars affect `/ready`.
4. Explain Docker port mapping.
5. Explain what CI proves.
6. Explain one support case.
7. Admit one limitation honestly.

Passing standard:

- You answer without reading.
- You use simple words.
- You do not exaggerate.
- You can connect every claim to a file, command, endpoint, or test in the repo.
