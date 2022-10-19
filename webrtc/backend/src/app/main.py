import sys
sys.path.append("./app/ai/.")
sys.path.append("./app/ai/OZEngine/.")

sys.path.append("./app/.")
sys.path.append("./app/omil/.")




print(sys.path)


import app.custom_logging


from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.api.api import api_router

app = FastAPI(
    title='omil zomil',
    description="test",
    openapi_url='/api/openapi.json'
)
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "*"
    # "http://localhost.tiangolo.com",
    # "https://localhost.tiangolo.com",
    # "http://localhost",
    # "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/aaaaa")
def read_root():
    return {'hello': 'world10'}


app.include_router(api_router)
app.mount("/", StaticFiles(directory="/backend/src/app/static", html = True), name="static")
