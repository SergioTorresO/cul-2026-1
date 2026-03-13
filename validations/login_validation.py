from utility.security import verify_password, create_access_token
from controllers.docente_controller import DocenteController
from models.docente_model import Docente
from models.login_model import Login

def validate(data:Login):
    login_controller = DocenteController()

    # Validar que el usuario exista
    try:
        usuario = Docente(**login_controller.get_docente_email(data.email))
    except Exception:
        return {"error": "Credenciales incorrectas"}
    
    if not verify_password(data.password, usuario.password_hash):
        return {"error": "Credenciales incorrectas"}
    
    token = create_access_token({
        "user_id": usuario.id,
        "rol": usuario.id_rol
    })

    return {"valid": True, "access_token": token}
