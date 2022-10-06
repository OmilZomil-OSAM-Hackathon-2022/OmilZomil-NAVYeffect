# Using base image provided by nginx unit

# nginx unit python
FROM nginx/unit:1.22.0-python3.9

# 라이브러리 설치
COPY backend/requirements.txt /fastapi/requirements.txt
RUN pip install -r /fastapi/requirements.txt

# 설정값 입력
COPY deploy/config.json /docker-entrypoint.d/config.json

# 소스코드 복사
COPY backend/src /fastapi