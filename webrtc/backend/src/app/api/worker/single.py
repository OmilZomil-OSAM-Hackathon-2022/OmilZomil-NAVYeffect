
from app.api.worker.db import DBWorker

from app.api.image_box.ai_adapter import ai_2_worker
from app.api.image_box.image_box import ImageBox

from app.api.image_box.front_adapter import worker_2_front

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
            msg = {
                "type" : "result",
                'ai': 'new',
            }
        else:
            # 이미지 박스 업데이트
            report = self.update_image_box(report=report)
            if 'main' in self.image_box.update_list:
                self.update_main()
                self.image_box.update_list.discard('main')

            for part_name in self.image_box.update_list:
                self.update_parts(part_name=part_name)

            # 업데이트 내역 초기화
            self.image_box.update_list.clear()    
            msg = {
                "type" : "result",
                'ai': 'update',
                }
        
        
        msg.update(self.image_box.inspection)
        msg.update(self.image_box.parts)
        msg = worker_2_front(msg)
        return msg 
