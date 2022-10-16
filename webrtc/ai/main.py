import sys

sys.path.append("/ai/OZEngine/.")

print(sys.path)

import cv2
import os
from OZEngine.person_detectors.PersonDetector import PersonDetector
from OZEngine.model import OmilZomil
    
person_detect = PersonDetector()
omil = OmilZomil(uniform_type='FULL_DRESS')

print("hello")
path = f"./webrtc_image.jpg"
img = cv2.imread(path)
# result = person_detect.detect(img)
result = omil.detect(img)
print(result)