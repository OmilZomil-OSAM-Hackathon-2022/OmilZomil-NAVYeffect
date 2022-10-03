#/bin/bash

echo [+] run web
sudo docker-compose -f docker-compose.server.yml --env-file .env.private up