# -*- coding: utf-8 -*-

import socketserver
from worker.manager import Manager


manager = Manager()

class TaskHandler(socketserver.BaseRequestHandler):
    def handle(self):
        """
        클라이언트와 연결될 때 호출되는 함수
        """
        self.data = self.request.recv(1024).strip()
        print(f"{self.client_address} = {self.data}")
        manager.add_task(msg={
            'socket' : self.request,
            'data' : self.data,
        })
