# Using base image provided by nginx unit

# nginx unit python
FROM nginx/unit:1.22.0-python3.9

# 라이브러리 설치
WORKDIR /backend
COPY requirements.txt /backend/requirements.txt
RUN pip install -r requirements.txt

# 설정값 입력
COPY deploy/config.json /docker-entrypoint.d/config.json

# 소스코드는 volume으로 연결
