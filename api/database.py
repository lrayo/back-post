import psycopg2
from psycopg2.extras import RealDictCursor

def get_db_connection():
    return psycopg2.connect(
        dbname='nombre_basedatos',
        user='usuario',
        password='contraseña',
        host='localhost',
        port='5432',
        cursor_factory=RealDictCursor
    )
