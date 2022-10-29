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

from app.api import deps
from app.api.simple.broker import SimpleBroker
from app.api.socket.broker import SocketBroker
from app.api.broker.single import SingleBroker

from app.api.websocket.image import photo_2_img, img_2_photo
from app.api.db.guardhouse import get_guardhouse, select_guardhouse
from app.ai.OZEngine.model import OmilZomil



router = APIRouter()

async def send_guardhous(websocket: WebSocket, db: Session):
    house_list = [data.house for data in get_guardhouse(db)]
    await websocket.send_json({
        'type' : "list",
        'list' : house_list,
    })


@router.websocket("/single")
async def websocket_endpoint(websocket: WebSocket, db: Session = Depends(deps.get_db)):
    """
    ai 요구사항만 맞춰서 실행
    병렬 처리 X
    버퍼 X - 파일로 저장 X
    단지 카메라 객체만 유지
    """
    # 기본 데이터 - id, time
    connect_start_time = datetime.now()
    camera_id = str(uuid.uuid4())

    # 처음 접속 =  위병소 리스트 전달
    await websocket.accept()
    await send_guardhous(websocket, db)
    
    # 브로커 생성    
    broker = SingleBroker(id=camera_id, db=db)
    
    # 수신 중
    print(" 이미지 수신 시작")
    try:
        while True:
            data = await websocket.receive_json()
            print(f'데이터 수신:- {camera_id} = {datetime.now()}')

            # img 로 변환
            img = photo_2_img(data['photo'])

            # broker에게 전달
            work_start = datetime.now()
            msg = broker.add_task(img=img, guardhouse=data['name'], work_time=work_start)
        
            msg['working_time'] = str(datetime.now() - work_start)

            await websocket.send_json(msg)
            # 1차 처리 로그 출력
            print(f'테스크 1차 처리 완료: {camera_id} : {datetime.now()} - {datetime.now() - work_start}')
            print()
            print()


    except WebSocketDisconnect:
        print(f'연결 종료: - {camera_id} {datetime.now() - connect_start_time}')
        pass


    
@router.websocket("/ping")
@router.websocket("/test")
async def websocket_endpoint(websocket: WebSocket, db: Session = Depends(deps.get_db)):
    """
    ai 요구사항만 맞춰서 실행
    병렬 처리 X
    버퍼 X - 파일로 저장 X
    단지 카메라 객체만 유지
    """
    # id, time
    connect_start_time = datetime.now()
    camera_id = str(uuid.uuid4())

    # 처음 접속 =  위병소 리스트 전달
    await websocket.accept()
    house_list = [data.house for data in get_guardhouse(db)]
    await websocket.send_json({
        'type' : "list",
        'list' : house_list,
    })

    print("소캣 연결 완료")
    
    # 수신 중
    print(" 이미지 수신 시작")
    try:
        while True:
            data = await websocket.receive_json()
            work_start = datetime.now()
            print(f'데이터 수신:- {camera_id}')
            # msg = {
            #     'type' : "result",
            #     "kind" : "blue",
            #     "photo": data['photo'],
            #     'hair' : True,
            #     'name_tag' : True,
            #     'level_tag' : True,
            #     'muffler' : True,
            #     'neck' : True,

            # }

            msg = {
                "type" : "status",
                "status" : "ready"
            }

            await websocket.send_json(msg)
            # 1차 처리 로그 출력
            print(f'테스크 1차 처리 완료: {camera_id} : {datetime.now() - work_start}')
            print()
            print()


    except WebSocketDisconnect:
        print(f'연결 종료: - {camera_id} {datetime.now() - connect_start_time}')
        pass

    
@router.websocket("/socket")
@router.websocket("/test")
async def websocket_endpoint(websocket: WebSocket, db: Session = Depends(deps.get_db)):
    """
    소켓으로 worker와 연결
    """
    # id, time
    connect_start_time = datetime.now()
    camera_id = str(uuid.uuid4())


    # 처음 접속 =  위병소 리스트 전달
    await websocket.accept()
    house_list = [data.house for data in get_guardhouse(db)]
    await websocket.send_json({
        'type' : "list",
        'list' : house_list,
    })

    # 브로커 생성    
    broker = SocketBroker(id=camera_id)
    
    # 수신 중
    print(" 이미지 수신 시작")
    try:
        while True:
            # 데이터 수신
            data = await websocket.receive_json()
            print(f"처리 시작 = {datetime.now()}")

            # broker에게 전달
            work_start = datetime.now()
            response_msg = broker.add_task(photo=data['photo'], guardhouse= data['name'], work_time=work_start)
            
            # 메세지 정리 및 응답 반환
            response_msg['working_time'] = str(datetime.now() - work_start)
            print(response_msg)
            await websocket.send_json(response_msg)
            print("=======================================")
            # 메세지 수신
            result_msg_list = broker.receive()
            
            print(f"전달해야 하는 메세지 {result_msg_list}")
            
            if not result_msg_list:
                continue
            # 메세지 전송
            for result_msg in result_msg_list:
                await websocket.send_json(result_msg)


    except WebSocketDisconnect:
        print(f'연결 종료: - {datetime.now() - connect_start_time}')
        
