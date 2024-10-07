import sqlite3
conn = sqlite3.connect("demo.sql")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS employee (id INTEGER PRIMARY KEY, name TEXT, salary INTEGER);''')
cursor.execute('''
    INSERT INTO employee(id, name, salary) VALUES(3, 'KAVIN', 20000);
''')
conn.commit()
print(cursor.execute(''' SELECT * FROM employee '''))
