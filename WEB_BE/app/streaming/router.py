from fastapi import APIRouter, Depends, Body, HTTPException
from fastapi.responses import JSONResponse, FileResponse
from fastapi.requests import Request
from sqlalchemy.orm import Session
from typing import List

from core.db import get_db

from app.streaming.socket import ConnectionManager

router = APIRouter(
    prefix="/streaming",
    tags=[" 스트리밍"],
    responses={404: {"description": "Not found"}},
)


manager = ConnectionManager()


@router.get("/")
async def get():
    return FileResponse("static/camera/index.html")


@router.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)
    # fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    # w = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    # h = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    # fps = cap.get(cv2.CAP_PROP_FPS)  # 카메라에 따라 값이 정상적, 비정상적
    # w, h, fps = 960, 480, 20
        
    # 1프레임과 다음 프레임 사이의 간격 설정
    # delay = round(1000 / fps)

    # 웹캠으로 찰영한 영상을 저장하기
    # cv2.VideoWriter 객체 생성, 기존에 받아온 속성값 입력
    # video_out = cv2.VideoWriter('output.mp4', fourcc, fps, (240, 320), False)
    try:
        while True:
            data = await websocket.receive_text()
            img = cv2.imdecode(np.fromstring(base64.b64decode(data.split(',')[1]), np.uint8), cv2.IMREAD_COLOR)
            cv2.imshow('image', img)
            # cv2.imwrite('grayIronMan.jpg', img)
            # print('----------------------------------------------------')
            # print(type(img))
            # print(img.shape)
            # print(type(img.shape))
            # print('----------------------------------------------------')
            # video_out.write(img)
            await manager.send_personal_message(f"You wrote: {data}", websocket)
            await manager.broadcast(f"Client #{client_id} says: {data}")
    except WebSocketDisconnect:
        print("end")
        # video_out.release()
        manager.disconnect(websocket)
        await manager.broadcast(f"Client #{client_id} left the chat")