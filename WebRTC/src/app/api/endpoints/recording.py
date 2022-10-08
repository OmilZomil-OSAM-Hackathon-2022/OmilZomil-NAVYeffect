from typing import List
from fastapi import APIRouter, Depends, WebSocket, WebSocketDisconnect
from sqlalchemy.orm import Session

from app.api.websocket.connections import ConnectionManager

socket_mng = ConnectionManager()

router = APIRouter()

@router.get("/")
async def test():
    return {'ge', 'tea'}

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
