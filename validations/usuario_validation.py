from models.usuario_model import Usuario
from controllers.usuario_controller import UsuarioController
import re

def validate(data: Usuario):
    if not data.primer_nombre:
        raise ValueError("El primer nombre es requerido")
    if not data.primer_apellido:
        raise ValueError("El primer apellido es requerido")
    if not data.email:
        raise ValueError("El email es requerido")
    if not data.password_hash:
        raise ValueError("La contraseña es requerida")
    if not data.id_rol:
        raise ValueError("El rol es requerido")
    
    # Validar formato de email
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_regex, data.email):
        return {"error": "Formato de email no válido"}
    
    # Validar que el rol exista
    if data.id_rol not in [1, 2]:  # Asumiendo que solo hay dos roles: 1 (admin) y 2 (usuario)
        return {"error": f"Rol con ID {data.id_rol} no existe"}
    
    # Validar que el email no esté registrado
    usuario_controller = UsuarioController()
    try:
        usuario_controller.get_usuario(data.email)
        return {"error": "El email ya está registrado"}
    except Exception:
        pass


    return {"valid": True}
