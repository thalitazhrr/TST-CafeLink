from fastapi import APIRouter, HTTPException, Depends, Request
from fastapi.responses import RedirectResponse
from authlib.integrations.starlette_client import OAuth
from supabase import create_client
import os

# Supabase Configuration
SUPABASE_URL = "https://oeradjopiaxfcymwfjzz.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im9lcmFkam9waWF4ZmN5bXdmanp6Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzI0NzQxMjgsImV4cCI6MjA0ODA1MDEyOH0.ik3a7JqIPOEgb1Wuz6yzmHn459Up7I1WAA3bycUlkTY"
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# OAuth Configuration
GOOGLE_CLIENT_ID = "997040951284-8dmpltijstn2d12grctb9r0l169pnvmu.apps.googleusercontent.com"
GOOGLE_CLIENT_SECRET = "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"
REDIRECT_URI = "http://localhost:8000/auth/callback"  # Adjust this based on your deployment

# FastAPI Router for Auth
auth_router = APIRouter()

# Initialize OAuth
oauth = OAuth()
oauth.register(
    name="google",
    client_id=GOOGLE_CLIENT_ID,
    client_secret=GOOGLE_CLIENT_SECRET,
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
    client_kwargs={"scope": "openid email profile"},
)

@auth_router.get("/login")
async def login_with_google(request: Request):
    """
    Step 1: Redirect the user to Google's OAuth consent screen.
    """
    redirect_uri = REDIRECT_URI
    return await oauth.google.authorize_redirect(request, redirect_uri)


@auth_router.get("/auth/callback")
async def google_auth_callback(request: Request):
    """
    Step 2: Handle the OAuth callback and authenticate the user.
    """
    try:
        # Fetch user info from Google
        token = await oauth.google.authorize_access_token(request)
        user_info = token.get("userinfo")

        if not user_info:
            raise HTTPException(status_code=400, detail="Failed to retrieve user information")

        # Optionally store or process user info with Supabase
        user = supabase.auth.sign_in_with_id_token(id_token=token["id_token"], provider="google")

        # Return user info
        return {"message": "Login successful", "user": user_info}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error during authentication: {str(e)}")
