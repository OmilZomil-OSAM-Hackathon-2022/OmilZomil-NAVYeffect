import base64
import numpy as np
import cv2
import sys

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

import uuid


from app.api.websocket.connections import ConnectionManager
from app.api.broker.create import create_broker

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




# @router.websocket("/test")
# async def websocket_endpoint(websocket: WebSocket):
#     await websocket.accept()
#     print('connect test')
#     try:
#         while True:
#             data = await websocket.receive_json()   
#             print("test 데이터 수신")
#             # 데이터 수신
#             img = data['photo']
#             # 메세지 전송
#             msg = {
#                 'type' : "result",
#                 'photo' : img,
#             }
#             await websocket.send_json(msg)
    
#     except WebSocketDisconnect:
#         print("연결 종료")
#         pass
    
@router.websocket("/{url}")
async def websocket_endpoint(url, websocket: WebSocket):
    """
    ai 요구사항만 맞춰서 실행
    병렬 처리 X
    버퍼 X - 파일로 저장 X
    단지 카메라 객체만 유지
    """
    connect_start_time = datetime.now()
    await websocket.accept()
    camera_id = str(uuid.uuid4())

    print(f'연결 시작: {url} - {camera_id}')
    broker = create_broker(name=url, ws=websocket, id=camera_id)

    try:
        while True:
            data = await websocket.receive_json()
            work_start = datetime.now()
            print(f'데이터 수신: {url} - {camera_id}')

            # 데이터 수신
            result = broker.execute_task(
                photo=data['photo'], work_start=work_start
            )

            # 메세지 전송
            msg = {
                'type' : "result",
            }
            msg.update(result)
            print(f'테스크 1차 처리 완료: {url} - {camera_id} : {datetime.now() - work_start}')
            await websocket.send_json(msg)
    
    except WebSocketDisconnect:
        print(f'연결 종료: {url} - {camera_id}')
        pass
 