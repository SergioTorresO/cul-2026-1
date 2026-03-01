from pydantic import BaseModel

class Jornada(BaseModel):
    id: int = None
    nombre:str
    hora_inicio:str
    hora_fin:str