echo [+] makeing DB 

# docker 빌드
sudo docker-compose -f docker-compose.server.yml --env-file .env.private build

# DB 실행
sudo docker-compose -f docker-compose.server.yml --env-file .env.private up -d db

# DB 테이블 만들기
sudo docker-compose -f docker-compose.server.yml --env-file .env.private run backend python src/init_db.py

# ssl 만들기
cd ./backend/deploy
sh make_ssl.sh 

# docker 빌드 캐쉬 제거
sudo docker builder prune