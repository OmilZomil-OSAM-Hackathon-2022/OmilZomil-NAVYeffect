from datetime import datetime, timedelta


from app.api.broker.image import ImageBroker

from app.api.worker.random_ai import RandomAI
from app.api.worker.worker import SingleWorker


EMPTY_PERSON_SECOND = 10

class WorkBroker(ImageBroker):
    def __init__(self, ws, id):
        super().__init__(ws, id)
  
class SingleWorkerBroker(WorkerBroker):
    def __init__(self, ws, id):
        super().__init__(ws, id)
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
                self.now_worker = worker_creater()
            # worker 동작
            result = self.order_worker(path)
            msg={
                "worker" : "사람 인식하여 worker 실행중임"
            }
            msg.update(result)


        else:
            msg = {
                "photo": photo,
                "person": person_result,
                "path": path,
            }

        # 처리 결과 반환
        return msg

        
        def order_worker(self, path):
            # result = self.worker.add_task(path=path)

            pass

    pass

class RandomSingleWorkerBroker(SingleWorkerBroker):
    
    def __init__(self, ws, id):
        super().__init__(ws, id)
        self.ai = RandomAI()

    def order_worker(self, path):
        result = self.worker.add_task(path=path, ai=self.ai)

        return result


    pass

class RandomSingleBroker(ImageBroker):
    def __init__(self, ws, id):
        super().__init__(ws, id)
        ai = RandomAI()
        self.worker = SingleWorker(ws=ws, ai=ai)
    
    def execute_task(self, photo, work_start):
        # 파일 경로 지정
        name = datetime.now().strftime("%H-%m-%s")
        path = f'{self.SAVE_PATH}/{self.id}_{name}.jpg'

        person_result = self.capture_human(photo=photo, path=path)

        # 이미지 읽기
        print(person_result)
        if person_result:
            result = self.send_task(msg=path)
            # 처리 결과 반환
            result_msg = {
                "person": person_result,
                "path": path,
            }
            result_msg.update(result)
            print(result_msg)
            return result_msg

        else:
            result_photo = photo
            # 처리 결과 반환
            result_msg = {
                "photo1": result_photo,
                "person": person_result,
                "path": path,
            }
            return result_msg

    def send_task(self, msg):
        print("업무 전달")
        return self.worker.add_task(path=msg)