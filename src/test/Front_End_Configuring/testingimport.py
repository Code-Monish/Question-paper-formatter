

import sys
import os

# Add the path
current_script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_script_dir, '..'))
lib_path = os.path.join(parent_dir, 'Back_End_Configuring', 'QuestFormater')
sys.path.insert(0, lib_path)

# Try importing specific modules
# from questions_ import YourSpecificFunction
# or
import questions_

questions_.QuestionManipulator.update_question()