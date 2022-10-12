import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
from tensorflow.keras.models import Model


class FeatureExtractor:
    def __init__(self, base_path):
        base_model = VGG16(weights='imagenet')
        # Customize the model to return features from fully-connected layer
        self.model = Model(inputs=base_model.input,
                           outputs=base_model.get_layer('fc1').output)

        self.base_path = base_path
        self.train_set_path = os.path.join(base_path, 'dataset', 'train_set')
        self.validation_set_path = os.path.join(base_path, 'dataset', 'validation_set')
        self.model_set_path = os.path.join(base_path, 'model')
        self.getFeatures()


    def getFeatures():
        # Load feature maps
        path = os.path.join(self.model_set_path, 'features')
        self.features = np.load(os.path.join(feature_path, 'features.npy'))

        # Load img paths
        path = os.path.join(self.model_set_path, 'img_paths')
        with open(path, "rb") as fr:
            self.img_paths = pickle.load(fr)

        # Load classes
        path = os.path.join(self.model_set_path, 'classes')
        with open(path, "rb") as fr:
            self.classes = pickle.load(fr)

    def get_train_paths(train_set_path):
        train_paths = []
        for (root, dirs, files) in os.walk(train_set_path):
            for file_name in files:
                train_paths.append(os.path.join(root, file_name))
        return train_paths

    def train(self):
        features = []
        img_paths = []
        classes = []

        train_paths = self.get_train_paths(self.train_set_path)

        for img_path in train_paths:
            class_name = img_path.split('/')[:-2]
            feature = fe.extract(img=Image.open(img_path))
            features.append(feature)
            img_paths.append(img_path)
            classes.append(class_name)

        feature_path = os.path.join(self.model_set_path, 'features')
        img_path = os.path.join(self.model_set_path, 'img_paths')
        class_path = os.path.join(self.model_set_path, 'classes')

        np.save(feature_path, features)

        with open(img_path, 'wb') as f:
            pickle.dump(img_paths, f)

        with open(class_path, 'wb') as f:
            pickle.dump(classes, f)

    def evaluate(self):
        all_cnt = 0
        cnt = 0
        for (root, dirs, files) in os.walk(self.validation_set_path):
            all_cnt = len(files)
            for file_name in files:
                path = os.path.join(self.validation_set_path, file_name)
                kind = path[-2]
                img = cv2.imread(path)
                res = self.predict(img)
                if res == kind:
                    cnt += 1
        return cnt / all_cnt * 100

    def extract(self, img):
        img = img.resize((224, 224))
        img = img.convert('RGB')
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
        feature = self.model.predict(x)[0]
        return feature / np.linalg.norm(feature)
