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


from app.api.websocket.connections import ConnectionManager
from app.api.websocket.broker import SingleBroker

# 관리 객체
socket_mng = ConnectionManager()

router = APIRouter()

@router.websocket("/ws")
async def debug_websocket(websocket: WebSocket):
    connect_start_time = datetime.now()
    socker_id = 1
    await websocket.accept()
    # await socket_mng.connect(f'{socker_id}', websocket)
    print("connected") 
    # await websocket.send_json("위병소")
    
    broker = SingleBroker(ws=websocket, id=1)
    # 소캣 연결 유지
    try:
        while True:
            data = await websocket.receive_json()
            work_start = datetime.now()
            # print(f"받음 : {data}")
            print(f"받음 ")
            result = await broker.give_task(data=data['img'])
            print(f"처리 완료 {result} - {datetime.now()-work_start}")   
            await websocket.send_json(result)
    except WebSocketDisconnect:
        # socket_mng.disconnect(f'{socker_id}')
        pass




@router.websocket("/test")
async def websocket_endpoint(websocket: WebSocket):
    print("ping")
    socker_id = 1
    await websocket.accept()
    # socket_mng.connect(f'{socker_id}', websocket)
    print('connect')
    # try:
    while True:
        data = await websocket.receive_text()   
        print("receive")
        msg = {
            'type' : "test",
            'msg' : data,
        }
        await websocket.send_json(data)
        pass
    # except WebSocketDisconnect:
    #     pass
        # websocket.disconnect()
        # socket_mng.disconnect(f'{socker_id}')


