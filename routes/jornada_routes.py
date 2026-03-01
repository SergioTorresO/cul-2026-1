from fastapi import APIRouter, HTTPException
from controllers.jornada_controller import *
from models.jornada_model import Jornada

router = APIRouter()

nuevo_jornada = JornadaController()


@router.post("/create_jornada")
async def create_jornada(jornada: Jornada):
    rpta = nuevo_jornada.create_jornada(jornada)
    return rpta


@router.get("/get_jornada/{jornada_id}",response_model=Jornada)
async def get_jornada(jornada_id: int):
    rpta = nuevo_jornada.get_jornada(jornada_id)
    return rpta

@router.get("/get_jornadas/")
async def get_jornadas():
    rpta = nuevo_jornada.get_jornadas()
    return rpta