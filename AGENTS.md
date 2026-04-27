# AGENTS.md

## Project Purpose

Cloud API + CI/CD Lab is a junior-friendly portfolio project for cloud/application support readiness.

It builds on Project 1, `b2b-saas-support-lab`, but has a different focus:

- Docker
- GitHub Actions
- CI test output
- service health checks
- environment variables
- deployment documentation
- basic cloud-readiness
- secrets handling
- rollback and redeploy notes

The goal is not to look like a senior platform engineer.

The goal is to prove practical readiness for roles like:

- Junior Technical Support Engineer
- Application Support Specialist
- Product Support Engineer
- Cloud Support Engineer
- API Support Engineer
- Junior Integration Specialist
- SaaS Technical Support Specialist

## Current State

The project plan has been reviewed and Slices 1-5 are implemented:

- local FastAPI app
- environment-based config
- `/health`, `/config`, and `/ready`
- pytest coverage
- Dockerfile
- GitHub Actions CI
- deployment-readiness documentation
- secrets-handling notes
- rollback/redeploy notes
- support cases and runbook
- career package
- interview practice guide

Do not add more application features unless the next task explicitly asks for them.

The current priority is portfolio packaging, interview practice, and small verification polish.

## Build Direction

Keep the project simple and support-focused.

Prefer:

- one small FastAPI service
- local development first
- clear environment configuration
- `GET /health` for process health
- `GET /ready` for configuration readiness
- pytest tests that run locally and in CI
- Docker for repeatable local runs
- GitHub Actions for automated tests
- deployment documentation, not paid deployment by default
- support cases and runbooks that explain failures clearly

Avoid:

- Kubernetes
- microservices
- complex authentication
- frontend work
- paid cloud services
- real production secrets
- fake production claims
- broad rewrites

## Engineering Rules

- Make small, reversible changes.
- Add tests for new behavior.
- Keep setup commands copy-pasteable.
- Document every important troubleshooting lesson.
- Prefer understandable code over clever abstractions.
- Do not add external services unless explicitly approved.
- Do not commit real secrets.
- Keep `.env.example` safe and non-secret.

## Portfolio Rule

This project should show that the owner can:

- run a local API
- read API responses
- understand health checks
- diagnose environment configuration mistakes
- read local and CI test output
- explain Docker basics honestly
- explain CI/CD basics honestly
- understand safe secrets handling at a beginner level
- write practical deployment, rollback, and redeploy notes
