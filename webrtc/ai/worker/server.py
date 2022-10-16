# -*- coding: utf-8 -*-

import socketserver

class TaskHandler(socketserver.BaseRequestHandler):
    """
    업무 요청 받음
    """

    def handle(self):
        """
        클라이언트와 연결될 때 호출되는 함수
        상위 클래스에는 handle() 메서드가 정의되어 있지 않기 때문에
        여기서 오버라이딩을 해야함
        """
        self.data = self.request.recv(1024).strip()
        print(f"{self.client_address}")
