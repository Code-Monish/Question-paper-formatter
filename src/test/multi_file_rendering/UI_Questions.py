import tkinter as tk
from tkinter import ttk

class QuestionPaperPage:
    # This class will be used to create the Question Paper Page.
    '''
        The page will first contain only one button to create new question.
        Once that's clicked, the user's will see a box that will prompt them to select what type of question they want? 
        Options are : 
            1. Multiple Choice Questions
            2. Case-study Questions
            3. Short Answer Questions
            4. Long Answer Questions
            5. Fill in the blanks
        After the type of question is selected, this box should disappear and the user should see the question paper template based of their choice.
        This should be another box with 2 columns, left for question and right for Marks (Text field), BTL and COs (Each being dropdowns)
        After the question is done, there should be a button that adds the question at the top of the list of questions.
        After which the orignial create new question button should appear again.
        and repeat the process.
        
        Also. Have a save button that saves the question paper in a file.
        And a quit button that quits the app.
    '''
    def __init__(self, root):
        self.root = root
        self.root.title("Question Paper Page")
        self.root.state("zoomed")
        # self.root.resizable(False, False)
        
        # Create the main frame
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill="both", expand=True)

        # Create the create new question button
        self.create_new_question_button = tk.Button(self.main_frame, text="Create New Question", command=self.create_new_question)
        self.create_new_question_button.pack(pady=20)

        # Create the question type selection frame
        self.question_type_frame = tk.Frame(self.main_frame)
        self.question_type_frame.pack(pady=20)

        # Create the question type selection label and options
        self.question_type_label = tk.Label(self.question_type_frame, text="Select Question Type:")
        self.question_type_label.pack(side="left", padx=10)

        self.question_type_options = ["Multiple Choice Questions", "Case-study Questions", "Short Answer Questions", "Long Answer Questions", "Fill in the blanks"]
        self.question_type_var = tk.StringVar()
        self.question_type_menu = ttk.OptionMenu(self.question_type_frame, self.question_type_var, *self.question_type_options)
        self.question_type_menu.pack(side="left", padx=10)

        # Create the question template frame
        self.question_template_frame = tk.Frame(self.main_frame)
        self.question_template_frame.pack(pady=20)

        # Create the question template label and entry
        self.question_label = tk.Label(self.question_template_frame, text="Question:")
        self.question_label.pack(side="left", padx=10)

        self.question_entry = tk.Entry(self.question_template_frame, width=50)
        self.question_entry.pack(side="left", padx=10)

        # Create the marks, BTL, and COs frames
        self.marks_frame = tk.Frame(self.question_template_frame)
        self.marks_frame.pack(side="left", padx=10)

        self.marks_label = tk.Label(self.marks_frame, text="Marks:")
        self.marks_label.pack(side="top")

        self.marks_entry = tk.Entry(self.marks_frame, width=5)
        self.marks_entry.pack(side="top")

        self.btl_frame = tk.Frame(self.question_template_frame)
        self.btl_frame.pack(side="left", padx=10)

        self.btl_label = tk.Label(self.btl_frame, text="BTL:")
        self.btl_label.pack(side="top")

        self.btl_var = tk.StringVar()
        self.btl_menu = ttk.OptionMenu(self.btl_frame, self.btl_var, "BTL1", "BTL2", "BTL3", "BTL4")
        self.btl_menu.pack(side="top")

        self.cos_frame = tk.Frame(self.question_template_frame)
        self.cos_frame.pack(side="left", padx=10)

        self.cos_label = tk.Label(self.cos_frame, text="COs:")
        self.cos_label.pack(side="top")

        self.cos_var = tk.StringVar()
        self.cos_menu = ttk.OptionMenu(self.cos_frame, self.cos_var, "CO1", "CO2", "CO3", "CO4")
        self.cos_menu.pack(side="top")

        # Create the add question button
        self.add_question_button = tk.Button(self.question_template_frame, text="Add Question", command=self.add_question)
        self.add_question_button.pack(side="left", padx=10)

        # Create the save button
        self.save_button = tk.Button(self.main_frame, text="Save", command=self.save_question_paper)
        self.save_button.pack(pady=20)

        # Create the quit button
        self.quit_button = tk.Button(self.main_frame, text="Quit", command=self.root.destroy)
        self.quit_button.pack(pady=20)

    def create_new_question(self):
        # Hide the create new question button
        self.create_new_question_button.pack_forget()

        # Show the question type selection frame
        self.question_type_frame.pack(pady=20)

    def add_question(self):
        # Get the question text, marks, BTL, and COs
        question_text = self.question_entry.get()
        marks = self.marks_entry.get()
        btl = self.btl_var.get()
        cos = self.cos_var.get()

        # Add the question to the list of questions
        # ...

        # Hide the question template frame
        self.question_template_frame.pack_forget()

        # Show the create new question button
        self.create_new_question_button.pack(pady=20)

    def save_question_paper(self):
        # Save the question paper to a file
        # ...
        pass
    