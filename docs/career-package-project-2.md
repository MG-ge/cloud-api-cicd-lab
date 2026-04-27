# Career Package: Project 2

Project: Cloud API + CI/CD Lab

GitHub repo: https://github.com/MG-ge/cloud-api-cicd-lab

This wording is for CV, LinkedIn, GitHub, and interview preparation. It is intentionally junior-appropriate.

Do not describe this as production experience.

## 1. English CV Project Entry

**Cloud API + CI/CD Lab**  
Junior portfolio project for cloud/application support readiness using FastAPI, Docker, GitHub Actions, pytest, and support documentation.

- Built a small FastAPI service with `/health`, `/config`, and `/ready` endpoints to demonstrate process health, safe config output, and configuration readiness.
- Packaged the API with Docker and added GitHub Actions CI to run pytest automatically on push and pull request.
- Documented practical support workflows for readiness failures, Docker port issues, CI failures, secrets handling, and rollback/redeploy checks.

## 2. Finnish CV Project Entry

**Cloud API + CI/CD Lab**  
Junior-tason portfolioprojekti pilvi- ja sovellustuen perusteisiin FastAPIlla, Dockerilla, GitHub Actionsilla, pytestilla ja tukidokumentaatiolla.

- Toteutin pienen FastAPI-palvelun, jossa on `/health`, `/config` ja `/ready` -endpointit prosessin tilan, turvallisen konfiguraation ja readiness-tarkistuksen harjoitteluun.
- Paketoin API:n Dockerilla ja lisäsin GitHub Actions -CI:n, joka ajaa pytest-testit automaattisesti push- ja pull request -tilanteissa.
- Dokumentoin käytännön tukitilanteita, kuten readiness-virheitä, Docker-porttiongelmia, CI-virheitä, salaisuuksien käsittelyä sekä rollback/redeploy-tarkistuksia.

## 3. LinkedIn Project Description In English

Cloud API + CI/CD Lab is a junior portfolio project focused on cloud and application support readiness.

I built a small FastAPI service with health, safe config, and readiness endpoints. The app reads configuration from environment variables, avoids exposing sensitive config values, runs locally and in Docker, and uses GitHub Actions to run pytest automatically.

The project also includes support-focused documentation: deployment-readiness notes, secrets-handling notes, rollback/redeploy notes, support cases, and a runbook. It is a learning project, not production experience.

## 4. LinkedIn Project Description In Finnish

Cloud API + CI/CD Lab on junior-tason portfolioprojekti, jossa harjoitellaan pilvi- ja sovellustuen perusteita.

Rakensin pienen FastAPI-palvelun, jossa on health-, config- ja readiness-endpointit. Sovellus lukee asetuksia ympäristömuuttujista, ei paljasta arkaluonteisia konfiguraatioarvoja, toimii paikallisesti ja Dockerissa sekä ajaa pytest-testit GitHub Actions -CI:ssä.

Projekti sisältää myös tukityöhön liittyvää dokumentaatiota: deployment-readiness-muistiinpanot, salaisuuksien käsittelyn ohjeet, rollback/redeploy-ohjeet, support case -tapaukset ja runbookin. Tämä on oppimis- ja portfolioprojekti, ei tuotantokokemusta.

## 5. Short GitHub Repo Description

Junior cloud/application support portfolio lab with FastAPI, Docker, GitHub Actions CI, health/readiness checks, and support runbooks.

## 6. Recruiter Keywords

- Application Support
- Cloud Support
- SaaS Support
- FastAPI
- Docker
- GitHub Actions
- CI/CD basics
- pytest
- REST API
- health check
- readiness check
- environment variables
- secrets handling
- rollback/redeploy
- support runbook

## 7. Interview Talking Points

- I can explain why `/health` and `/ready` are different.
- I can show how a missing environment variable makes `/ready` return `503`.
- I can explain what Docker does for this project and what it does not do.
- I can explain what GitHub Actions CI proves and what it does not prove.
- I can walk through support cases using symptom, command, result, likely cause, resolution, and prevention.
- I can explain why `/config` avoids exposing `REQUIRED_DEPENDENCY_URL`.
- I can be honest that this is not a real cloud deployment or production system.

## 8. Honest AI Usage Explanation

I used AI as a mentor and coding assistant while building this portfolio lab.

I am responsible for understanding the code, running the commands, reading the test and CI output, explaining the endpoints, and describing the project limitations honestly.

I would present this as guided learning and hands-on practice, not as production work.
