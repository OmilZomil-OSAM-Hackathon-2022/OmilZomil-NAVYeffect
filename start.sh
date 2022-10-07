#/bin/bash

echo [+] Checking build files...
if [ -f ./frontend/omilzomil/dist/index.html ] ; then
    :
else
    echo "[!] Please run 'build.sh' first!"
    exit
fi

echo [+] run web
sudo docker-compose --env-file .env.lock up web