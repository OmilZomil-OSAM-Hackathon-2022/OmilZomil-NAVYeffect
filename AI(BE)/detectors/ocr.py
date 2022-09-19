import numpy as np
import cv2
import requests
from lib.utils import *

API_URL = 'https://dapi.kakao.com/v2/vision/text/ocr'
KEY = '5b60f7aeb82db9bf02f3eea5a94a69c0'

def str_encoder(str):
    str = str.replace('\\', "#'W'#").replace('/', "#'R'#").replace(':', "#'C'#").replace('*', "#'S'#").replace('?', "#'Q'#").replace('"', "#'d'#")
    str = str.replace('<', "#'L'#").replace('>', "#'G'#").replace('/', "#'O'#").replace('.', "#'E'#")
    return str


def str_decoder(str):
    str = str.replace("#'W'#", '\\').replace("#'R'#", '/').replace("#'C'#", ':').replace("#'S'#", '*').replace("#'Q'#", '?').replace("#'D'#", '"')
    str = str.replace("#'L'#", '<').replace("#'G'#", '>').replace("#'O'#", '/').replace("#'E'#", '.')
    return str


def draw_rectangle(image, p1, p3, color, border, padding):
    pp1 = (p1[0]-padding, p1[1]-padding)
    pp2 = (p3[0]+padding, p3[1]+padding)
    cv2.rectangle(image, pp1, pp2, color, border)

def ocr(image):
    c_image = image.copy()
    boxes = np.zeros(image.shape[:2], np.uint8)  # height, width
    headers = {'Authorization': 'KakaoAK {}'.format(KEY)}
    jpeg_image = cv2.imencode(".jpg", image)[1]
    data = jpeg_image.tobytes()
    ocr_json = requests.post(API_URL, headers=headers, files={"image": data})
    
    roi_list = []
    res = ''
    outputs = ocr_json.json()['result']
    for output in outputs:
        padding = 10 # 10
        p1,p2,p3,p4 = output['boxes']  # LU RU RD LD
        
        try:
            draw_rectangle(c_image, p1, p3, GREEN, 2, padding)
            draw_rectangle(boxes, p1, p3, WHITE, -1, padding)
        except Exception as e:
                print("out of image !! ", e)
            
        if not output['recognition_words'] == '':
            res += " ".join(output['recognition_words']) + " "
        
    res = res.replace('ø', '').strip().replace(' ', '_')
    return {'str':str_encoder(res), 'img':c_image, 'boxes':boxes, 'roi_list':roi_list}
    