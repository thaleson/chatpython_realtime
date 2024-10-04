# app/routers/websocket.py
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.models.connection_manager import manager

router = APIRouter()

@router.websocket("/ws/chat")
async def websocket_endpoint(websocket: WebSocket):
    """
    WebSocket endpoint for a real-time chat system.

    This endpoint allows clients to connect via WebSocket for real-time communication.
    When a client connects, they are added to the active connections list and can
    send and receive messages. All received messages are broadcasted to other connected
    users. When a client disconnects, they are removed from the active connections list,
    and a message is broadcasted to notify others.

    Parameters:
    -----------
    websocket : WebSocket
        The WebSocket connection instance used to communicate with the client.

    Raises:
    -------
    WebSocketDisconnect:
        This exception is raised when the client disconnects from the WebSocket.
        Upon disconnection, the client is removed from the active connections,
        and a message is broadcasted to the remaining users.

    Example:
    --------
    To use this WebSocket endpoint, a client must connect to "/ws/chat". After connecting,
    they can send messages that will be broadcast to all other connected clients.

    """
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(f"Usuario diz: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast("Um usuário saiu do chat.")
