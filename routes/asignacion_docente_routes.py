from fastapi import APIRouter, HTTPException
from controllers.asignacion_docente_controller import *
from models.asignacion_docente_model import AsignacionDocente
from validations.asignacion_docente_validation import validate


router = APIRouter()

nuevo_asignacionDocente = AsignacionDocenteController()


@router.post("/create_asignacion_docente")
async def create_asignacion_docente(asignacionDocente: AsignacionDocente):
    #Validar datos de entrada
    validation = validate(asignacionDocente)
    if "error" in validation:
        raise HTTPException(status_code=400, detail=validation["error"])
    
    rpta = nuevo_asignacionDocente.create_asignacion_docente(asignacionDocente)
    return rpta


@router.get("/get_asignacion_docente/{asignacionDocente_id}",response_model=AsignacionDocente)
async def get_asignacion_docente(asignacionDocente_id: int):
    rpta = nuevo_asignacionDocente.get_asignacion_docente(asignacionDocente_id)
    return rpta

@router.get("/get_asignacion_docentes/")
async def get_asignacion_docentes():
    rpta = nuevo_asignacionDocente.get_asignacion_docentes()
    return rpta