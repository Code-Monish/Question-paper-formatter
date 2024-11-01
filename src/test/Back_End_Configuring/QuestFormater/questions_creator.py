"""This script will generate questions and it's meta data"""

QUESTION_BANK = {}
WEIGHT_SUM = 0

def QuestionAdd():
    print(QUESTION_BANK)
    question = input("Enter the question here: ")
    question_weight = int(input("Enter the mark it holds: "))
    question_BTL = input("Enter BLT: ")
    question_CO = input("Enter CO: ")
    
    question_input = {"question":question,
                          "marks":question_weight,
                          "BTL":question_BTL,
                          "CO":question_CO}
    
    if len(QUESTION_BANK) == 0:
        pass
    else:
        QUESTION_BANK.update(question_input)
        
        
    return QUESTION_BANK