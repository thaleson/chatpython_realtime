# app/models/connection_manager.py
from typing import List
from fastapi import WebSocket

class ConnectionManager:
    """
    Manages active WebSocket connections and facilitates communication between them.

    Attributes:
    -----------
    active_connections : List[WebSocket]
        A list that stores the active WebSocket connections.

    Methods:
    --------
    connect(websocket: WebSocket):
        Accepts a new WebSocket connection, adds it to the list of active connections,
        and broadcasts a message notifying that a new user has joined the chat.

    disconnect(websocket: WebSocket):
        Removes a WebSocket connection from the list of active connections.

    send_personal_message(message: str, websocket: WebSocket):
        Sends a specific text message to an individual WebSocket connection.

    broadcast(message: str):
        Sends a text message to all active WebSocket connections.

    Examples:
    ---------
    manager = ConnectionManager()
    # Example of usage when handling WebSockets:
    await manager.connect(websocket)
    await manager.send_personal_message("Private message", websocket)
    await manager.broadcast("Message to all connected users")
    manager.disconnect(websocket)
    """
    
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)
        await self.broadcast(f"Um novo usuário entrou no chat.")

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

manager = ConnectionManager()
