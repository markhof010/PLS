def menu():
    while True:
        print("\\nPlease enter the number that stands before the actions you want to do\n[1] Look at all loans\n[2] Add a book\n[3] Add a customer\n[4] Make a backup\n[5] Restore data [6] Exit")
        userInput = input()
        if userInput == "1":
            print("loans")
        elif userInput == "2":
            print("add book")
        elif userInput == "3":
            print("add customer")
        elif userInput == "4":
            print("back up")
        elif userInput == "5":
            print("restore")
        elif userInput == "6":
            break