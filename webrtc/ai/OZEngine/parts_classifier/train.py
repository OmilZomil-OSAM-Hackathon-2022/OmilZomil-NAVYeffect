# Import the libraries
from random import uniform
from pathlib import Path
from PIL import Image
import numpy as np
import os, sys

from OZEngine.parts_classifier.FeatureExtractor import FeatureExtractor

# ignore tf warning message
# TF_CPP_MIN_LOG_LEVEL

def get_train_paths(train_set_path, model_set_path):
    train_paths = []
    model_paths = []
    for (root, dirs, files) in os.walk(train_set_path):
        d_split = root.strip('./').split('/')
        if len(d_split) == 3:
            train_dir_name, uniform_kind, parts_kind = d_split
            
            for file in files:
                # 학습모델 path 저장
                train_paths.append(os.path.join(root, file))
                
                # 최종 모델 이름 설정
                model_name = file.split('.')[0] # + '.npy'
                
                # model이 저장될 위치
                dst_path = os.path.join(model_set_path, uniform_kind, parts_kind)
                os.makedirs(dst_path, exist_ok=True)
                model_paths.append(os.path.join(dst_path, model_name))
    return train_paths, model_paths



train_set_path = './train_set'
model_set_path = './model'
train_paths, model_paths = get_train_paths(train_set_path, model_set_path)
print(train_paths, model_paths)

features = []
img_paths = []

fe = FeatureExtractor()
for img_path, feature_path in zip(train_paths, model_paths):
    print(img_path, feature_path)
    
    img_paths.append(img_path)
    feature = fe.extract(img=Image.open(img_path))
    features.append(feature)
    np.save(feature_path, feature)


img = Image.open("./test_set/0.jpg")
query = fe.extract(img)
dists = np.linalg.norm(features - query, axis=1)
ids = np.argsort(dists)[:30]
scores = [(dists[id], img_paths[id], id) for id in ids]
print(scores)