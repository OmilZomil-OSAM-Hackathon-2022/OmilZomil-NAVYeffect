from fastapi import APIRouter, Depends, Body, HTTPException
from fastapi.responses import JSONResponse, FileResponse
from fastapi.requests import Request
from sqlalchemy.orm import Session
from typing import List

from core.db import get_db

from app.camera.schema import CameraDisplay, CameraCreate
from app.camera import crud


router = APIRouter(
    prefix="/camera",
    tags=[" 카메라 관리"],
    responses={404: {"description": "Not found"}},
)

@router.post("/create/", response_model=CameraDisplay)
async def 생성(camera: CameraCreate = Body(), db: Session = Depends(get_db)):
    """
    카메라 생성
    """
    db_camera = crud.get_camera_by_uid(db, uid=camera.uid)
    if db_camera:
        raise HTTPException(status_code=400, detail="해당 uid가 이미 존재합니다.")
    return crud.create_camera(db, camera=camera)


@router.get("/read", response_model=List[CameraDisplay])
async def 전체조회(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    cameras = crud.get_camera(db, skip=skip, limit=limit)
    return cameras

@router.get("/test")
async def 테스트(req: Request):
    return FileResponse("static/camera/index.html")

# @router.get("/update")
# async def 유저업데이트(req: Request):
#     return JSONResponse({
#         'green': 'rain'
#     })

# @router.get("/delete")
# async def 유저탈퇴(req: Request):
#     return JSONResponse({
#         'green': 'rain'
#     })
