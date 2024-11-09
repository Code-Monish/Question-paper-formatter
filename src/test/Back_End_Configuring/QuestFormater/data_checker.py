"""This module will help you get general info of the database"""

import sqlite3
import os

class DataChecker:
    @staticmethod
    def get_database_connection():
        db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../db/COURSES.db'))
        return sqlite3.connect(db_path)

    @staticmethod
    def get_table_names(cursor):
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        return [row[0] for row in cursor.fetchall()]

    @staticmethod
    def print_top_5_rows(cursor, table_name):
        cursor.execute(f"SELECT * FROM {table_name} LIMIT 5;")
        rows = cursor.fetchall()
        print(f"Top 5 rows from table {table_name}:")
        for row in rows:
            print(row)
        print("\n")

def main():
    conn = DataChecker.get_database_connection()
    cursor = conn.cursor()

    table_names = DataChecker.get_table_names(cursor)
    for table_name in table_names:
        DataChecker.print_top_5_rows(cursor, table_name)

    conn.close()

# if __name__ == "__main__":
#     main()