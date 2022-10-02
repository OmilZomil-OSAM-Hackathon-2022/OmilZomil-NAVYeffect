# python main.py
pytest
# sh docker/make_ssl.sh --  안됨
uvicorn main:app --host 0.0.0.0 --port 8000 --reload --ssl-keyfile=./docker/key.pem --ssl-certfile=./docker/cert.pem
# uvicorn main:app --host 0.0.0.0 --port 8000 --reload