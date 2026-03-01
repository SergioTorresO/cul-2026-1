import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.asignacion_docente_model import AsignacionDocente
from fastapi.encoders import jsonable_encoder
    
class AsignacionDocenteController:
        
    def create_asignacion_docente(self, asignacionDocente: AsignacionDocente):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO asignacion_docente_grupo (id_docente,id_grupo, estado) VALUES (%s,%s,%s)", (asignacionDocente.id_docente,asignacionDocente.id_grupo,asignacionDocente.estado))
            conn.commit()
            conn.close()
            return {"resultado": "asignacionDocente creado"}
        except psycopg2.Error as err:
            print(err)
            # Si falla el INSERT, los datos no quedan guardados parcialmente en la base de datos
            # Se usa para deshacer los cambios de la transacción activa cuando ocurre un error en el try.
            conn.rollback()
        finally:
            conn.close()
        

    def get_asignacion_docente(self, asignacionDocente_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT ad.id_asignacion, ad.id_docente, d.primer_nombre, d.segundo_nombre, d.primer_apellido, d.segundo_apellido, ad.id_grupo, g.codigo_grupo, ad.estado FROM asignacion_docente_grupo ad join docentes d on ad.id_docente = d.id_docente join grupos g on g.id_grupo = ad.id_grupo WHERE id_asignacion = %s", (asignacionDocente_id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            content={
                    'id':int(result[0]),
                    'id_docente':int(result[1]),
                    'nombre':f"{result[2]} {result[3] if result[3] else ''} {result[4]} {result[5] if result[5] else ''}".strip(),
                    'id_grupo':int(result[6]),
                    'codigo_grupo': result[7],
                    'estado':bool(result[8])
            }
            payload.append(content)
            
            json_data = jsonable_encoder(content)            
            if result:
                return  json_data
            else:
                ##Esto interrumpe la ejecución y responde al cliente con un código 404
                ## comunica al cliente de la API qué pasó (error HTTP).
                ##código 404,comportamiento correcto según las reglas HTTP
                raise HTTPException(status_code=404, detail="asignacionDocente not found")  
                
        except psycopg2.Error as err:
            print(err)
            # Se usa para deshacer los cambios de la transacción activa cuando ocurre un error en el try.
            ##Maneja el estado de la transacción en la base de datos.Si un INSERT, UPDATE o DELETE falla dentro de una transacción, rollback() revierte esos cambios.
            conn.rollback()
        finally:
            conn.close()
    
    def get_asignacion_docentes(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT ad.id_asignacion, ad.id_docente, d.primer_nombre, d.segundo_nombre, d.primer_apellido, d.segundo_apellido, ad.id_grupo, g.codigo_grupo, ad.estado FROM asignacion_docente_grupo ad join docentes d on ad.id_docente = d.id_docente join grupos g on g.id_grupo = ad.id_grupo")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id':data[0],
                    'id_docente':int(data[1]),
                    'nombre':f"{data[2]} {data[3] if data[3] else ''} {data[4]} {data[5] if data[5] else ''}".strip(),
                    'id_grupo':int(data[6]),
                    'codigo_grupo': data[7],
                    'estado':bool(data[8])
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)        
            if result:
                return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="asignacionDocente not found")  
                
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()