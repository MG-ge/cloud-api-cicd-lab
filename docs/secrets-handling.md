# Secrets Handling Notes

This project does not use real production secrets.

The goal is to show safe habits around configuration and secret values.

## Rules

- Commit `.env.example` with variable names and fake values only.
- Do not commit `.env`.
- Do not paste real secrets into README files, support cases, logs, screenshots, or GitHub issues.
- Do not print raw environment dumps.
- Do not expose secret-like values from `/config`.
- Use GitHub Actions secrets only by name if secrets are needed later.

## Safe Example

```text
REQUIRED_DEPENDENCY_URL=https://example.invalid/dependency
```

This is safe because it is a fake documentation value.

## Unsafe Example

```text
EXAMPLE_TOKEN=<do-not-commit-real-value>
```

This should never be committed or pasted into a support case.

## Local Development

Local developers may create `.env` for their own machine, but `.env` must stay ignored by git.

Check ignore rules:

```bash
cat .gitignore
```

Check for accidental secret-looking text before committing:

```bash
rg -n "SECRET|TOKEN|PASSWORD|API_KEY" .
```

If a real secret is committed by mistake, removing it in a later commit is not enough. The secret should be rotated in the system where it was created.

## GitHub Actions

This project's current CI workflow does not need secrets.

If secrets are needed later, the workflow should reference secret names like this:

```yaml
env:
  EXAMPLE_API_TOKEN: ${{ secrets.EXAMPLE_API_TOKEN }}
```

The workflow should never contain the real secret value.
