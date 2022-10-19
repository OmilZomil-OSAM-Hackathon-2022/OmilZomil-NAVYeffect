import cv2
import base64
import numpy as np
import os
import asyncio
from omil.app.crud import rank as rank_crud

from multiprocessing import Process, Queue

class Worker:
    def __init__(self, db):
        self.result_state = None
        self.db = db

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


class StatusWorker(Worker):
    def __init__(self, db):
        super().__init__(db)
        self.result_state = None
        print("worker 생성")

    def update_status(self, data_list):
        if self.result_state is None:
            print(f"기존 데이터가 없어 갱신 - {self.result_state} - {data_list}")
            self.result_state = data_list
            return True

        for idx, val in data_list.items():
            # 상태가 양호인경우만 업데이트
            if type(val) == bool and val == True:
                self.result_state[idx] = val           
                print(f"상태 업데이트 {idx} - {val}")

        print(f"상태 업데이트 {self.result_state}")
    def save_db(self):
        pass

class SingleWorker(StatusWorker):

    def add_task(self, path, ai):
        # 이미지를 읽어 ai 동작
        img = cv2.imread(path)
        result = ai.detect(img)

        print("AI 처리")
        # 이전 데이터 갱신
        self.update_status(data_list=result)
        # DB에 저장
        print("DB에 저장")

        result_photo  = self.img_2_photo(img)
        # 메세지 제작
        msg =  {
            "photo": result_photo,
            "img_result": result,
            "total_result": self.result_state,
            "path": path,
        }
        msg.update(self.result_state)
    
        # 프론트에게 응답
        return msg




        pass

    pass




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
"""