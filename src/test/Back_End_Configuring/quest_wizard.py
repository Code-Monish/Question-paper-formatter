from QuestFormater import question_paper_setup
from QuestFormater import questions_creator
from QuestFormater import question_quit

print("My main is running!")
SESSION, QUESTION_META = question_paper_setup.QuestionPaperSetup()


QUESTION_RUNNING = True
QUESTION_BANK = {}
QUESTION_PARAMETERS = {"quiz":20,"mid_semester":50,"end_semester":100}
QUESTION = 1
PAPER_WEIGHT = 0

while QUESTION_RUNNING:
    QUESTION_BANK = questions_creator.QuestionAdd(QUESTION_BANK,QUESTION)
    question_mark_list = []
    
    # print(QUESTION_META)
    for question_details in QUESTION_BANK.values():
        question_weight = question_details["marks"]  # Ensure this is correct
        question_mark_list.append(question_weight)
        
    PAPER_WEIGHT = sum(question_mark_list)
        
    print(f"---This paper holds now : {PAPER_WEIGHT}---")
    print("=========")
    
    MARK_QUOTA = QUESTION_PARAMETERS[SESSION]
    print(MARK_QUOTA)
    if PAPER_WEIGHT < MARK_QUOTA:
        pass
    elif PAPER_WEIGHT == MARK_QUOTA:
        print("You've reached the mark limit!")
        question_quit.quitting_safe()
        QUESTION_RUNNING = False
        break
    else:
        print("Uh Oh... You're overboard")
        QUESTION_RUNNING = False
        break
    
    user_option = input("Do you want to add another question? Y/N: ")
    if user_option.lower() == "y":
        pass
    else:
        question_quit.quitting_safe()
        QUESTION_RUNNING = False
    QUESTION += 1
    
    
        
print("My program ends here...")