from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.orm import Session
from typing import Union
from datetime import timedelta


from app.token.schema import Token
from app.user.schema import UserDisplay

from app.token.user import get_current_user, authenticate_user
from app.token.jwt import ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token
from core.db import get_db

router = APIRouter(
    prefix="/token",
    tags=["로그인 토큰"],
    responses={404: {"description": "Not found"}},
)


@router.post("/", response_model=Token)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    """
    로그인을 위한 토큰 발급 api
    username - id
    password - 비번
    을 입력하면 jwt 토큰이 나옵니다.
    """
    user = authenticate_user(db=db, uid=form_data.username, pw=form_data.password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # 토큰 생성
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"uid": user.uid}, expires_delta=access_token_expires
    )
    # 토큰 전달
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/me/", response_model=UserDisplay)
async def read_users_me(db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    """
    현재 접속중인 유저가 누구인지 조회
    """
    return current_user