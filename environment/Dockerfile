FROM python:3.12-slim@sha256:ac212230555ffb7ec17c214fb4cf036ced11b30b5b460994376b0725c7f6c151

RUN pip install --no-cache-dir pytest==8.4.1 pytest-json-ctrf==0.3.5

WORKDIR /app

COPY access.log /app/access.log
