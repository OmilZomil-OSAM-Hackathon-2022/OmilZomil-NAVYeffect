import cv2
import base64
import numpy as np
import os
import asyncio

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


class SingleWorker(Worker):
    def __init__(self, db):
        super().__init__(db)
        self.result_state = None

    def add_task(self, path, ai):
        # 이미지를 읽어 ai 동작
        img = cv2.imread(path)
        result = ai.detect(img)

        print("AI 처리")
        # 이전 데이터 갱신

        # DB에 저장
        print("DB에 저장")

        result_photo  = self.img_2_photo(img)
        # 메세지 제작
        msg =  {
            "photo": result_photo,
            "ai_result": result,
            "path": path,
        }
        msg.update(result)
    
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