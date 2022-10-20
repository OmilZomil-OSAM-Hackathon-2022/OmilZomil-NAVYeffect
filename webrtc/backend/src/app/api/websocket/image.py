
import cv2
import base64
import numpy as np


    
def photo_2_img(photo):
    """
    photo를 image로 변환
    img = numpy
    photo = base64
    """
    img = cv2.imdecode(np.fromstring(base64.b64decode(photo.split(',')[1]), np.uint8), cv2.IMREAD_COLOR)        
    return img

def img_2_photo(img):
    """
    image를 photo로 변환
    img = numpy
    photo = base64
    """
    photo = cv2.imencode('.jpg', img)[1]
    photo_as_text = base64.b64encode(photo)
    return "data:image/jpeg;base64," + photo_as_text.decode('utf-8')

