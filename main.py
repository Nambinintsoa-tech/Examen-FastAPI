from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.responses import HTMLResponse, PlainTextResponse
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel
from datetime import datetime
from starlette.exceptions import HTTPException as StarletteHTTPException
from typing import List

app = FastAPI()
security = HTTPBasic()

class Post(BaseModel):
    author: str
    title: str
    content: str
    creation_datetime: datetime

@app.get("/ping", response_class=PlainTextResponse)
async def ping():
    return "pong"


@app.get("/home")
async def home():
    return {"message": "Welcome to the home page"}


@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request, exc):
    if exc.status_code == 404:
        return HTMLResponse(content="404 NOT FOUND", status_code=404)
    return await exc