# NEXT_STEPS.md

## Current Recommendation

Slice 3 is complete. The project has been pushed to GitHub and the GitHub Actions CI workflow has passed.

Do not add deployment yet.

## Slice 3 Verification

Local tests:

```bash
cd <project-folder>
source .venv/bin/activate
pytest
```

Review the workflow:

```bash
cat .github/workflows/ci.yml
```

The workflow should:

- check out the repository
- set up Python 3.12
- install dependencies
- run pytest

GitHub CI should also show a passing run for the latest commit.

## What CI Means

CI means:

```text
GitHub automatically runs checks after code changes.
```

For this project, CI answers:

```text
Can GitHub install the project and run the tests successfully?
```

CI does not mean:

```text
The app is deployed.
The app is production-ready.
The app is monitored.
```

## What To Understand Before Deployment Docs

- `push` means the workflow runs when code is pushed to GitHub.
- `pull_request` means the workflow runs when a PR is opened or updated.
- `actions/checkout` gives the workflow access to the repo files.
- `actions/setup-python` installs the requested Python version.
- `pytest` is the actual test command.
- A green CI run means tests passed in GitHub's runner.
- A red CI run means something failed and the logs must be read.

## Slice 4: Deployment, Secrets, Rollback, Redeploy Docs

Next implementation should add documentation only:

- deployment checklist
- required environment variables
- health and readiness verification after deploy
- secrets-handling notes
- rollback checklist
- redeploy checklist
- support case for CI failure or readiness failure

Do not add:

- cloud hosting
- paid services
- Kubernetes
- Terraform
- database
- authentication
- frontend
