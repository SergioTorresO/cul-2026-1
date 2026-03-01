from fastapi import APIRouter, HTTPException
from controllers.disponibilidad_docente_controller import *
from models.disponibilidad_docente_model import DisponibilidadDocente

router = APIRouter()

nuevo_disponibilidad_docente = DisponibilidadDocenteController()


@router.post("/create_disponibilidad_docente")
async def create_disponibilidad_docente(disponibilidadDocente: DisponibilidadDocente):
    rpta = nuevo_disponibilidad_docente.create_disponibilidad_docente(disponibilidadDocente)
    return rpta


@router.get("/get_disponibilidad_docente/{disponibilidadDocente_id}",response_model=DisponibilidadDocente)
async def get_disponibilidad_docente(disponibilidadDocente_id: int):
    rpta = nuevo_disponibilidad_docente.get_disponibilidad_docente(disponibilidadDocente_id)
    return rpta

@router.get("/get_disponibilidad_docentes/")
async def get_disponibilidad_docentes():
    rpta = nuevo_disponibilidad_docente.get_disponibilidad_docentes()
    return rpta