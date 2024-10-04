# app/main.py
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.routers import websocket
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME)

# Include the WebSocket router
app.include_router(websocket.router)

# Mount static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Configure templates
templates = Jinja2Templates(directory="app/templates")

# Route for the main page
from fastapi import Request

@app.get("/")
async def get(request: Request):
    """
    Handles GET requests for the main page of the application.

    This route serves the main HTML page, rendering it using Jinja2 templates.
    The request object is passed to the template for context, allowing for
    dynamic content rendering.

    Parameters:
    -----------
    request : Request
        The FastAPI request object, providing context for the template.

    Returns:
    --------
    TemplateResponse
        The rendered HTML template response for the main page.

    Example:
    --------
    When a user navigates to the root URL ("/"), this route will return the
    rendered "index.html" template, which is located in the "app/templates" directory.
    """
    return templates.TemplateResponse("index.html", {"request": request})
