import random


class RandomAI:


    def __init__(self):
        # self.kind = random.choice(["black", 'blue', 'green'])
        pass

    def get_uniform(self):
        return random.choice(["black", 'blue', 'green'])

    def get_affiliation(self):
        return random.choice(["육군", '해군', '공군', "국직"])

    def predict(self, list=[True, False]):
        return random.choices([True, False], weights = [0.1, 0.9])[0]

    def detect(self, img):
        return {
            "hair" : self.predict(),
            "nametag" : self.predict(),
            "leveltag" : self.predict(),
            "muffler" : self.predict(),
            "neck" : self.predict(),
            "flag" : self.predict(),
            
        }

    def random_name(self):
        first_name_samples = "김이박최정강조윤장임"
        middle_name_samples = "민서예지도하주윤채현지"
        last_name_samples = "준윤우원호후서연아은진"
        result = ""
        result += random.choice(first_name_samples)
        result += random.choice(middle_name_samples)
        result += random.choice(last_name_samples)

        # 이름도 일정 확률로 인식
        return random.choices([result, None], weights = [0.1, 0.9])[0]
    
    def random_rank(self):
        rank = random.choice(["이병", '일병', '상병', "병장"])
        return random.choices([rank, None], weights = [0.1, 0.9])[0]
