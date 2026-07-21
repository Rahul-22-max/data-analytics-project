# data-analytics-project

## Day 11 Progress

- Dockerized the FastAPI churn prediction API for local and portable deployment.
- Added a production-ready Dockerfile that runs the app with Uvicorn on a slim Python base image.
- Added a `.dockerignore` and `.gitignore` to keep the build context and workspace clean.
- Reduced the root requirements file to only the runtime dependencies needed by the API.
- Documented the build, run, Swagger testing, and common Docker troubleshooting steps.

### Docker Workflow

Build the image from the repository root:

```powershell
docker build -t churn-api .
```

Run the container:

```powershell
docker run --rm -p 8000:8000 --name churn-api churn-api
```

Open Swagger UI at `http://localhost:8000/docs`, click `POST /predict`, choose `Try it out`, paste a full customer payload, and execute the request to verify the containerized API.