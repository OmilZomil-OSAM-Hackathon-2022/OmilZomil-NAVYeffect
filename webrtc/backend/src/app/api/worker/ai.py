from app.api.worker.base import BaseWorker

from app.ai.OZEngine.model import OmilZomil

UPDATE_COUNT = 5

class AIWorker(BaseWorker):
    def __init__(self):
        super().__init__()
        self.ai = OmilZomil()
        self.image_box = None
    
    def execute(self, img):
        # 받은 이미지에 따라 이미지 박스 업데이트
        report = self.update_image_box(img=img)

        # ai 인식 결과에 따라 처리
        if report['ai'] == 'stop':
            return report
        # DB 저장 없이 바로 프론트에게 반환
        else:
            return report
        
        
    def update_image_box(self, img):
        # ai 실행
        report = self.ai.detect(org_img=img)

        # 인식이 안되면 그냥 싹 무시 
        if report['step'] != 3:
            return {
                "ai" : "stop",
                "step" : report['step'],
            }

        # 이미지 박스가 없으면 생성

        if self.image_box is None:
            print(report)
            return {
                'ai' : "new",
            }
        else:
            
            return {
                'ai' : "update"
            }


class DBWorker(AIWorker):
    pass