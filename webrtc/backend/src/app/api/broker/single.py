from app.api.broker.base import BaseBroker

from app.api.worker.ai import AIWorker, FrontAIWorker
from app.api.worker.single import SingleWorker

class SingleBroker(BaseBroker):
    is_save_queue = False
    worker_creater = SingleWorker
    
    def __init__(self, id, db):
        super().__init__(id)
        self.db = db
        
    def add_task(self, img, guardhouse, work_time):
        
        # 사람 확인
        person_msg = self.check_person(img=img)
        if person_msg['status'] != "human":
            return person_msg
        
        # worker 업데이트
        # self.update_worker(work_time=work_time)   # 특정 시간마다 오밀 객체 생성
        # self.now_worker = self.worker_creater(work_time=work_time) # 모든 이미지 마다 오밀 객체 생성
        self.now_worker = self.worker_creater(guardhouse=guardhouse, db=self.db) # 모든 이미지 마다 오밀 객체 생성

        # 업무 지시
        result_msg = self.now_worker.execute(img=img, guardhouse=guardhouse, work_time=work_time)
        return result_msg


