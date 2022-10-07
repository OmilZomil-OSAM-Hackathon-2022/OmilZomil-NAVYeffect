echo sudo docker-compose $@
sudo docker-compose --env-file .env.lock $@
