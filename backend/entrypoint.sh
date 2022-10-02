# 작업 폴더로 이동
cd backend/src
# 테스트 실행
pytest
# 서버 실행
uvicorn main:app --host 0.0.0.0 --port 8000 --reload --ssl-keyfile=../deploy/key.pem --ssl-certfile=../deploy/cert.pem
