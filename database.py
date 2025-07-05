import sqlite3

def create_db():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    # Create table with UNIQUE constraint on email
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT UNIQUE,
            phone TEXT,
            timestamp TEXT
        )
    ''')

    conn.commit()
    conn.close()

def get_connection():
    return sqlite3.connect('data.db')