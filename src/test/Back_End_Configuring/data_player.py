import sqlite3
import os 

db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "db/COURSES.db"))
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# cursor.execute("""
#                CREATE TABLE IF NOT EXISTS Questions
#                     (id INTEGER PRIMARY KEY,
#                     Question TEXT NOT NULL,
#                     Marks INTEGER NOT NULL,
#                     BTL TEXT NOT NULL,
#                     FOREIGN KEY (CO) REFERENCES COs (CO))
                    
#                """)

cursor.execute("DROP TABLE sqlite_sequence")
conn.commit()
conn.close()