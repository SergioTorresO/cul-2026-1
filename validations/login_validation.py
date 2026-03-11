from utility.security import verify_password, create_access_token
from controllers.usuario_controller import UsuarioController
from models.usuario_model import Usuario

def validate(data):
    login_controller = UsuarioController()

    # Validar que el usuario exista
    
    try:
        usuario = Usuario(**login_controller.get_usuario_email(data["email"]))
        print("usuario", usuario)
    except Exception:
        return {"error": "Credenciales incorrectas"}
    
    if not verify_password(data["password"], usuario.password_hash):
        return {"error": "Credenciales incorrectas"}
    
    token = create_access_token({
        "user_id": usuario.id,
        "rol": usuario.id_rol
    })

    return {"valid": True, "access_token": token}
