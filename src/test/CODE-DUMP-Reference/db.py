import sqlite3
import json

conn = sqlite3.connect('monish.db')
cursor = conn.cursor()

with open("testing.json", mode='r', encoding="utf8") as f:
    data = json.load(f)
    
cursor.execute("""CREATE TABLE IF NOT EXISTS course_data
               (course_code TEXT PRIMARY KEY, course_name TEXT)""")

# courses = [("23RAI111","C Programming"),("23MEE116","Engineering Mecanics")]

# cursor.executemany("""
#                 INSERT OR IGNORE INTO course_data VALUES
#                 (?, ?)
#                """,courses)



# conn.commit()
# result = cursor.execute("SELECT * FROM course_data")
# print(result.fetchall())

conn.close()