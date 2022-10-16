from fastapi import APIRouter
from app.api.endpoints import rank
from app.api.endpoints import affiliation
from app.api.endpoints import role
from app.api.endpoints import military_unit
from app.api.endpoints import user
from app.api.endpoints import login
from app.api.endpoints import uniform
from app.api.endpoints import appearance
from app.api.endpoints import statistics


api_router = APIRouter()
api_router.include_router(rank.router, prefix="/rank", tags=["계급 관리"])
api_router.include_router(affiliation.router, prefix="/affiliation", tags=["소속 관리"])
api_router.include_router(role.router, prefix="/role", tags=["권한 관리"])
api_router.include_router(military_unit.router, prefix="/unit", tags=["부대 관리"])
api_router.include_router(user.router, prefix="/user", tags=["유저 관리"])
api_router.include_router(login.router, prefix="/login", tags=["로그인 기능"])
api_router.include_router(uniform.router, prefix="/uniform", tags=["군복 관리"])
api_router.include_router(appearance.router, prefix="/appearance", tags=["외형 관리"])
api_router.include_router(statistics.router, prefix="/stats", tags=["통계 기능"])
