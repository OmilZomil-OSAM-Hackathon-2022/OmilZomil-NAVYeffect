# syntax=docker/dockerfile:1
FROM python:3.9
ENV PYTHONUNBUFFERED=1

# 작업 폴더 설정
WORKDIR /backend

# 이미지 및 ai 작업에 필요한 프로그램 설치
RUN apt-get update -y && \
    apt-get install build-essential cmake pkg-config -y
RUN apt-get -y install libgl1-mesa-glx

# 라이브러리 설치
RUN pip install --upgrade pip
COPY requirements.txt /backend/requirements.txt
RUN pip install -r requirements.txt

# 개발용으로 entrypoint.sh 파일를 연결
CMD ["sh", "/backend/entrypoint.sh"]