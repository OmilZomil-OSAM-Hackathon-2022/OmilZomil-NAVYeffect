from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.settings import CORS_ORIGINS
from app.user import router as user_router
from app.test import router as test_router
from app.token import router as token_router
from app.camera import router as camera_router
from app.enlisted_personnel import router as enlisted_personnel_router
from app.base_access import router as base_access_router

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(user_router.router)
app.include_router(token_router.router)
app.include_router(test_router.router)
app.include_router(camera_router.router)
app.include_router(enlisted_personnel_router.router)
app.include_router(base_access_router.router)


@app.get("/")
async def read_main():
    return {"msg": "Hello World"}
