"""Helps in quitting the question file safely"""

def quitting_safe():
            print("1. Save File Progress\n2. Export Question Paper")
            file_option = int(input(">> "))
            if file_option == 1:
                print("Saving...")
            elif file_option == 2:
                print("Exporting...")
            else:
                print("Incorrect option, try again")
                return quitting_safe()