import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from app.user import router as user_router
from core.settings import CORS_ORIGINS

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(user_router.router)
