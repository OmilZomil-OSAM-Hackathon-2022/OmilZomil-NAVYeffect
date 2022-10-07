import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from core.settings import CORS_ORIGINS
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

app = FastAPI()

# app.mount("/", StaticFiles(directory="/vue/dist", html=True), name="static")

# @app.get("/.*", include_in_schema=False)
# def root():
#     with open('/vue/dist/index.html') as f:
#         return HTMLResponse(content=f.read(), status_code=200)

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from app.user import router as user_router
from app.test import router as test_router
from app.token import router as token_router
from app.camera import router as camera_router


app.include_router(user_router.router)
app.include_router(token_router.router)
app.include_router(test_router.router)
app.include_router(camera_router.router)