from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.api import api_router
from app.core.config import settings
from app.core.SPAStaticFiles import SPAStaticFiles


app = FastAPI()

if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router)
app.mount("/image", SPAStaticFiles(directory="/image", html=True), name="image")
app.mount("/", SPAStaticFiles(directory="/backend/src/app/static", html=True), name="static")
