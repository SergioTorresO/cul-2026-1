from fastapi import APIRouter, HTTPException
from controllers.asignatura_controller import *
from models.asignatura_model import Asignatura

router = APIRouter()

nuevo_asignatura = AsignaturaController()


@router.post("/create_asignatura")
async def create_asignatura(asignatura: Asignatura):
    rpta = nuevo_asignatura.create_asignatura(asignatura)
    return rpta


@router.get("/get_asignatura/{asignatura_id}",response_model=Asignatura)
async def get_asignatura(asignatura_id: int):
    rpta = nuevo_asignatura.get_asignatura(asignatura_id)
    return rpta

@router.get("/get_asignaturas/")
async def get_asignaturas():
    rpta = nuevo_asignatura.get_asignaturas()
    return rpta