from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from passlib.context import CryptContext
from jose import jwt

from typing import Union
from datetime import timedelta, datetime

# 비밀키 생성 코드 : openssl rand -hex 32
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# 인증 함수
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# 비번 채크
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# 비번 생성
def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=15)):
    """
    토큰 생성
    data에 들어있는 값을 jwt 토큰으로 변경
    """
    # 토큰에 들어갈 데이터 준비
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})   # 만료시간

    # jwt 인코딩
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt