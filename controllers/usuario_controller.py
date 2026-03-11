import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.usuario_model import Usuario
from utility.security import hash_password
from fastapi.encoders import jsonable_encoder
    
class UsuarioController:

    def create_usuario(self, usuario: Usuario):   
        try:
            #password_hash
            usuario.password_hash = hash_password(usuario.password_hash)

            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO usuarios (primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, email, password_hash, id_rol, activo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (usuario.primer_nombre, usuario.segundo_nombre, usuario.primer_apellido, usuario.segundo_apellido, usuario.email, usuario.password_hash, usuario.id_rol, usuario.activo))
            conn.commit()
            conn.close()
            return {"resultado": "usuario creado"}
        except psycopg2.Error as err:
            print(err)
            # Si falla el INSERT, los datos no quedan guardados parcialmente en la base de datos
            # Se usa para deshacer los cambios de la transacción activa cuando ocurre un error en el try.
            conn.rollback()
            raise HTTPException(status_code=500, detail="Error al crear usuario")
        finally:
            conn.close()
        

    def get_usuario(self, usuario_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            
            result = cursor.fetchone()
            cursor.execute("SELECT u.id_usuario, u.primer_nombre, u.segundo_nombre, u.primer_apellido, u.segundo_apellido, u.email, u.password_hash, u.id_rol, r.nombre, u.activo FROM usuarios u LEFT JOIN roles r ON u.id_rol = r.id_rol WHERE u.id_usuario = %s", (usuario_id,))
            if result:
                content={
                        'id':int(result[0]),
                        'primer_nombre': result[1],
                        'segundo_nombre': result[2] if result[2] else None,
                        'primer_apellido': result[3],
                        'segundo_apellido': result[4] if result[4] else None,
                        'email':result[5],
                        'password_hash':result[6],
                        'id_rol':result[7],
                        'rol':result[8],
                        'activo':result[9]
                }
                
                json_data = jsonable_encoder(content)            
                return  json_data
            else:
                ##Esto interrumpe la ejecución y responde al cliente con un código 404
                ## comunica al cliente de la API qué pasó (error HTTP).
                ##código 404,comportamiento correcto según las reglas HTTP
                raise HTTPException(status_code=404, detail="usuario not found")  
                
        except psycopg2.Error as err:
            print(err)
            # Se usa para deshacer los cambios de la transacción activa cuando ocurre un error en el try.
            ##Maneja el estado de la transacción en la base de datos.Si un INSERT, UPDATE o DELETE falla dentro de una transacción, rollback() revierte esos cambios.
            conn.rollback()
            raise HTTPException(status_code=500, detail="Error al obtener usuario")
        finally:
            conn.close()

    def get_usuario_email(self, email: str):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT u.id_usuario, u.primer_nombre, u.segundo_nombre, u.primer_apellido, u.segundo_apellido, u.email, u.password_hash, u.id_rol, r.nombre, u.activo FROM usuarios u LEFT JOIN roles r ON u.id_rol = r.id_rol WHERE u.email = %s", (email,))
            result = cursor.fetchone()
            
            if result:
                content={
                        'id':int(result[0]),
                        'primer_nombre': result[1],
                        'segundo_nombre': result[2] if result[2] else None,
                        'primer_apellido': result[3],
                        'segundo_apellido': result[4] if result[4] else None,
                        'email':result[5],
                        'password_hash':result[6],
                        'id_rol':result[7],
                        'rol':result[8],
                        'activo':result[9]
                }
                
                return content
            else:
                ##Esto interrumpe la ejecución y responde al cliente con un código 404
                ## comunica al cliente de la API qué pasó (error HTTP).
                ##código 404,comportamiento correcto según las reglas HTTP
                raise HTTPException(status_code=404, detail="Usuario not found")  
                
        except psycopg2.Error as err:
            print(err)
            # Se usa para deshacer los cambios de la transacción activa cuando ocurre un error en el try.
            ##Maneja el estado de la transacción en la base de datos.Si un INSERT, UPDATE o DELETE falla dentro de una transacción, rollback() revierte esos cambios.
            conn.rollback()
            raise HTTPException(status_code=500, detail="Error al obtener Usuarios")
        finally:
            conn.close()