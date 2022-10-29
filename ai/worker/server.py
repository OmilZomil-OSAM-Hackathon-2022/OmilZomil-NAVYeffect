# -*- coding: utf-8 -*-
import time
import cv2
import json
import socketserver
from multiprocessing import Process, Queue


from OZEngine.model import OmilZomil
from worker.worker import SocketWorker
from app.api import deps
from app.db.session import SessionLocal


# 종료 옵션을 추가해야함
def master(q, socket):
    # 프로세서에 필요한 객체 구성
    db = SessionLocal()
    ai = OmilZomil()
    
    worker = None

    while True:
        # queue에서 데이터 가져오기
        data_json = q.get()

        # 공백인 경우
        if data_json == b'':
            time.sleep(1)
            continue
        
        # 데이터 수신
        data_str = data_json.decode('ascii')

        # 여러 json을 dict 형태로 변환
        data_list = data_str.split('{') # json이 여러개인 경우 처리
        data_list.remove('') # 첫번째 값 제거 - json이 여러개 오는 경우를 처리하기 위함
        query_list = list(map(lambda x : json.loads("{"+ x), data_list))
        print(query_list)

        # 각 요청별 처리    
        for query in query_list:
            """
            요청 dict
            path - queue에 저장된 이미지 경로
            guardhouse - worker생성시 필요한 위병소 데이터
            """
            # 위병소 데이터가 있는 경우 새 worker 를 생성
            if 'guardhouse' in query.keys():
                worker = SimpleWorker(ai=ai, db=db, guardhouse=query['guardhouse'])

            # 이미지 열기
            img = cv2.imread(query['path'])

            # ai 처리
            result_msg = worker.execute(img=img)

            # 메세지 전송
            print(f"ai 처리 결과를 webrtc로 전달 {result_msg}")
            json_msg = json.dumps(result_msg)
            socket.sendall(bytes(json_msg, 'ascii'))
            

class TaskHandler(socketserver.BaseRequestHandler):

    def setup(self):
        # 요청들을 보관할 queue
        self.q = Queue()
        
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
