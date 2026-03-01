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
            conn.rollback()
            raise HTTPException(status_code=500, detail="Error al crear asignacionDocente")
        finally:
            conn.close()

    def get_asignacion_docente(self, asignacionDocente_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT ad.id_asignacion, ad.id_docente, d.primer_nombre, d.segundo_nombre, d.primer_apellido, d.segundo_apellido, ad.id_grupo, g.codigo_grupo, ad.estado FROM asignacion_docente_grupo ad join docentes d on ad.id_docente = d.id_docente join grupos g on g.id_grupo = ad.id_grupo WHERE id_asignacion = %s", (asignacionDocente_id,))
            result = cursor.fetchone()

            if result:
                content={
                        'id':int(result[0]),
                        'id_docente':int(result[1]),
                        'nombre':f"{result[2]} {result[3] if result[3] else ''} {result[4]} {result[5] if result[5] else ''}".strip(),
                        'id_grupo':int(result[6]),
                        'codigo_grupo': result[7],
                        'estado':bool(result[8])
                }
                
                json_data = jsonable_encoder(content) 
                return  json_data
            else:
                # Si no se encuentra el registro, se lanza una excepción HTTP 404 Not Found con un mensaje de error.
                raise HTTPException(status_code=404, detail="asignacion docente no encontrada")  
                
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
            raise HTTPException(status_code=500, detail="Error al obtener asignacionDocente")
        finally:
            conn.close()
    
    def get_asignacion_docentes(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT ad.id_asignacion, ad.id_docente, d.primer_nombre, d.segundo_nombre, d.primer_apellido, d.segundo_apellido, ad.id_grupo, g.codigo_grupo, ad.estado FROM asignacion_docente_grupo ad join docentes d on ad.id_docente = d.id_docente join grupos g on g.id_grupo = ad.id_grupo")
            result = cursor.fetchall()
            
            if result:
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
                return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="asignacionDocente not found")  
                
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
            raise HTTPException(status_code=500, detail="Error al obtener asignacionDocentes")
        finally:
            conn.close()