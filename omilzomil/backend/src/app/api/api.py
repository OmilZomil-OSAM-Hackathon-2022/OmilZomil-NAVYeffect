from fastapi import APIRouter
from app.api.endpoints import military_unit
from app.api.endpoints import user


api_router = APIRouter()
api_router.include_router(military_unit.router, prefix="/unit", tags=["부대 정보"])
api_router.include_router(user.router, prefix="/user", tags=["유저 정보"])
