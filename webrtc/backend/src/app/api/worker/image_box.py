
UNIFORM_PARTS = {
    "blue" : [  # 샘당
        "hair", "nametag", "leveltag"
        ],
    "black" : [ # 정복
        "hair", "nametag", "leveltag", "muffler", "neck" 
        ],
    "green" : [ # 군복
        "hair", "nametag", "leveltag", "flag"
    ],
}


class ImageBox():
    def __init__(self, ai, guardhouse):
        self.ai = ai
        self.guardhouse = guardhouse      # 위병소
        self.affiliation = None     # 소속
        self.rank = None            # 계급
        self.name = None            # 이름
        self.uniform = None         # 복장
        self.parts = {} # 기타 파츠

    
    def image_process(self, image, path):
        # 복장 양호 불량 인식
        result = self.ai.detect(image)

        # 복장이 없는 경우 == 첫 이미지임
        if not self.uniform:
            self.uniform = self.ai.get_uniform()
            # 유니폼에 따라 파츠 리스트 생성
            self.parts = {key: None for key in UNIFORM_PARTS[self.uniform]}
        
        # 소속이 없는 경우 == 첫 이미지임 - 복장과 동일
        # 소속 부대인 경우 맨 하단에 작성
        if not self.affiliation:
            self.affiliation = self.ai.get_affiliation()
            
        # 이름 태그가 있으면
        if result["nametag"]:
            # 이름 인식
            self.name = self.ai.random_name()
        
        # 계급장이 있으면
        if result["leveltag"]:
            # 계급 인식
            self.rank = self.ai.random_name()
        
        msg = {
            "guardhouse" : self.guardhouse,
            "affiliation" : self.affiliation,
            "rank" : self.rank,
            "name" : self.name,
            "uniform" : self.uniform,
        }
        #기타 정보 기입  - 복장별 세부 항목
        for part in UNIFORM_PARTS[self.uniform]:
            if result[part]:
                self.parts[part] = True # 양호로 갱신
            # 메세지에 저장
            msg[part] = self.parts[part]

        # 처리 결과를 반환
        return msg

    def create_db_date(self):
        pass

    def update_db_data(self):
        pass
