# Case 002: Docker Container Runs But Port Is Not Reachable

## Symptom

The Docker container appears to be running, but `curl` cannot reach the API from the host machine.

## Commands Used

```bash
docker ps
curl -s -i http://127.0.0.1:8020/health
docker logs cloud-api-cicd-lab
```

## Observed Result

The container is running, but the host request fails or connects to the wrong port.

## Likely Cause

The container was started without the correct port mapping.

The app listens inside the container, but the host cannot reach it unless the port is published with `-p`.

## Resolution

Stop the container:

```bash
docker stop cloud-api-cicd-lab
```

Run it with the expected port mapping:

```bash
docker run --rm --name cloud-api-cicd-lab \
  -p 8020:8020 \
  -e REQUIRED_DEPENDENCY_URL=https://example.invalid/dependency \
  cloud-api-cicd-lab:local
```

Verify:

```bash
curl -s -i http://127.0.0.1:8020/health
curl -s -i http://127.0.0.1:8020/ready
```

## Prevention

- Document the host port and container port clearly.
- Use the same port in README examples.
- Check `docker ps` before assuming the app failed.
