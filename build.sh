#! /bin/bash
# 스크립트 설명: 서비스를 시작하기전 필요한 파일들을 생성
# 프론트 빌드도 해당 스크립트에서 동작


# ============== 기타 필요한 파일 생성 
args_1=$1
PROJECT_NAME=${args_1:-omil}

# .env 파일이 있는지 검증
if [ ! -e ".env.private" ]; then
	echo ".env.private 파일이 없습니다."
    echo ".env.public 를 복사하여 만들어 주시길 바랍니다."
    exit
fi

mkdir -p ./image/queue
mkdir -p ./image/inspection
mkdir -p ./image/detail


DIR_PATH=`pwd`

# 환경변수 파일 정의
cat .env.private > .env.lock
echo DIR_PATH="$DIR_PATH" >> .env.lock
echo OMIL_DIR_PATH="$DIR_PATH"/omilzomil/backend >> .env.lock
echo WEBRTC_DIR_PATH="$DIR_PATH"/webrtc/backend >> .env.lock



# ssl 만들기 - .pem 파일이 있는지 검증 => 없으면 생성
if [ ! -e "./omilzomil/backend/cert.pem" ]; then
    echo [+] omilzomil 에 cert.pem 파일이 없어 생성합니다.
    openssl req -x509 -newkey rsa:4096 -nodes -out ./omilzomil/backend/cert.pem -keyout ./omilzomil/backend/key.pem -days 365
    cd $DIR_PATH
fi
if [ ! -e "./webrtc/backend/cert.pem" ]; then
    echo [+] webrtc 에 cert.pem 파일이 없어 생성합니다.
    openssl req -x509 -newkey rsa:4096 -nodes -out ./webrtc/backend/cert.pem -keyout ./webrtc/backend/key.pem -days 365
fi

# ============== 기존 컨테이너 삭제

# 기존 컨테이너 지우기
echo [+] remove container
sudo docker-compose -p ${PROJECT_NAME} --env-file .env.lock down --remove-orphans

# ============== docker 재 build

# docker 빌드
echo [+] docker build
sudo docker-compose -p ${PROJECT_NAME} --env-file .env.lock build

# 프론트 빌드
echo [+] frontend build
sudo docker-compose -p ${PROJECT_NAME} --env-file .env.lock up omilzomil_front
sudo docker-compose -p ${PROJECT_NAME} --env-file .env.lock up webrtc_front

echo [+] frontend build 대기

while sudo docker-compose -p ${PROJECT_NAME} --env-file .env.lock ps --services --filter status=running | grep -q 'front'; do
    echo `sudo docker-compose --env-file .env.lock ps --services --filter status=running`
    wait_time=`date +%T`
    echo frontend $wait_time
    sleep 1;
done;

# ============== DB 구축

# DB 실행
echo [+] make db
sudo docker-compose -p ${PROJECT_NAME} --env-file .env.lock up -d db

# DB 테이블 만들기 - omilzomil backend 참조
echo [+] make db tables
if [ ! -e "./data/mysql.sock" ]; then
    echo [+] DB 초기 세팅을 시작합니다.
    sudo docker-compose -p ${PROJECT_NAME} --env-file .env.lock run --rm omilzomil python src/initial_data.py
fi


# ============== 기타 잔여 파일 컨테이너 캐쉬 삭제


# docker 빌드 캐쉬 제거
echo [+] remove build cache
sudo docker builder prune -f
sudo docker volume prune -f
sudo docker image prune -f

sudo docker-compose -p ${PROJECT_NAME} --env-file .env.lock rm -f

echo [+] Done