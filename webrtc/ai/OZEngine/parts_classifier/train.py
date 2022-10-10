# Import the libraries
from random import uniform
from pathlib import Path
from PIL import Image
import numpy as np
import os, sys
import pickle

from OZEngine.parts_classifier.FeatureExtractor import FeatureExtractor
from OZEngine.parts_classifier.PartsClassifier import PartsClassifier

# ignore tf warning message
# TF_CPP_MIN_LOG_LEVEL

def get_train_paths(train_set_path):
    train_paths = []
    for (root, dirs, files) in os.walk(train_set_path):
        for file_name in files:
            train_paths.append(os.path.join(root, file_name))
    return train_paths

train_set_path = './train_set'
model_set_path = './model'

train_paths = get_train_paths(train_set_path)

features = []
img_paths = []
classes = []

fe = FeatureExtractor()
for img_path in train_paths:
    class_name = img_path.split('/')[:-2]
    feature = fe.extract(img=Image.open(img_path))
    features.append(feature)
    img_paths.append(img_path)
    classes.append(class_name)

feature_path = os.path.join(model_set_path, 'features')
img_path = os.path.join(model_set_path, 'img_paths')
class_path = os.path.join(model_set_path, 'classes')

np.save(feature_path, features)

with open(img_path, 'wb') as f:
    pickle.dump(img_paths, f)

with open(class_path, 'wb') as f:
    pickle.dump(classes, f)