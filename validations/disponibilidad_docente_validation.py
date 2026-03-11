from controllers.docente_controller import DocenteController
from models.disponibilidad_docente_model import DisponibilidadDocente

def validate(data: DisponibilidadDocente):
    docente_controller = DocenteController()

    # Validar que el docente exista
    try:
        docente_controller.get_docente(data.id_docente)
    except Exception:
        return {"error": "Docente no existe"}

    return {"valid": True}