# import dlib
import time
import cv2
import os
from OZEngine.lib.utils import *
import tensorflow

class HairDetector():
    def __init__(self):
        model_path = os.path.join(os.environ['AI_PATH'], 'OZEngine', 'hair_detectors', 'weights', 'weight_5.hdf5')
        self.model = tensorflow.keras.models.load_model(model_path)

    def predict(image, height=224, width=224):
        im = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        im = im / 255
        im = cv2.resize(im, (height, width))
        im = im.reshape((1,) + im.shape)

        pred = self.model.predict(im)

        mask = pred.reshape((224, 224))

        return mask
    
    def detect(self, img):
        st = time.time()
        dmask = predict(img)
        d1 = time.time()

        print(f"segment: {d1-st}, color:%f")
