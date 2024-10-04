# tests/test_websocket.py
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_websocket_connection():
    with client.websocket_connect("/ws/chat") as websocket:
        # Receber a mensagem inicial de conexão
        initial_message = websocket.receive_text()
        assert initial_message == "Um novo usuário entrou no chat."

        # Enviar uma mensagem
        websocket.send_text("Olá, mundo!")

        # Receber a mensagem enviada
        data = websocket.receive_text()
        assert data == "Usuario diz: Olá, mundo!"
