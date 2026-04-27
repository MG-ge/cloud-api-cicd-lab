# Case 003: CI Fails After A Code Change

## Symptom

GitHub Actions shows a failed CI run after a push or pull request.

## Commands Used

```bash
pytest
gh run list --repo MG-ge/cloud-api-cicd-lab --limit 5
gh run view --repo MG-ge/cloud-api-cicd-lab --log
```

## Observed Result

The GitHub Actions workflow fails during the `Run tests` step.

## Likely Cause

A code change broke an expected endpoint response or configuration behavior.

CI is doing its job: it catches the break before the project is shared further.

## Resolution

1. Read the failed pytest output in GitHub Actions.
2. Reproduce locally with:

```bash
pytest
```

3. Fix the smallest cause.
4. Run tests locally again.
5. Push the fix.
6. Confirm GitHub Actions passes.

## Prevention

- Keep endpoint behavior covered by tests.
- Run `pytest` before pushing.
- Treat red CI as a signal to read logs, not as a mystery.
- Do not skip failing tests to make CI green.
