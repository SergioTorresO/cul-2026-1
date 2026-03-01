from fastapi import APIRouter, HTTPException
from controllers.salon_controller import *
from models.salon_model import Salon

router = APIRouter()

nuevo_salon = SalonController()


@router.post("/create_salon")
async def create_salon(salon: Salon):
    rpta = nuevo_salon.create_salon(salon)
    return rpta


@router.get("/get_salon/{salon_id}",response_model=Salon)
async def get_salon(salon_id: int):
    rpta = nuevo_salon.get_salon(salon_id)
    return rpta

@router.get("/get_salones/")
async def get_salones():
    rpta = nuevo_salon.get_salones()
    return rpta