from pydantic import BaseModel

class Facultad(BaseModel):
    id: int = None
    nombre: str