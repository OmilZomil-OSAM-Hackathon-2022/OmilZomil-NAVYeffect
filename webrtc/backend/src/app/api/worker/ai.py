

from app.ai.OZEngine.model import OmilZomil


from app.api.worker.base import BaseWorker
from app.api.image_box.db_adapter import ai_2_db
from app.api.image_box.ai_adapter import ai_2_worker
from app.api.image_box.front_adapter import worker_2_front
from app.api.image_box.image_box import ImageBox


UPDATE_COUNT = 5

class AIWorker(BaseWorker):
    def __init__(self):
        super().__init__()
        self.ai = OmilZomil()
        self.image_box = None
    
    def execute(self, img, guardhouse):
        # ai 실행
        report = self.ai.detect(org_img=img)

        # 인식이 안되면 그냥 싹 무시 
        if report['step'] != 3:
            return {
                "ai" : "stop",
                "step" : report['step'],
            }

        # ai 결과에 따라 이미지 박스 업데이트
        report = ai_2_worker(report)

        # 이미지 박스가 없으면 생성
        if self.image_box is None:
            self.image_box = ImageBox(
                uniform=report['uniform'], 
                guardhouse=guardhouse
                )
            msg = {'ai': 'new'}
        else:
            msg = {'ai': 'update'}
        
        report = self.update_image_box(report=report)
        msg.update(report)
        return msg 
                
        
    def update_image_box(self, report):
        self.image_box.update(report)
        return {
            "type" : "result",
            'inspection' : self.image_box.inspection,
            'parts' : self.image_box.parts,
        }


class FrontAIWorker(AIWorker):

    def update_image_box(self, report):
        self.image_box.update(report)
        msg = {
            "type" : "result",
        }
        msg.update(self.image_box.inspection)
        msg.update(self.image_box.parts)
        msg = worker_2_front(msg)
        return msg
