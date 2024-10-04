# Chat em Tempo Real com WebSockets 🗨️💬

Bem-vindo ao projeto **Chat em Tempo Real**! Este projeto utiliza **FastAPI** e **WebSockets** para fornecer uma experiência de chat em tempo real. 🚀

## Funcionalidades ✨

- **Comunicação em Tempo Real**: Converse instantaneamente com outros usuários. ⏱️
- **Interface Simples**: Um design intuitivo que facilita o uso. 🖥️
- **Multiusuário**: Vários usuários podem se conectar e conversar ao mesmo tempo! 👥

## Tecnologias Utilizadas 🛠️

- [FastAPI](https://fastapi.tiangolo.com/): Um moderno framework web para construir APIs com Python.
- [WebSockets](https://websockets.readthedocs.io/en/stable/): Para comunicação em tempo real.
- [JavaScript](https://www.javascript.com/): Para interatividade no frontend.

## Como Executar o Projeto 🚀

### 1. Clone o repositório

```bash
git clone https://github.com/thaleson/chatpython_realtime.git
cd chatpython_realtime
```

### 2. Crie um ambiente virtual

**Windows**:
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux e macOS**:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute o servidor

```bash
uvicorn app.main:app --reload
```

### 5. Abra o navegador e acesse

```
http://127.0.0.1:8000
```

## Testes 🧪

Para executar os testes, use:

```bash
pytest
```

## Contribuições 🤝

Contribuições são bem-vindas! Se você deseja contribuir, siga estas etapas:

1. Faça um fork do projeto.
2. Crie sua feature branch (`git checkout -b feature/YourFeature`).
3. Faça commit das suas mudanças (`git commit -m 'Add some feature'`).
4. Faça push para a branch (`git push origin feature/YourFeature`).
5. Abra um Pull Request.

## Licença 📄

Este projeto está licenciado sob a [MIT License](LICENSE).

