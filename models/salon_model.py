from pydantic import BaseModel

class Salon(BaseModel):
    id: int = None
    codigo: str
    capacidad: int
    tipo: str
    ubicacion: str
    estado: bool