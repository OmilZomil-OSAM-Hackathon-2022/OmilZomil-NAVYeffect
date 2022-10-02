# syntax=docker/dockerfile:1
FROM node:14

# 작업 폴더 설정
WORKDIR /home
RUN mkdir "frontend"
WORKDIR /home/frontend/

ENTRYPOINT ["sh", "/home/frontend/entrypoint.sh"]
