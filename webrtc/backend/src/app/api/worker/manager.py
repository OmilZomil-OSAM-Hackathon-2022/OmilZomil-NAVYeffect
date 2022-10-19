"""      
관리자 객체
이미지를 온 것을 확인 후 worker에게 지시

사람 유무 상태 관리

"""

MAX_PROCESS = 10

class Master:
    process_list = []
    task_list = []


    def create_worker():
        pass

    




    def add_task(self, path, ai=None):
        
        self.task_list.append({
            'path':path, 'ai':ai
            })
        order

    def order(self, path, ai=None):
        print(f"오더 - {path}")
        self.pool.apply_async(working, (path, ai))
        pass

def working(img, ai):
    print(f"img:{img} - {ai}")
    pass


worker_master = Master()