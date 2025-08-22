# Dockerfile
FROM python:3.11-slim

WORKDIR /app

ENV PIP_NO_CACHE_DIR=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

COPY requirements.txt ./
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . .

CMD ["python", "src/train.py", "--epochs", "1"]