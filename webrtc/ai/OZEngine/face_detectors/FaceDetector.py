# import dlib
from mtcnn import MTCNN

import cv2
from OZEngine.lib.utils import *

# class FaceDetector():
#     def __init__(self):
#         self.detector = dlib.get_frontal_face_detector()
    
#     def detect(self, img):
#         detected_boxes = self.detector(img)
#         if len(detected_boxes) >= 2:
#             raise("두명이상 인식 불가능합니다!")
        
#         print(len(detected_boxes))
#         box = detected_boxes[0]
#         return (box.top(), box.left()), (box.bottom(), box.right())

class FaceDetector():
    def __init__(self):
        self.detector = detector = MTCNN()
    
    def detect(self, img):
        detections = self.detector.detect_faces(img)
        for detection in detections:
            score = detection["confidence"]
            if score > 0.90:
                x, y, w, h = detection["box"]
                x, y, w, h = int(x), int(y), int(w), int(h)
                return ((y,x), (y+h, x+w))
        return None