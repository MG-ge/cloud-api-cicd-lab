# Cloud API Support Runbook

This runbook is for a small FastAPI service with local, Docker, and CI checks.

It is written for junior application support practice, not production operations.

## 1. Confirm The App Starts Locally

```bash
cd <project-folder>
source .venv/bin/activate
PORT=8020 scripts/run-dev.sh
```

If startup fails:

- confirm dependencies are installed with `pip install -r requirements.txt`
- confirm the command is run from the project folder
- read the Python traceback from the terminal
- run `pytest` to check whether tests still pass

## 2. Check Health

```bash
curl -s -i http://127.0.0.1:8020/health
```

Expected:

```text
HTTP/1.1 200 OK
```

If `/health` fails:

- confirm the server is running
- confirm the port is correct
- check whether another process is using the port
- check the terminal logs

## 3. Check Readiness

```bash
curl -s -i http://127.0.0.1:8020/ready
```

Expected without `REQUIRED_DEPENDENCY_URL`:

```text
HTTP/1.1 503 Service Unavailable
```

Expected with `REQUIRED_DEPENDENCY_URL`:

```text
HTTP/1.1 200 OK
```

If `/health` is `200` but `/ready` is `503`, the process is alive but required config is missing.

## 4. Check Safe Config

```bash
curl -s http://127.0.0.1:8020/config | python -m json.tool
```

Confirm:

- safe values are visible
- `REQUIRED_DEPENDENCY_URL` is not exposed
- no secret values are exposed

## 5. Check Docker

Build:

```bash
docker build -t cloud-api-cicd-lab:local .
```

Run:

```bash
docker run --rm --name cloud-api-cicd-lab \
  -p 8020:8020 \
  -e REQUIRED_DEPENDENCY_URL=https://example.invalid/dependency \
  cloud-api-cicd-lab:local
```

If Docker does not respond:

- confirm the container is running with `docker ps`
- confirm the host port mapping includes `-p 8020:8020`
- check logs with `docker logs cloud-api-cicd-lab`
- stop stale containers with `docker stop cloud-api-cicd-lab`

## 6. Check CI

Open the GitHub Actions run for the latest commit.

If CI fails:

- identify the failed step
- read the pytest output
- reproduce locally with `pytest`
- fix the smallest cause
- push again and confirm CI turns green

## 7. Redeploy Or Rollback Decision

Redeploy if:

- the same version should work but config or restart failed
- environment variables were corrected

Rollback if:

- the latest commit introduced the failure
- tests fail on the latest commit
- the service cannot be recovered quickly with config

After either action, verify:

```bash
curl -s -i <base-url>/health
curl -s -i <base-url>/ready
```
