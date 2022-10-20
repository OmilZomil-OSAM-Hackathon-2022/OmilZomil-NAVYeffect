import random


class RandomAI:
    """
    랜덤 ai 모든건 랜덤으로 적용
    """
    def __init__(self):
        # self.kind = random.choice(["black", 'blue', 'green'])
        pass

    def get_uniform(self):
        # 샘당, 정복, 군복
        return random.choice([2, 3, 4])

    def get_affiliation(self):
        # 육군 공군 해군 해병대 
        return random.choice([2, 3, 4, 5])

    def predict(self, list=[True, False]):
        # 양호 불량
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
        return random.choices([result, ""], weights = [0.1, 0.9])[0]
    
    def random_rank(self):
        # 이병, 일병, 상병, 병장
        rank = random.choice([2, 3, 4, 5])
        return random.choices([rank, 1], weights = [0.1, 0.9])[0]
