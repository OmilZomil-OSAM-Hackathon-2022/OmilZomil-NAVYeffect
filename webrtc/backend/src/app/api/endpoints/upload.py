from typing import List
import cv2
import numpy as np
from datetime import datetime
import uuid


from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.orm import Session

from app.api.websocket.image import photo_2_img, img_2_photo
from app.api import deps

from app.api.simple.broker import SimpleBroker


router = APIRouter()


@router.post("/image")
async def create_upload_files(files: List[UploadFile] = File(...), db: Session = Depends(deps.get_db)):
    # 기본 데이터
    connect_start_time = datetime.now()
    camera_id = str(uuid.uuid4())

    # 브로커 생성    
    broker = SimpleBroker(id=camera_id, db=db)
    
    # 수신 중
    print(" 이미지 수신 시작")
    guardhouse = "계룡대 1정문"

    result_msg = {}
    for file in files:
        print(f"{file.filename} - 처리 시작")
        # img 로 변환
        contents = await file.read()
        img = cv2.imdecode(np.fromstring(contents, np.uint8), cv2.IMREAD_COLOR)
        # broker에게 전달
        work_start = datetime.now()
        msg = broker.once_task(img=img, guardhouse=guardhouse, work_time=work_start)
        msg['working_time'] = datetime.now() - work_start
        msg.pop('photo')
        result_msg[file.filename] = msg
    
    result_msg['total_time'] = datetime.now() - connect_start_time
    print(f"업로드 완료 - {datetime.now() - connect_start_time}")
    return result_msg