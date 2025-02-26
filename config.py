import pymysql

# Configuración de la conexión a MySQL
def obtener_conexion():
    return pymysql.connect(
        host="localhost",
        user="root",   
        password="",  
        database="usuarios_db",
        cursorclass=pymysql.cursors.DictCursor
    )
