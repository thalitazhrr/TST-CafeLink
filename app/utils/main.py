from fastapi import FastAPI
from app.routers.auth import auth_router
from dotenv import load_dotenv

load_dotenv()

# Create FastAPI app
app = FastAPI(
    title="TST-CafeLink API",
    description="An API for TST-CafeLink with Google OAuth and Supabase integration.",
    version="1.0.0",
)

# Include the auth router
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])

# Root endpoint for testing
@app.get("/")
async def root():
    return {"message": "Welcome to TST-CafeLink API"}
