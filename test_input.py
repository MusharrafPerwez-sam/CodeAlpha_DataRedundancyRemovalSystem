import sqlite3
from database import create_db
from redundancy_checker import insert_entry

# Reset database before each test run
def reset_db():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS entries")
    conn.commit()
    conn.close()

# Reset and recreate table
reset_db()
create_db()

# Sample data entries
entries = [
    {
        "name": "Alice Johnson",  # Should insert
        "email": "alice@example.com",
        "phone": "1234567890",
        "colony": "Green Park",
        "timestamp": "2025-06-14 14:00"
    },
    {
        "name": "Alice Johnson",  # Duplicate
        "email": "alice@example.com",
        "phone": "1234567890",
        "colony": "Green Park",
        "timestamp": "2025-06-14 14:05"
    },
    {
        "name": "Alyce Jonson",   # False positive (fuzzy match)
        "email": "alyce@example.com",
        "phone": "1234567899",
        "colony": "Green Park",
        "timestamp": "2025-06-14 14:10"
    },
    {
        "name": "Bob Smith",      # Should insert
        "email": "bob@example.com",
        "phone": "9876543210",
        "colony": "Silver Colony",
        "timestamp": "2025-06-14 14:15"
    }
]

# Run test entries
for entry in entries:
    insert_entry(entry)