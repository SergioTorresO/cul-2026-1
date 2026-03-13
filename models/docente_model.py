from pydantic import BaseModel

class Docente(BaseModel):
    id: int = None
    tipo_documento: str
    n_documento: int
    primer_nombre: str
    segundo_nombre: str | None
    primer_apellido: str
    segundo_apellido: str | None
    telefono: str
    email: str
    password_hash: str
    id_rol: int = 2
    rol: str | None
    estado: bool = True