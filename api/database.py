import psycopg2
from psycopg2.extras import RealDictCursor

def get_db_connection():
    return psycopg2.connect(
        dbname='neondb',
        user='neondb_owner',
        password='npg_8LBHPVWg0zaK',
        host='ep-rapid-brook-a4bdlztx-pooler.us-east-1.aws.neon.tech',
        port='5432',
        cursor_factory=RealDictCursor
    )
