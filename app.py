from flask import Flask, request, jsonify
from redundancy_checker import insert_entry
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Data Redundancy Removal System API is Live!"

@app.route('/add', methods=['POST'])
def add_entry():
    data = request.json
    required_fields = ["name", "email", "phone", "colony", "timestamp"]
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing fields"}), 400

    insert_entry(data)
    return jsonify({"message": "Processed"}), 200

@app.route('/view', methods=['GET'])
def view_entries():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM entries")
    rows = cursor.fetchall()
    conn.close()
    return jsonify(rows)

if __name__ == '_main_':
    app.run(debug=True)