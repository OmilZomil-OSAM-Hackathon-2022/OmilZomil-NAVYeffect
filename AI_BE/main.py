from OZEngine import OmilZomil
from OZEngine.lib.utils import *
from OZEngine.edge_detectors import Morph, HED
import os
import sys
import traceback
import cv2
from operator import itemgetter
import matplotlib.pyplot as plt

cur_path = os.getcwd()
engine_path = os.path.join(cur_path, 'OZEngine')
if engine_path not in sys.path:
    sys.path.append(engine_path)


try:
    component_dic, box_position_dic = model.detect(yCrCb_dst)
except Exception as e:
    print(e)
    print(traceback.format_exc())

print(component_dic)
