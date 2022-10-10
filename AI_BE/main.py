import os, sys
import traceback
cur_path = os.getcwd()
engine_path = os.path.join(cur_path, 'OZEngine')
if engine_path not in sys.path:
    sys.path.append(engine_path)

import cv2
from operator import itemgetter
import matplotlib.pyplot as plt
# from matplotlib import font_manager,rc

from OZEngine.edge_detectors import Morph, HED
from OZEngine.lib.utils import *
from OZEngine import OmilZomil


org_img = cv2.imread('image/full_dress_uniform/person/9.jpg', cv2.IMREAD_COLOR)
# org_img = cv2.imread('image/militery_uniform/1.jpg', cv2.IMREAD_COLOR)
# org_img = cv2.imread('image/navy_service_uniform/1.jpg', cv2.IMREAD_COLOR)
img = cv2.resize(org_img, (500, 500))
hsv_dst, yCrCb_dst = histNorm(org_img)
# img = yCrCb_dst
plt_imshow(["org", "hsv_dst", "yCrCb_dst"], [org_img, hsv_dst, yCrCb_dst])

model = OmilZomil()
# model.detect(org_img)

try:
    model.detect(yCrCb_dst)
except Exception as e:
    print(e)
    print(traceback.format_exc())