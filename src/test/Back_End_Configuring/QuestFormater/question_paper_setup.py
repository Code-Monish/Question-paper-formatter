"""This script will ask the user few quetion paper data for the set up"""

import json
import sqlite3

CONN = sqlite3.connect("Test.db")
CURSOR = CONN.cursor()

def QuestionPaperSetup():
    """Function runs when the question setup window shows up with options to initialize the paper file"""
    
    # Takes in the important header data
    Course_code = input("Enter the course code: ") # Using this code, we generate the rest of course related data
    Session = input("Enter the session: ")
    Branch = input("Enter the branch: ")
    
    
    # This is opening the course's json 'database' which has all the course detail info 
    with open('testing.json', 'r') as course_file:
        course_data = json.load(course_file)
    course_file.close()
    
    
    CURSOR.execute("""CREATE TABLE IF NOT EXISTS courses
                   (code TEXT PRIMARY KEY, details TEXT)""")
    
    
    
    
    # Helps in spotting the exact code details of the code given.
    # TODO : Find our a better searching algorithm. 
    print("========")
    for value in course_data.values():
        for course_dict in value:
            if Course_code in course_dict.values():
                print(f"Details on course found! \n{Course_code}")
                print("=======")
                question_paper_course = course_dict
                # print(question_paper_course["course_details"])
                break
            else:
                question_paper_course = {}
                continue
            
    # Returning the session and the code's details
    return Session, question_paper_course
    
    # print("========")
    # print(f"Code - {Course_code}\nBranch - {Branch}\nSess - {Session}")
    # print("Here is the data you've enterted:")
    # print("========")