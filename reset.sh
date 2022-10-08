#/bin/bash

# 스크립트 설명: 도커를 초기화해주는 스크립트
# 빌드된 이미지까지 모두 지워줌
# 

# 해당 docker-compose 파일에 연관된 모든 컨테이너 제거
sudo docker-compose --env-file .env.lock down --remove-orphans

# 도커 초기화 - 다른 프로젝트의 컨테아너가 있으면 영향이 갈 수 있음
sudo docker system prune --all