from pydantic import BaseModel

class Programa(BaseModel):
    id: int = None
    nombre:str
    codigo:str
    estado:bool