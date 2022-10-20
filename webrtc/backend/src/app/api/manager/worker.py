import cv2
import os

from app.models.inspection_log import InspectionLog
from app.models.inspection_detail import InspectionDetail


from app.api.manager.image_box import ImageBox
from app.api.websocket.image import img_2_photo

PART_ID = {
    "hair": 1, 
    "nametag": 2, 
    "leveltag": 3, 
    "flag": 4, 
    "cap": 5, 
    "muffler": 6, 
    "neck": 7, 
}

class Worker:
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
        self.image_box = ImageBox(ai=ai, guardhouse=guardhouse)
        self.db_data_id = None
        self.parts_path = {}

    def read_image(self, path):
        # 이미지 읽어오기
        img = cv2.imread(path)

        # 읽은 후 해당 이미지 삭제
        if os.path.isfile(path):
            print(f"이미지 삭제 - {path}")
            os.remove(path)
        else:
            raise FileNotFoundError("파일 삭제 실패")
        # 읽은 이미지 전달        
        return img

    def create_data(self, path):
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
            image_path=path,
        )
        self.db.add(db_data)
        self.db.commit()
        self.db.refresh(db_data)
        # pk 값은 worker에서 보관
        self.db_data_id = db_data.inspection_id  

        # 각 파츠도 DB에 생성
        part_list = self.image_box.get_parts()
        print(f"각 파츠도 DB에 생성 - {part_list}")

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
            

        print("DB에 데이터 생성 완료 - 각 파츠 생성 미구현")


    def update_data(self):

        db_data = self.db.query(InspectionLog).filter_by(inspection_id=self.db_data_id)
        print(db_data)
        if not db_data.count():
            raise NotImplementedError(f"해당 객체를 조회할 수 없음 - {self.db_data_id}")

        inspection_dict = self.image_box.get_inspection()
        db_data.update(inspection_dict)
        self.db.commit()
        print(f"업데이트 완료 - {db_data}")
       
            
    
    def update_parts(self, part_name):
        db_data = self.db.query(InspectionDetail).filter_by(inspection_id=self.db_data_id).filter_by(appearance_type=PART_ID[part_name])
        print(db_data)
        if not db_data.count():
            raise NotImplementedError(f"해당 객체를 조회할 수 없음 - {self.db_data_id}")

        part_dict = {
            "status": True,
            "image_path": self.parts_path[part_name]
        }
        
        db_data.update(part_dict)
        self.db.commit()
        print(f"파츠 업데이트 완료 - {db_data}")


class SingleWorker(Worker):

    def execute(self, path):
        # 처리할 이미지 가져오기
        img = self.read_image(path)

        # ai에게 처리
        # print("이미지 처리 시작 ===============================")
        parts_image_list = self.image_box.image_process(image=img, path=path)
        if parts_image_list:
            for part_name, part_image in parts_image_list.items():
                # 파츠 이미지 저장
                # 일단 저장한 척
                self.parts_path[part_name] = part_image

        # 데이터가 없으면 생성
        if self.db_data_id is None:
            self.create_data(path=path)

        # DB에 반영
        if self.image_box.is_update:
            # DB에 데이터 업데이트
            self.update_data()
            self.image_box.is_update = False
        # 각 파츠 업데이트
        for part_name in self.image_box.parts_update:
            self.update_parts(part_name)
            self.image_box.parts_update.remove(part_name)

        # 답장
        photo  = img_2_photo(img)
        inspection_dict = self.image_box.get_inspection()
        parts_dict = self.image_box.get_parts()

        # 메세지 제작
        msg =  {
            "photo": photo,
            "path": path,
        }
        msg.update(inspection_dict)
        msg.update(parts_dict)
        return msg