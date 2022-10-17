

class Manager:
    task_queue = []
    is_run = True  # 스래드가 많아 더이상 실행 못하는 경우 false
    def __init__(self):
        pass

    def add_task(self, msg):
        # 작업 추가
        self.task_queue.append(msg)
        # 작업 실행
        if self.is_run:
            # 스래드 수에 여유가 있는 경우
            self.run_task()
        else:
            # worker를 생성하지 못하는 경우
            return False
    
    def run_task(self):
        print("run task")
        print(self.task_queue)
        
        # 작업이 없는 경우는 종료
        if not self.task_queue:
            return True
        
        # 작업이 없을때까지 반복
        self.run_task()