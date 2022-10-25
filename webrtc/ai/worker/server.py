# -*- coding: utf-8 -*-
import time
import cv2
import json
import socketserver
from multiprocessing import Process, Queue


from OZEngine.model import OmilZomil
from app.api.simple.worker import SimpleWorker
from app.api import deps
from app.db.session import SessionLocal



def master(q, socket):
    db = SessionLocal()
    ai = OmilZomil()
    print(db)
    print(type(db))
    while True:
        data_json = q.get()
        if data_json != b'':
            print(data_json.decode('ascii'))
            data_str = data_json.decode('ascii')
            data_list = data_str.split('{')
            print(data_list)
            for i in data_list:
                if i == '':
                    continue
                data = json.loads("{"+ i)
                
                if 'guardhouse' in data.keys():
                    worker = SimpleWorker(ai=ai, db=db, guardhouse=data['guardhouse'])

                # 이미지 열기
                img = cv2.imread(data['path'])
                # ai 처리
                result_msg = worker.execute(img=img)

                # 메세지 전송
                json_msg = json.dumps(result_msg)
                socket.sendall(bytes(json_msg, 'ascii'))
                
        time.sleep(1)


class TaskHandler(socketserver.BaseRequestHandler):

    def setup(self):
        self.q = Queue()
        
        self.worker = Process(
            name='worker',
            target=master,
            args=(self.q, self.request),
        )
        self.worker.start()




    def handle(self):
        """
        클라이언트와 연결될 때 호출되는 함수
        """
        while True:
            data_json = self.request.recv(1024).strip()
            if data_json != b'':
                self.q.put(data_json)
                print(data_json.decode())
                self.request.sendall(data_json)  
            