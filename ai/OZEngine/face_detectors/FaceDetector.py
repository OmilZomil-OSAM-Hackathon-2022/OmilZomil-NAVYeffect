import dlib
import cv2
from OZEngine.lib.utils import *

class FaceDetector():
    def __init__(self):
        self.detector = dlib.get_frontal_face_detector()
    
    def detect(self, img):
        img2 = img.copy()
        detected_boxes = self.detector(img)
        for box in detected_boxes:
            print('box')
            # print(box)
        # cv2.rectangle(img2, (res_box[0], res_box[1]),(res_box[2], res_box[3]), (0, 255, 0), 2)
        