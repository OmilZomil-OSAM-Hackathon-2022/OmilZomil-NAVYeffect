#/bin/bash



echo [+] Checking build files...
if [ -f .env.lock ] ; then
    :
else
    echo "[!] Please run 'build.sh' first!"
    exit
fi

echo [+] Stopping docker container

sudo docker-compose --env-file .env.lock stop frontend backend