from config.db_config import get_db_connection
from controllers.programa_controller import ProgramaController
from models.asignatura_model import Asignatura

def validate(data: Asignatura):
    programa_controller = ProgramaController()

    # Validar que el programa exista
    try:
        programa_controller.get_programa(data.id_programa)
    except Exception:
        return {"error": "Programa no existe"}

    return {"valid": True}