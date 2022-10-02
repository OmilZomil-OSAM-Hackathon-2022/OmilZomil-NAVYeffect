echo [+] makeing DB 
# DB 실행
sudo docker-compose up -d db

# DB 테이블 만들기
sudo docker-compose run backend python src/init_db.py