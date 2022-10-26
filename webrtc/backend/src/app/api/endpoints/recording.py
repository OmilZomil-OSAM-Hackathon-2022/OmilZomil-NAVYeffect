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

from app.api.websocket.image import photo_2_img, img_2_photo
from app.api.db.guardhouse import get_guardhouse, select_guardhouse
from app.ai.OZEngine.model import OmilZomil



router = APIRouter()

    
@router.websocket("/aaaaa")
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

    print("소캣 연결 완료2222")
    broker = SimpleBroker(id=camera_id, db=db)
    
    # 수신 중
    print(" 이미지 수신 시작")
    try:
        while True:
            data = await websocket.receive_json()
            work_start = datetime.now()
            print(f'데이터 수신:- {camera_id} - {work_start}')

            # 업무 전달
            img = photo_2_img(data['photo'])
            guardhouse = data['name']
            msg = broker.add_task(img=img, guardhouse=guardhouse, work_time=work_start)

            # 프론트에게 전달
            print(msg)
            await websocket.send_json(msg)
            # 1차 처리 로그 출력
            print(f'테스크 1차 처리 완료: {camera_id} : {datetime.now() - work_start}')
            print()
            print()


    except WebSocketDisconnect:
        print(f'연결 종료: - {camera_id} {datetime.now() - connect_start_time}')
        pass

    


@router.websocket("/ai")
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
    omil_detecter = OmilZomil()
    
    # 수신 중
    print(" 이미지 수신 시작")
    try:
        while True:
            data = await websocket.receive_json()
            work_start = datetime.now()
            print(f'데이터 수신:- {camera_id} = {datetime.now()}')
            img = photo_2_img(data['photo'])
            report = omil_detecter.detect(img)


            
            cv2.imwrite(f"./image_list/{report['step']}_{work_start.strftime('%H-%M-%S')}.jpg", img)

            
            print(report)
            print(report['step'])
            print(report.get('component'))

            msg = {
                'type' : "ai",
                'step' : report['step'],
                'component' : report.get('component'),
            }
            await websocket.send_json(msg)
            # 1차 처리 로그 출력
            print(f'테스크 1차 처리 완료: {camera_id} : {datetime.now()} - {datetime.now() - work_start}')
            print()
            print()


    except WebSocketDisconnect:
        print(f'연결 종료: - {camera_id} {datetime.now() - connect_start_time}')
        pass


    
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
            msg = {
                'type' : "result",
                "uniform" : "blue",
                "photo": data['photo'],
                'hair' : True,
                'name_tag' : True,
                'level_tag' : True,
                'muffler' : True,
                'neck' : True,

            }
            await websocket.send_json(msg)
            # 1차 처리 로그 출력
            print(f'테스크 1차 처리 완료: {camera_id} : {datetime.now() - work_start}')
            print()
            print()


    except WebSocketDisconnect:
        print(f'연결 종료: - {camera_id} {datetime.now() - connect_start_time}')
        pass

    
@router.websocket("/aaaaa")
async def websocket_endpoint(websocket: WebSocket, db: Session = Depends(deps.get_db)):
    """
    ai 요구사항만 맞춰서 실행
    병렬 처리 X
    버퍼 X - 파일로 저장 X
    단지 카메라 객체만 유지
    """
    # id, time
    connect_start_time = datetime.now()


    # 처음 접속 =  위병소 리스트 전달
    await websocket.accept()
    house_list = [data.house for data in get_guardhouse(db)]
    await websocket.send_json({
        'type' : "list",
        'list' : house_list,
    })

    # 브로커 생성    
    broker = SocketBroker(id=1)
    
    # 수신 중
    print(" 이미지 수신 시작")
    guardhouse = "계룡대 1정문"
    while True:
        data = await websocket.receive_json()

        print(f"처리 시작 = {datetime.now()}")

        img = photo_2_img(data['photo'])
        # guardhouse = data['name']

        # broker에게 전달
        work_start = datetime.now()
        msg = broker.add_task(photo=data['photo'], guardhouse=guardhouse, work_time=work_start)
        
        # 메세지 정리
        msg['working_time'] = datetime.now() - work_start
        # await websocket.send_json(msg)
        print(f"========================================================")
        result_list = broker.receive()
        print(f"========================================================{result_list}")


        result_msg = {
            "type" : "result",
            "img" : data['photo'],
            "uniform" : "blue",
            'name_tag' : True,
            'rank_tag' : True,
            'muffler' : True,

        }

        await websocket.send_json(result_msg)
        # if type(result_list) is list:

        #     for result_msg in result_list:
        #         print(result_msg)
        #         if 'path' in result_msg:
        #             result_img = cv2.imread(result_msg['path'])
        #             result_photo = img_2_photo(result_img)
        #             result_msg['photo'] = result_photo  
        #             result_msg['uniform'] = 2
        #             result_msg['type'] = "result"
        #         print(f"ㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁ")
        #         print(result_msg)
        #         await websocket.send_json(result_msg)
        # else:
        #     await websocket.send_json(result_list)
    camera_id = str(uuid.uuid4())



