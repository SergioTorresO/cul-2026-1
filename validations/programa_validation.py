from models.programa_model import Programa
from controllers.facultad_controller import FacultadController

def validate(data: Programa):
    # Validar nombre no vacío
    if not data.nombre.strip():
        return {"error": "Nombre del programa es requerido"}

    # Validar que el ID de la facultad sea válido
    facultad_controller = FacultadController()
    try:
        facultad_controller.get_facultad(data.id_facultad)
    except Exception:
        return {"error": f"Facultad con ID {data.id_facultad} no existe"}

    # Validar código no vacío
    if not data.codigo.strip():
        return {"error": "Código del programa es requerido"}

    # Validar longitud del código (ejemplo: entre 2 y 10 caracteres)
    if len(data.codigo) < 2 or len(data.codigo) > 10:
        return {"error": "Código del programa debe tener entre 2 y 10 caracteres"}

    return {"valid": True}