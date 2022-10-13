import base64
import numpy as np
import cv2
import sys

from typing import List
from fastapi import APIRouter, Depends, WebSocket, WebSocketDisconnect
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse

from app.api.websocket.connections import ConnectionManager

import time
import logging
logger = logging.Logger('asdf')


socket_mng = ConnectionManager()

router = APIRouter()

@router.get("/")
async def test():
    return {'ge': 'tea 1'}


@router.get("/")
async def get():
    return FileResponse("v1/websocket/v4/index.html")

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await socket_mng.connect('single', websocket)

    logger.warn("connected")
    try:
        while True:
            data = await websocket.receive_text()
            
            logger.warn(sys.getsizeof(data))
            img = cv2.imdecode(np.fromstring(base64.b64decode(data.split(',')[1]), np.uint8), cv2.IMREAD_COLOR)
            # cv2.imshow('image', img)
            logger.warn(sys.getsizeof(img))
            logger.warn(img.shape)
            logger.warn(type(img))
            cv2.imwrite('webrtc_image.jpg', img)
    except WebSocketDisconnect:
        socket_mng.disconnect('single')


@router.websocket("/ws2")
async def websocket_endpoint(websocket: WebSocket):
    await socket_mng.connect('single', websocket)

    logger.warn("connected")
    try:
        while True:
            data = await websocket.receive_text()
            time.sleep(3)
            await websocket.send_text(data)
            logger.warn("end")

            
    except WebSocketDisconnect:
        socket_mng.disconnect('single')


@router.websocket("/json")
async def websocket_endpoint(websocket: WebSocket):
    await socket_mng.connect('single', websocket)

    logger.warn("connected")
    try:
        while True:
            data = await websocket.receive_text()
            time.sleep(3)
            result = {
                "img" : data,
                "id" : 2134,
            }
            await websocket.send_json(data)
            logger.warn("end")

            
    except WebSocketDisconnect:
        socket_mng.disconnect('single')
