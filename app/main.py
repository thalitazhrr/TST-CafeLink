from fastapi import FastAPI, Depends, HTTPException, Security
from fastapi.security.api_key import APIKeyHeader
from app.dependencies import get_api_key
from app.auth import google_login

app = FastAPI()

# Root endpoint untuk memastikan aplikasi berjalan
@app.get("/")
async def root():
    return {"message": "Welcome to TST-CafeLink API!"}

# Endpoint untuk protected route (autentikasi dengan API key)
@app.get("/protected-route")
async def protected_route(api_key: str = Depends(get_api_key)):
    return {"message": "You have access to this route!"}

# Endpoint untuk login menggunakan Google OAuth
@app.post("/login")
async def login(id_token: str):
    user_data = google_login(id_token)
    return user_data

@app.get("/debug-env")
async def debug_env():
    from app.config import settings
    return {
        "API_KEY": settings.api_key,
        "SUPABASE_URL": settings.supabase_url,
        "SUPABASE_KEY": settings.supabase_key,
    }
