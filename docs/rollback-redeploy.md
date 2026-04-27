# Rollback And Redeploy Notes

This project does not have a real production deployment.

These notes describe the support thinking behind rollback and redeploy decisions.

## Redeploy

Redeploy means running the same intended version again.

Use redeploy when:

- the code is correct but the platform did not restart cleanly
- an environment variable was missing and has now been fixed
- the container or process needs to be restarted with the same image or commit

After redeploy:

```bash
curl -s <base-url>/health | python -m json.tool
curl -s -i <base-url>/ready
```

## Rollback

Rollback means returning to a previous known-good version.

Use rollback when:

- the latest version breaks tests
- the latest version starts but health checks fail
- a config change cannot safely fix the problem
- the root cause is not understood and service recovery is more urgent

## Simple Rollback Checklist

- Identify the broken version or commit.
- Identify the last known-good commit.
- Read the failing CI logs or runtime logs.
- Run tests locally if possible.
- Rebuild or redeploy the known-good version.
- Verify `/health`.
- Verify `/ready`.
- Document what changed and what remains unknown.

## Local Known-Good Docker Example

Build from the current checked-out commit:

```bash
docker build -t cloud-api-cicd-lab:local .
```

Run with readiness config:

```bash
docker run --rm --name cloud-api-cicd-lab \
  -p 8020:8020 \
  -e REQUIRED_DEPENDENCY_URL=https://example.invalid/dependency \
  cloud-api-cicd-lab:local
```

Verify:

```bash
curl -s http://127.0.0.1:8020/health | python -m json.tool
curl -s -i http://127.0.0.1:8020/ready
```

## What To Record

- time of issue
- observed symptom
- failing command or URL
- status code
- relevant log line
- suspected cause
- action taken
- verification result

This is more important than guessing. A support engineer should show the evidence trail.
