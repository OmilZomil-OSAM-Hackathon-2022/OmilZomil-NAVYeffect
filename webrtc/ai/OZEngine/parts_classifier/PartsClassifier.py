import numpy as np
import os
import pickle
from PIL import Image
from OZEngine.parts_classifier import FeatureExtractor

class PartsClassifier():
    def __init__(self):
        self.feature_extractor = FeatureExtractor()
        
        model_set_path = './model'
        ## Load pickle
        feature_path = os.path.join(model_set_path, 'features')
        img_path = os.path.join(model_set_path, 'img_paths')
        class_path = os.path.join(model_set_path, 'classes')

        self.features = np.load('./model/features.npy')

        with open(img_path, "rb") as fr:
            self.img_paths = pickle.load(fr)

        with open(class_path, "rb") as fr:
            self.classes = pickle.load(fr)

    def classify(self, img):
        query = fe.extract(img)
        dists = np.linalg.norm(self.features - query, axis=1)
        ids = np.argsort(dists)[0]
        return (dists[id], self.classes[id], id)
    