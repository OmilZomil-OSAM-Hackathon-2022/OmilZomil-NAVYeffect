from typing import List
from fastapi import APIRouter, Depends, WebSocket, WebSocketDisconnect
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
import cv2
import numpy as np
import base64
from datetime import datetime
import traceback
from loguru import logger

from app.ai.OZEngine.person_detectors.PersonDetector import PersonDetector
from app.ai.OZEngine.model import OmilZomil
from app.api.websocket.connections import ConnectionManager

# 관리 객체
socket_mng = ConnectionManager()
omil_detector = OmilZomil(uniform_type='FULL_DRESS')
person_detector = PersonDetector()

router = APIRouter()

@router.get("/")
async def test():
    return {'ge': 'tea'}


@router.get("/")
async def get():
    return FileResponse("v1/websocket/v4/index.html")




@router.websocket("/test")
async def websocket_endpoint(websocket: WebSocket):
    print("ping")
    socker_id = 1
    await websocket.accept()
    # socket_mng.connect(f'{socker_id}', websocket)
    print('connect')
    try:
        while True:
            data = await websocket.receive_text()   
            print("receive")
            msg = {
                'type' : "test",
                'msg' : data,
            }
            await websocket.send_json(data)
            pass
    except WebSocketDisconnect:
        socket_mng.disconnect(f'{socker_id}')





@router.websocket("/ws2")
async def debug_websocket(websocket: WebSocket):
    socker_id = datetime.now()
    await socket_mng.connect(f'{socker_id}', websocket)
    logger.info(":ASdf")
    print("connected")
    try:
        while True:
            data = await websocket.receive_text()   
            try:
                img = cv2.imdecode(np.fromstring(base64.b64decode(data.split(',')[1]), np.uint8), cv2.IMREAD_COLOR)
                result = omil_detector.detect(img)
                resp = {
                    "result" : result
                }
                print(f"결과물 - {resp}")
                await websocket.send_json(resp)
            except Exception as e:
                traceback.print_exc()
                error_msg = {
                    'type' : "error",
                    'msg' : 'ai 처리 오류',
                }
                await websocket.send_json(error_msg)
            
    except WebSocketDisconnect:
        socket_mng.disconnect(f'{socker_id}')
