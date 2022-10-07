
# .env 파일이 있는지 검증
if [ ! -e ".env.private" ]; then
	echo ".env.private 파일이 없습니다."
    echo ".env.publoc 를 복사하여 만들어 주시길 바랍니다."
    exit
fi


# 프론트 빌드
echo [+] frontend build
sudo docker-compose --env-file .env.lock up -d vue

