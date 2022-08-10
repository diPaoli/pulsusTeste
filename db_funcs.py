import mysql.connector


v_host='localhost'
v_port = 3306
v_user='root'
v_pw = 'admin'
v_db = 'pulsusteste'

conn = mysql.connector.connect(host=v_host,  
                                    port=v_port,
                                    user=v_user,
                                    password=v_pw,
                                    db=v_db)


# Retorna todos os Devices
def select_AllDevs():    
    query = "SELECT * FROM devices"
    
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()

    
    #for row in rows:
     #   print(row)

    return rows
    


# Retorna 1 Device
def select_Dev(dev_id):
    query = "SELECT * FROM devices WHERE id = %s"
    
    cursor = conn.cursor()
    cursor.execute(query, [dev_id])
    rows = cursor.fetchone()
    return rows




# Retorna todos os Locals
def select_AllLocals():
    query = "SELECT * FROM locals"
    
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()



    return rows

   


# Retorna todos os locais por onde 1 Device passou
def select_DevLocals(dev_id):
    query = ("SELECT d.id, d.motorista, l.data, l.lat, l.lon "
            "FROM devices d, locals l "
            "WHERE d.id = l.dev_id AND d.id = %s"
            "ORDER BY d.id, l.data")
    
    cursor = conn.cursor()
    cursor.execute(query, [dev_id])
    rows = cursor.fetchall()

    return rows




# Registra 1 Local
def insert_Local(dev_id, lat, lon):
    query = ("INSERT INTO locals (dev_id, data, lat, lon) "
            "values (%s, now(), %s, %s)")

    cursor = conn.cursor()
    cursor.execute(query, [dev_id, lat, lon])
    return cursor.lastrowid