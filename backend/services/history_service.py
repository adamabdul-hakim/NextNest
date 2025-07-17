import sqlite3

DB_NAME = "search_history.db"

def save_search(origin_city, destination_city, role, travel_date):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute(
        "INSERT INTO history (origin_city, destination_city, role, travel_date) VALUES (?, ?, ?, ?)",
        (origin_city, destination_city, role, travel_date)
    )
    conn.commit()
    conn.close()

def get_history():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT origin_city, destination_city, role, travel_date FROM history ORDER BY id DESC")
    rows = c.fetchall()
    conn.close()
    history = []
    for row in rows:
        history.append({
            "origin_city": row[0],
            "destination_city": row[1],
            "role": row[2],
            "travel_date": row[3]
        })
    return history

def clear_history():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("DELETE FROM history")
    conn.commit()
    conn.close()
