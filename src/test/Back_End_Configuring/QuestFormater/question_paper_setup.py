"""This script will ask the user few quetion paper data for the set up"""

import json


def QuestionPaperSetup():
    Course_code = input("Enter the course code: ")
    Session = input("Enter the session: ")
    Branch = input("Enter the branch: ")
    with open('testing.json', 'r') as course_file:
        course_data = json.load(course_file)
    course_file.close()
    print("========")
    for value in course_data.values():
        for course_dict in value:
            if Course_code in course_dict.values():
                print(f"Details on course found! \n{Course_code}")
                print("=======")
                question_paper_course = course_dict
                print(question_paper_course["course_details"])
                break
            else:
                continue
            
    print("========")
    print("Here is the data you've enterted:")
    print(f"Code - {Course_code}\nBranch - {Branch}\nSess - {Session}")
    print("========")