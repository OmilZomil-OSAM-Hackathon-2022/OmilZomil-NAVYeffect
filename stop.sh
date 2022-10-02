#/bin/bash

echo [+] Stopping backend docker container
echo

sudo docker-compose -f ./backend/docker-compose.yaml down
echo

echo [+] Done!