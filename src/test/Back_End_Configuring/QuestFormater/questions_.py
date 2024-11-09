"""This script will generate questions and it's meta data"""

import sqlite3
import os
# from datetime import datetime

db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../db/COURSES.db'))
conn = sqlite3.connect(db_path)
cursor = conn.cursor()



class QuestionManipulator():
    """
        This class holds the methods for adding, deleting and updating questions
    """
    
    def QuestionAdd(QID):
        try:
            question_id = str(QID)
            # print(type(QID))
            question = input("Enter the question here: ")
            question_weight = int(input("Enter the mark it holds: "))
            question_BTL = input("Enter BLT: ")
            question_CO = input("Enter CO: ")
            
            cursor.execute("""
                            CREATE TABLE IF NOT EXISTS Questions (
                                id TEXT PRIMARY KEY,
                                Question TEXT NOT NULL,
                                Marks INTEGER NOT NULL,
                                BTL TEXT NOT NULL,
                                CO TEXT NOT NULL
                            )
                           """)
            print("Brodie this ran")
            
            cursor.execute("""
                INSERT INTO Questions (id, Question, Marks, BTL, CO)
                VALUES (?, ?, ?, ?, ?)
            """, (question_id, question, question_weight, question_BTL, question_CO))
            print("🤫🧏")
            conn.commit()
        except sqlite3.Error as e:
            print(f"Sqlite error {e}")
        except ValueError:
            print("There was some value error")
        finally:
            if conn:
                conn.close()
        
    def QuestionDelete():
        question_id = int(input("Enter the question id: "))
        cursor.execute("""
                       DELETE FROM Questions WHERE id = ?
                       """,(question_id,))

        conn.commit()
        conn.close()

    def update_question():
        try:
            question_id = int(input("Enter the question id: "))
            question = input("Enter the question here: ")
            question_weight = int(input("Enter the mark it holds: "))
            question_BTL = input("Enter BLT: ")
            question_CO = input("Enter CO: ")

            conn = sqlite3.connect('path_to_your_database.db')
            cursor = conn.cursor()

            cursor.execute("""
                UPDATE Questions SET Question = ?, Marks = ?, BTL = ?, CO = ? WHERE id = ?
            """, (question, question_weight, question_BTL, question_CO, question_id))

            conn.commit()
            print("Question updated successfully.")

        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
        except ValueError:
            print("Invalid input. Please enter the correct data types.")
        finally:
            if conn:
                conn.close()
