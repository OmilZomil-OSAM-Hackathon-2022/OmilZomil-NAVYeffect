from fastapi import APIRouter
from app.api.endpoints import enlisted_personnel


api_router = APIRouter()
api_router.include_router(enlisted_personnel.router, prefix="/enlisted", tags=["장병 복장 정보"])
