import numpy as np
import os
import pickle
from PIL import Image
from OZEngine.parts_classifier import FeatureExtractor


class PartsClassifier():
    def __init__(self):
        self.feature_extractor = FeatureExtractor()

        model_set_path = './model'
        # Load feature maps
        path = os.path.join(model_set_path, 'features')
        self.features = np.load(os.path.join(feature_path, 'features.npy'))

        # Load img paths
        path = os.path.join(model_set_path, 'img_paths')
        with open(path, "rb") as fr:
            self.img_paths = pickle.load(fr)

        # Load classes
        path = os.path.join(model_set_path, 'classes')
        with open(path, "rb") as fr:
            self.classes = pickle.load(fr)

    def evaluate(self):
        validation_path = './dataset/valiation_set'
        all_cnt = 0
        cnt = 0
        for (root, dirs, files) in os.walk(validation_path):
            all_cnt = len(files)
            for file_name in files:
                path = os.path.join(validationn_path, file_name)
                kind = path[-2]
                img = cv2.imread(path)
                res = self.predict(img)
                if res == kind:
                    cnt += 1
        return cnt / all_cnt * 100

    def predict(self, img):
        query = self.feature_extractor.extract(img)
        dists = np.linalg.norm(self.features - query, axis=1)
        id = np.argsort(dists)[0]
        dist = dists[id]
        kind = self.classes[id]
        if dist < 1:,
            return (dist, kind, id)
        else:
            return (None, None, None)
