#/bin/bash

echo [+] Checking frontend build files...
if [ -f ./frontend/deploy/public/build/bundle.js ] ; then
    :
else
    echo "[!] Please run 'build.sh' first!"
    exit
fi

echo [+] Creating backend docker container
echo

sudo docker-compose -f ./backend/docker-compose.yaml up -d
echo

echo [+] Done!