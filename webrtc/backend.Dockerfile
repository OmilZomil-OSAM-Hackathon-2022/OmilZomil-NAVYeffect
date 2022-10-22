# syntax=docker/dockerfile:1
FROM python:3.9
ENV PYTHONUNBUFFERED=1

# 작업 폴더 설정
WORKDIR /backend
COPY ./webrtc/backend /backend
COPY ./webrtc/ai /backend/src/app/ai
COPY ./omilzomil/backend/src  /backend/src/app/omil
COPY ./omilzomil/backend/src/app/models  /backend/src/app/models

# 
RUN mkdir -p /omil_image/queue
RUN mkdir -p /omil_image/inspection
RUN mkdir -p /omil_image/detail

# 가중치 파일 다운로드
RUN wget -q https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v3_optimal/yolov4.weights
RUN mkdir -p /ai/OZEngine/person_detectors/refs/weights/
RUN mv yolov4.weights /ai/OZEngine/person_detectors/refs/weights/yolov4.weights

# 기타 프로그램 설치
RUN apt-get clean
RUN apt-get update -y && \
    apt-get install build-essential cmake pkg-config -y
RUN apt-get -y install libgl1-mesa-glx

RUN apt-get update
RUN apt-get install -y libgl1-mesa-glx

# 라이브러리 설치
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# 개발용으로 entrypoint.sh 파일를 연결
CMD ["sh", "/backend/entrypoint.sh"]