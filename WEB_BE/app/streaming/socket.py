from typing import List, Dict

from fastapi.websockets import WebSocket


class ConnectionManager:
    def __init__(self):
        self.active_connections: Dict[WebSocket] = {}

    async def connect(self, str: name,  websocket: WebSocket):
        if name in self.active_connections:
            return False
        
        await websocket.accept()
        self.active_connections[name] =(websocket)
        return True

    def disconnect(self, name: str):
        self.active_connections.pop(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for name, connection in self.active_connections.items():
            await connection.send_text(message)