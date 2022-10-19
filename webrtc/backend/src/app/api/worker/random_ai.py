import random


class RandomAI:

    def __init__(self):
        self.kind = random.choice(["black", 'blue', 'green'])

    def predict(self, list=[True, False]):
        return random.choices([True, False], weights = [0.2, 0.8])[0]

    def detect(self, img):
        return {
            "kind" : self.kind,
            "hair" : self.predict(),
            "nametag" : self.predict(),
            "leveltag" : self.predict(),
            "muffler" : self.predict(),
            "neck" : self.predict(),
            
        }