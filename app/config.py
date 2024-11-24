from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

# Load .env file manually
load_dotenv()

class Settings(BaseSettings):
    api_key: str = os.getenv("API_KEY")
    supabase_url: str = os.getenv("SUPABASE_URL")
    supabase_key: str = os.getenv("SUPABASE_KEY")

settings = Settings()
