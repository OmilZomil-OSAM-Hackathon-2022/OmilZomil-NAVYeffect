import cv2
import base64
import numpy as np
import os
import asyncio

from multiprocessing import Process, Queue


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