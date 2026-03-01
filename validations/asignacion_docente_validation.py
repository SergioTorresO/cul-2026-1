from config.db_config import get_db_connection
from controllers.docente_controller import DocenteController
from controllers.grupo_controller import GrupoController
from models.asignacion_docente_model import AsignacionDocente

def validate(data: AsignacionDocente):
    docente_controller = DocenteController()
    grupo_controller = GrupoController()

    # Validar que el docente exista
    try:
        docente_controller.get_docente(data.id_docente)
    except Exception:
        return {"error": "Docente no existe"}

    # Validar que el grupo exista
    try:
        grupo_controller.get_grupo(data.id_grupo)
    except Exception:
        return {"error": "Grupo no existe"}

    return {"valid": True}