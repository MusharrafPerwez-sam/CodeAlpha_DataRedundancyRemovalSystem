# 🧹 Data Redundancy Removal System

A Python-based system to identify, classify, and remove redundant or similar (false-positive) data entries. It ensures a clean and accurate local database by validating new inputs before insertion.

---

## 🚀 Features

✅ Appends only *unique & validated entries*  
❌ Prevents *duplicate* data from being inserted  
⚠️ Flags *similar (false positive)* data for review  
🗃 Uses a local *SQLite database* (data.db)  
🔧 Modular, testable, and *easy to extend*  
📦 Works fully *offline* – no cloud required

---

## 🧠 How It Works

1. *database.py* initializes a SQLite database and creates the required table.
2. *redundancy_checker.py*:
   - Detects duplicates via exact match.
   - Detects similar entries using difflib.SequenceMatcher.
3. *test_input.py* provides sample/test data to demonstrate system behavior.

---

## 📂 Project Structure