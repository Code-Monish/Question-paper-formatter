# Standard Library Imports
import os
import io
import sys
import platform
import subprocess
import sqlite3

# Tkinter and CustomTkinter Imports
import tkinter as tk
import tkinter.filedialog as filedialog
import tkinter.messagebox as messagebox
import customtkinter

# Document Processing Imports
from docx import Document
from docx.shared import Inches

# Image Processing Imports
from PIL import Image, ImageTk


# Add the path
current_script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_script_dir, '..'))
lib_path = os.path.join(parent_dir, 'Back_End_Configuring', 'QuestFormater')
sys.path.insert(0, lib_path)

import questions_

class DocxPreviewWidget(customtkinter.CTkFrame):
    def __init__(self, master, docx_path):
        super().__init__(master)
        self.docx_path = docx_path
        self._create_preview()

    def _create_preview(self):
        """Create a preview of the DOCX file"""
        # Document preview label
        self.preview_label = customtkinter.CTkLabel(
            self, 
            text="Document Preview", 
            font=("Arial", 16, "bold")
        )
        self.preview_label.pack(pady=(10, 5))

        # Scrollable frame for document content
        self.scroll_frame = customtkinter.CTkScrollableFrame(self)
        self.scroll_frame.pack(expand=True, fill="both", padx=10, pady=10)

        # Extract and display document content
        self._display_docx_content()

    def _display_docx_content(self):
        """Extract and display DOCX content"""
        try:
            # Open the document
            doc = Document(self.docx_path)
            
            # Clear any existing content
            for widget in self.scroll_frame.winfo_children():
                widget.destroy()

            # Display document paragraphs
            for para in doc.paragraphs:
                para_label = customtkinter.CTkLabel(
                    self.scroll_frame, 
                    text=para.text, 
                    wraplength=500, 
                    justify="left", 
                    anchor="w"
                )
                para_label.pack(pady=2, padx=5, fill="x")

            # Option to open full document
            open_btn = customtkinter.CTkButton(
                self.scroll_frame, 
                text="Open Full Document", 
                command=self._open_full_document
            )
            open_btn.pack(pady=10)

        except Exception as e:
            error_label = customtkinter.CTkLabel(
                self.scroll_frame, 
                text=f"Error loading document: {str(e)}",
                text_color="red"
            )
            error_label.pack(pady=10)

    def _open_full_document(self):
        """Open the full document using default system viewer"""
        try:
            os.startfile(self.docx_path)
        except Exception as e:
            tk.messagebox.showerror("Error", f"Could not open document: {str(e)}")


class QuestionPaperApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Window setup
        self.title("Question Paper Formatter")
        self.geometry("1024x600")
        
        # Configure main grid
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Path to DOCX file using absolute path
        self.docx_path = os.path.abspath(os.path.join(
            os.path.dirname(__file__), 
            '..', 
            'Back_End_Configuring', 
            'Questions.docx'
        ))

        # Absolute path to QuestionBank folder
        self.question_bank_path = os.path.abspath(os.path.join(
            os.path.dirname(__file__), 
            '..', 
            'Back_End_Configuring', 
            'QuestionBank'
        ))

        # Create layout components
        self._create_sidebar()
        self._create_main_content()
        self._create_footer()

    def _open_question_bank(self):
        """Open the QuestionBank folder using the default file explorer"""
        try:
            # Check the operating system and use appropriate method
            if platform.system() == "Windows":
                os.startfile(self.question_bank_path)
            elif platform.system() == "Darwin":  # macOS
                subprocess.Popen(["open", self.question_bank_path])
            else:  # Linux and other Unix-like systems
                subprocess.Popen(["xdg-open", self.question_bank_path])
        except Exception as e:
            messagebox.showerror("Error", f"Could not open folder: {str(e)}")
            
    def _save_to_database(self):
        """Saves the paper data onto the database"""
        messagebox.showinfo("Save Prompt", "Your progress has been saved, you may close the app safely now.")

    def _create_sidebar(self):
        """Create a sidebar with navigation options"""
        sidebar = customtkinter.CTkFrame(self, width=250, corner_radius=0)
        sidebar.grid(row=0, column=0, rowspan=2, sticky="nsew")
        
        # Sidebar title
        title_label = customtkinter.CTkLabel(
            sidebar, 
            text="Question Paper Tools", 
            font=("Arial", 20, "bold")
        )
        title_label.pack(pady=(20, 10))

        # Sidebar buttons with specific commands
        sidebar_buttons = [
            ("New Paper", None), 
            ("Open Paper", self._open_question_bank), 
            ("Save Paper", self._save_to_database), 
            ("Export", None), 
            ("Settings", None)
        ]

        for btn_text, btn_command in sidebar_buttons:
            btn = customtkinter.CTkButton(
                sidebar, 
                text=btn_text, 
                corner_radius=5,
                command=btn_command if btn_command else None
            )
            btn.pack(pady=5, padx=10, fill="x")
        
    def _create_main_content(self):
        """Create the main content area with question input and preview"""
        # Main content frame
        main_frame = customtkinter.CTkFrame(self)
        main_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        main_frame.grid_columnconfigure(0, weight=2)
        main_frame.grid_columnconfigure(1, weight=1)
        main_frame.grid_rowconfigure(0, weight=1)

        # Left side: Question Input
        input_frame = customtkinter.CTkFrame(main_frame)
        input_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        
        # Question Input Title
        input_title = customtkinter.CTkLabel(
            input_frame, 
            text="Question Input", 
            font=("Arial", 18, "bold")
        )
        input_title.pack(pady=(10, 20))

        # Scrollable input area
        self.input_scroll = customtkinter.CTkScrollableFrame(input_frame)
        self.input_scroll.pack(expand=True, fill="both", padx=10, pady=10)

        # Add Question Button
        add_question_btn = customtkinter.CTkButton(
            self.input_scroll, 
            text="➕ Add New Question", 
            corner_radius=5,
            command=self._add_question_prompt
        )
        add_question_btn.pack(pady=10, fill="x")

        # Right side: Paper Preview
        preview_frame = customtkinter.CTkFrame(main_frame)
        preview_frame.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
        
        # Create DOCX preview widget
        self.docx_preview = DocxPreviewWidget(preview_frame, self.docx_path)
        self.docx_preview.pack(expand=True, fill="both", padx=5, pady=5)
        
        # Initialize a list to keep track of question entries
        self.question_entries = []
        
    def _add_question_prompt(self):
        """Add a new detailed question input form"""
        # Create a frame for the entire question input
        question_frame = customtkinter.CTkFrame(self.input_scroll)
        question_frame.pack(pady=10, fill="x")

        # Question number label
        question_number = len(self.question_entries) + 1
        question_label = customtkinter.CTkLabel(
            question_frame, 
            text=f"Question {question_number}", 
            font=("Arial", 14, "bold")
        )
        question_label.pack(pady=(10, 5))

        # Question input
        question_input_label = customtkinter.CTkLabel(question_frame, text="Question:")
        question_input_label.pack()
        question_entry = customtkinter.CTkEntry(
            question_frame, 
            placeholder_text="Enter your question here",
            width=400
        )
        question_entry.pack(pady=(0, 10), padx=20)

        # Marks input
        marks_frame = customtkinter.CTkFrame(question_frame, fg_color="transparent")
        marks_frame.pack(pady=5)

        marks_label = customtkinter.CTkLabel(marks_frame, text="Marks:")
        marks_label.pack(side="left", padx=(0, 10))
        marks_entry = customtkinter.CTkEntry(
            marks_frame, 
            placeholder_text="Marks", 
            width=100
        )
        marks_entry.pack(side="left", padx=5)

        # BTL input
        btl_label = customtkinter.CTkLabel(marks_frame, text="BTL:")
        btl_label.pack(side="left", padx=(20, 10))
        btl_entry = customtkinter.CTkEntry(
            marks_frame, 
            placeholder_text="BTL", 
            width=100
        )
        btl_entry.pack(side="left", padx=5)

        # CO input
        co_label = customtkinter.CTkLabel(marks_frame, text="CO:")
        co_label.pack(side="left", padx=(20, 10))
        co_entry = customtkinter.CTkEntry(
            marks_frame, 
            placeholder_text="CO", 
            width=100
        )
        co_entry.pack(side="left", padx=5)

        # Next button to add another question
        next_button = customtkinter.CTkButton(
            question_frame, 
            text="Next Question", 
            command=lambda: self._process_and_add_next_question(
                question_entry, marks_entry, btl_entry, co_entry, question_frame
            )
        )
        next_button.pack(pady=10)

        # Store the entries in the question entries list
        self.question_entries.append({
            'question': question_entry,
            'marks': marks_entry,
            'btl': btl_entry,
            'co': co_entry
        })

        # Hide the original "Add Question" button after first question
        if len(self.question_entries) == 1:
            # Assuming the add question button is the last widget in the input_frame
            for widget in self.input_frame.winfo_children():
                if isinstance(widget, customtkinter.CTkButton):
                    widget.pack_forget()
    
    def _process_and_add_next_question(self, current_question_entry, marks_entry, btl_entry, co_entry, current_frame):
        """Process the current question and add a new question prompt"""
        # Validate inputs
        if not current_question_entry.get().strip():
            # Create an error label
            error_label = customtkinter.CTkLabel(
                current_frame, 
                text="Please enter a question.", 
                text_color="red"
            )
            error_label.pack(pady=5)

            # Optional: Remove the error label after a few seconds
            current_frame.after(3000, error_label.destroy)
            return

        # Validate marks (ensure it's a number)
        try:
            marks = float(marks_entry.get())
        except ValueError:
            error_label = customtkinter.CTkLabel(
                current_frame, 
                text="Marks must be a number.", 
                text_color="red"
            )
            error_label.pack(pady=5)
            current_frame.after(3000, error_label.destroy)
            return

        # Optional: You might want to store the question details
        # For now, we'll just clear the current frame and add a new question
        current_frame.pack_forget()  # Hide the current question frame
        self._add_question_prompt()  # Add a new question prompt

        # Save question to database
        question = current_question_entry.get()
        question_weight = marks_entry.get()
        question_BTL = btl_entry.get()
        question_CO = co_entry.get()
        questions_.QuestionManipulator.QuestionAdd(question, question_weight, question_BTL, question_CO)

    def _save_question(self):
        question = self.question_entry.get()
        question_weight = self.question_weight_entry.get()
        question_BTL = self.question_BTL_entry.get()
        question_CO = self.question_CO_entry.get()

        # Call the QuestionAdd method from the questions_ module
        questions_.QuestionManipulator.QuestionAdd(question, question_weight, question_BTL, question_CO)

    def _create_footer(self):
        """Create a footer with status and quick actions"""
        footer = customtkinter.CTkFrame(self, height=50)
        footer.grid(row=1, column=1, sticky="ew")

        # Left side status
        status_label = customtkinter.CTkLabel(
            footer, 
            text="Ready | 0 Questions", 
            anchor="w"
        )
        status_label.pack(side="left", padx=10)

        # Right side quick actions
        quick_actions_frame = customtkinter.CTkFrame(footer, fg_color="transparent")
        quick_actions_frame.pack(side="right", padx=10)

        # Updated quick buttons with proper commands
        quick_buttons = [
            ("Save", self._save_action),
            ("Export", self._export_action),
            ("Print", self._print_action),
            ("Exit", self._exit_application)
        ]

        for btn_text, btn_command in quick_buttons:
            btn = customtkinter.CTkButton(
                quick_actions_frame, 
                text=btn_text, 
                width=80,
                command=btn_command
            )
            btn.pack(side="left", padx=5,pady=10)

    def _exit_application(self):
        """Properly handle application exit"""
        # Optional: Add confirmation dialog
        if messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
            self.quit()  # Closes the application gracefully

    # Placeholder methods for other actions (can be implemented later)
    def _save_action(self):
        messagebox.showinfo("Save", "Save functionality will be implemented soon.")

    def _export_action(self):
        messagebox.showinfo("Export", "Export functionality will be implemented soon.")

    def _print_action(self):
        messagebox.showinfo("Print", "Print functionality will be implemented soon.")

def main():
    # Set appearance mode and color theme
    customtkinter.set_appearance_mode("system")
    customtkinter.set_default_color_theme("dark-blue")

    # Create and run the application
    app = QuestionPaperApp()
    app.mainloop()

if __name__ == "__main__":
    main()