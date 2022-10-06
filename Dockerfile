FROM python:3.9 as backend-builder


RUN pip install -U pip setuptools wheel && \
    pip install poetry
    
# 작업 폴더 지정
# WORKDIR /app
# RUN mkdir "backend"
WORKDIR /app/backend/

# 가상환경 설정
ENV POETRY_VIRTUALENVS_IN_PROJECT=true

COPY backend/pyproject.toml backend/poetry.lock ./
RUN poetry install --no-dev
COPY backend/src/ app/



# nginx
FROM nginx/unit:1.26.1-python3.9

WORKDIR /app

COPY --from=backend-builder /app/backend backend

COPY deploy/config.json /docker-entrypoint.d/config.json