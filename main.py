from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.get("/ping", response_class=PlainTextResponse)
async def ping():
    return "pong"


@app.get("/home")
async def home():
    return {"message": "Welcome to the home page"}