from datetime import datetime


from app.api.broker.image import ImageBroker

from app.api.worker.random_ai import RandomAI
from app.api.worker.worker import SingleWorker

class RandomWorkBroker(ImageBroker):
    def __init__(self, ws, id):
        super().__init__(ws, id)
        self.ai = RandomAI()
        self.worker = SingleWorker(ws=ws)
    
    def execute_task(self, photo, work_start):
        # 파일 경로 지정
        name = datetime.now().strftime("%H-%m-%s")
        path = f'{self.SAVE_PATH}/{self.id}_{name}.jpg'

        person_result = self.capture_human(photo=photo, path=path)

        # 이미지 읽기
        print(person_result)
        if person_result:
            self.send_task(msg=path)
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
        self.worker.add_task(path=msg, ai=self.ai)


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