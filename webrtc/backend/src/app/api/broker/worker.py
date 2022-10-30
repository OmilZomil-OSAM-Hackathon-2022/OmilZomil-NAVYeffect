from datetime import datetime, timedelta


from app.api.broker.image import ImageBroker

from app.api.worker.random_ai import RandomAI
from app.api.worker.worker import SingleWorker


EMPTY_PERSON_SECOND = 10

class WorkerBroker(ImageBroker):
    def __init__(self, ws, id, db, guardhouse):
        super().__init__(ws, id, db, guardhouse)
        
  
class SingleWorkerBroker(WorkerBroker):
    def __init__(self, ws, id, db, guardhouse):
        super().__init__(ws, id, db, guardhouse)
        self.ai = None
        self.worker_creater = SingleWorker  # worker 생성 클래스
        self.now_worker = None      # 현재 동작중인 worker
        self.last_person_time = datetime.now() - timedelta(seconds=EMPTY_PERSON_SECOND) # 처음은 무조건 새로운 사람이니깐
    
    
    def execute_task(self, photo, work_start):
        # 파일 경로 지정
        now_time = datetime.now()
        name = now_time.strftime("%H-%m-%s")
        path = f'{self.SAVE_PATH}/{self.id}_{name}.jpg'

        # 사람 유무 인식
        person_result = self.capture_human(photo=photo, path=path)

        # 사람 있으면 worker에게 업무 전달
        if person_result:

            # 해당 시간동안 사람이 없었는 경우 => 새로운 사람이다.
            if now_time - self.last_person_time > timedelta(seconds=EMPTY_PERSON_SECOND):
                self.now_worker = self.worker_creater(db=self.db, ai=self.ai, guardhouse=self.guardhouse)
                # 처음 업무를 받아서 업무를 처리
                msg = self.now_worker.create_task(path=path)

            else:
                # 이전에 있던 사용자로 업무 지시
                msg = self.order_worker(path)

            # 프론트에 맞게 네이밍 변경
            msg['kind'] = msg.pop('uniform')

            # 시간 갱신
            self.last_person_time = now_time

        else:
            msg = {
                "photo": photo,
                "person": person_result,
                "msg" : "사람이 아닙니다."
            }

        # 처리 결과 반환
        return msg
       
    def order_worker(self, path):
        msg = self.now_worker.add_task(path=path)
        return msg
   
class RandomSingleWorkerBroker(SingleWorkerBroker):
    
    def __init__(self, ws, id, db, guardhouse):
        super().__init__(ws, id, db, guardhouse)
        self.ai = RandomAI()
