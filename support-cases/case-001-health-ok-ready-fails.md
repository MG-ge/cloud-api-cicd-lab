# Case 001: Health Is OK But Readiness Fails

## Symptom

The API process is running, but the readiness check returns `503`.

## Commands Used

```bash
curl -s -i http://127.0.0.1:8020/health
curl -s -i http://127.0.0.1:8020/ready
```

## Observed Result

`/health` returns `200`.

`/ready` returns `503`.

## Likely Cause

`REQUIRED_DEPENDENCY_URL` is missing or blank.

The app is alive, but it is not ready according to its required configuration check.

## Resolution

Restart the app with the required environment variable:

```bash
REQUIRED_DEPENDENCY_URL=https://example.invalid/dependency PORT=8020 scripts/run-dev.sh
```

Then verify:

```bash
curl -s -i http://127.0.0.1:8020/ready
```

Expected result:

```text
HTTP/1.1 200 OK
```

## Prevention

- Document required environment variables before deployment.
- Check `/ready` after startup, not only `/health`.
- Keep `/health` and `/ready` meanings separate.
