# syntax=docker/dockerfile:1
FROM python:3.9
ENV PYTHONUNBUFFERED=1

# 작업 폴더 설정
WORKDIR /home
RUN mkdir "backend"
WORKDIR /home/backend/

# 파이썬 라이브러리 설치
RUN pip install --upgrade pip
RUN pip install fastapi
RUN pip install "uvicorn[standard]"
RUN pip install "python-jose[cryptography]"
RUN pip install "passlib[bcrypt]"
RUN pip install python-multipart
RUN pip install sqlalchemy
RUN pip install psycopg2
RUN pip install pymysql
RUN pip install pytest
RUN pip install requests

# dockerfile 기준으로 설치
# COPY ./deploy/requirements.txt /home/backend 
# RUN pip install -r requirements.txt

# 개발용으로 entrypoint.sh 파일를 연결
CMD ["sh", "/home/backend/entrypoint.sh"]
