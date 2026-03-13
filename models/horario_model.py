from pydantic import BaseModel

class Horario(BaseModel):
    id:int=None
    id_grupo:int
    codigo_grupo:str|None
    id_docente:int
    docente:str|None
    id_salon:int
    codigo_salon:str|None
    id_jornada:int
    jornada:str|None
    dia_semana:int
    hora_inicio:str
    hora_fin:str