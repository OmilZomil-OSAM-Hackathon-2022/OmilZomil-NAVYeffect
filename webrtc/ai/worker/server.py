# -*- coding: utf-8 -*-

import socketserver

class TaskHandler(socketserver.BaseRequestHandler):
    def handle(self):
        """
        클라이언트와 연결될 때 호출되는 함수
        """
        data = self.request.recv(1024).strip()
        print(data)