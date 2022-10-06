from fastapi import APIRouter
from app.api.endpoints import base_access, enlisted_personnel


api_router = APIRouter()
api_router.include_router(base_access.router, prefix="/access", tags=["부대 출입 정보"])
api_router.include_router(enlisted_personnel.router, prefix="/enlisted", tags=["장병 복장 정보"])
