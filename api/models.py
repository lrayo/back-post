import psycopg2

def save_beacon_event(mac, lat, lon, phone, event_type, platform):
    conn = psycopg2.connect(
        host="ep-rapid-brook-a4bdlztx-pooler.us-east-1.aws.neon.tech",
        database="neondb",
        user="neondb_owner",
        password="npg_8LBHPVWg0zaK",
        sslmode="require"
    )

    cursor = conn.cursor()
    query = """
        INSERT INTO beacon_events (mac_address, latitude, longitude, phone_number, event_type, platform)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (mac, lat, lon, phone, event_type, platform))
    conn.commit()
    cursor.close()
    conn.close()
