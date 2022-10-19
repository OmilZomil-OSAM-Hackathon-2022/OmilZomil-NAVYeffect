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

from app.api.broker.create import create_broker
from app.api import deps

router1 = APIRouter()
router2 = APIRouter()



    
@router1.websocket("/{url}")
async def websocket_endpoint(url, websocket: WebSocket, db: Session = Depends(deps.get_db)):
    """
    ai 요구사항만 맞춰서 실행
    병렬 처리 X
    버퍼 X - 파일로 저장 X
    단지 카메라 객체만 유지
    """
    # id, time
    connect_start_time = datetime.now()
    camera_id = str(uuid.uuid4())

    # 처음 접속
    await websocket.accept()
    first_data = await websocket.receive_json()
    guardhouse = 2

    print(f'연결 시작: {url} - {camera_id}')
    broker = create_broker(name=url, ws=websocket, id=camera_id, db=db, guardhouse=guardhouse)

    try:
        while True:
            data = await websocket.receive_json()
            work_start = datetime.now()
            print(f'데이터 수신: {url} - {camera_id} = {url}')

            # 데이터 수신
            result = broker.execute_task(
                photo=data['photo'], work_start=work_start
            )
            # worker가 없는 경우
            if result:
                # 메세지 전송
                msg = {
                    'type' : "result",
                }
                msg.update(result)
                await websocket.send_json(msg)
            # 1차 처리 로그 출력
            print(f'테스크 1차 처리 완료: {url} - {camera_id} : {datetime.now() - work_start}')
            print()
            print()


    except WebSocketDisconnect:
        print(f'연결 종료: {url} - {camera_id}')
        pass
