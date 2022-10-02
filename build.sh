#/bin/bash

echo [+] Cleaning up frontend build files
sudo rm -rf ./backend/app/templates/*
sudo rm -rf ./frontend/deploy/public/*
sudo rm -rf ./frontend/app/public/build
sudo cp -r ./frontend/app/public/* ./frontend/deploy/public/

echo [+] Building frontend docker container
echo

sudo docker-compose -f ./frontend/docker-compose.yaml up --build -d
echo

echo [+] Waiting for frontend build... \(This might take several minutes to complete.\)
until [ -f ./frontend/deploy/public/build/bundle.js ]; do
    sleep 1;
done;

sudo cp -r ./frontend/deploy/public/* ./backend/app/templates/
sudo chown -R $(id -u):$(id -g) ./frontend/deploy/public
sudo chown -R $(id -u):$(id -g) ./backend/app/templates

echo [+] Building backend docker container
echo

sudo docker-compose -f ./backend/docker-compose.yaml build
echo

echo [+] Done!