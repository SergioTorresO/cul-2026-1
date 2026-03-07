from controllers.docente_controller import DocenteController
from controllers.asignatura_controller import AsignaturaController
from models.docente_asignatura_model import DocenteAsignatura

def validate(docente_asignatura: DocenteAsignatura):
    docente_controller = DocenteController()
    asignatura_controller = AsignaturaController()

    # Validar que el docente exista
    try:
        docente_controller.get_docente(docente_asignatura.id_docente)
    except Exception:
        return {"error":f"Docente con ID {docente_asignatura.id_docente} no existe"}

    # Validar que la asignatura exista
    try:
        asignatura_controller.get_asignatura(docente_asignatura.id_asignatura)
    except Exception:
        return {"error":f"Asignatura con ID {docente_asignatura.id_asignatura} no existe"}
    
    return {"valid": True}