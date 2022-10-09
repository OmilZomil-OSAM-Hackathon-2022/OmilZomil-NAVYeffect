#! /bin/bash
# 스크립트 설명: 서비스를 시작하기전 필요한 파일들을 생성
# 프론트 빌드도 해당 스크립트에서 동작


# .env 파일이 있는지 검증
if [ ! -e ".env.private" ]; then
	echo ".env.private 파일이 없습니다."
    echo ".env.public 를 복사하여 만들어 주시길 바랍니다."
    exit
fi

DIR_PATH=`pwd`

# 환경변수 파일 정의
cat .env.private > .env.lock
echo DIR_PATH="$DIR_PATH" >> .env.lock

# 기존 컨테이너 지우기
echo [+] remove container
sudo docker-compose --env-file .env.lock down --remove-orphans

# docker 빌드
echo [+] docker build
sudo docker-compose --env-file .env.lock build

# 이전 프론트 빌드 제거
sudo rm -r omilzomil/frontend/dist
sudo rm -r webrtc/frontend/dist

mkdir omilzomil/frontend/dist
mkdir webrtc/frontend/dist

chown $USER:$USER omilzomil/frontend/dist
chown $USER:$USER webrtc/frontend/dist

# 프론트 빌드
echo [+] frontend build
sudo docker-compose --env-file .env.lock up web_vue
sudo docker-compose --env-file .env.lock up camera_vue

echo [+] frontend build 대기

while sudo docker-compose --env-file .env.lock ps --services --filter status=running | grep -q 'vue'; do
    echo `sudo docker-compose --env-file .env.lock ps --services --filter status=running`
    wait_time=`date +%T`
    echo frontend $wait_time
    sleep 1;
done;


echo [+] Checking build files...
while [ ! -f ./omilzomil/frontend/dist/index.html ] ; do
    wait_time=`date +%T`
    echo [!] omilzomil 프론트 빌드 실패 - $wait_time
    sleep 1;
done
while [ ! -f ./webrtc/frontend/dist/index.html ] ; do
    wait_time=`date +%T`
    echo [!] webrtc 프론트 빌드 실패 - $wait_time
    sleep 1;
done





# DB 실행
echo [+] make db
sudo docker-compose --env-file .env.lock up -d db

# DB 테이블 만들기 - omilzomil backend 참조
echo [+] make db tables
sudo docker-compose --env-file .env.lock run --rm web python src/initial_data.py


# ssl 만들기 - .env 파일이 있는지 검증 => 없으면 생성
if [ ! -e "./omilzomil/backend/cert.pem" ]; then
    echo [+] omilzomil 에 cert.pem 파일이 없어 생성합니다.
    openssl req -x509 -newkey rsa:4096 -nodes -out ./omilzomil/backend/cert.pem -keyout ./omilzomil/backend/key.pem -days 365
    cd $DIR_PATH
fi
if [ ! -e "./webrtc/backend/cert.pem" ]; then
    echo [+] webrtc 에 cert.pem 파일이 없어 생성합니다.
    openssl req -x509 -newkey rsa:4096 -nodes -out ./webrtc/backend/cert.pem -keyout ./webrtc/backend/key.pem -days 365
fi


# docker 빌드 캐쉬 제거
echo [+] remove build cache
sudo docker builder prune -f



sudo docker-compose --env-file .env.lock rm -f

echo [+] Done