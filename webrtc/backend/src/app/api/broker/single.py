from app.api.broker.base import BaseBroker



class SingleBroker(BaseBroker):
    is_save_queue = False
    worker_creater = None
    
    def __init__(self, id, db):
        super().__init__(id)
        self.db = db
        
    def add_task(self, img, guardhouse, work_time):
        
        # 사람 확인
        person_msg = self.check_person(img=img)
        if person_msg['status'] != "human":
            return person_msg
        
        # worker 업데이트
        self.update_worker(db=self.db)
        
        # 업무 지시
        result_msg = self.now_worker.execute(img=img)
        return result_msg

