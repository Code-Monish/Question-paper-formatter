import sqlite3

# We make a connection with a database (Makes one if doesn't already exists.)
conn = sqlite3.connect("Hello.db")

# This is a 'Cursor/pointer' to where are connection is made
cursor = conn.cursor()

# Here using the simple execute cmd, we run SQL commands that is then read by the database.
cursor.execute('''CREATE TABLE IF NOT EXISTS employees
                  (id INTEGER PRIMARY KEY, name TEXT, position TEXT, salary REAL)''')
conn.commit() # And here.. finally we get to commit the changes to the database to be read....

# Till now we have 4 columns, 2 candidate keys (id , name)
# But we have zero records in it, let's write some right now....
data = [
    (1,"Monish N Pillay","Founder",2000000.00),
    (2,"John Doe","CEO",1800000.00),
    (3,"Chugus","Janitor",10000000000.99)
]

conn.executemany("INSERT OR IGNORE INTO employees VALUES (?, ?, ?, ?)", data)
conn.commit()

# db_data = cursor.execute("SELECT * FROM employees")
# db_data.fetchall()
# for i in range(0,len(data)):
#     print(db_data[i])

cursor.execute("SELECT * FROM employees")
employees = cursor.fetchall()

for employee in employees:
    print(employee)

conn.close()