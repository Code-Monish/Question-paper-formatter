"""This script will generate questions and it's meta data"""

def QuestionAdd(question_set,question_number):
    question = input("Enter the question here: ")
    question_weight = int(input("Enter the mark it holds: "))
    question_BTL = input("Enter BLT: ")
    question_CO = input("Enter CO: ")
    
    question_input = {"question":question,
                          "marks":question_weight,
                          "BTL":question_BTL,
                          "CO":question_CO}
    
    question_set[question_number] = question_input
    
    return question_set