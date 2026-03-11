from pydantic import BaseModel

class Usuario(BaseModel):
    id: int = None
    primer_nombre: str
    segundo_nombre: str | None
    primer_apellido: str
    segundo_apellido: str | None
    email: str
    password_hash: str
    id_rol: int
    rol: str | None
    activo: bool