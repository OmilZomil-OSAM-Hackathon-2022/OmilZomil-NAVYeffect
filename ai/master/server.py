from multiprocessing import Process, Manager



class TaskHandler(socketserver.BaseRequestHandler):

    def setup(self):
        # 요청들을 보관할 queue
        m = Manager()
        self.q = m.Queue()
        
        #ai 작업을 처리할 프로세서
        self.master = Process(
            name='master',
            target=master,
            args=(self.q, self.request),
        )
        self.master.start()

    def handle(self):
        """
        클라이언트와 연결될 때 호출되는 함수
        """
        while True:
            # 데이터 수신
            data_json = self.request.recv(1024).strip()
            
            # 빈 데이터는 무시
            if data_json == b'':
                continue

            # master에게 업무 추가
            self.q.put(data_json)
            print(f"master에게 업무 전달 완료 - {data_json}")

            # print(data_json.decode())
            # self.request.sendall(data_json)  
        
    def finish(self):
        # 프로세스 종료
        self.master.join()
