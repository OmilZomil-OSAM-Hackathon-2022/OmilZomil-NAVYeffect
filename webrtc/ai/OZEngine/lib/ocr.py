from lib.defines import *
from sys import path as syspath
from os.path import abspath, join, dirname
from requests.exceptions import ConnectionError
import numpy as np
import cv2
import requests

syspath.append(abspath(join(dirname(__file__), '../../lib/')))
# from lib.utils import *


print('OCR loaded!')
API_URL = 'https://dapi.kakao.com/v2/vision/text/ocr'
KEY = '5b60f7aeb82db9bf02f3eea5a94a69c0'


def str_encoder(str):
    str = str.replace('\\', "#'W'#").replace('/', "#'R'#").replace(':',
                                                                   "#'C'#").replace('*', "#'S'#").replace('?', "#'Q'#").replace('"', "#'d'#")
    str = str.replace('<', "#'L'#").replace(
        '>', "#'G'#").replace('/', "#'O'#").replace('.', "#'E'#")
    return str


def str_decoder(str):
    str = str.replace("#'W'#", '\\').replace("#'R'#", '/').replace("#'C'#",
                                                                   ':').replace("#'S'#", '*').replace("#'Q'#", '?').replace("#'D'#", '"')
    str = str.replace("#'L'#", '<').replace(
        "#'G'#", '>').replace("#'O'#", '/').replace("#'E'#", '.')
    return str


def draw_rectangle(image, p1, p3, color, border, padding):
    pp1 = (p1[0]-padding, p1[1]-padding)
    pp2 = (p3[0]+padding, p3[1]+padding)
    cv2.rectangle(image, pp1, pp2, color, border)


def OCR(img):
    headers = {'Authorization': 'KakaoAK {}'.format(KEY)}
    jpeg_img = cv2.imencode(".jpg", img)[1]
    data = jpeg_img.tobytes()
    try:
        ocr_json = requests.post(API_URL, headers=headers, files={"image": data})
    except ConnectionError as error_msg:
        raise Exception("네트워크 오류")
        
    outputs = ocr_json.json()['result']


    return outputs
