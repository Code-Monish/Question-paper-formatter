from QuestFormater import question_paper_setup
from QuestFormater import questions_creator

print("My main is running!")
# question_paper_setup.QuestionPaperSetup()


APP_RUNNING = True

while APP_RUNNING:
    questions_creator.QuestionAdd()
    user_option = input("Do you want ot add another question? Y/N: ")
    if user_option.lower() == "y":
        continue
    else:
        APP_RUNNING = False
        
print("My program ends here...")