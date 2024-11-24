import secrets

def generate_api_key():
    return secrets.token_hex(16)  # Menghasilkan API key sepanjang 32 karakter

print("Your API Key:", generate_api_key())