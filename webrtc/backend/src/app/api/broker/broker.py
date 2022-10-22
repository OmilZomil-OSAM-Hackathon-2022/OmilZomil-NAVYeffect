import cv2
import base64
import numpy as np
import random
from app.core.config import settings

# from app.ai.OZEngine.model import OmilZomil
from app.ai.OZEngine.person_detectors.PersonDetector import PersonDetector
from app.api.worker.random_ai import RandomAI


class BrokerBase:
    """
    테스트용으로 단순 전달
    """
    def __init__(self, ws, id, db, guardhouse):
        self.id = id
        self.ws = ws
        self.db = db
        self.guardhouse=guardhouse


    def execute_task(self, photo, work_start):
        return {
            "photo": photo,   # 이미지는 단순 전달
            "kind" : random.choice(["black", 'blue', 'green']),
            "hair" : True,
            "nametag" : False,
            "leveltag" : bool(random.getrandbits(1)),
            "muffler" : bool(random.getrandbits(1)),
            "neck" : bool(random.getrandbits(1)),
        }
    def photo_2_img(self, photo):
        img = cv2.imdecode(np.fromstring(base64.b64decode(photo.split(',')[1]), np.uint8), cv2.IMREAD_COLOR)        
        return img
    
    def img_2_photo(self, img):
        photo = cv2.imencode('.jpg', img)[1]
        photo_as_text = base64.b64encode(photo)
        return "data:image/jpeg;base64," + photo_as_text.decode('utf-8')

class SimpleBroker(BrokerBase):
    """
    ai 요구사항만 맞춰서 실행
    병렬 처리 X
    버퍼 X - 파일로 저장 X
    단지 카메라 객체만 유지
    DB에 저장 X
    """
    def __init__(self, ws, id, db, guardhouse):
        super().__init__(ws, id, db, guardhouse)
        # self.omil_detector = OmilZomil(uniform_type='FULL_DRESS')
        self.person_detector = PersonDetector()
        self.ai = RandomAI()



    def execute_task(self, photo, work_start):

        # 사진 분석
        img = self.photo_2_img(photo)
        person_result = self.person_detector.detect(img)
        if person_result:
            msg =  {
                "photo": photo,
                "person": person_result,
            }
            result = self.ai.detect(img)
            msg.update(result)
            # 처리 결과 반환
            return msg
        else:
            # 처리 결과 반환
            return {
                "photo": photo,
                "person": person_result,
            }

