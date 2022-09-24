import uvicorn
from fastapi import FastAPI

from app.user import router as user_router

app = FastAPI()

app.include_router(user_router.router)
