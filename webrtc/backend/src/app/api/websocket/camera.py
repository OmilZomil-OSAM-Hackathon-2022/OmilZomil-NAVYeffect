
import base64
import cv2
import numpy as np


from app.ai.OZEngine.person_detectors.PersonDetector import PersonDetector
from app.ai.OZEngine.model import OmilZomil


omil_detector = OmilZomil(uniform_type='FULL_DRESS')
person_detector = PersonDetector()


def capture(data):
    img = cv2.imdecode(np.fromstring(base64.b64decode(data.split(',')[1]), np.uint8), cv2.IMREAD_COLOR)
    return img
    
def check_human(img):
    try:
        result = person_detector.detect(img)
    except TypeError as e:
        print(f"사람 인식 시패 {e}")
        return {
            "msg": "사람 아님"
        }

    if result:
        return {
            "msg" : "사람임",
            "human" : True,
            "data" : result,
        }
    else:
        return {
            "msg" : "사람 아님",
            "human": False,
            "data" : result,
        }
