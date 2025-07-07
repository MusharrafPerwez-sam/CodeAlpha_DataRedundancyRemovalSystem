import sqlite3

def create_db():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    # Create table with UNIQUE email and required fields
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            phone TEXT NOT NULL,
            colony TEXT NOT NULL,
            timestamp TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

def get_connection():
    return sqlite3.connect('data.db')