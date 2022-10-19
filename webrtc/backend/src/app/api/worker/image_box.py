from omil.app.models.inspection_log import InspectionLog




UNIFORM_PARTS = {
    2 : [  # 샘당
        "hair", "nametag", "leveltag"
        ],
    3 : [ # 정복
        "hair", "nametag", "leveltag", "muffler", "neck" 
        ],
    4 : [ # 군복
        "hair", "nametag", "leveltag", "flag"
    ],
}


class ImageBox:
    def __init__(self, db, ai, guardhouse):
        self.ai = ai
        self.db = db
        self.guardhouse = guardhouse      # 위병소
        self.affiliation = 1     # 소속
        self.rank = 1            # 계급
        self.name = ""            # 이름
        self.uniform = 1         # 복장
        self.parts = {} # 기타 파츠
        self.best_path = None
        self.db_exist = False

    
    def image_process(self, image, path):
        # 복장 양호 불량 인식
        result = self.ai.detect(image)

        # 복장이 없는 경우 == 첫 이미지임
        if self.uniform == 1:
            self.uniform = self.ai.get_uniform()
            self.parts = {key: None for key in UNIFORM_PARTS[self.uniform]} # 유니폼에 따라 파츠 리스트 생성
        # 소속이 없는 경우 
        if self.affiliation == 1:
            self.affiliation = self.ai.get_affiliation()

        # 데이터 갱신
        for part in UNIFORM_PARTS[self.uniform]:
            if result[part]:
                self.parts[part] = True # 양호로 갱신

        # 새 데이터 DB에 저장 
        if not self.db_exist:
            self.create_db_date(image_path=path)

        

            
        # 이름 태그가 있으면
        if result["nametag"] and self.name == "":
            # 이름 인식
            self.name = self.ai.random_name()
            self.update_db_data()
        
        # 계급장이 있으면
        if result["leveltag"] and self.rank == 1:
            # 계급 인식
            self.rank = self.ai.random_rank()
            self.update_db_data()
        
        # 메세지 기입
        msg = {
            "guardhouse" : self.guardhouse,
            "affiliation" : self.affiliation,
            "rank" : self.rank,
            "name" : self.name,
            "uniform" : self.uniform,
        }
        # 메세지에 저장
        for part in UNIFORM_PARTS[self.uniform]:
            msg[part] = self.parts[part]

        # 처리 결과를 반환
        return msg

    def create_db_date(self, image_path):
        log = InspectionLog(
            guardhouse=self.guardhouse,
            affiliation=self.affiliation,
            rank=self.rank,
            name=self.name,
            uniform=self.uniform,
            image_path=image_path,
        )
        print(log)
        self.db.add(log)
        self.db.commit()
        self.db.refresh(log)
        

    def update_db_data(self):
        pass
