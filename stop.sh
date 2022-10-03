#/bin/bash

echo [+] Stopping docker container

sudo docker-compose --env-file .env.private stop frontend backend