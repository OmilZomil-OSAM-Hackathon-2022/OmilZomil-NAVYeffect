# syntax=docker/dockerfile:1
FROM python:3.9

RUN apt-get update -y && \
    apt-get install build-essential cmake pkg-config -y

RUN pip install dlib==19.9.0

WORKDIR omil
CMD ["sh", "entrypoint.sh"]