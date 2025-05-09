import tkinter as tk
from tkinter import ttk, PhotoImage
from PIL import Image, ImageTk
from UI_Questions import QuestionPaperPage

class QuestionPaperFormatterApp:
    def __init__(self, root):
        self.root = root
        self.root.resizable(False, False)
        self.root.title("Question Paper Formatter")
        self.img = PhotoImage(file='../../data/app-icon.png')
        root.iconphoto(False, self.img)

        # Nav Bar
        self.nav_bar = tk.Frame(self.root, bg="#007bff")
        self.nav_bar.pack(fill="x")

        self.app_name = tk.Label(self.nav_bar, text="Question Paper Formatter", bg="#007bff", fg="white", font=("Arial", 25, "bold"))
        self.app_name.pack(side="left", padx=10, pady=10)

        self.settings_image = Image.open("../../data/settings-icon.png")
        self.settings_image = self.settings_image.resize((30, 30))  # Resize the image to 20x20 pixels
        self.settings_image = ImageTk.PhotoImage(self.settings_image)
        self.settings_icon = tk.Button(self.nav_bar, image=self.settings_image, command=self.settings)
        self.settings_icon.image = self.settings_image  # Keep a reference to the image
        self.settings_icon.pack(side="right", padx=10, pady=10)
        
        # Creating a window for question_page.
        # self.qp_root = tk.Tk()


        # Hero Section
        self.hero_section = tk.Frame(self.root)
        self.hero_section.pack(fill="both", expand=True)

        # Primary Rows
        self.primary_rows = tk.Frame(self.hero_section)
        self.primary_rows.pack(fill="x")

        # Row 1: Create New Question Paper
        self.row1 = tk.Frame(self.primary_rows)
        self.row1.pack(fill="x", pady=20)

        self.create_new_paper_button = tk.Button(self.row1, text="Create New Question Paper", command=self.create_new_paper, font=("Arial", 16))
        self.create_new_paper_button.pack(side="left", padx=10)

        # Row 2: List of Question Papers
        self.row2 = tk.Frame(self.primary_rows)
        self.row2.pack(fill="x")

        self.list_of_papers_label = tk.Label(self.row2, text="List of Question Papers", font=("Arial", 16))
        self.list_of_papers_label.pack(side="left", padx=10)

        self.search_entry = tk.Entry(self.row2, font=("Arial", 16))
        self.search_entry.pack(side="left", padx=10)

        self.search_button = tk.Button(self.row2, text="Search", font=("Arial", 16))
        self.search_button.pack(side="left", padx=10)

        # List of Question Papers
        self.list_of_papers = tk.Listbox(self.hero_section, font=("Arial", 16))
        self.list_of_papers.pack(fill="both", expand=True)
        
        # Footer section 
        self.footer = tk.Frame(self.root, bg="#007bff")
        self.footer.pack(fill="x")
        
        # Quit app button
        self.quit_app = tk.Button(self.footer, text="Quit App", font=("Arial", 16), command=self.root.destroy)
        self.quit_app.pack(side="top", padx = 10, pady = 5)

    def settings(self):
        # Settings window functionality
        
        pass

    def create_new_paper(self):
        # Create new paper window functionality
        self.new_paper_window = tk.Toplevel(self.root)
        self.new_paper_window.geometry("800x600")
        self.new_paper_window.resizable(False, False)
        self.new_paper_window.iconphoto(False, self.img)
        self.new_paper_window.title("Create New Question Paper")

        # Header
        self.header_frame = tk.Frame(self.new_paper_window, bg="#007bff")
        self.header_frame.pack(fill="x")
        self.header_label = tk.Label(self.header_frame, text="Create New Question Paper", bg="#007bff", fg="white", font=("Arial", 24, "bold"))
        self.header_label.pack(pady=20)

        # Content Frame
        self.content_frame = tk.Frame(self.new_paper_window)
        self.content_frame.pack(padx=20, pady=20, fill="both", expand=True)

        # University Name
        self.university_name_label = tk.Label(self.content_frame, text="University Name:", font=("Arial", 16))
        self.university_name_label.pack(anchor="w")
        self.university_name_var = tk.StringVar()
        self.university_name_combobox = ttk.Combobox(self.content_frame, textvariable=self.university_name_var, font=("Arial", 16))
        self.university_name_combobox['values'] = ['Amrtia Vidhya Vishwapeetham, Bengaluru', 'Amrtia Vidhya Vishwapeetham, Chennai', 'Amrtia Vidhya Vishwapeetham, Coimbatore']
        self.university_name_combobox.pack(anchor="w")

        # Degree
        self.degree_label = tk.Label(self.content_frame, text="Degree:", font=("Arial", 16))
        self.degree_label.pack(anchor="w")
        self.degree_var = tk.StringVar()
        self.degree_combobox = ttk.Combobox(self.content_frame, textvariable=self.degree_var, font=("Arial", 16))
        self.degree_combobox['values'] = ['Btech', 'Mtech', 'MBA']
        self.degree_combobox.pack(anchor="w")

        # Examination
        self.examination_label = tk.Label(self.content_frame, text="Examination:", font=("Arial", 16))
        self.examination_label.pack(anchor="w")
        self.examination_var = tk.StringVar()
        self.examination_combobox = ttk.Combobox(self.content_frame, textvariable=self.examination_var, font=("Arial", 16))
        self.examination_combobox['values'] = ['Quiz', 'Mid Semester', 'End Semester']
        self.examination_combobox.pack(anchor="w")

        # Session/Year
        self.session_year_label = tk.Label(self.content_frame, text="Session/Year:", font=("Arial", 16))
        self.session_year_label.pack(anchor="w")
        self.session_year_entry = tk.Entry(self.content_frame, font=("Arial", 16))
        self.session_year_entry.pack(anchor="w")

        # Branch
        self.branch_label = tk.Label(self.content_frame, text="Branch:", font=("Arial", 16))
        self.branch_label.pack(anchor="w")
        self.branch_var = tk.StringVar()
        self.branch_combobox = ttk.Combobox(self.content_frame, textvariable=self.branch_var, font=("Arial", 16))
        self.branch_combobox['values'] = ['Mech', 'RAI', 'CSE', 'ECE', 'EAC', 'ELC', 'AIE', 'AID']
        self.branch_combobox.pack(anchor="w")

        # Semester
        self.semester_label = tk.Label(self.content_frame, text="Semester:", font=("Arial", 16))
        self.semester_label.pack(anchor="w")
        self.semester_var = tk.StringVar()
        self.semester_combobox = ttk.Combobox(self.content_frame, textvariable=self.semester_var, font=("Arial", 16))
        self.semester_combobox['values'] = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th']
        self.semester_combobox.pack(anchor="w")

        # Course Code
        self.course_code_label = tk.Label(self.content_frame, text="Course Code:", font=("Arial", 16))
        self.course_code_label.pack(anchor="w")
        self.course_code_entry = tk.Entry(self.content_frame, font=("Arial", 16))
        self.course_code_entry.pack(anchor="w")

        # Button Frame
        self.button_frame = tk.Frame(self.new_paper_window)
        self.button_frame.pack(pady=20)

        # Next Button
        self.next_button = tk.Button(self.button_frame, text="Next", bg="#007bff", fg="white", font=("Arial", 16), command=self.open_next_page)
        self.next_button.pack(side="left", padx=10)

        # Back to Home Button
        self.back_to_home_button = tk.Button(self.button_frame, text="Back to Home", command=self.new_paper_window.destroy, font=("Arial", 16))
        self.back_to_home_button.pack(side="left", padx=10)
        
    def open_next_page(self):
        self.next_page()
        self.new_paper_window.destroy()
        
    
    def next_page(self):
        # Next page functionality
        self.prompt_window = tk.Toplevel(self.root)
        self.prompt_window.geometry("600x200")
        self.prompt_window.resizable(False,False)
        self.prompt_window.iconphoto(False,self.img)
        self.prompt_window.title("Information")
    
        self.prompt_label = tk.Label(self.prompt_window, text="Do you want to segment your paper into sections?", font=("Arial", 16, "bold"))
        self.prompt_label.pack(pady=20)
    
        self.prompt_window_btn = tk.Frame(self.prompt_window)
        self.prompt_window_btn.pack(pady=20)
    
        self.button_yes = tk.Button(self.prompt_window_btn, text="Yes", font=("Arial", 16), command=self.open_question_paper_page)
        self.button_yes.pack(side="left", padx=10)
        self.button_no = tk.Button(self.prompt_window_btn, text="No", font=("Arial", 16))
        self.button_no.pack(side="left", padx=10)

    def open_question_paper_page(self):
        self.prompt_window.destroy()
        self.question_paper_window = tk.Toplevel(self.root)
        self.question_paper_window.title("Question Paper")
        self.question_paper_page = QuestionPaperPage(self.question_paper_window)
        
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")
    app = QuestionPaperFormatterApp(root)
    root.mainloop()
    
# todo : make a the question paper page.