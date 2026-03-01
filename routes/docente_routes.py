from fastapi import APIRouter, HTTPException
from controllers.docente_controller import *
from models.docente_model import Docente

router = APIRouter()

nuevo_docente = DocenteController()


@router.post("/create_docente")
async def create_docente(docente: Docente):
    rpta = nuevo_docente.create_docente(docente)
    return rpta


@router.get("/get_docente/{docente_id}",response_model=Docente)
async def get_docente(docente_id: int):
    rpta = nuevo_docente.get_docente(docente_id)
    return rpta

@router.get("/get_docentes/")
async def get_docentes():
    rpta = nuevo_docente.get_docentes()
    return rpta