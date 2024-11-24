from fastapi import FastAPI, Depends
from app.dependencies import get_api_key
from app.auth import google_login

app = FastAPI()

@app.get("/protected-route")
async def protected_route(api_key: str = Depends(get_api_key)):
    return {"message": "You have access to this route!"}

@app.post("/login")
async def login(id_token: str):
    user_data = google_login(id_token)
    return user_data

@app.get("/")
async def root():
    return {"message": "Welcome to TST-CafeLink API!"}
