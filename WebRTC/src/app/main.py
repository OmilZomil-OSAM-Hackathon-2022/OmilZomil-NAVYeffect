from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

# from app.api.api import api_router


app = FastAPI()
# app.include_router(api_router)

app.mount("/", StaticFiles(directory="/backend/src/app/static", html = True), name="static")
# app.mount("/", StaticFiles(directory="/backend/src/app/test", html = True), name="static")
