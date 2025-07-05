from database import get_connection
from fuzzywuzzy import fuzz
import sqlite3

# Threshold for name similarity to detect false positives (adjustable)
SIMILARITY_THRESHOLD = 90

def is_duplicate(entry, cursor):
    """
    Check for exact duplicates based on email and phone.
    """
    cursor.execute(
        "SELECT * FROM entries WHERE lower(email) = lower(?) AND phone = ?",
        (entry["email"], entry["phone"])
    )
    return cursor.fetchone() is not None

def is_false_positive(entry, cursor):
    """
    Check for similar names already in the database using fuzzy matching.
    Flags false positives based on SIMILARITY_THRESHOLD.
    """
    cursor.execute("SELECT name FROM entries")
    names = [row[0] for row in cursor.fetchall()]
    for name in names:
        if fuzz.ratio(name.lower(), entry["name"].lower()) > SIMILARITY_THRESHOLD:
            return True
    return False

def insert_entry(entry):
    """
    Attempts to insert a new data entry after checking for:
    - Exact duplicates (rejected)
    - Similar names (flagged for manual review)
    - Otherwise, inserts into database
    """
    conn = get_connection()
    cursor = conn.cursor()

    if is_duplicate(entry, cursor):
        print("Duplicate entry detected. Not inserted.")
    elif is_false_positive(entry, cursor):
        print("Similar (False Positive) entry found. Review required.")
    else:
        try:
            cursor.execute('''
                INSERT INTO entries (name, email, phone, timestamp)
                VALUES (?, ?, ?, ?)
            ''', (entry["name"], entry["email"], entry["phone"], entry["timestamp"]))
            conn.commit()
            print("Entry inserted successfully.")
        except sqlite3.IntegrityError:
            print("Database rejected the entry as duplicate (UNIQUE constraint).")

    conn.close()