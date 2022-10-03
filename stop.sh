#/bin/bash

echo [+] Stopping docker container

sudo docker-compose -f docker-compose.server.yml --env-file .env.private stop frontend backend