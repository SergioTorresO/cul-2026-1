from fastapi import APIRouter, HTTPException
from controllers.programa_controller import *
from models.programa_model import Programa

router = APIRouter()

nuevo_programa = ProgramaController()


@router.post("/create_programa")
async def create_programa(programa: Programa):
    rpta = nuevo_programa.create_programa(programa)
    return rpta


@router.get("/get_programa/{programa_id}",response_model=Programa)
async def get_programa(programa_id: int):
    rpta = nuevo_programa.get_programa(programa_id)
    return rpta

@router.get("/get_programas/")
async def get_programas():
    rpta = nuevo_programa.get_programas()
    return rpta