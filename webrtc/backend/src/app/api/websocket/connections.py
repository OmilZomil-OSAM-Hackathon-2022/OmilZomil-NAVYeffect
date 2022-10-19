from typing import Dict

from fastapi.websockets import WebSocket
from loguru import logger
class Connection:
    def __init__(self, ws: WebSocket):
        self.ws = ws
        ip = '123'
        self.logger = logger.bind(ip=ip)

    async def send_json(self, message: dict):
        await websocket.send_json(message)

class ConnectionManager:
    def __init__(self):
        self.active_connections: Dict[WebSocket] = {}

    async def connect(self, name: str, websocket: WebSocket):
        request_logger = logger.bind(ip="123")
        websocket.accept()
        logger.info("asdfasdf")
        request_logger.info("11111111")
        # 객체를 생성해서 추가
        conn = Connection(ws=websocket)
        self.active_connections[name] = conn

    def disconnect(self, name: str):
        del self.active_connections[name]



