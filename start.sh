#/bin/bash

# 스크립트 설명: 서비스를 시작
# 재시작시 백앤드에서 코드를 수정하면 반영이 되지만 프론트 앤드는 반영이 안되어서 build.sh부터 실행시켜줘야함


echo [+] Checking build files...
if [ ! -f ./omilzomil/frontend/dist/index.html ] ; then
    echo "[!] Please run 'build.sh' first! - omilzomil front NONE"
    exit
fi
if [ ! -f ./webrtc/frontend/dist/index.html ] ; then
    echo "[!] Please run 'build.sh' first! - webrtc front NONE"
    exit
fi


echo [+] run web & camera
sudo docker-compose --env-file .env.lock up web camera