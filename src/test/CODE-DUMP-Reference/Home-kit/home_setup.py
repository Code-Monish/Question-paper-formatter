import customtkinter 
from PIL import Image

class SetupFrame(customtkinter.CTkFrame):
    def __init__(master):
        super().__init__(master)
        
        # Label - "Setup"
        self.setup_label = customtkinter.CTkLabel(self, text="Setup", font=("Arial", 30))
        self.setup_label.grid(row=0, column=0, padx=10, pady=10)
        
        # Combo box - "Select course code"
        self.course_label = customtkinter.CTkLabel(self, text="Select course code", font=("Arial", 15))
        self.course_label.grid(row=1, column=0, padx=10, pady=10)
        
        self.course_code = customtkinter.CTkCombobox(self, values=["CS101", "CS102", "CS103", "CS104", "CS105"])
        self.course_code.grid(row=1, column=1, padx=10, pady=10)
        
        # Combo box - "Select Session"
        self.session_label = customtkinter.CTkLabel(self, text="Select Session", font=("Arial", 15))
        self.session_label.grid(row=2, column=0, padx=10, pady=10)
        
        self.session = customtkinter.CTkCombobox(self, values=["2020-2021", "2021-2022", "2022-2023", "2023-2024", "2024-2025"])
        self.session.grid(row=2, column=1, padx=10, pady=10)
        
        # Combo box - "Select Semester"
        self.semester_label = customtkinter.CTkLabel(self, text="Select Semester", font=("Arial", 15))
        self.semester_label.grid(row=3, column=0, padx=10, pady=10)
        
        self.semester = customtkinter.CTkCombobox(self, values=["1", "2", "3", "4", "5", "6", "7", "8"])
        self.semester.grid(row=3, column=1, padx=10, pady=10)
        
        
        # Button - "Next"
        self.next_button = customtkinter.CTkButton(self, text="Next", command=self.next_button_click)
        self.next_button.grid(row=4, column=1, padx=10, pady=10)
        
        