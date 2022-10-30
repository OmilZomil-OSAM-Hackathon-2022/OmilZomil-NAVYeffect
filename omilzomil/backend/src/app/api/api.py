from fastapi import APIRouter
from app.api.endpoints import test
from app.api.endpoints import affiliation
from app.api.endpoints import rank
from app.api.endpoints import role
from app.api.endpoints import uniform
from app.api.endpoints import appearance
from app.api.endpoints import military_unit
from app.api.endpoints import user
from app.api.endpoints import login
from app.api.endpoints import vacation
from app.api.endpoints import guardhouse
from app.api.endpoints import unit_house_relation
from app.api.endpoints import real_time_monitor
from app.api.endpoints import statistics
from app.api.endpoints import ranking


api_router = APIRouter()
api_router.include_router(test.router, prefix="/test", tags=["테스트 케이스 생성"])
api_router.include_router(affiliation.router, prefix="/affiliation", tags=["소속 관리"])
api_router.include_router(rank.router, prefix="/rank", tags=["계급 관리"])
api_router.include_router(role.router, prefix="/role", tags=["권한 관리"])
api_router.include_router(uniform.router, prefix="/uniform", tags=["군복 관리"])
api_router.include_router(appearance.router, prefix="/appearance", tags=["외형 관리"])
api_router.include_router(military_unit.router, prefix="/unit", tags=["부대 관리"])
api_router.include_router(user.router, prefix="/user", tags=["유저 관리"])
api_router.include_router(login.router, prefix="/login", tags=["로그인 기능"])
api_router.include_router(vacation.router, prefix="/vacation", tags=["휴가 관리"])
api_router.include_router(guardhouse.router, prefix="/house", tags=["위병소 관리"])
api_router.include_router(unit_house_relation.router, prefix="/unit/relation", tags=["위병소 연결"])
api_router.include_router(real_time_monitor.router, prefix="/rtm", tags=["실시간 감지 기능"])
api_router.include_router(statistics.router, prefix="/stats", tags=["통계 기능"])
api_router.include_router(ranking.router, prefix="/ranking", tags=["랭킹 기능"])
