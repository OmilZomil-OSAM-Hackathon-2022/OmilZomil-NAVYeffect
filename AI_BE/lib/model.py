from .classificate import classificate

class OmilZomil:
    def __init__(self):
        # self.HED_engine = HED()
        print('init!')
        self.org = None
        self.gray = None
        self.edge = None
    
    def detect(self, img):
        self.org = img
        # check_person(org) 사람인식
        # hair_segmentation(org) 머리카락인식
        kind = classificate(self.org) # 복장종류인식 (전투복, 동정복, 샘당)
        # if kind == '1':
        #   
        # elif kind == '2':
        #   
        # elif kind == '3':
        #   
        return None