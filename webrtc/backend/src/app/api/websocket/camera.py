
import base64
import cv2
import numpy as np


from app.ai.OZEngine.person_detectors.PersonDetector import PersonDetector
from app.ai.OZEngine.model import OmilZomil
from app.api.websocket.manager import Manager


omil_detector = OmilZomil(uniform_type='FULL_DRESS')
person_detector = PersonDetector()


class Camera:
    def __init__(self, ws):
        self.manager = Manager(ws=ws)
        

    async def capture(self, data):
        img = cv2.imdecode(np.fromstring(base64.b64decode(data.split(',')[1]), np.uint8), cv2.IMREAD_COLOR)
        try:
            result = person_detector.detect(img)
        except TypeError as e:
            print(f"사람 인식 시패 {e}")
            return {
                "msg": "사람 아님"
            }

        if result:
            # 이미지
            self.manager.give_task(img)

            return {
                "msg" : "사람임",
                "data" : result,
            }
        else:
            return {
                "msg" : "사람 아님",
                "data" : result,
            }

