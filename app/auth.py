from supabase import create_client

SUPABASE_URL = "https://oeradjopiaxfcymwfjzz.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im9lcmFkam9waWF4ZmN5bXdmanp6Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzI0NzQxMjgsImV4cCI6MjA0ODA1MDEyOH0.ik3a7JqIPOEgb1Wuz6yzmHn459Up7I1WAA3bycUlkTY"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def google_login(id_token: str):
    response = supabase.auth.sign_in_with_id_token(id_token=id_token, provider="google")
    return response
