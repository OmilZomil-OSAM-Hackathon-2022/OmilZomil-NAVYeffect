from app.models.inspection_log import InspectionLog




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
    def __init__(selfqu, ai, guardhouse):
        self.ai = ai
        self.inspection = {
            'guardhouse':guardhouse    ,  # 위병소
            'affiliation':1     ,# 소속
            'rank':1      ,      # 계급
            'name':""     ,       # 이름
            'uniform':1 ,        # 복장
        }
        self.parts = {} # 기타 파츠
        self.image_path = None
        self.is_exist = False
        self.db_data_id=None
        self.is_update = False
        self.old_image_count=0

    def create_data(self, path):
        if self.is_exist:
            raise Exception
        self.is_exist = True

        # 복장 확인
        self.uniform = self.ai.get_uniform()
        self.parts = {key: None for key in UNIFORM_PARTS[self.uniform]} # 유니폼에 따라 파츠 리스트 생성

        # 데이터 갱신
        self.image_process(image, path)

        # DB 저장
        self.create_data()
        


    def image_process(self, image, path):
        # 복장 양호 불량 인식
        result = self.ai.detect(image)

        # 복장이 없는 경우 == 첫 이미지임
        if self.uniform == 1:
            self.uniform = self.ai.get_uniform()

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
            self.db_exist = True

        if not self.image_path or self.best_image(path):
            pass

            
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


    def best_image(self, path):
        # 이미지 상태 검사
        count=0

        for part_val in self.parts.values():
            if part_val:
                count += 1
            pass

        if self.old_image_count < count:
            self.image_path=path
        old_image_count=0

    def create_db_date(self):
        log = InspectionLog(
            guardhouse=self.guardhouse,
            affiliation=self.affiliation,
            rank=self.rank,
            name=self.name,
            uniform=self.uniform,
            image_path=self.image_path,
        )
        self.db.add(log)
        self.db.commit()
        self.db.refresh(log)
        self.db_data_id = log.inspection_id       

    def update_db_data(self):
        return False
        log =  db.query(InspectionLog).filter_by(inspection_id=self.db_data_id).all()
        if not log.count():
            raise Exception
        else:
            information = {
                "guardhouse":self.guardhouse,
                "affiliation":self.affiliation,
                "rank":self.rank,
                "name":self.name,
                "uniform":self.uniform,
                "image_path":self.image_path,
            }
            log.update(information)
            db.commit()
            pass
