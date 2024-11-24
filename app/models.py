from pydantic import BaseModel

class User(BaseModel):
    id: str
    email: str
    name: str

class StainDetectionRequest(BaseModel):
    image_url: str
