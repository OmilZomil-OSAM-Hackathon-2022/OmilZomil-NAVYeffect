import cv2
import base64
import numpy as np
import os
import asyncio
from app.api.worker.image_box import ImageBox

from omil.app.crud import rank as rank_crud

from multiprocessing import Process, Queue

class Worker:
    def __init__(self, db, ai, guardhouse):
        self.result_state = None
        self.db = db
        self.ai = ai
        self.image_box = ImageBox(ai=ai, guardhouse=guardhouse)

    def photo_2_img(self, photo):
        img = cv2.imdecode(np.fromstring(base64.b64decode(photo.split(',')[1]), np.uint8), cv2.IMREAD_COLOR)        
        return img
    
    def img_2_photo(self, img):
        photo = cv2.imencode('.jpg', img)[1]
        photo_as_text = base64.b64encode(photo)
        return "data:image/jpeg;base64," + photo_as_text.decode('utf-8')
    
    def delete_img(self, path):
        if os.path.isfile(path):
            os.remove(path)
        else:
            print("이미지 삭제 실패")
            raise Exception

class SingleWorker(Worker):

    def add_task(self, path):
        # 이미지를 읽어 ai 동작
        img = cv2.imread(path)
        
        print("AI 처리")
        report = self.image_box.image_process(image=img, path=path)
        
        # 답장
        photo  = self.img_2_photo(img)
        # 메세지 제작
        msg =  {
            "photo": photo,
            "report": report,
            "path": path,
        }

        msg.update(report)
    
        # 프론트에게 응답
        return msg


"""

class Worker:
    pass

    def __init__(self, ws):
        self.ws = ws
        self.is_run = False
        self.q = Queue()

        # 프로세스
        # queue
        
        pass

    def photo_2_img(self, photo):
        img = cv2.imdecode(np.fromstring(base64.b64decode(photo.split(',')[1]), np.uint8), cv2.IMREAD_COLOR)        
        return img
    
    def img_2_photo(self, img):
        photo = cv2.imencode('.jpg', img)[1]
        photo_as_text = base64.b64encode(photo)
        return "data:image/jpeg;base64," + photo_as_text.decode('utf-8')
    
    def delete_img(self, path):
        if os.path.isfile(path):
            os.remove(path)
        else:
            print("이미지 삭제 실패")
            raise Exception

class SingleWorker(Worker):
    def __init__(self, ws, ai):
        super().__init__(ws)
        self.ai = ai

    def add_task(self, path):
        # 그냥 실행
        return self.run(path)
    
        

    def run(self, path):
        # 이미지 읽기
        print("worker 동작중")
        img = cv2.imread(path)

        # 이미지 처리
        result = self.ai.detect(img)
        photo = self.img_2_photo(img=img)

        # 전달
        msg = {
            "type": result,
            "msg": f"SingleWorker task",
            "photo": photo,   # 이미지는 단순 전달

        }
        msg.update(result)
        return msg


class StatusWorker(Worker):
    def __init__(self, db):
        super().__init__(db)
        self.result_state = {}
        print("worker 생성")

    def update_status(self, data_list):
        if self.result_state is None:
            print(f"기존 데이터가 없어 갱신 - {self.result_state} - {data_list}")
            # DB에 데이터 생성
            self.create_db_data()
            return True

        for idx, val in data_list.items():
            # 상태가 양호인경우만 업데이트
            if type(val) == bool and val == True:
                self.result_state[idx] = val           
                print(f"상태 업데이트 {idx} - {val}")

        print(f"상태 업데이트 {self.result_state}")

    def get_good_img_path(self):
        pass

    def create_db_data(self, data_list):

        self.result_state = {

        }


        log = InspectionLog(
            guardhouse=log.guardhouse,
            affiliation=log.affiliation,
            rank=log.rank,
            name=log.name,
            uniform=log.uniform,
            image_path=log.image_path,
        )
        db.add(log)
        db.commit()
        db.refresh(log)


    def update_db_data(self):
        pass
"""