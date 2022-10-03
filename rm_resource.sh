#/bin/bash

echo [+] Removing docker container

sudo docker-compose -f docker-compose.server.yml --env-file .env.private down