# NEXT_STEPS.md

## Current Recommendation

Slice 5 is complete. The project now has career-package text and interview practice material.

Do not add real cloud hosting yet.

## Current Verification

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

Documentation to review:

```bash
cat docs/deployment-readiness.md
cat docs/secrets-handling.md
cat docs/rollback-redeploy.md
cat runbooks/cloud-api-support-runbook.md
cat docs/career-package-project-2.md
cat docs/project-2-interview-practice.md
ls support-cases
```

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

## What To Understand Now

- `push` means the workflow runs when code is pushed to GitHub.
- `pull_request` means the workflow runs when a PR is opened or updated.
- `actions/checkout` gives the workflow access to the repo files.
- `actions/setup-python` installs the requested Python version.
- `pytest` is the actual test command.
- A green CI run means tests passed in GitHub's runner.
- A red CI run means something failed and the logs must be read.
- `/health` means the process can respond.
- `/ready` means required configuration is present.
- Docker packaging is not the same as deployment.
- Deployment docs are not the same as a real deployed service.
- Secrets should be referenced by name, not written into files or chat.

## Next: Practice Before More Features

Before adding more code, practice:

- 60-second project explanation
- `/health` versus `/ready`
- environment variables and readiness
- Docker port mapping
- GitHub Actions CI
- one support case
- one honest limitation

After practice, choose one:

1. Add Project 2 to CV and LinkedIn.
2. Add a Docker build check to CI as a small technical improvement.
3. Start a no-cost deployment simulation doc.

Recommended next step:

```text
Test the owner with interview questions before adding more features.
```

Do not add:

- cloud hosting
- paid services
- Kubernetes
- Terraform
- database
- authentication
- frontend
