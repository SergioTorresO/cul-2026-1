from fastapi import APIRouter, HTTPException
from controllers.grupo_controller import *
from models.grupo_model import Grupo

router = APIRouter()

nuevo_grupo = GrupoController()


@router.post("/create_grupo")
async def create_grupo(grupo: Grupo):
    rpta = nuevo_grupo.create_grupo(grupo)
    return rpta


@router.get("/get_grupo/{grupo_id}",response_model=Grupo)
async def get_grupo(grupo_id: int):
    rpta = nuevo_grupo.get_grupo(grupo_id)
    return rpta

@router.get("/get_grupos/")
async def get_grupos():
    rpta = nuevo_grupo.get_grupos()
    return rpta