from PIL import Image
from OZEngine.parts_classifier.PartsClassifier import PartsClassifier

classifier = PartsClassifier()
img = Image.open("./validation_set/navy_service_uniform/class_tag/4.jpg")
classifier.classify(img)
