from pydantic import BaseModel

class DisponibilidadDocente(BaseModel):
    id:int=None
    id_docente:int
    nombre:str|None
    dia_semana:str
    hora_inicio:str
    hora_fin:str
    observacion:str