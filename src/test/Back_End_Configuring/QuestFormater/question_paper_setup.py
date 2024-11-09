"""This script will ask the user few quetion paper data for the set up"""

import sqlite3
import os

db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../db/COURSES.db'))
# Connect to the SQLite database (creates it if it doesn't exist)
conn = sqlite3.connect(db_path)
cursor = conn.cursor()


def QuestionPaperSetup():
    """Function runs when the question setup window shows up with options to initialize the paper file"""
    
    Course_code = input("Enter the course code: ") # Using this code, we generate the rest of course related data
    Session = input("Enter the session: ")
    Branch = input("Enter the branch: ")
    
    # Create a temporary table
    cursor.execute("""
        CREATE TEMPORARY TABLE CourseDummy AS
        SELECT *
        FROM Courses
        JOIN CourseOutcomes ON Courses.course_code = CourseOutcomes.course_code
        WHERE Courses.course_code = ?
    """, (Course_code,))

    # Drop the unwanted column from the temporary table
    cursor.execute("""
        ALTER TABLE CourseDummy
        DROP COLUMN course_code
    """)

    # Select all data from the temporary table
    cursor.execute("""
        SELECT * FROM CourseDummy
    """)

    # Fetch the results if needed
    results = cursor.fetchall()
    # print(results)

    # Drop the temporary table
    cursor.execute("""
        DROP TABLE CourseDummy
    """)

    
    return Session, results


# print("Courses Table:")
# for row in cursor.execute("SELECT * FROM Courses"):
#     print(row)

# print("\nCourseOutcomes Table:")
# for row in cursor.execute("SELECT * FROM CourseOutcomes"):
#     print(row)
    
#     # Helps in spotting the exact code details of the code given.
#     print("========")
#     for value in course_data.values():
#         for course_dict in value:
#             if Course_code in course_dict.values():
#                 print(f"Details on course found! \n{Course_code}")
#                 print("=======")
#                 question_paper_course = course_dict
#                 # print(question_paper_course["course_details"])
#                 break
#             else:
#                 question_paper_course = {}
#                 continue
            
#     # Returning the session and the code's details
#     return Session, question_paper_course
# QuestionPaperSetup()