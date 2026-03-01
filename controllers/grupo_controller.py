import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.grupo_model import Grupo
from fastapi.encoders import jsonable_encoder
    
class GrupoController:
        
    def create_grupo(self, grupo: Grupo):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO grupos (id_semestre,id_asignatura,id_jornada,codigo_grupo,cupo,estado) VALUES (%s,%s,%s,%s,%s,%s)", (grupo.id_semestre,grupo.id_asignatura,grupo.id_jornada,grupo.codigo,grupo.cupo,grupo.estado))
            conn.commit()
            conn.close()
            return {"resultado": "grupo creado"}
        except psycopg2.Error as err:
            print(err)
            # Si falla el INSERT, los datos no quedan guardados parcialmente en la base de datos
            # Se usa para deshacer los cambios de la transacción activa cuando ocurre un error en el try.
            conn.rollback()
        finally:
            conn.close()
        

    def get_grupo(self, grupo_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT g.id_grupo, g.id_semestre, s.nombre, g.id_asignatura, a.nombre, g.id_jornada, j.nombre, g.codigo_grupo, g.cupo, g.estado FROM grupos g join semestres s on g.id_semestre = s.id_semestre join asignaturas a on g.id_asignatura = a.id_asignatura join jornadas j on g.id_jornada = j.id_jornada WHERE id_grupo = %s", (grupo_id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            content={
                    'id':int(result[0]),
                    'id_semestre':int(result[1]),
                    'semestre':result[2],
                    'id_asignatura':int(result[3]),
                    'asignatura':result[4],
                    'id_jornada':int(result[5]),
                    'jornada':result[6],
                    'codigo':result[7],
                    'cupo':int(result[8]),
                    'estado':bool(result[9])
            }
            payload.append(content)
            
            json_data = jsonable_encoder(content)            
            if result:
                return  json_data
            else:
                ##Esto interrumpe la ejecución y responde al cliente con un código 404
                ## comunica al cliente de la API qué pasó (error HTTP).
                ##código 404,comportamiento correcto según las reglas HTTP
                raise HTTPException(status_code=404, detail="grupo not found")  
                
        except psycopg2.Error as err:
            print(err)
            # Se usa para deshacer los cambios de la transacción activa cuando ocurre un error en el try.
            ##Maneja el estado de la transacción en la base de datos.Si un INSERT, UPDATE o DELETE falla dentro de una transacción, rollback() revierte esos cambios.
            conn.rollback()
        finally:
            conn.close()
    
    def get_grupos(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT g.id_grupo, g.id_semestre, s.nombre, g.id_asignatura, a.nombre, g.id_jornada, j.nombre, g.codigo_grupo, g.cupo, g.estado FROM grupos g join semestres s on g.id_semestre = s.id_semestre join asignaturas a on g.id_asignatura = a.id_asignatura join jornadas j on g.id_jornada = j.id_jornada")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id':data[0],
                    'id_semestre':data[1],
                    'semestre':data[2],
                    'id_asignatura':data[3],
                    'asignatura':data[4],
                    'id_jornada':data[5],
                    'jornada':data[6],
                    'codigo':data[7],
                    'cupo':int(data[8]),
                    'estado':bool(data[9])
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)        
            if result:
                return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="grupo not found")  
                
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()