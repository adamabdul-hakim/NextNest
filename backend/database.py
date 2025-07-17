import sqlite3

def init_db():
    conn = sqlite3.connect('search_history.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            origin_city TEXT NOT NULL,
            destination_city TEXT NOT NULL,
            role TEXT,
            travel_date TEXT
        )
    ''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
