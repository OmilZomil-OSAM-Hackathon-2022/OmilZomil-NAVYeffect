# worker를 생성해주는 객체
# ai 실행 주기를 설정
import cv2
from datetime import datetime, timedelta


from app.core.config import settings
from app.ai.OZEngine.person_detectors.PersonDetector import PersonDetector
from app.api.websocket.image import photo_2_img, img_2_photo

EMPTY_PERSON_SECOND = 10
EXPIRATION_COUNT = 5


INSPECTION_PATH = f"{settings.IMAGE_PATH}/inspection"


class BaseBroker:
    person_detector = PersonDetector()
    worker_creater= None
    
    def __init__(self, id):
        self.id = id
        self.last_person_time = datetime.now() - timedelta(seconds=EMPTY_PERSON_SECOND) # 처음은 무조건 새로운 사람이니깐
        self.now_worker = None

    def update_worker(self, **args):
        # 1. 오랜만에 온 사람인 경우 
        if work_time - self.last_person_time > timedelta(seconds=EMPTY_PERSON_SECOND):
            self.now_worker = self.worker_creater(**args)

    def check_person(self, img):
        
        # 사람 유무를 판별
        person_result = self.person_detector.detect(img)

        # 사람이 아니면 무시
        if not person_result:
            print(f" 사람이 아닙니다. 처리를 마칩니다.")
            return {
                "type" : "status",
                "status" : "no human",
            }
        else:
            print(f" 사람 확인")
            return {
                "type" : "status",
                "status" : "human",
            }



    def save_img(self, guardhouse, work_time):
        img_path = f"{QUEUE_PATH}/{guardhouse}_{work_time.strftime('%H-%m-%s')}.jpg"
        cv2.imwrite(img_path, img)
        pass

        