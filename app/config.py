from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    api_key: str
    supabase_url: str
    supabase_key: str

    class Config:
        env_file = ".env"

settings = Settings()
