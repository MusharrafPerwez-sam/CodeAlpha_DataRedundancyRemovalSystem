# insert_entry_manual.py
# Optional file for testing single data entry manually

from redundancy_checker import insert_entry

# Manual test entry
entry = {
    "name": "Charlie Daniel",
    "email": "charlie@example.com",
    "phone": "9876512345",
    "colony": "Silver Garden",
    "timestamp": "2025-07-05 18:20"
}

# Call the main logic
insert_entry(entry)