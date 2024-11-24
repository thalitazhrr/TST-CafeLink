from supabase import create_client
from app.config import settings

supabase = create_client(settings.supabase_url, settings.supabase_key)

def google_login(id_token: str):
    try:
        response = supabase.auth.sign_in_with_id_token(id_token=id_token, provider="google")
        return response
    except Exception as e:
        raise Exception(f"Error during Google login: {e}")
