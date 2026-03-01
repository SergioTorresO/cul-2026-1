from config.db_config import get_db_connection
from controllers.semestre_controller import SemestreController
from controllers.asignatura_controller import AsignaturaController
from controllers.jornada_controller import JornadaController
from models.grupo_model import Grupo

def validate(data: Grupo):
    semestre_controller = SemestreController()
    asignatura_controller = AsignaturaController()
    jornada_controller = JornadaController()

    # Validar que el semestre exista
    try:
        semestre_controller.get_semestre(data.id_semestre)
    except Exception:
        return {"error": "Semestre no existe"}

    # Validar que la asignatura exista
    try:
        asignatura_controller.get_asignatura(data.id_asignatura)
    except Exception:
        return {"error": "Asignatura no existe"}

    # Validar que la jornada exista
    try:
        jornada_controller.get_jornada(data.id_jornada)
    except Exception:
        return {"error": "Jornada no existe"}

    return {"valid": True}