# syntax=docker/dockerfile:1
FROM python:3.9

RUN apt-get update -y && \
    apt-get install build-essential cmake pkg-config -y
RUN apt-get install ffmpeg libsm6 libxext6  -y

RUN pip install --upgrade pip
COPY requirements.txt /omil/requirements.txt
RUN pip install -r /omil/requirements.txt

WORKDIR /omil


CMD ["sh", "entrypoint.sh"]