from fastapi import APIRouter
from app.api.endpoints import recording, db_view

api_router = APIRouter()
api_router.include_router(recording.router1, prefix="/v1", tags=["버전 1"])
api_router.include_router(recording.router2, prefix="/v2", tags=["비동기 방식"])
api_router.include_router(db_view.router, prefix="/db", tags=["DB 조회"])
