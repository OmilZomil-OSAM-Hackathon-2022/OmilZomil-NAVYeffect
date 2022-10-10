from OZEngine.parts_classifier.PartsClassifier import PartsClassifier

classifier = PartsClassifier()
img = Image.open("./test_set/0.jpg")
classifier.classify(img)
