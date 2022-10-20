import cv2
from datetime import datetime, timedelta

from app.ai.OZEngine.person_detectors.PersonDetector import PersonDetector
from app.api.manager.worker import SingleWorker
from app.api.manager.ai import RandomAI
from app.api.websocket.image import img_2_photo, photo_2_img
from app.core.config import settings


EMPTY_PERSON_SECOND = 10
SAVE_PATH = f"{settings.IMAGE_PATH}/queue"

FRONT_NAME = {
    'uniform' : {
        1 : "null_value",
        2 : "black",
        3 : "blue",
        4 : "green",
    }
}

class Broker:
    """
    이미지를 받음
    받은 이미지를 사람 유무를 판별 -> 사람이 아니면 무시
    이미지를 저장
    새 이미지인 경우 worker를 생성
    worker에게 업무를 전달 - 저장한 이미지 경로를 전달
    websocket에게 업무 수행 완료 메세지를 전달
    """


    def __init__(self, ws, id, db, guardhouse):
        # 공유 정보 등록
        self.id = id
        self.ws = ws
        self.db = db
        self.guardhouse=guardhouse

        # 사용 ai 등록
        self.ai = RandomAI()  # ai는 카메라 별로 1개씩 존재
        self.person_detector = PersonDetector()
        

        # 현재 동작중인 worker 관리
        self.worker_creater = SingleWorker  # worker 생성 클래스
        self.now_worker = None      # 현재 동작중인 worker
        self.last_person_time = datetime.now() - timedelta(seconds=EMPTY_PERSON_SECOND) # 처음은 무조건 새로운 사람이니깐
    
    def image_is_person(self, photo, path):
        # 해당 이미지가 사람인지 판별
        img = photo_2_img(photo)
        person_result = self.person_detector.detect(img)

        # 사람이면 이미지를 저장
        if person_result:
            cv2.imwrite(path, img)
        
        return person_result


class SingleBroker(Broker):
    """
    단일 작업하는 broker
    업무를 바로 수행
    """
    
    def add_task(self, photo, work_start):
        # 파일 경로 지정
        name = datetime.now().strftime("%H-%m-%s")
        path = f'{SAVE_PATH}/{self.id}_{name}.jpg'

        # 이미지 처리
        person_result = self.image_is_person(photo=photo, path=path)
        # 사람이면 worker 생성
        if person_result:
            # 마지막 사람이 있던 시간으로부터 오래됬으면 새로운 사람으로 인식
            if work_start - self.last_person_time > timedelta(seconds=EMPTY_PERSON_SECOND):
                # worker 생성 및 첫 업무 수행              
                self.now_worker = self.worker_creater(db=self.db, ai=self.ai, guardhouse=self.guardhouse)
            
            # 업무 수행 지시
            msg = self.now_worker.execute(path=path)
                
            # 시간 갱신
            self.last_person_time = work_start

            # 프론트에 맞게 네이밍 변경
            msg['kind'] = FRONT_NAME['uniform'][msg.pop('uniform')]
            print(msg)
            return msg
        
        # 서람이 아닌 경우는 해당 메세지 반환
        msg = {
            "photo": photo,
            "person": person_result,
            "msg" : "사람이 아닙니다."
        }
        # 처리 결과 반환
        return msg
