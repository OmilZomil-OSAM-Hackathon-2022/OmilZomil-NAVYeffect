import socket
from datetime import datetime
import cv2
import base64
import os
import time

from app.api.broker.broker import SimpleBroker
from app.util.memory import memory_usage
from app.core.config import settings
from app.api.worker.random_ai import RandomAI
IP, PORT = settings.WORKER_SERVER

class ImageBroker(SimpleBroker):
    """
    이미지 저장 
    """
    SAVE_PATH = f"{settings.IMAGE_PATH}/queue"
  

    def execute_task(self, photo, work_start):
        # 파일 경로 지정
        name = datetime.now().strftime("%H-%m-%s")
        path = f'{self.SAVE_PATH}/{self.id}_{name}.jpg'

        person_result = self.capture_human(photo=photo, path=path)

        # 이미지 읽기
        if not person_result:
            print(person_result)
            result_photo = self.read_img(path)
            memory_usage()
            
            # 삭제
            self.delete_img(path)
        else:
            print(person_result)
            result_photo = photo
        # 처리 결과 반환
        result_msg = {
            "photo": result_photo,
            "person": person_result,
            "path": path,
        }

        return result_msg

    def capture_human(self, photo, path):
        
        # 사진 분석
        img = self.photo_2_img(photo)
        person_result = self.person_detector.detect(img)

        # 사람이 아니면 처리 X
        if not person_result:
            return person_result

        # 이미지 저장
        self.save_img(img, path)
        return person_result

    def save_img(self, img, path):
        cv2.imwrite(path, img)
        print(f"저징 완료 {path}")
    
    def read_img(self, path):
        img = cv2.imread(path)
        photo = self.img_2_photo(img)
        return photo

    def delete_img(self, path):
        if os.path.isfile(path):
            os.remove(path)
            print("이미지 읽은후 삭제 완료")
        else:
            print("이미지 삭제 실패")
            raise Exception

"""



class SingleBroker(Broker):
    def __init__(self, ws, id):
        super().__init__(ws, id)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((IP, PORT))
    
    def send_task(self, msg):
        # self.socket.sendall(bytes(msg, 'ascii'))
        path = msg
        img = cv2.imread(path)
        print(img)
        return check_omil(img)
        pass

class SocketBroker(Broker):
    
    def __init__(self, ws, id):
        super().__init__(ws, id)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((IP, PORT))
    
    def send_task(self, msg):
        self.socket.sendall(bytes(msg, 'ascii'))
        # return check_omil(img)
        pass
"""