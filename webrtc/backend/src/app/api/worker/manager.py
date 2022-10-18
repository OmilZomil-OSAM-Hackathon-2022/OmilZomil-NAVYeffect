"""      
관리자 객체
이미지를 온 것을 확인 후 worker에게 지시

사람 유무 상태 관리

"""
from multiprocessing import Pool

MAX_PROCESS = 10

class Master:
    
    person_list = {}
    pool = Pool(MAX_PROCESS)

    def capture(self, img):

        # 사람이야?

        # if
            # person 객체가 없으면 생성
            # 없으면 camera id 로 person 객체를 가져옴
            # worker 생성
        # else:
        # return False
        pass

    def order(self):
        pass