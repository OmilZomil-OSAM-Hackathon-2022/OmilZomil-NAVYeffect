import sys
sys.path.append("./app/ai/.")
sys.path.append("./app/ai/OZEngine/.")

import app.custom_logging


from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.api.api import api_router

app = FastAPI(
    title='omil zomil',
    description="test",
    openapi_url='/api/openapi.json'
)
config_path="logging_config.json"

# app.logger = logger

@app.get("/aaaaa")
def read_root():
    return {'hello': 'world5'}

app.include_router(api_router)
app.mount("/", StaticFiles(directory="/backend/src/app/static", html = True), name="static")
