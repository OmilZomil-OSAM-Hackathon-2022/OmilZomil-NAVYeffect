from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.api.api import api_router


app = FastAPI(
    title='omil zomil',
    description="test",
    openapi_url='/api/openapi.json'
)


@app.get("/aaaaa")
def read_root():
    return {'hello': 'world'}


app.include_router(api_router)

app.mount("/", StaticFiles(directory="/backend/src/app/static", html = True), name="static")
