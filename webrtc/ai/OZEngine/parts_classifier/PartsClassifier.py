import numpy as np
import os
import pickle
from PIL import Image
from OZEngine.parts_classifier import FeatureExtractor


class PartsClassifier(FeatureExtractor):
    def __init__(self, dress_kind):
        if dress_kind == 'navy_service_uniform':
            base_url = 'NavyServiceUniform'
        elif dress_kind == 'full_navy_uniform':
            base_url = 'FullNavyUniform'
        super().__init__(base_url)

        self.feature_extractor = FeatureExtractor()

    def predict(self, img):
        query = self.feature_extractor.extract(img)
        dists = np.linalg.norm(self.features - query, axis=1)
        id = np.argsort(dists)[0]
        dist = dists[id]
        kind = self.classes[id]
        if dist < 1:
            return (dist, kind, id)
        else:
            return (None, None, None)

if __name__ == '__main__':
    pc = PartsClassifier('navy_service_uniform')
    res = pc.evaluate()
    print(res)