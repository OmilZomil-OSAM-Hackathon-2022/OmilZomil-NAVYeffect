echo [+] makeing DB 

# docker 빌드
sudo docker-compose -f docker-compose.server.yml build

# DB 실행
sudo docker-compose -f docker-compose.server.yml up -d db

# DB 테이블 만들기
sudo docker-compose -f docker-compose.server.yml run backend python backend/src/init_db.py

# ssl 만들기
cd ./backend/deploy
sh make_ssl.sh 

# docker 빌드 캐쉬 제거
sudo docker builder prune