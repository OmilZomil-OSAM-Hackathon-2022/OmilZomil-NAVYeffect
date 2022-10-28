# worker를 생성해주는 객체
# ai 실행 주기를 설정


EMPTY_PERSON_SECOND = 10
EXPIRATION_COUNT = 5


INSPECTION_PATH = f"{settings.IMAGE_PATH}/inspection"


class BaseBroker:
    person_detector = PersonDetector()
    is_save_queue = False
    worker_creater = None
    
    def __init__(self, id):
        self.id = id
        self.last_person_time = datetime.now() - timedelta(seconds=EMPTY_PERSON_SECOND) # 처음은 무조건 새로운 사람이니깐
        self.now_worer = None


    def add_task(self, photo, guardhouse, work_time):

        # 사람 유무를 판별
        img = photo_2_img(photo)
        person_result = self.person_detector.detect(img)

        # 사람이 아니면 무시
        if not person_result:
            print(f" 사람이 아닙니다. 처리를 마칩니다.")
            return {
                "type" : "status",
                "status" : "no human",
            }

        # 사람인 경우 이미지 파일 저장 - 옵션 설정
        if self.is_save_queue:
            img_path = f"{QUEUE_PATH}/{guardhouse}_{work_time.strftime('%H-%m-%s')}.jpg"
            cv2.imwrite(img_path, img)

        # worker에게 지시
        msg = self.order_worker()
        
        # 프론트에게 1차 응답
        return {
            "result" : "status",
            "status" : "send task",
            "work_time": work_time,
            "msg": msg,
        }

    def order_worker(self):
        
        # 1. 오랜만에 온 사람인 경우 -> 새 사람임
        if work_time - self.last_person_time > timedelta(seconds=EMPTY_PERSON_SECOND):
            self.now_worer = self.worker_creater()
        
        # 업무 지시
        self.now_worer
        