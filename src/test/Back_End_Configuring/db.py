import sqlite3
import json

conn = sqlite3.connect('monish.db')
cursor = conn.cursor()

with open("testing.json", 'r') as f:
    data = json.load(f)

print(data)