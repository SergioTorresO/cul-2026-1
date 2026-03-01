from pydantic import BaseModel

class AsignacionDocente(BaseModel):
    id: int = None
    id_docente: int
    nombre: str | None
    id_grupo: int
    codigo_grupo: str | None
    estado: bool