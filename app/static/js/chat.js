// app/static/js/chat.js
const chatBox = document.getElementById('chat-box');
const messageInput = document.getElementById('message-input');

// Estabelecer a conexão WebSocket
const ws = new WebSocket(`ws://${window.location.host}/ws/chat`);

ws.onmessage = function(event) {
    const message = document.createElement('div');
    message.textContent = event.data;
    chatBox.appendChild(message);
    chatBox.scrollTop = chatBox.scrollHeight;
};

ws.onopen = function(event) {
    console.log("Conectado ao servidor de chat.");
};

ws.onclose = function(event) {
    console.log("Desconectado do servidor de chat.");
};

function sendMessage() {
    const message = messageInput.value;
    if (message.trim() !== "") {
        ws.send(message);
        messageInput.value = "";
    }
}

// Enviar mensagem ao pressionar Enter
messageInput.addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        sendMessage();
    }
});
