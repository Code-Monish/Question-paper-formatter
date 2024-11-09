from QuestFormater import question_paper_setup
from QuestFormater import questions_
from QuestFormater import question_quit
from QuestFormater import data_checker

from datetime import datetime
import sqlite3

conn = sqlite3.connect("db/COURSES.db")
cursor = conn.cursor()

print("My main is running!")
print("========== COURSES.db PREVIEW =============")
print(data_checker.main())
print("========== PREVIEW END =============")

SESSION, QUESTION_META = question_paper_setup.QuestionPaperSetup()

print(SESSION)
for questmeta in range(0,len(QUESTION_META)):
    print(QUESTION_META[questmeta])
    
now = datetime.now()

QUESTION_RUNNING = True
QUESTION_TITLE = str(now)
print("=======================")
print(QUESTION_TITLE)
print("=======================")
# QUESTION_PARAMETERS = {"quiz":20,"mid_semester":50,"end_semester":100}
PAPER_WEIGHT = 0

while QUESTION_RUNNING:
    print("GIMME some questions! 🗣️  🗣️  🗣️")
    print(f"Here's the QID's data type : {type(QUESTION_TITLE)}")
    print("==================")
    questions_.QuestionManipulator.QuestionAdd(QUESTION_TITLE)
    # PAPER_WEIGHT += 1
    
    print("==================")
    
    user_option = input("Do you want to add another question? Y/N: ")
    if user_option.lower() == "y":
        pass
    else:
        question_quit.quitting_safe()
        QUESTION_RUNNING = False
        
#     QUESTION_BANK = questions_.QuestionAdd(QUESTION_BANK,QUESTION)
#     question_mark_list = []
    
#     # print(QUESTION_META)
#     for question_details in QUESTION_BANK.values():
#         question_weight = question_details["marks"]  # Ensure this is correct
#         question_mark_list.append(question_weight)
        
#     PAPER_WEIGHT = sum(question_mark_list)
        
#     print(f"---This paper holds now : {PAPER_WEIGHT}---")
#     print("=========")
    
#     MARK_QUOTA = QUESTION_PARAMETERS[SESSION]
#     print(MARK_QUOTA)
#     if PAPER_WEIGHT < MARK_QUOTA:
#         pass
#     elif PAPER_WEIGHT == MARK_QUOTA:
#         print("You've reached the mark limit!")
#         question_quit.quitting_safe()
#         QUESTION_RUNNING = False
#         break
#     else:
#         print("Uh Oh... You're overboard")
#         QUESTION_RUNNING = False
#         break
    
#     QUESTION += 1
    
    
        
print("My program ends here...")