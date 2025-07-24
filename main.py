from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def lire_racine():
    return {"message":
    "Bienvenue à l'API FastAPI"}