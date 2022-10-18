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
    

    def add_task(self, path, ai):
        # 그냥 실행

        # worker가 미실행인 경우 생성
        if not self.is_run:
            print("worker 생성")
            proc = Process(target=self.run, args=(self.q,))
            proc.start()
        else:
            pass
        

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
        print("업무 처리 완료 전달 직전")
        async def send_msg():
            await self.ws.send_json(msg)
        asyncio.get_running_loop().run_until_complete(send_msg())

        print("============================ 완료 ===============")

