# Installation Guide

## Clone Repository

```bash
git clone <repository-url>
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Start API

```bash
uvicorn backend.app.main:app --reload
```

## Open Swagger

http://127.0.0.1:8000/docs