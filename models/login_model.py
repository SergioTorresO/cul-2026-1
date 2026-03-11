from pydantic import BaseModel

class Login(BaseModel):
    nombre: str
    password: str