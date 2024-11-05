"""This script will ask the user few quetion paper data for the set up"""
# def QuestionPaperSetup():
#     """Function runs when the question setup window shows up with options to initialize the paper file"""
    
#     # Takes in the important header data
#     Course_code = input("Enter the course code: ") # Using this code, we generate the rest of course related data
#     Session = input("Enter the session: ")
#     Branch = input("Enter the branch: ")
    
    
#     # Helps in spotting the exact code details of the code given.
#     # TODO : Find our a better searching algorithm. 
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

import sqlite3
import json

# Connect to the SQLite database (creates it if it doesn't exist)
conn = sqlite3.connect("../db/COURSES.db")
cursor = conn.cursor()

print("Courses Table:")
for row in cursor.execute("SELECT * FROM Courses"):
    print(row)

print("\nCourseOutcomes Table:")
for row in cursor.execute("SELECT * FROM CourseOutcomes"):
    print(row)

def QuestionPaperSetup():
    """Function runs when the question setup window shows up with options to initialize the paper file"""
    
    Course_code = input("Enter the course code: ") # Using this code, we generate the rest of course related data
    Session = input("Enter the session: ")
    Branch = input("Enter the branch: ")
    
    cursor.execute("""
                        SELECT * FROM Courses
                        JOIN CourseOutcomes ON Courses.course_code = CourseOutcomes.course_code
                        WHERE Courses.course_code = ?
                    """,(Course_code, ))
    
    course_meta = cursor.fetchall()
    print(course_meta)
    
# QuestionPaperSetup()