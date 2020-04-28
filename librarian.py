import customer

class Librarian(customer.Subscriber):
    @staticmethod
    def Lmenu():
        while True:
            print("\nPlease enter the number that stands before the actions you want to do\n[1] See all available books\n[2] Search for a book\n[3] Add a book\n[4] See all loans\n[5] Make a loan\n[6] Cancel a loan\n[7] See all subscribers\n[8] Add a subscriber\n[9] Make a backup\n[10] Restore from backup\n[11] Exit")
            userInput = input()
            if userInput == "1":
                customer.Subscriber.SeeBooks()
            elif userInput == "2":
                customer.Subscriber.SearchBook()
            elif userInput == "3":
                print("add book")
            elif userInput == "4":
                print("see all loans")
            elif userInput == "5":
                customer.Subscriber.LoanBook()
            elif userInput == "6":
                print("Cancel loans")
            elif userInput == "7":
                print("See all subscribers")
            elif userInput == "8":
                print("Add a subscriber")
            elif userInput == "9":
                print("Make a backup")
            elif userInput == "10":
                print("restore from backup")
            elif userInput == "11":
                break
            else:
                print("Enter an option from the menu")
            
    
    

Librarian.Lmenu()
