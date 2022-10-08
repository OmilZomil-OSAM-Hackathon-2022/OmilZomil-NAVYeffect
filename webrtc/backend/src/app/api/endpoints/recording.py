from typing import List
from fastapi import APIRouter, Depends, WebSocket, WebSocketDisconnect
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse

from app.api.websocket.connections import ConnectionManager

socket_mng = ConnectionManager()

router = APIRouter()

@router.get("/")
async def test():
    return {'ge': 'tea'}


@router.get("/")
async def get():
    return FileResponse("v1/websocket/v4/index.html")

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await socket_mng.connect('single', websocket)

    print("connected")
    try:
        while True:
            data = await websocket.receive_text()
            print(data)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
