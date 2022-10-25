from datetime import datetime, timedelta
import cv2
import socket
import json

from app.ai.OZEngine.person_detectors.PersonDetector import PersonDetector
from app.core.config import settings
from app.api.websocket.image import photo_2_img, img_2_photo


EMPTY_PERSON_SECOND = 10


IP, PORT = settings.WORKER_SERVER

QUEUE_PATH = f"{settings.IMAGE_PATH}/queue"

class SocketBroker:
    person_detector = PersonDetector()

    pass

    def __init__(self, id):
        self.id = id
        self.last_person_time = datetime.now() - timedelta(seconds=EMPTY_PERSON_SECOND) # 처음은 무조건 새로운 사람이니깐
        # 소켓 연결
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((IP, PORT))
        print("소켓 연결 완료")


    def add_task(self, photo, guardhouse, work_time):

        img = photo_2_img(photo)
        # 사람 유무를 판별
        person_result = self.person_detector.detect(img)
        
        # 사람이 아니면 무시
        if not person_result:
            return {
                "result" : "no human"
            }
        
        # 사람인 경우 이미지 파일 저장
        img_path = f"{QUEUE_PATH}/{guardhouse}_{work_time.strftime('%H-%m-%s')}.jpg"
        cv2.imwrite(img_path, img)

        # 1. 오랜만에 온 사람인 경우
        if work_time - self.last_person_time > timedelta(seconds=EMPTY_PERSON_SECOND):
            msg = {
                "guardhouse" : guardhouse, 
                "path": img_path,
                }
        # 2. 연속적인 사람인 경우
        else:
            msg = {
                "path": img_path,
            }
        # 메세지 전송
        json_msg = json.dumps(msg)
        self.socket.sendall(bytes(json_msg, 'ascii'))

        # 프론트에게 1차 응답
        return {
            "result" : "send task",
            "msg": msg,
            }
        
    