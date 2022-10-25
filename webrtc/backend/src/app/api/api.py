from fastapi import APIRouter
from app.api.endpoints import recording, db_view, task, upload

api_router = APIRouter()
api_router.include_router(recording.router, prefix="/v1", tags=["버전 1"])
api_router.include_router(db_view.router, prefix="/db", tags=["DB 조회"])
api_router.include_router(upload.router, prefix="/upload", tags=["upload"])
