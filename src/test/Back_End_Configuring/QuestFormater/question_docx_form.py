from docx import Document
import sqlite3
import os

db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../db/COURSES.db'))
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

def QuestionDOCX():
    cursor.execute("SELECT Question, Marks, BTL, CO FROM Questions")
    questions = cursor.fetchall()

    # Create a new Document
    doc = Document()
    doc.add_heading('Questions', level=1)
    # doc.add_section()
    for question, marks, btl, co in questions:
        # Add question
        p = doc.add_paragraph()
        p.add_run(question).bold = True
        # doc.add_page_break()
        # doc.add_section()
        # Add marks, BTL, and CO to the right of the question
        p.add_run(f' (Marks: {marks}, BTL: {btl}, CO: {co})')

    # Save the document
    doc.save('Questions.docx')

    print("Questions.docx created successfully.")
    conn.close()

# if __name__ == "__main__":
#     QuestionDOCX()