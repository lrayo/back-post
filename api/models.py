from database import get_db_connection

def save_beacon_event(mac, latitude, longitude, phone, event_type):
    conn = get_db_connection()
    cur = conn.cursor()

    query = """
        INSERT INTO beacon_events (mac_address, latitude, longitude, phone_number, event_type)
        VALUES (%s, %s, %s, %s, %s)
    """
    cur.execute(query, (mac, latitude, longitude, phone, event_type))

    conn.commit()
    cur.close()
    conn.close()
