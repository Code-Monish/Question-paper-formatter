from QuestFormater import questions_, question_quit, question_docx_form, question_paper_setup, data_checker

print(data_checker.main())

from datetime import datetime
def main():
    print("========== QUESTION PAPER SETUP ==========")
    # course_code = input("Enter the course code: ")
    # session = input("Enter the session: ")
    # branch = input("Enter the branch: ")

    # # Store course details in a dictionary
    # course_details = {
    #     "course_code": course_code,
    #     "session": session,
    #     "branch": branch,
    # }
    
    session, results = question_paper_setup.QuestionPaperSetup()
    print(type(session))
    print("===========")
    print(results)
    print("\nCourse details loaded:\n")
    # print(f"Session: {course_details['session']} \n==========================================\n")

    file_name = datetime.now()
    while True:
        print("Choose an option:")
        print("1. Add a question")
        print("2. Save and Exit")
        print("3. Export to Word Document")
        option = input(">> ")

        if option == "1":
            while True:
                print("\nAdding a question...")
                # question = input("Enter the question here: ")
                # marks = int(input("Enter the marks: "))
                # btl = int(input("Enter the BTL: "))
                # co = int(input("Enter the CO: "))
                question_details = (file_name)
                questions_.QuestionManipulator.QuestionAdd(question_details)
                print("Question added successfully.\n")

                # Ask the user what to do next
                print("Choose an option:")
                print("1. Save and Exit")
                print("2. Export to Word Document")
                print("3. Continue adding questions")
                next_option = input(">> ")

                if next_option == "1":
                    print("\nSaving and exiting...")
                    # question_quit.save_and_exit(course_details)  # Call the correct function
                    return
                elif next_option == "2":
                    print("\nExporting to Word document...")
                    question_docx_form.QuestionDOCX()  # Call the correct method
                    print("Export complete.\n")
                elif next_option == "3":
                    print("\nContinuing to add questions...\n")
                    break  # Exit the inner loop to add the next question
                else:
                    print("\nInvalid option. Please try again.\n")

        elif option == "2":
            print("\nSaving and exiting...")
            # question_quit.save_and_exit(course_details)  # Call the correct function
            break
        elif option == "3":
            print("\nExporting to Word document...")
            question_docx_form.QuestionDOCX()  # Call the correct method
            print("Export complete.\n")
        else:
            print("\nInvalid option. Please try again.\n")
            
main()