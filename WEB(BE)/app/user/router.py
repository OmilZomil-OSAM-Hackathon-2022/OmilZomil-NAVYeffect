from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse, FileResponse

router = APIRouter(
    prefix="/user",
    tags=["유저 관리"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def homepage(req: Request):
    return JSONResponse({
        'green': 'rain'
    })
