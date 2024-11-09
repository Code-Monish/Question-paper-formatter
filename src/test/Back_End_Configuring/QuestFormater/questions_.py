"""This script will generate questions and it's meta data"""

import sqlite3
import os

db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../db/COURSES.db'))
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

class QuestionManipulator():
    """
        This class holds the methods for adding, deleting and updating questions
    """
    
    def QuestionAdd():
        question = input("Enter the question here: ")
        question_weight = int(input("Enter the mark it holds: "))
        question_BTL = input("Enter BLT: ")
        question_CO = input("Enter CO: ")

        cursor.execute("""
                       INSERT INTO Questions (Question, Marks, BTL, CO)
                         VALUES (?,?,?,?)
                        """,(question,question_weight,question_BTL,question_CO))

        conn.commit()
        conn.close()
        
    def QuestionDelete():
        question_id = int(input("Enter the question id: "))
        cursor.execute("""
                       DELETE FROM Questions WHERE id = ?
                       """,(question_id,))

        conn.commit()
        conn.close()
        
    def QuestionUpdate():
        question_id = int(input("Enter the question id: "))
        question = input("Enter the question here: ")
        question_weight = int(input("Enter the mark it holds: "))
        question_BTL = input("Enter BLT: ")
        question_CO = input("Enter CO: ")

        cursor.execute("""
                       UPDATE Questions SET Question = ?, Marks = ?, BTL = ?, CO = ? WHERE id = ?
                       """,(question,question_weight,question_BTL,question_CO,question_id))

        conn.commit()
        conn.close()
    