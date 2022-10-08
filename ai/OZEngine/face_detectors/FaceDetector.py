import dlib
import cv2
from OZEngine.lib.utils import *

class FaceDetector():
    def __init__(self):
        self.detector = dlib.get_frontal_face_detector()
    
    def detect(self, img):
        detected_boxes = self.detector(img)
        print('boxe :', type(detected_boxes))
        if len(detected_boxes) >= 2:
            raise("두명이상 인식 불가능합니다!")
        
        box = detected_boxes[0]
        return (box.top(), box.left()), (box.bottom(), box.right())