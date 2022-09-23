
from .utils import *
import numpy as np
import cv2
from matplotlib import pyplot as plt

def check_person(org_img):
    img = org_img.copy()
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    body_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')
    body = body_cascade.detectMultiScale(gray_img, 1.01, 10)

    for (x,y,w,h) in body:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)

    plt_imshow(["body"], img)
    return None