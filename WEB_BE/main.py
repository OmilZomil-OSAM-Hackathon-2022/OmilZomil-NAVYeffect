import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware



from core.settings import CORS_ORIGINS


app = FastAPI()

@app.get("/")
async def read_main():
    return {"msg": "Hello World"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from app.user import router as user_router
from app.test import router as test_router



app.include_router(user_router.router)
app.include_router(test_router.router)