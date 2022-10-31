from PIL import Image
from OZEngine.parts_classifier.PartsClassifier import PartsClassifier

classifier = PartsClassifier()
img = Image.open("./validation_set/navy_service_uniform/rank_tag4.jpg")
res = classifier.classify(img)
print(res)
