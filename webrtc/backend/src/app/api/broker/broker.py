import cv2
from datetime import datetime
from app.core.config import settings
import socket

from app.api.websocket.camera import capture, check_human, check_omil
# from app.ai.OZEngine.model import OmilZomil
from app.ai.OZEngine.person_detectors.PersonDetector import PersonDetector




IP, PORT = settings.WORKER_SERVER


class BrokerBase:
    """
    테스트용으로 단순 전달
    """
    def __init__(self, ws, id):
        self.id = id
        self.ws = ws

    def execute_task(self, img, work_start):
        return {
            "photo": img,
        }

class SimpleBroker(BrokerBase):
    """
    ai 요구사항만 맞춰서 실행
    병렬 처리 X
    버퍼 X - 파일로 저장 X
    단지 카메라 객체만 유지
    DB에 저장 X
    """
    def __init__(self, ws, id):
        super().__init__(ws, id)
        # self.omil_detector = OmilZomil(uniform_type='FULL_DRESS')
        self.person_detector = PersonDetector()


    def execute_task(self, photo, work_start):
        img = capture(photo)
        person_result = self.person_detector.detect(img)
        return {
            "photo": photo,
            "person": person_result,
        }

    pass

