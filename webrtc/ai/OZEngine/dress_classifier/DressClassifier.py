import numpy as np
import os
from OZEngine.FeatureExtractor import FeatureExtractor


class DressClassifier(FeatureExtractor):
    def __init__(self):
        project_path = '/config/workspace/WEB_CLOUD_OmilZomil_NAVYeffect/webrtc/ai/OZEngine/dress_classifier/Dress'
        super().__init__(base_url)

    def predict(self, img):
        query = super().extract(img)
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