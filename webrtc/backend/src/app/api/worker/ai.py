

from app.ai.OZEngine.model import OmilZomil


from app.api.worker.base import BaseWorker
from app.api.image_box.db_adapter import ai_2_db
from app.api.image_box.ai_adapter import ai_2_worker
from app.api.image_box.image_box import ImageBox


UPDATE_COUNT = 5

class AIWorker(BaseWorker):
    def __init__(self):
        super().__init__()
        self.ai = OmilZomil()
        self.image_box = None
    
    def execute(self, img, guardhouse):
        # 받은 이미지에 따라 이미지 박스 업데이트
        report = self.update_image_box(img=img, guardhouse=guardhouse)

        # ai 인식 결과에 따라 처리
        if report['ai'] == 'stop':
            return report
        # DB 저장 없이 바로 프론트에게 반환
        else:
            return report
        
        
    def update_image_box(self, img, guardhouse):
        # ai 실행
        report = self.ai.detect(org_img=img)

        # 인식이 안되면 그냥 싹 무시 
        if report['step'] != 3:
            return {
                "ai" : "stop",
                "step" : report['step'],
            }

        # 이미지 박스가 없으면 생성
        result = ai_2_worker(report)

        if self.image_box is None:
            self.image_box = ImageBox(
                uniform=result['uniform'], 
                guardhouse=guardhouse
                )
            self.image_box.update(result)
            return {
                'ai' : "new",
            }
        else:
            
            return {
                'ai' : "update"
            }


class DBWorker(AIWorker):
    pass