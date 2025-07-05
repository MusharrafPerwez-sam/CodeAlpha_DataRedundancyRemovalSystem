from flask import Flask, render_template, request, redirect
import sqlite3
from fuzzywuzzy import fuzz
import os

app = Flask(__name__)

# Initialize or connect to the database
def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL,
            colony TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# Helper function to check redundancy
def is_redundant(name, email, phone, colony):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT name, email, phone, colony FROM entries")
    all_entries = c.fetchall()
    conn.close()

    for entry in all_entries:
        existing_name, existing_email, existing_phone, existing_colony = entry

        # Fuzzy matching
        name_ratio = fuzz.ratio(name.lower(), existing_name.lower())
        email_ratio = fuzz.ratio(email.lower(), existing_email.lower())
        phone_ratio = fuzz.ratio(phone, existing_phone)
        colony_ratio = fuzz.ratio(colony.lower(), existing_colony.lower())

        if name_ratio > 90 and email_ratio > 90 and phone_ratio > 90 and colony_ratio > 90:
            return True

    return False

# Insert new entry
def insert_entry(name, email, phone, colony):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("INSERT INTO entries (name, email, phone, colony) VALUES (?, ?, ?, ?)",
              (name, email, phone, colony))
    conn.commit()
    conn.close()

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    colony = request.form['colony']

    if not is_redundant(name, email, phone, colony):
        insert_entry(name, email, phone, colony)
        return render_template('result.html', message="✅ Unique entry added to the database.")
    else:
        return render_template('result.html', message="⚠️ Redundant entry detected. Not added.")

@app.route('/view')
def view_entries():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT name, email, phone, colony FROM entries")
    data = c.fetchall()
    conn.close()
    return render_template('view.html', data=data)

# Render-specific: bind to dynamic PORT
if __name__ == '_main_':
    port = int(os.environ.get('PORT', 5000))  # required for Render
    app.run(host='0.0.0.0', port=port)