import traceback
from datetime import datetime, timedelta
import cv2

from app.ai.OZEngine.person_detectors.PersonDetector import PersonDetector
from app.ai.OZEngine.model import OmilZomil



from app.api.websocket.image import photo_2_img, img_2_photo
from app.api.simple.worker import SimpleWorker

EMPTY_PERSON_SECOND = 10



class BaseBroker:
    def __init__(self, id, db):
        self.id = id
        self.db = db
        self.last_person_time = datetime.now() - timedelta(seconds=EMPTY_PERSON_SECOND) # 처음은 무조건 새로운 사람이니깐
        self.worker = None
        self.end_detect = False

        

class SimpleBroker(BaseBroker):
    person_detector = PersonDetector()
    def __init__(self, id, db):
        super().__init__(id, db)
        self.ai = OmilZomil()

    def __del__(self):
        del self.ai

    def add_task(self, data, work_time):

        # 해당 이미지가 사람인지 판별
        img = photo_2_img(data['photo'])
        person_result = self.person_detector.detect(img)

        # 사람이 아니면 무시
        if not person_result:
            return {
                "msg" : "no human"
            }
        
        # 오랜만에 사람이 탐지 된 경우
        if work_time - self.last_person_time > timedelta(seconds=EMPTY_PERSON_SECOND):
            if self.end_detect: # 일정 시간 뒤 다시 인식
                self.end_detect = False # ai 탐지 초기화
            # 새 worker 생성
            self.worker = SimpleWorker(ai=self.ai, db=self.db, guardhouse=data['name'])

        self.last_person_time = work_time # 사람이니깐 시간 갱신 - ai 가 탐지 완료후 사람이 탐지된 경우 탐지 시간 갱신

        # ai 처리가 끝난 경우 그대로 반환
        if self.end_detect:
            return {
                "msg" : "detect end"
            }        
        # worker로 이미지 처리
        result_msg = self.worker.execute(img=img)
        # 인식 홧수 초과시 더이상 인식 X
        if self.worker.expiration_count == 0:
            self.end_detect = True

        return result_msg
    
