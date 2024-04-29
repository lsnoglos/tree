import os
from dotenv import load_dotenv
import pyodbc

load_dotenv()

DB_HOST=os.getenv('DB_HOST')
DB_NAME=os.getenv('DB_NAME')
DB_USER=os.getenv('DB_USER')
DB_PASSWORD=os.getenv('DB_PASSWORD')
DRIVER='ODBC Driver 17 for SQL Server'

def create_connection (driver, server, db, user, password):
    try:
        connection_string = f'DRIVER={{{driver}}};SERVER={server};DATABASE={db};UID={user};PWD={password}'
        conn = pyodbc.connect(connection_string)
        print("Conexio'n exitosa.")
        return conn
    except Exception as e:
        print("Error de conexio'n", e)
        return None

connection = create_connection(DRIVER, DB_HOST, DB_NAME, DB_USER, DB_PASSWORD)

if(connection):
    connection.close()