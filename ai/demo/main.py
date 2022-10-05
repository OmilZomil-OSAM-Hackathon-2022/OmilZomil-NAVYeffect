import matplotlib.pyplot as plt
from operator import itemgetter
import cv2
import traceback
from OZEngine.edge_detectors import Morph, HED
from OZEngine.lib.utils import *
from OZEngine import OmilZomil
from .libs.utils import setImportPath

setImportPath()


try:
    component_dic, box_position_dic = model.detect(yCrCb_dst)
except Exception as e:
    print(e)
    print(traceback.format_exc())

print(component_dic)
