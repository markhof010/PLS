import Companies
import Loans

class Subscriber(Companies.PublishingCompany):
    @staticmethod
    def Smenu(username,BookList,LoanList, PersonList):
        while True:
            print("\nPlease enter a number that stand before the action you want to do")
            print("[1] See all available books\n[2] Search for a book\n[3] Loan a book\n[4] Exit")
            userInput = input()
            if userInput == "1":
                Subscriber.SeeBooks(BookList)
            elif userInput == "2":
                Subscriber.SearchBook(BookList)
            elif userInput == "3":
                Subscriber.LoanBook(username,BookList,PersonList,LoanList)
            elif userInput == "4":
                break
    
    @staticmethod
    def LoanBook(username,BookList, PersonList, LoanList):
        inpuntTitle = input("Please enter the title of the book you want to reserve\n")
        for book in BookList.bookList:
            if book.title == inpuntTitle:
                if book.amount > book.loaned:
                    for person in PersonList.nameList:
                        if username == person.username:
                            book.loaned = book.loaned + 1
                            BookList._saveBooks()
                            LoanList.AddLoan(book,person)
                else:
                    print("This book is not available")