import customer
import Loans
import person
from backup import Backup
import backup

class Librarian(customer.Subscriber):
    @staticmethod
    def Lmenu(BookList,LoanList,PersonList):
        while True:
            print("\nPlease enter the number that stands before the actions you want to do\n[1] See all available books\n[2] Search for a book\n[3] Add a book\n[4] See all loans\n[5] Make a loan\n[6] Cancel a loan\n[7] See all subscribers\n[8] Add a subscriber\n[9] Make a backup\n[10] Restore from backup\n[11] Exit")
            userInput = input()
            
            if userInput == "1":
                Librarian.SeeBooks(BookList)
            
            elif userInput == "2":
                Librarian.SearchBook(BookList)
            
            elif userInput == "3":
                while True:
                    BookList.addBook()
                    print("Do you want to add another book?\n[1] yes\n[2] no")
                    YorN = input()
                    if YorN == "2":
                        break
            
            elif userInput == "4":
                Librarian.SeeLoans(LoanList)
            
            elif userInput == "5":
                username = input("Please enter the username of the person that wants to loan a book\n")
                Librarian.LoanBook(username,BookList,PersonList,LoanList)
            
            elif userInput == "6":
                Librarian.RemoveLoans(LoanList)
            
            elif userInput == "7":
                for person in PersonList.nameList:
                    print(person.display())
            
            elif userInput == "8":
                PersonList.addPerson()
            
            elif userInput == "9":
                print("Make a backup")
                Backup().makeBackup()
            
            elif userInput == "10":
                backup.restore()
            elif userInput == "11":
                break
            else:
                print("Enter an option from the menu")
    
    @staticmethod
    def SeeLoans(LoanList):
        for loan in LoanList.ListofLoans:
            print(loan.DisplayLoan())

    @staticmethod
    def RemoveLoans(LoanList):
        username = input("Please enter the username\n")
        title = input("Please enter the title of the book\n")
        LoanList.RemoveLoan(title, username)
