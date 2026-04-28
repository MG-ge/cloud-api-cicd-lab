# Career Package: Project 2

Project: Cloud API + CI/CD Lab

GitHub repo: https://github.com/MG-ge/cloud-api-cicd-lab

This wording is for CV, GitHub, portfolio, LinkedIn, and interview preparation. It is intentionally junior-credible.

Do not describe this as production experience.

## Short Project Summary For Recruiters

Cloud API + CI/CD Lab is a junior portfolio project showing cloud/application support readiness with a small FastAPI service, health/readiness checks, Docker, GitHub Actions CI, safe config handling, support cases, and runbooks.

## Technical Summary

The project includes:

- Python and FastAPI
- `/health`, `/config`, and `/ready` endpoints
- environment-based configuration
- pytest tests
- Dockerfile
- Docker build/run documentation
- GitHub Actions pytest job
- GitHub Actions Docker build job
- deployment-readiness notes
- secrets-handling notes
- rollback/redeploy notes
- support cases and runbook

It does not include real cloud deployment or production operations.

## Support, Application, And Cloud Relevance

This project is relevant for junior support roles because it shows:

- API response reading
- HTTP status-code reasoning
- health versus readiness troubleshooting
- environment variable investigation
- safe config exposure
- Docker basics
- CI result reading
- deployment-readiness thinking
- clear support documentation

Target roles:

- Junior Technical Support Engineer
- SaaS Technical Support Specialist
- Application Support Specialist
- Product Support Engineer
- Cloud Support Engineer, junior level
- API Support Engineer
- Junior Integration Specialist
- Sovellusasiantuntija

## English CV Bullets

**Cloud API + CI/CD Lab**  
Junior portfolio project for cloud/application support readiness using FastAPI, Docker, GitHub Actions, pytest, and support documentation.

- Built a small FastAPI service with `/health`, `/config`, and `/ready` endpoints to demonstrate process health, safe config output, and readiness checks.
- Packaged the API with Docker and added GitHub Actions CI to run pytest and build the Docker image.
- Documented support workflows for readiness failures, Docker port issues, CI failures, secrets handling, and rollback/redeploy checks.

## Finnish CV Bullets

**Cloud API + CI/CD Lab**  
Junior-tason portfolioprojekti pilvi- ja sovellustuen perusteisiin FastAPIlla, Dockerilla, GitHub Actionsilla, pytestilla ja tukidokumentaatiolla.

- Toteutin pienen FastAPI-palvelun, jossa on `/health`, `/config` ja `/ready` -endpointit prosessin tilan, turvallisen konfiguraation ja readiness-tarkistusten harjoitteluun.
- Paketoin API:n Dockerilla ja lisäsin GitHub Actions -CI:n, joka ajaa pytest-testit ja buildaa Docker-imagen.
- Dokumentoin tukitilanteita, kuten readiness-virheitä, Docker-porttiongelmia, CI-virheitä, salaisuuksien käsittelyä sekä rollback/redeploy-tarkistuksia.

## English GitHub Or Portfolio Description

Cloud API + CI/CD Lab is a junior cloud/application support portfolio project.

It demonstrates a small FastAPI service with `/health`, `/config`, and `/ready` endpoints, environment-based configuration, Docker build/run basics, GitHub Actions CI for pytest and Docker image build, and support documentation for readiness failures, CI failures, secrets handling, and rollback/redeploy checks.

This is a learning and portfolio project, not production experience.

## Finnish GitHub Or Portfolio Description

Cloud API + CI/CD Lab on junior-tason pilvi- ja sovellustuen portfolioprojekti.

Se näyttää pienen FastAPI-palvelun, jossa on `/health`, `/config` ja `/ready` -endpointit, ympäristömuuttujiin perustuva konfiguraatio, Docker build/run -perusteet, GitHub Actions -CI pytest-testeille ja Docker-imagen buildille sekä tukidokumentaatiota readiness-virheistä, CI-virheistä, salaisuuksien käsittelystä ja rollback/redeploy-tarkistuksista.

Tämä on oppimis- ja portfolioprojekti, ei tuotantokokemusta.

## Interview Talking Points

- I can explain why `/health` and `/ready` are different.
- I can explain why `/config` only returns safe values.
- I can show how a missing environment variable makes `/ready` return `503`.
- I can explain what Docker build/run proves.
- I can explain what GitHub Actions CI proves and what it does not prove.
- I can walk through a support case using symptom, command, result, likely cause, resolution, and prevention.
- I can explain why this project is intentionally not production experience.

## Things I Must Be Able To Explain

### Health vs Readiness

`/health` means the API process can respond.

`/ready` means required configuration is present.

The app can be healthy but not ready.

### Safe Config Endpoint

`/config` returns only safe values:

- app name
- environment name
- app version
- feature flag value

It does not expose `REQUIRED_DEPENDENCY_URL`, secrets, tokens, passwords, or raw environment dumps.

### Environment Variables

Environment variables let the same app run with different runtime configuration.

In this project, `REQUIRED_DEPENDENCY_URL` controls readiness behavior.

### Docker Build And Run

Docker build proves the image can be created from the Dockerfile.

Docker run proves the container can start and respond through a mapped port.

Docker does not prove production readiness.

### GitHub Actions CI

GitHub Actions runs checks after code changes.

In this project, CI runs:

- pytest
- Docker image build

CI does not mean the app is deployed, monitored, secured, or production-ready.

### Why This Is Not Production Experience

This is a local portfolio lab.

It does not include:

- real customers
- real cloud deployment
- production secrets
- production monitoring
- alerting
- autoscaling
- incident response tooling

It should be presented as hands-on learning and portfolio proof.

## AI Usage Note

AI tools were used for planning, implementation suggestions, refactoring, test-case generation, and documentation support.

Final code was reviewed, run locally, tested, debugged, and documented by me.
