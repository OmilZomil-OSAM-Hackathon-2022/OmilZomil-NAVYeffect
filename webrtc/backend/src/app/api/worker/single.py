
from app.api.worker.db import DBWorker

from app.api.image_box.ai_adapter import ai_2_worker
from app.api.image_box.image_box import ImageBox


class SingleWorker(DBWorker):
    pass

    def execute(self, img, guardhouse, work_time):
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
                guardhouse=guardhouse,
            )
            # 이미지 박스 업데이트
            report = self.update_image_box(report=report)
            # 객체 생성
            self.create_main(work_time=work_time)
            msg = {'ai': 'new'}
        else:
            # 이미지 박스 업데이트
            report = self.update_image_box(report=report)

            msg = {'ai': 'update'}
        
        
        msg.update(report)
        return msg 
