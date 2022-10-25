import cv2
from datetime import datetime



from app.models.inspection_log import InspectionLog
from app.models.inspection_detail import InspectionDetail
from app.core.config import settings

from app.api.websocket.image import img_2_photo
from app.api.simple.image_box import ImageBox
from app.api.db.guardhouse import select_guardhouse


MAIN_IMAGE_PATH = f"{settings.IMAGE_PATH}/inspection"
PARTS_IMAGE_PATH = f"{settings.IMAGE_PATH}/detail"

EXPIRATION_COUNT = 5


PART_ID = {
    "hair": 1, 
    "name_tag": 2, 
    "class_tag": 3, 
    "flag": 4, 
    "cap": 5, 
    "muffler": 6, 
    "neck": 7, 
}



class BaseWorker:
    """
    이미지 경로를 받음
    받은 경로의 이미지를 가져옴
    가져온 이미지를 ai에게 넘겨줌
    ai 가 정보를 갱신
    ㄴ 새로운 정보면 DB에 create
    ㄴ 업데이트가 필요하면 DB에 update
    ㄴ 둘다 아닌 경우 무시

    """
    def __init__(self, db, ai, guardhouse):
        self.db = db
        self.image_box = ImageBox(ai=ai, guardhouse=select_guardhouse(db, guardhouse))
        self.db_data_id = None
        # 파일 경로 지정
        name = datetime.now().strftime("%H-%M-%S")
        self.name = f"{guardhouse}_{name}"
        self.main_image_path = f"{MAIN_IMAGE_PATH}/{self.name}.jpg"
        # REFRESH_COUNT
        self.expiration_count = EXPIRATION_COUNT

    def create_data(self):
        # 생성할 정보 가져오기
        data_dict = self.image_box.get_inspection()
        # model 객체 생성
        print(f"DB 데이터 생성 - {data_dict}")
        db_data = InspectionLog(
            guardhouse=data_dict['guardhouse'],
            affiliation=data_dict['affiliation'],
            rank=data_dict['rank'],
            name=data_dict['name'],
            uniform=data_dict['uniform'],
            image_path=self.main_image_path,
        )
        self.db.add(db_data)
        self.db.commit()
        self.db.refresh(db_data)
        # pk 값은 worker에서 보관
        self.db_data_id = db_data.inspection_id  

        # 각 파츠도 DB에 생성
        part_list = self.image_box.get_parts()
        for part_name, status in part_list.items():
            db_part = InspectionDetail(
                inspection_id=self.db_data_id,
                appearance_type=PART_ID[part_name],
                status=status,
                image_path="",
            )
            self.db.add(db_part)
            self.db.commit()
            self.db.refresh(db_part)

        self.expiration_count = EXPIRATION_COUNT
        print("DB에 데이터 생성 완료")


    def update_data(self):
        db_data = self.db.query(InspectionLog).filter_by(inspection_id=self.db_data_id)
        if not db_data.count():
            raise NotImplementedError(f"해당 객체를 조회할 수 없음 - {self.db_data_id}")

        inspection_dict = self.image_box.get_inspection()
        db_data.update(inspection_dict)
        self.db.commit()

        # 갱신할 이미지가 있으면 덮어쓰기
        if self.image_box.is_best_image:
            cv2.imwrite(self.main_image_path, self.image_box.main_image)
            self.image_box.is_best_image = False

        self.expiration_count = EXPIRATION_COUNT
        print(f"업데이트 완료")
       
            
    
    def update_parts(self, part_name):
        db_data = self.db.query(InspectionDetail).filter_by(inspection_id=self.db_data_id).filter_by(appearance_type=PART_ID[part_name])
        if not db_data.count():
            raise NotImplementedError(f"해당 객체를 조회할 수 없음 - {self.db_data_id}")

        part_path = f"{PARTS_IMAGE_PATH}/{self.name}_{part_name}.jpg"
        part_dict = {
            "status": True,
            "image_path": part_path
        }
        
        db_data.update(part_dict)
        self.db.commit()

        # 사진 업데이트
        part_img = self.image_box.parts_image.get(part_name)
        if part_img is not None:
            cv2.imwrite(part_path, part_img)

        self.expiration_count = EXPIRATION_COUNT
        print(f"파츠 업데이트 완료 - {part_name}")



class SimpleWorker(BaseWorker):
     def execute(self, img):

        # ai에게 처리
        print("이미지 처리 시작2 ===============================")
        error = self.image_box.image_process(image=img)

        self.expiration_count -= 1 #인식 횟수 감소
        
        # 군복이 아닌 경우
        if error:
            return {
                "msg" : "no human",
                "error" : error,
            }




        # 데이터가 없으면 생성
        if self.db_data_id is None:
            self.create_data()

        # DB에 반영
        if self.image_box.is_update:
            # DB에 데이터 업데이트
            self.update_data()
            self.image_box.is_update = False

        # 각 파츠 업데이트
        print("qqqqqqqqqq")
        print(self.image_box.parts_update)
        for part_name in self.image_box.parts_update:
            print(part_name)
            self.update_parts(part_name)
        self.image_box.parts_update = []    # 업데이트 완료후 빈 데이터로 변환
        # 답장
        photo  = img_2_photo(self.image_box.main_image)


        # 메세지 제작
        msg =  {
            "type": "result",
            "photo": photo,
        }


        msg.update(self.image_box.get_inspection())
        msg.update(self.image_box.get_parts())
        return msg

 