# 작업 폴더로 이동
cd /backend/src
# 테스트 실행
pytest
# 서버 실행
uvicorn app.main:app --host 0.0.0.0 --port 80 --reload --ssl-keyfile=../key.pem --ssl-certfile=../cert.pem
