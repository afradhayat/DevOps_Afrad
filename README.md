# REST API Development & Deployment

## Part A: Develop & Deploy a REST API

This project implements a basic REST API with automated deployment using Docker and GitHub Actions CI/CD pipeline.

---

### 1. Develop a REST API

- Implemented using **FastAPI** (Python).
- API Endpoints:
  - **`/api/hello`**  
    Returns JSON data containing:
    ```json
    {
      "hostname": "server1",
      "datetime": "YYMMDDHHmm",
      "version": "version",
      "weather": {
        "dhaka": {
          "temperature": "14",
          "temp_unit": "c"
        }
      }
    }
    ```
    - Fetches current weather data for Dhaka from a free third-party weather API (`open-meteo.com`).
  - **`/api/health`**  
    Health check endpoint that verifies the API is reachable and confirms third-party weather API availability.

---

### 2. Containerize the Application

- Created a `Dockerfile` to containerize the FastAPI application.
- Dockerfile is optimized for security and performance using best practices.
- Added `docker-compose.yaml` for easy build and local development.

---

### 3. Version Control & CI/CD Pipeline

- Public GitHub repository created: [afradhayat/fastapi-weather-api](https://github.com/afradhayat/fastapi-weather-api)
- CI/CD pipeline configured with GitHub Actions to automate deployment:
  - Triggered on new **GitHub Release** creation.
  - Builds Docker image tagged with the release version.
  - Validates that the version returned by `/api/hello` matches the release tag.
  - Pushes the Docker image to Docker Hub (`afradaidid/fastapi-weather-api`).
  - Deploys the new version with **zero downtime** by safely stopping the old container and running the new one with restart policies.

---

### How to Use

1. Clone the repository.
2. Build and run locally with Docker or `docker-compose`.
3. Create a GitHub Release to trigger automated CI/CD deployment.
4. Access the API at `http://<host>:8000/api/hello` and `http://<host>:8000/api/health`.

---

### Technologies Used

- FastAPI (Python)
- Docker & Docker Compose
- GitHub Actions for CI/CD
- Open-Meteo public API for weather data

---

### Notes

- For security, Docker Hub credentials should ideally be stored in GitHub Secrets. [ For permission purpose, it has been added on the workflow for testing purpose]
- The version check currently warns on mismatches but can be configured to fail the pipeline.
- Zero downtime achieved using Docker container replacement.
- Docker repository Link: https://hub.docker.com/r/afradaidid/fastapi-weather-api
---

Thank you for reviewing this project!  
Feel free to raise issues or contribute.

