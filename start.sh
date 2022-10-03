#/bin/bash

echo [+] Checking build files...
if [ -f .env.lock ] ; then
    :
else
    echo "[!] Please run 'build.sh' first!"
    exit
fi

echo [+] run web
sudo docker-compose --env-file .env.lock up