#/bin/bash

# 스크립트 설명: 서비스를 시작
# 재시작시 백앤드에서 코드를 수정하면 반영이 되지만 프론트 앤드는 반영이 안되어서 build.sh부터 실행시켜줘야함
#
# --build - 프론트만 다시 빌드 - 백앤드와는 연관이 없도록 작성
# --server - 서버 배포용 - host의 폴더와 상관없이 동작하도록 구성 bind 항목을 제거
# =-dev-back - 백앤드 개발용 - 백앤드 빌드와 실행을 동시에 동작, 프론트는 영향 없음
args_2=$2
PROJECT_NAME=${args_2:-omil}

DIR_PATH=`pwd`

input=$1
if [ "$input" = "--build" ]; then
    # 프론트 빌드 - 단지 프론트 백앤드 빌드만 다시함
    echo [+] frontend build 프론트 재빌드 - 백앤드 실행 X
    sudo docker-compose --env-file .env.lock build web_vue camera_vue
    sudo docker-compose --env-file .env.lock up web_vue
    sudo docker-compose --env-file .env.lock up camera_vue

    echo [+] frontend build 대기

    while sudo docker-compose --env-file .env.lock ps --services --filter status=running | grep -q 'vue'; do
        echo `sudo docker-compose --env-file .env.lock ps --services --filter status=running`
        wait_time=`date +%T`
        echo frontend $wait_time
        sleep 1;
    done;

elif [ "$input" = "--server" ]; then
    echo [+] run web camera 서버환경
    sudo docker-compose --env-file .env.private up web camera

elif [ "$input" = "--dev-back" ]; then
    # 백앤드 개발용 코드 - 라이브러리 재설치 및 apt install 에 따른 build가 필요한 경우 사용
    echo [+] run web camera 백앤드 개발환경
    sudo docker-compose --env-file .env.lock up --build web camera    

elif [ "$input" = "--name" ]; then
    # 백앤드 개발용 코드 - 라이브러리 재설치 및 apt install 에 따른 build가 필요한 경우 사용
    echo [+] run web camera 플젝명 직접 지정 ${PROJECT_NAME}
    sudo docker-compose -p ${PROJECT_NAME} --env-file .env.lock up web camera

else
    echo [+] run web camera 개발환경 ${PROJECT_NAME}

    sudo docker-compose -p ${PROJECT_NAME} --env-file .env.lock up web camera

fi


