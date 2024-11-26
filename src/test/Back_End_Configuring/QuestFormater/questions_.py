"""This script will generate questions and it's meta data"""



import sqlite3
import os

db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../db/COURSES.db'))

class QuestionManipulator:
    """
    This class holds the methods for adding, deleting, and updating questions
    """

    @staticmethod
    def connect_db():
        db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'db/COURSES.db'))
        return sqlite3.connect(db_path)

    @staticmethod
    def QuestionAdd(question, question_weight, question_BTL, question_CO):
        try:
            with QuestionManipulator.connect_db() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS Questions (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        Question TEXT NOT NULL,
                        Marks INTEGER NOT NULL,
                        BTL TEXT NOT NULL,
                        CO TEXT NOT NULL
                    )
                """)
                cursor.execute("""
                    INSERT INTO Questions (Question, Marks, BTL, CO)
                    VALUES (?, ?, ?, ?)
                """, (question, question_weight, question_BTL, question_CO))
                print("Question added successfully.")
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
        except ValueError:
            print("Invalid input. Please enter the correct data types.")

    @staticmethod
    def QuestionDelete():
        try:
            question_file = input("Enter the question file: ")
            with QuestionManipulator.connect_db() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    DELETE FROM Questions WHERE file = ?
                """, (question_file,))
                if cursor.rowcount == 0:
                    print("No question found with that file.")
                else:
                    print("Question deleted successfully.")
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")

    @staticmethod
    def update_question():
        try:
            question_file = input("Enter the question file: ")
            question = input("Enter the question here: ")
            question_weight = int(input("Enter the mark it holds: "))
            question_BTL = input("Enter BLT: ")
            question_CO = input("Enter CO: ")

            with QuestionManipulator.connect_db() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    UPDATE Questions SET Question = ?, Marks = ?, BTL = ?, CO = ? WHERE file = ?
                """, (question, question_weight, question_BTL, question_CO, question_file))
                if cursor.rowcount == 0:
                    print("No question found with that ID.")
                else:
                    print("Question updated successfully.")

        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
        except ValueError:
            print("Invalid input. Please enter the correct data types.")