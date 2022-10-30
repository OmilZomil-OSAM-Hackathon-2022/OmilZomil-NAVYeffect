from demo_lib.utils import setImportPath
setImportPath()
import tensorflow as tf
from tqdm import tqdm
tf.autograph.set_verbosity(0)

import os
import traceback
import time
from OZEngine.lib.utils import *
from OZEngine import OmilZomil

save_path = os.path.join(os.getcwd(), 'image/res/arm_01')
os.makedirs(save_path, exist_ok=True)
model = OmilZomil()

frame_path = 'image/video_frame/arm01'
frames = os.listdir(frame_path)
frame_n = len(frames)
print('frame n ', frame_n)
for i in tqdm(range(1, frame_n), desc='detecting'):
    read_path = os.path.join(frame_path, f'{i}.jpg')
    img = cv2.imread(read_path)
    
    result = model.detect(img)
    if result['step'] >= 1:
        model.saveImg({'result':result['boxed_img']}, save_path=save_path)
    if result['step'] >= 2:
        # model.saveImg({'hed_result':result['hed_boxed_img']}, save_path=save_path)
        model.saveImg({'shirts':result['shirt_img']}, save_path=save_path)
    
    if result['step'] >= 3:
        if result.get('roi'):
            model.saveImg(result['roi'], save_path=save_path)