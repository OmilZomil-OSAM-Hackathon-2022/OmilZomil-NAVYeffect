#! /bin/bash

# .env 파일이 있는지 검증
if [ ! -e ".env.private" ]; then
	echo ".env.private 파일이 없습니다."
    echo ".env.publoc 를 복사하여 만들어 주시길 바랍니다."
    exit
fi

DIR_PATH=`pwd`

# 환경변수 파일 정의
cat .env.private > .env.lock
echo BACKEND_DIR_PATH="$DIR_PATH"/backend >> .env.lock
echo FRONTEND_DIR_PATH="$DIR_PATH"/frontend >> .env.lock

# 기존 컨테이너 지우기
echo [+] remove container
sudo docker-compose --env-file .env.lock down

# docker 빌드
echo [+] docker build
sudo docker-compose --env-file .env.lock build


# DB 실행
echo [+] make db
sudo docker-compose --env-file .env.lock up -d db

# DB 테이블 만들기
echo [+] make db tables
sudo docker-compose --env-file .env.lock run web python src/initial_data.py

# 프론트 빌드
echo [+] frontend build
sudo docker-compose --env-file .env.lock up -d vue

# ssl 만들기
# .env 파일이 있는지 검증
if [ ! -e "./backend/key.pem" ]; then
    echo [+] key.pem 파일이 없어 생성합니다.
    cd ./backend
    openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
fi

# docker 빌드 캐쉬 제거
# echo [+] remove build cache
# sudo docker builder prune 