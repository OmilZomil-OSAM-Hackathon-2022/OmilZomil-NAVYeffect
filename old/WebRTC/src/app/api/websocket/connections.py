from typing import Dict

from fastapi.websockets import WebSocket


class ConnectionManager:
    def __init__(self):
        self.active_connections: Dict[WebSocket] = {}

    async def connect(self, name: str, websocket: WebSocket):
        await websocket.accept()
        self.active_connections[name] = websocket

    def disconnect(self, name: str):
        self.active_connections[name]

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)
