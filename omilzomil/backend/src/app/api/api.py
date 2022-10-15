from fastapi import APIRouter
from app.api.endpoints import military_unit
from app.api.endpoints import user
from app.api.endpoints import login
from app.api.endpoints import statistics


api_router = APIRouter()
api_router.include_router(military_unit.router, prefix="/unit", tags=["부대 관리"])
api_router.include_router(user.router, prefix="/user", tags=["유저 관리"])
api_router.include_router(login.router, prefix="/login", tags=["로그인 기능"])
api_router.include_router(statistics.router, prefix="/stats", tags=["통계 기능"])
