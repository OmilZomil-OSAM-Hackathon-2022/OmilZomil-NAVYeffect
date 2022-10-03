#/bin/bash

echo [+] Stopping docker container

sudo docker-compose --env-file .env.lock stop frontend backend