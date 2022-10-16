import base64
import cv2
import numpy as np


from app.ai.OZEngine.person_detectors.PersonDetector import PersonDetector
from app.ai.OZEngine.model import OmilZomil

omil_detector = OmilZomil(uniform_type='FULL_DRESS')
person_detector = PersonDetector()

def data_processing(data):
    img = cv2.imdecode(np.fromstring(base64.b64decode(data.split(',')[1]), np.uint8), cv2.IMREAD_COLOR)
    try:
        result = person_detector.detect(img)
    except TypeError as e:
        print(f"사람 인식 시패 {e}")
        result = "None"
    if result:
        return {
            "msg" : "사람임",
            "data" : result,
        }
    else:
        return {
            "msg" : "사람 아님",
            "data" : result,
        }

