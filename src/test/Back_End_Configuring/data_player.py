import sqlite3
import os

def get_database_connection():
    db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'db/COURSES.db'))
    return sqlite3.connect(db_path)

def find_and_remove_duplicates(cursor):
    # Find duplicates
    query = """
    SELECT course_code, description, COUNT(*)
    FROM CourseOutcomes
    GROUP BY course_code, description
    HAVING COUNT(*) > 1;
    """
    cursor.execute(query)
    duplicates = cursor.fetchall()

    # Remove duplicates, keeping one instance
    for course_code, description, count in duplicates:
        delete_query = """
        DELETE FROM CourseOutcomes
        WHERE rowid NOT IN (
            SELECT MIN(rowid)
            FROM CourseOutcomes
            WHERE course_code = ? AND description = ?
        ) AND course_code = ? AND description = ?;
        """
        cursor.execute(delete_query, (course_code, description, course_code, description))

def main():
    conn = get_database_connection()
    cursor = conn.cursor()

    find_and_remove_duplicates(cursor)
    conn.commit()

    print("Duplicate course outcomes removed.")

    cursor.execute("DROP TABLE Question")
    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()