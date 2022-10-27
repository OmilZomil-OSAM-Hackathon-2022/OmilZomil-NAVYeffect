#/bin/bash

# 스크립트 설명: 서비스를 중지하기 위한 스크립트
# DB 포함 모든 컨테이너를 일시 중지
args_1=$1
PROJECT_NAME=${args_1:-omil}

echo [+] Checking build files...
if [ -f .env.lock ] ; then
    :
else
    echo "[!] Please run 'build.sh' first!"
    exit
fi

echo [+] Stopping docker container

sudo docker-compose -p ${PROJECT_NAME} --env-file .env.lock stop