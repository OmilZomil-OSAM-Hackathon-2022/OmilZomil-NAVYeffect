# import dlib
from mtcnn import MTCNN
import time
import cv2
from OZEngine.lib.utils import *

class HairDetector():
    def __init__(self):
        self.model = keras.models.load_model('checkpoints/new/checkpoint.hdf5')
        self.detector = detector = MTCNN()

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
