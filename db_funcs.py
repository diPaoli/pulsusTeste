import mysql.connector
from datetime import datetime

from log.log_gen import createLog


v_host='localhost'
v_port = 3306
v_user='root'
v_pw = 'admin'
v_db = 'pulsusteste'

"""
    Num sistema sério seria esperado um módulo separado para
    autenticação e autorização.
    Nesse exemplo, como não temos outros objetos e funções, 
    faremos tudo no mesmo módulo.
"""

# Conecta o DB
try:
    conn = mysql.connector.connect(host=v_host,  
                                    port=v_port,
                                    user=v_user,
                                    password=v_pw,
                                    db=v_db)
except Exception as e:
    createLog(datetime.now(), v_user, e)


    

# Retorna todos os Devices
def select_AllDevs():    
    query = "SELECT * FROM devices"
    
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows
    except Exception as e:
        createLog(datetime.now(), v_user, e)
        return None


    
    


# Retorna 1 Device
def select_Dev(dev_id):
    query = "SELECT * FROM devices WHERE id = %s"
    
    try:
        cursor = conn.cursor()
        cursor.execute(query, [dev_id])
        rows = cursor.fetchone()
        return rows
    except Exception as e:
        createLog(datetime.now(), v_user, e)
    return None




# Retorna todos os Locals
def select_AllLocals():
    query = "SELECT * FROM locals"
    
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows
    except Exception as e:
        createLog(datetime.now(), v_user, e)
    return None

   


# Retorna todos os locais por onde 1 Device passou
def select_DevLocals(dev_id):
    query = ("SELECT d.id, d.motorista, l.data, l.lat, l.lon "
            "FROM devices d, locals l "
            "WHERE d.id = l.dev_id AND d.id = %s"
            "ORDER BY d.id, l.data")
    
    try:
        cursor = conn.cursor()
        cursor.execute(query, [dev_id])
        rows = cursor.fetchall()
        return rows
    except Exception as e:
        createLog(datetime.now(), v_user, e)
    return None




# Registra 1 Local
def insert_Local(dev_id, lat, lon):
    query = ("INSERT INTO locals (dev_id, data, lat, lon) "
            "values (%s, now(), %s, %s)")

    try:
        cursor = conn.cursor()
        cursor.execute(query, [dev_id, lat, lon])
        return cursor.lastrowid
    except Exception as e:
        createLog(datetime.now(), v_user, e)
    return None