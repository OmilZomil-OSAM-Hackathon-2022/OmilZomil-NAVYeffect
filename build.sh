echo [+] makeing DB 

# docker 빌드
sudo docker-compose build

# DB 실행
sudo docker-compose up -d db

# DB 테이블 만들기
sudo docker-compose run backend python backend/src/init_db.py

# ssl 만들기
cd ./backend/deploy
sh make_ssl.sh 