import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.horario_model import Horario
from fastapi.encoders import jsonable_encoder
    
class HorarioController:
        
    def create_horario(self, horario: Horario):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO horarios (id_grupo,id_salon,id_jornada,dia_semana,hora_inicio,hora_fin) VALUES (%s,%s,%s,%s,%s,%s)", (horario.id_grupo,horario.id_salon,horario.id_jornada,horario.dia_semana,horario.hora_inicio,horario.hora_fin))
            conn.commit()
            conn.close()
            return {"resultado": "horario creado"}
        except psycopg2.Error as err:
            print(err)
            # Si falla el INSERT, los datos no quedan guardados parcialmente en la base de datos
            # Se usa para deshacer los cambios de la transacción activa cuando ocurre un error en el try.
            conn.rollback()
        finally:
            conn.close()
        

    def get_horario(self, horario_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT h.id_horario, h.id_grupo, g.codigo_grupo, h.id_salon, s.codigo, h.id_jornada, j.nombre, h.dia_semana, h.hora_inicio, h.hora_fin FROM horarios h join grupos g on h.id_grupo = g.id_grupo join salones s on h.id_salon = s.id_salon join jornadas j on h.id_jornada = j.id_jornada WHERE id_horario = %s", (horario_id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            content={
                    'id':int(result[0]),
                    'id_grupo':int(result[1]),
                    'codigo_grupo':result[2],
                    'id_salon':int(result[3]),
                    'codigo_salon':result[4],
                    'id_jornada':int(result[5]),
                    'jornada':result[6],
                    'dia_semana':result[7],
                    'hora_inicio':result[8],
                    'hora_fin':result[9]
            }
            payload.append(content)
            
            json_data = jsonable_encoder(content)            
            if result:
                return  json_data
            else:
                ##Esto interrumpe la ejecución y responde al cliente con un código 404
                ## comunica al cliente de la API qué pasó (error HTTP).
                ##código 404,comportamiento correcto según las reglas HTTP
                raise HTTPException(status_code=404, detail="horario not found")  
                
        except psycopg2.Error as err:
            print(err)
            # Se usa para deshacer los cambios de la transacción activa cuando ocurre un error en el try.
            ##Maneja el estado de la transacción en la base de datos.Si un INSERT, UPDATE o DELETE falla dentro de una transacción, rollback() revierte esos cambios.
            conn.rollback()
        finally:
            conn.close()
    
    def get_horarios(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT h.id_horario, h.id_grupo, g.codigo_grupo, h.id_salon, s.codigo, h.id_jornada, j.nombre, h.dia_semana, h.hora_inicio, h.hora_fin FROM horarios h join grupos g on h.id_grupo = g.id_grupo join salones s on h.id_salon = s.id_salon join jornadas j on h.id_jornada = j.id_jornada")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id':data[0],
                    'id_grupo':data[1],
                    'codigo_grupo':data[2],
                    'id_salon':data[3],
                    'codigo_salon':data[4],
                    'id_jornada':data[5],
                    'jornada':data[6],
                    'dia_semana':data[7],
                    'hora_inicio':data[8],
                    'hora_fin':data[9]
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)        
            if result:
                return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="horario not found")  
                
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()