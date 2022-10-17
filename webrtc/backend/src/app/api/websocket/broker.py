import cv2
from datetime import datetime
from app.core.config import settings
import socket

from app.api.websocket.camera import capture, check_human, check_omil


IP, PORT = settings.WORKER_SERVER

class Broker:
    SAVE_PATH = f"{settings.IMAGE_PATH}/queue"

    def __init__(self, ws, id):
        self.id = id
        self.ws = ws
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((IP, PORT))

    async def give_task(self, data):
        # 사진 분석
        img = capture(data)
        result = check_human(img)
        # 추후 해당 부분 삭제 img
        # result['img'] = data

    
        # 사람이 아니면 처리 X
        if not result['human']:
            return result
        
        # 저장
        name = datetime.now().strftime("%H-%m-%s")
        path = f'{self.SAVE_PATH}/{self.id}_{name}.jpg'
        self.save_img(img, path)

        # task 전송
        msg = path
        print(result)
        result['omil'] = check_omil(img)
        result['task'] = self.send_task(msg=msg)
        return result

    def send_task(self, msg):
        # self.socket.sendall(bytes(msg, 'ascii'))
        # return check_omil(img)
        pass
    def save_img(self, img, path):
        print(path)
        cv2.imwrite(path, img)
        print(f"저징 완료 {path}")
