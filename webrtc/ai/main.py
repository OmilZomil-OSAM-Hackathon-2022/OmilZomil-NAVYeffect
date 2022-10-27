import sys

sys.path.append("/ai/OZEngine/.")
import socketserver

from worker.manager import Manager
from worker.server import TaskHandler
# 통신 정보 설정
HOST, PORT = "0.0.0.0", 7777

# 서버를 생성합니다. 호스트는 localhost, 포트 번호는 3000
server = socketserver.TCPServer((HOST, PORT), TaskHandler)

print(f"run")
# Ctrl - C 로 종료하기 전까지는 서버는 멈추지 않고 작동
server.serve_forever()
