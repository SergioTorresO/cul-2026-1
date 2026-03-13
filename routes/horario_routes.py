from fastapi import APIRouter, HTTPException
from controllers.horario_controller import *
from models.horario_model import Horario
from validations.horario_validation import validate

router = APIRouter()

nuevo_horario = HorarioController()


@router.post("/create_horario")
async def create_horario(horario: Horario):
    validation = validate(horario)
    if "error" in validation:
        raise HTTPException(status_code=400, detail=validation["error"])
    
    rpta = nuevo_horario.create_horario(horario)
    return rpta


@router.get("/get_horario/{horario_id}",response_model=Horario)
async def get_horario(horario_id: int):
    rpta = nuevo_horario.get_horario(horario_id)
    return rpta

@router.get("/get_horario_docente/{docente_id}")
async def get_horario_docente(docente_id: int):
    rpta = nuevo_horario.get_horario_docente(docente_id)
    return rpta

@router.get("/get_horarios/")
async def get_horarios():
    rpta = nuevo_horario.get_horarios()
    return rpta