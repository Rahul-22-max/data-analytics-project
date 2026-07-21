# Docker Deployment Report

## Day 11 Goal

Package the FastAPI churn prediction service into a production-ready Docker image that remains lightweight enough for a student laptop and works on Windows with Docker Desktop.

## What Changed

- Replaced the original Dockerfile with a slim Python image.
- Added a non-root runtime user.
- Kept the API import path stable with `PYTHONPATH=/app`.
- Copied only the FastAPI source and saved model required at runtime.
- Added a `HEALTHCHECK` so the container can report whether the API is responding.
- Added `.dockerignore` to keep the build context small.
- Added `.gitignore` to keep local-only files out of version control.
- Trimmed `requirements.txt` to only the runtime dependencies used by the API.

## Build Command

Run these commands from the repository root in PowerShell:

```powershell
docker build -t churn-api .
```

## Run Command

Start the container and publish port 8000:

```powershell
docker run --rm -p 8000:8000 --name churn-api churn-api
```

If port 8000 is already in use, map a different host port:

```powershell
docker run --rm -p 8001:8000 --name churn-api churn-api
```

## Testing the API in Swagger

1. Open `http://localhost:8000/docs` in a browser.
2. Expand `POST /predict`.
3. Click `Try it out`.
4. Paste a JSON payload that includes every required customer feature field.
5. Click `Execute`.
6. Confirm the response contains `prediction` and `churn_probability`.

Use the Swagger schema to fill the full payload because the request body contains many one-hot encoded feature fields.

## Why This Dockerfile Is Production-Ready

- Uses `python:3.11-slim` to reduce image size.
- Installs only runtime dependencies.
- Runs the application as a non-root user.
- Avoids writing `.pyc` files and keeps logs unbuffered.
- Keeps the container focused on the API instead of bundling training assets and reports.

## Common Docker Build Errors and Fixes

### 1. `ModuleNotFoundError: No module named 'models'`

Cause: The container is not running from the repository root or the Python path does not include `/app`.

Fix: Keep `WORKDIR /app`, set `PYTHONPATH=/app`, and build from the repo root.

### 2. `FileNotFoundError: models/chrun_model/churn_model.pkl`

Cause: The saved model was not copied into the image or it was excluded by `.dockerignore`.

Fix: Copy `models/chrun_model` into the image and make sure the `.pkl` file is not ignored.

### 3. `Could not find a version that satisfies the requirement ...`

Cause: A dependency version is incompatible with the selected Python base image.

Fix: Use a supported Python base image such as `python:3.11-slim` and keep the runtime dependency list minimal.

### 4. `port is already allocated`

Cause: Another process is already using host port 8000.

Fix: Use a different host port, for example `-p 8001:8000`.

### 5. Docker Desktop cannot access the repository files on Windows

Cause: The drive or folder is not shared with Docker Desktop.

Fix: Ensure Docker Desktop is running and the project drive is available to Docker Desktop file sharing or WSL2 integration.

## Windows Notes

- Run the commands from PowerShell in the repository root.
- Keep Docker Desktop running before building or starting the container.
- Open Swagger at `http://localhost:8000/docs` after the container starts.
- If you move the project to another drive, verify that Docker Desktop can still see that path.

## Suggested Commit Message

`Day 11: Dockerize FastAPI churn API with production-ready container setup`
