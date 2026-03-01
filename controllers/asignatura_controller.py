import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.asignatura_model import Asignatura
from fastapi.encoders import jsonable_encoder
    
class AsignaturaController:
        
    def create_asignatura(self, asignatura: Asignatura):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO asignaturas (id_programa, nombre, codigo, horas_semanales, estado) VALUES (%s,%s,%s,%s,%s)", (asignatura.id_programa,asignatura.nombre,asignatura.codigo,asignatura.horas_semanales,asignatura.estado))
            conn.commit()
            conn.close()
            return {"resultado": "asignatura creado"}
        except psycopg2.Error as err:
            print(err)
            # Si falla el INSERT, los datos no quedan guardados parcialmente en la base de datos
            # Se usa para deshacer los cambios de la transacción activa cuando ocurre un error en el try.
            conn.rollback()
        finally:
            conn.close()
        

    def get_asignatura(self, asignatura_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM asignaturas WHERE id_asignatura = %s", (asignatura_id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            content={
                    'id':int(result[0]),
                    'id_programa':int(result[1]),
                    'nombre':result[2],
                    'codigo':result[3],
                    'horas_semanales':int(result[4]),
                    'estado':bool(result[5])
            }
            payload.append(content)
            
            json_data = jsonable_encoder(content)            
            if result:
                return  json_data
            else:
                ##Esto interrumpe la ejecución y responde al cliente con un código 404
                ## comunica al cliente de la API qué pasó (error HTTP).
                ##código 404,comportamiento correcto según las reglas HTTP
                raise HTTPException(status_code=404, detail="asignatura not found")  
                
        except psycopg2.Error as err:
            print(err)
            # Se usa para deshacer los cambios de la transacción activa cuando ocurre un error en el try.
            ##Maneja el estado de la transacción en la base de datos.Si un INSERT, UPDATE o DELETE falla dentro de una transacción, rollback() revierte esos cambios.
            conn.rollback()
        finally:
            conn.close()
    
    def get_asignaturas(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM asignaturas")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id':data[0],
                    'id_programa':int(data[1]),
                    'nombre':data[2],
                    'codigo':data[3],
                    'horas_semanales':int(data[4]),
                    'estado':bool(data[5])
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)        
            if result:
                return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="asignatura not found")  
                
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()