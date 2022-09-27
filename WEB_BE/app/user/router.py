from fastapi import APIRouter, Depends, Body, HTTPException
from fastapi.responses import JSONResponse, FileResponse
from fastapi.requests import Request
from sqlalchemy.orm import Session
from typing import List

from core.db import get_db

from app.user.schema import UserDisplay, UserCreate
from app.user import crud


router = APIRouter(
    prefix="/user",
    tags=["유저 관리"],
    responses={404: {"description": "Not found"}},
)


@router.get("/test")
async def 테스트(req: Request):
    return FileResponse("static/user/index.html")

@router.post("/create/", response_model=UserDisplay)
async def 회원가입(user: UserCreate = Depends(UserCreate), db: Session = Depends(get_db)):
    """
    user 생성
    회원가입때 사용하는 
    """
    db_user = crud.get_user_by_uid(db, uid=user.uid)
    if db_user:
        raise HTTPException(status_code=400, detail="해당 uid가 이미 존재합니다.")
    return crud.create_user(db=db, user=user)



@router.get("/read", response_model=List[UserDisplay])
async def 전체조회(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/update")
async def 유저업데이트(req: Request):
    return JSONResponse({
        'green': 'rain'
    })

@router.get("/delete")
async def 유저탈퇴(req: Request):
    return JSONResponse({
        'green': 'rain'
    })
