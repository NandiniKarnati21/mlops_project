
FROM python:3.10-slim

WORKDIR /app

COPY pyproject.toml README.md ./
COPY src ./src

RUN pip install --upgrade pip
RUN pip install .

ENV PORT=8080

CMD ["uvicorn", "mlops_project.app:app", "--host", "0.0.0.0", "--port", "8080"]
