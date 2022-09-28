from fastapi import APIRouter, Depends, Body, HTTPException
from fastapi.responses import JSONResponse, FileResponse
from fastapi.requests import Request

from typing import List


router = APIRouter(
    prefix="/test",
    tags=["테스트"],
    responses={404: {"description": "Not found"}},
)


@router.post("/input")
async def 입력(req: Request):
    print(req)
    return JSONResponse(req)