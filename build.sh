DIR_PATH=`pwd`

cat .env.private > .env.lock
echo BACKEND_DIR_PATH="$DIR_PATH"/backend >> .env.lock
echo FRONTEND_DIR_PATH="$DIR_PATH"/frontend >> .env.lock

echo [+] makeing DB 

# 기존 컨테이너 지우기
sudo docker-compose --env-file .env.lock down

# docker 빌드
sudo docker-compose --env-file .env.lock build

# DB 실행
sudo docker-compose --env-file .env.lock up -d db

# DB 테이블 만들기
sudo docker-compose --env-file .env.lock run backend python src/init_db.py

# ssl 만들기
cd ./backend/deploy
sh make_ssl.sh 

# docker 빌드 캐쉬 제거
sudo docker builder prune