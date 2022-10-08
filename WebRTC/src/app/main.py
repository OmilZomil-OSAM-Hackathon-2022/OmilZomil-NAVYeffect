from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.api.api import api_router


app = FastAPI()

app.mount("/", StaticFiles(directory="/backend/src/app/static", html = True), name="static")

app.include_router(api_router)

