from pydantic import BaseModel

class Programa(BaseModel):
    id: int = None
    nombre:str
    codigo:str
    id_facultad: int
    nombre_facultad: str | None
    estado:bool