from fastapi import APIRouter
from app.api.endpoints import recording

api_router = APIRouter()
api_router.include_router(recording.router, prefix="/v1", tags=["버전 1"])
