import customtkinter
from PIL import Image

# Header Frame Definition
class HeaderFrame(customtkinter.CTkFrame):
    def __init__(self, master, height=100):
        super().__init__(master, height=height)

        # Logo (left-aligned)
        self.logo_image = customtkinter.CTkImage(
            light_image=Image.open("./download.png"),
            size=(40, 40)
        )
        self.logo_label = customtkinter.CTkLabel(self, image=self.logo_image, text="")
        self.logo_label.grid(row=0, column=0, padx=(20, 10), pady=10, sticky="w")

        # Title (centered)
        self.title_label = customtkinter.CTkLabel(
            self, text="Question Paper Formatter", font=("Arial", 24, "bold")
        )
        self.title_label.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        # Options Menu (right-aligned)
        self.optionmenu = customtkinter.CTkOptionMenu(
            self, values=["Settings", "Source Code", "Get Help"], width=150
        )
        self.optionmenu.grid(row=0, column=2, padx=(10, 20), pady=10, sticky="e")

        # Configure column weights to balance layout
        self.grid_columnconfigure(0, weight=1)  # Logo
        self.grid_columnconfigure(1, weight=2)  # Title
        self.grid_columnconfigure(2, weight=1)  # Menu

# Left Frame Definition
class LeftFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, corner_radius=10)

        # Section title label
        self.label = customtkinter.CTkLabel(self, text="Setup Options", font=("Arial", 18, "bold"), anchor="w")
        self.label.grid(row=0, column=0, columnspan=2, padx=10, pady=(15, 5), sticky="w")

        # Course Code
        self.course_code_label = customtkinter.CTkLabel(self, text="Course Code:", font=("Arial", 14))
        self.course_code_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        self.course_code_combo = customtkinter.CTkComboBox(self, values=["CS101", "CS102", "CS103"], width=200)
        self.course_code_combo.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        # Exam Session
        self.exam_session_label = customtkinter.CTkLabel(self, text="Exam Session:", font=("Arial", 14))
        self.exam_session_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")

        self.exam_session_combo = customtkinter.CTkComboBox(self, values=["Spring", "Summer", "Fall"], width=200)
        self.exam_session_combo.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        # Semester
        self.semester_label = customtkinter.CTkLabel(self, text="Semester:", font=("Arial", 14))
        self.semester_label.grid(row=3, column=0, padx=10, pady=10, sticky="e")

        self.semester_combo = customtkinter.CTkComboBox(self, values=["1", "2", "3", "4", "5", "6", "7", "8"], width=200)
        self.semester_combo.grid(row=3, column=1, padx=10, pady=10, sticky="w")

        self.toplevel_window = None

        def open_question_paper_formatter():
            main_app = self.winfo_toplevel()  # Get reference to main App window
            if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
                self.toplevel_window = ToplevelWindow(main_app)  # Pass App as master
            else:
                self.toplevel_window.focus()

        self.create_paper_button = customtkinter.CTkButton(
            self, text="Create Paper", font=("Arial", 14), corner_radius=10, command=open_question_paper_formatter
        )
        self.create_paper_button.grid(row=4, column=0, columnspan=2, padx=10, pady=(20, 10))

        # Configure grid layout for spacing
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

# Question Paper Formatter Toplevel Window Definition
class ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Question Paper Formatter")
        self.state("zoomed")
        
        # Iconify (minimize) the main application window
        master.iconify()

        # Initialize question count
        self.question_count = 0

        # Configure layout
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Create Scrollable Area for Question Inputs
        self.create_scrollable_frame()

        # Footer frame for buttons
        footer_frame = customtkinter.CTkFrame(self)
        footer_frame.grid(row=1, column=0, pady=(0, 10), sticky="ew")
        footer_frame.grid_columnconfigure(0, weight=1)
        footer_frame.grid_columnconfigure(1, weight=1)

        # 'Save and Exit' button
        save_and_exit_button = customtkinter.CTkButton(
            footer_frame, text="Save and Exit", command=self.save_and_exit
        )
        save_and_exit_button.grid(row=0, column=0, padx=10, pady=10)

        # 'Export' button
        export_button = customtkinter.CTkButton(
            footer_frame, text="Export", command=self.export_and_close
        )
        export_button.grid(row=0, column=1, padx=10, pady=10)

    def create_scrollable_frame(self):
        # Create a canvas to hold the scrollable frame
        canvas = customtkinter.CTkCanvas(self)
        canvas.grid(row=0, column=0, sticky="nsew")

        # Create a scrollbar linked to the canvas
        scrollbar = customtkinter.CTkScrollbar(self, orientation="vertical", command=canvas.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")

        canvas.configure(yscrollcommand=scrollbar.set)

        # Create a frame inside the canvas to hold question frames
        self.scrollable_frame = customtkinter.CTkFrame(canvas)
        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        # Update the scrollable area when new questions are added
        self.scrollable_frame.bind(
            "<Configure>", lambda event, canvas=canvas: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        # Add the 'Add Question' button
        self.add_question_button = customtkinter.CTkButton(
            self.scrollable_frame, text="Add Question", command=self.show_question_input
        )
        self.add_question_button.grid(row=self.question_count, column=0, padx=10, pady=10)

    def show_question_input(self):
        # Hide the 'Add Question' button
        self.add_question_button.grid_forget()

        # Increment question count
        self.question_count += 1

        # Create the child frame for the question
        child_frame = customtkinter.CTkFrame(self.scrollable_frame)
        child_frame.grid(row=self.question_count, column=0, pady=(10, 0), sticky="ew")

        # Create a text field for question input
        question_label = customtkinter.CTkLabel(child_frame, text="Enter Question:")
        question_label.grid(row=0, column=0, padx=10, pady=5)
        question_input = customtkinter.CTkEntry(child_frame)
        question_input.grid(row=0, column=1, padx=10, pady=5)

        # Create text fields for Marks, BLT, and CO
        marks_label = customtkinter.CTkLabel(child_frame, text="Marks:")
        marks_label.grid(row=1, column=0, padx=10, pady=5)
        marks_input = customtkinter.CTkEntry(child_frame)
        marks_input.grid(row=1, column=1, padx=10, pady=5)

        blt_label = customtkinter.CTkLabel(child_frame, text="BLT:")
        blt_label.grid(row=1, column=2, padx=10, pady=5)
        blt_input = customtkinter.CTkEntry(child_frame)
        blt_input.grid(row=1, column=3, padx=10, pady=5)

        co_label = customtkinter.CTkLabel(child_frame, text="CO:")
        co_label.grid(row=1, column=4, padx=10, pady=5)
        co_input = customtkinter.CTkEntry(child_frame)
        co_input.grid(row=1, column=5, padx=10, pady=5)

        # Create a 'Next' button for this child frame
        next_button = customtkinter.CTkButton(child_frame, text="Next", command=self.next_question)
        next_button.grid(row=2, column=0, columnspan=6, pady=10)

    def next_question(self):
        # Ensure that the current question frame is properly removed
        for widget in self.scrollable_frame.winfo_children():
            if isinstance(widget, customtkinter.CTkFrame):
                # Check if the widget is a question frame and it is in the last added row
                grid_info = widget.grid_info()
                if "row" in grid_info and grid_info["row"] == self.question_count:
                    widget.grid_forget()

        # Show the next question input
        self.show_question_input()

    def save_and_exit(self):
        self.master.deiconify()  # Restore the main window
        self.destroy()

    def export_and_close(self):
        self.master.deiconify()  # Restore the main window
        self.destroy()



# Right Frame Definition (Scrollable)
class RightFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master, corner_radius=10)
        
        # Section label
        self.label = customtkinter.CTkLabel(self, text="Saved Papers", font=("Arial", 18, "bold"), anchor="w")
        self.label.grid(row=0, column=0, padx=10, pady=(15, 5), sticky="w")

        # Placeholder for future saved paper items
        for i in range(5):
            paper_label = customtkinter.CTkLabel(self, text=f"Saved Paper {i+1}", font=("Arial", 14), padx=10)
            paper_label.grid(row=i + 1, column=0, padx=10, pady=5, sticky="w")

# Main App Definition
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("CustomTkinter Home Page")
        self.geometry("1024x600")

        # Configure main grid layout
        self.grid_rowconfigure(0, weight=0) 
        self.grid_rowconfigure(1, weight=1)  
        self.grid_columnconfigure(0, weight=1)

        # Header Frame
        self.header_frame = HeaderFrame(self, height=100)
        self.header_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="new")

        # Main Content Frame
        self.content_frame = customtkinter.CTkFrame(self)
        self.content_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        
        # Configure content frame grid
        self.content_frame.grid_columnconfigure(0, weight=1)
        self.content_frame.grid_columnconfigure(1, weight=1)
        self.content_frame.grid_rowconfigure(0, weight=1)

        # Left and Right Frames
        self.left_frame = LeftFrame(self.content_frame)
        self.left_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.right_frame = RightFrame(self.content_frame)
        self.right_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

app = App()
app.mainloop()
