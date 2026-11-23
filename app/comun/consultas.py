from app import db

ESTATUS = ("Puntual", "Retardo", "falta", "Falta justificada", "Salida anticipada")

INSIGNIA = {
    "Puntual": "insignia-puntual",
    "Retardo": "insignia-retardo",
    "Falta": "insignia-falta",
    "Falta justificada": "insignia-justificada",
    "Salida anticipada": "insignia-salida",
}

def alumno_por_uid(uid):
    """Busca al alumno dueño de una credencial ACTIVA. Devuelve None si no exixte."""
    return db.consultar_uno(
        """SELECT a.alumno_id, a.matricula, a.nombre, a.apellidos, a.grupo_id 
            FROM credencial c
            JOIN alumno a ON a.alumno_id = c.alumno_id
           WHERE c.uid_rfid = %s AND c.estatus = 'Activa' AND a.estado = 'Activo' """,
        (uid,),
    )

def horario_del_dia(grupo_id, dia_semana):
    """ """