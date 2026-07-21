FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
	PYTHONUNBUFFERED=1 \
	PIP_NO_CACHE_DIR=1 \
	PYTHONPATH=/app

WORKDIR /app

RUN groupadd --system app && useradd --system --gid app --create-home app

COPY --chown=app:app requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY --chown=app:app models/chrun_model ./models/chrun_model

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=5s --start-period=30s --retries=3 CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8000/')"

USER app

CMD ["uvicorn", "models.chrun_model.api:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "1"]