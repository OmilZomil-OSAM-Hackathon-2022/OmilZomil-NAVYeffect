from demo_lib.utils import setImportPath
setImportPath()
import tensorflow as tf
tf.autograph.set_verbosity(0)

import os
import traceback
from OZEngine.lib.utils import *
from OZEngine import OmilZomil

save_path = os.path.join(os.getcwd(), 'image/res/fd_2')
os.makedirs(save_path, exist_ok=True)
model = OmilZomil(debug_list=['imwrite'], save_path=save_path)

frame_path = 'image/video_frame/fd_1'
frames = os.listdir(frame_path)
frame_n = len(frames)
print('frame n ', frame_n)
for i in range(0, 2):
    read_path = os.path.join(frame_path, f'{i}.jpg')
    img = cv2.imread(read_path)
    result = model.detect(img)
    # print(result['component'])