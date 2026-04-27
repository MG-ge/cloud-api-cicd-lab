# NEXT_STEPS.md

## Current Recommendation

Stop Project 2.

Project 2 v1 is complete and should not keep expanding.

## Why Project 2 Is Complete

Project 2 now proves the intended junior cloud/application support readiness skills:

- local FastAPI app
- environment-based configuration
- `/health`, `/config`, and `/ready`
- safe non-secret config output
- pytest coverage
- Docker build and run basics
- GitHub Actions test job
- GitHub Actions Docker build job
- deployment-readiness documentation
- secrets-handling notes
- rollback/redeploy notes
- support cases
- runbook
- known limitations
- AI usage note

It does not claim production experience or real cloud deployment.

## Do Not Add To Project 2 Now

- Kubernetes
- frontend
- authentication
- database
- SaaS ticket system
- paid cloud hosting
- real production secrets
- production monitoring stack
- broad refactors

## Project 3: Observability + Incident Response Lab

Next project should be:

```text
Project 3: Observability + Incident Response Lab
```

Goal:

```text
Prove junior-ready troubleshooting around logs, metrics, alerts, incidents, runbooks, and post-incident review.
```

Project 3 should build on Project 2 without turning Project 2 into a larger system.

Suggested Project 3 scope:

- structured application logs
- request IDs or correlation IDs
- simple metrics endpoint or metrics simulation
- fake incident scenarios
- alert investigation notes
- incident timeline
- postmortem document
- runbook for common failures
- local-only or no-cost tooling

Keep it junior-credible.

Do not start Project 3 until its plan is written and reviewed.

## What To Practice Before Project 3

- Explain `/health` versus `/ready`.
- Explain what CI proves and does not prove.
- Explain what Docker proves and does not prove.
- Explain one Project 2 support case.
- Explain one honest limitation of Project 2.
